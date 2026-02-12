import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { google } from 'googleapis';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Gmail API setup
const SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly'];
const TOKEN_PATH = path.join(__dirname, '../AI_Employee_Vault/gmail_token.json');
const CREDENTIALS_PATH = path.join(__dirname, '../AI_Employee_Vault/gmail_credentials.json');

class EmailMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'email-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.gmail = null;
    this.setupHandlers();
    this.setupErrorHandling();
  }

  async initializeGmail() {
    try {
      const credentials = JSON.parse(await fs.readFile(CREDENTIALS_PATH, 'utf-8'));
      const { client_secret, client_id, redirect_uris } = credentials.installed || credentials.web;

      const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

      // Load token
      const token = JSON.parse(await fs.readFile(TOKEN_PATH, 'utf-8'));
      oAuth2Client.setCredentials(token);

      this.gmail = google.gmail({ version: 'v1', auth: oAuth2Client });
      return true;
    } catch (error) {
      console.error('Gmail initialization error:', error);
      return false;
    }
  }

  setupErrorHandling() {
    this.server.onerror = (error) => {
      console.error('[MCP Error]', error);
    };

    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'send_email',
          description: 'Send an email via Gmail',
          inputSchema: {
            type: 'object',
            properties: {
              to: {
                type: 'string',
                description: 'Recipient email address',
              },
              subject: {
                type: 'string',
                description: 'Email subject line',
              },
              body: {
                type: 'string',
                description: 'Email body content (plain text or HTML)',
              },
              cc: {
                type: 'string',
                description: 'CC email addresses (comma-separated)',
              },
              bcc: {
                type: 'string',
                description: 'BCC email addresses (comma-separated)',
              },
              dry_run: {
                type: 'boolean',
                description: 'If true, validate but do not actually send',
                default: false,
              },
            },
            required: ['to', 'subject', 'body'],
          },
        },
        {
          name: 'draft_email',
          description: 'Create a draft email in Gmail',
          inputSchema: {
            type: 'object',
            properties: {
              to: {
                type: 'string',
                description: 'Recipient email address',
              },
              subject: {
                type: 'string',
                description: 'Email subject line',
              },
              body: {
                type: 'string',
                description: 'Email body content',
              },
            },
            required: ['to', 'subject', 'body'],
          },
        },
        {
          name: 'search_emails',
          description: 'Search emails in Gmail',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'Gmail search query (e.g., "from:user@example.com subject:invoice")',
              },
              max_results: {
                type: 'number',
                description: 'Maximum number of results to return',
                default: 10,
              },
            },
            required: ['query'],
          },
        },
        {
          name: 'get_email',
          description: 'Get full details of a specific email by ID',
          inputSchema: {
            type: 'object',
            properties: {
              email_id: {
                type: 'string',
                description: 'Gmail message ID',
              },
            },
            required: ['email_id'],
          },
        },
        {
          name: 'mark_as_read',
          description: 'Mark an email as read',
          inputSchema: {
            type: 'object',
            properties: {
              email_id: {
                type: 'string',
                description: 'Gmail message ID',
              },
            },
            required: ['email_id'],
          },
        },
      ],
    }));

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (!this.gmail) {
        const initialized = await this.initializeGmail();
        if (!initialized) {
          throw new Error('Failed to initialize Gmail API');
        }
      }

      switch (request.params.name) {
        case 'send_email':
          return await this.handleSendEmail(request.params.arguments);
        case 'draft_email':
          return await this.handleDraftEmail(request.params.arguments);
        case 'search_emails':
          return await this.handleSearchEmails(request.params.arguments);
        case 'get_email':
          return await this.handleGetEmail(request.params.arguments);
        case 'mark_as_read':
          return await this.handleMarkAsRead(request.params.arguments);
        default:
          throw new Error(`Unknown tool: ${request.params.name}`);
      }
    });
  }

  createEmailMessage(to, subject, body, cc = '', bcc = '') {
    const messageParts = [
      `To: ${to}`,
      cc ? `Cc: ${cc}` : '',
      bcc ? `Bcc: ${bcc}` : '',
      `Subject: ${subject}`,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset=utf-8',
      '',
      body,
    ].filter(Boolean);

    const message = messageParts.join('\n');
    return Buffer.from(message).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  }

  async handleSendEmail(args) {
    const { to, subject, body, cc, bcc, dry_run } = args;

    try {
      if (dry_run) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                status: 'dry_run',
                message: 'Email validated successfully (not sent)',
                details: {
                  to,
                  subject,
                  body_length: body.length,
                  cc: cc || 'none',
                  bcc: bcc || 'none',
                },
              }, null, 2),
            },
          ],
        };
      }

      const encodedMessage = this.createEmailMessage(to, subject, body, cc, bcc);

      const response = await this.gmail.users.messages.send({
        userId: 'me',
        requestBody: {
          raw: encodedMessage,
        },
      });

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'success',
              message: 'Email sent successfully',
              email_id: response.data.id,
              thread_id: response.data.threadId,
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'error',
              message: error.message,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  }

  async handleDraftEmail(args) {
    const { to, subject, body } = args;

    try {
      const encodedMessage = this.createEmailMessage(to, subject, body);

      const response = await this.gmail.users.drafts.create({
        userId: 'me',
        requestBody: {
          message: {
            raw: encodedMessage,
          },
        },
      });

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'success',
              message: 'Draft created successfully',
              draft_id: response.data.id,
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'error',
              message: error.message,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  }

  async handleSearchEmails(args) {
    const { query, max_results = 10 } = args;

    try {
      const response = await this.gmail.users.messages.list({
        userId: 'me',
        q: query,
        maxResults: max_results,
      });

      const messages = response.data.messages || [];

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'success',
              count: messages.length,
              messages: messages.map(msg => ({
                id: msg.id,
                thread_id: msg.threadId,
              })),
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'error',
              message: error.message,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  }

  async handleGetEmail(args) {
    const { email_id } = args;

    try {
      const response = await this.gmail.users.messages.get({
        userId: 'me',
        id: email_id,
        format: 'full',
      });

      const headers = response.data.payload.headers;
      const subject = headers.find(h => h.name === 'Subject')?.value || 'No Subject';
      const from = headers.find(h => h.name === 'From')?.value || 'Unknown';
      const date = headers.find(h => h.name === 'Date')?.value || 'Unknown';

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'success',
              email: {
                id: response.data.id,
                thread_id: response.data.threadId,
                subject,
                from,
                date,
                snippet: response.data.snippet,
              },
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'error',
              message: error.message,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  }

  async handleMarkAsRead(args) {
    const { email_id } = args;

    try {
      await this.gmail.users.messages.modify({
        userId: 'me',
        id: email_id,
        requestBody: {
          removeLabelIds: ['UNREAD'],
        },
      });

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'success',
              message: 'Email marked as read',
              email_id,
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              status: 'error',
              message: error.message,
            }, null, 2),
          },
        ],
        isError: true,
      };
    }
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Email MCP Server running on stdio');
  }
}

const server = new EmailMCPServer();
server.run().catch(console.error);
