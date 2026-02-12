# Email Triage Skill

**Skill Name:** Email Triage and Response
**Version:** 1.0
**Category:** Communication
**Priority:** High

---

## 🎯 Purpose

Analyze incoming emails, categorize by urgency, draft appropriate responses, and determine if approval is needed before sending.

---

## 📋 Skill Inputs

- Email task file from `/Needs_Action`
- Email metadata (sender, subject, snippet)
- Company_Handbook.md for response guidelines
- Business_Goals.md for context

---

## 🔄 Skill Process

### Step 1: Analyze Email Content
- Read the full email task file
- Identify email type (inquiry, complaint, invoice, meeting request, etc.)
- Determine sender relationship (existing client, new lead, vendor, etc.)
- Extract key information and action items

### Step 2: Categorize Priority
- **P0 (Critical):** System outages, urgent client issues, payment problems
- **P1 (High):** New business inquiries, important deadlines, client requests
- **P2 (Medium):** General inquiries, routine communications
- **P3 (Low):** Newsletters, marketing, non-urgent updates

### Step 3: Draft Response
Based on email type, use appropriate template:

**For Business Inquiries:**
```
Hi [Name],

Thank you for reaching out! I'd be happy to help with [specific need].

[Provide relevant information or next steps]

Would you be available for a brief call this week to discuss further?

Best regards,
[Your Name]
```

**For Client Issues:**
```
Hi [Name],

Thank you for bringing this to my attention. I understand [restate their concern].

I'm looking into this immediately and will have an update for you by [timeframe].

In the meantime, [any immediate actions or workarounds].

Best regards,
[Your Name]
```

**For Meeting Requests:**
```
Hi [Name],

Thanks for the meeting request. I'm available:
- [Option 1]
- [Option 2]
- [Option 3]

Please let me know which works best for you, or suggest an alternative time.

Best regards,
[Your Name]
```

### Step 4: Determine Approval Requirement
**Requires Approval:**
- New client/lead (first contact)
- Pricing or contract discussions
- Commitments over $50
- Sensitive topics (complaints, legal, HR)
- Anything outside standard templates

**No Approval Needed:**
- Routine responses to existing clients
- Acknowledgment emails
- Meeting confirmations
- Information requests (non-sensitive)

### Step 5: Create Output
If approval needed:
- Create approval request in `/Pending_Approval`
- Include drafted response
- Set expiry time (4 hours for urgent, 24 hours for normal)

If no approval needed:
- Create response file in `/Needs_Action` with "READY_TO_SEND" tag
- Log the action

---

## 📤 Skill Outputs

- Drafted email response (markdown format)
- Priority classification
- Approval status (required/not required)
- Recommended send time
- Updated task file with analysis

---

## ✅ Success Criteria

- Email correctly categorized
- Response is professional and on-brand
- All key points addressed
- Appropriate approval workflow triggered
- Response time meets priority guidelines

---

## 🚨 Error Handling

- If email content unclear: Flag for manual review
- If sender unknown: Default to requiring approval
- If multiple issues in one email: Break into separate tasks
- If urgent but complex: Create approval request with short expiry

---

## 📊 Performance Metrics

- Average triage time: < 2 minutes
- Response accuracy: > 95%
- Approval accuracy: > 98% (no unauthorized sends)
- Client satisfaction with responses: > 4.5/5

---

## 💡 Tips for Best Results

1. Always check Company_Handbook for latest response templates
2. Personalize responses - avoid generic copy-paste
3. Include specific details from their email
4. Set clear expectations for next steps
5. When in doubt, require approval

---

## 🔗 Related Skills

- `approval_request_skill.md` - For creating approval requests
- `dashboard_update_skill.md` - For updating task status
- `create_action_plan_skill.md` - For complex multi-step responses

---

**Last Updated:** 2026-02-13
**Skill Owner:** AI Employee System
