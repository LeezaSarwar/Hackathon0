# WhatsApp Response Skill

**Skill Name:** WhatsApp Message Handling
**Version:** 1.0
**Category:** Communication
**Priority:** High

---

## 🎯 Purpose

Analyze WhatsApp messages, draft appropriate responses, route to templates, and handle escalations efficiently.

---

## 📋 Skill Inputs

- WhatsApp task file from `/Needs_Action`
- Message content and sender information
- Company_Handbook.md for response guidelines
- Business_Goals.md for context
- Previous conversation history (if available)

---

## 🔄 Skill Process

### Step 1: Analyze Message

**Identify Message Type:**
- Pricing inquiry
- Order/delivery question
- Technical support
- General inquiry
- Complaint/issue
- Follow-up
- Urgent request

**Assess Sender:**
- Existing client (check history)
- New lead
- Vendor/partner
- Unknown/spam

**Determine Urgency:**
- Immediate (emergency, critical issue)
- High (business inquiry, time-sensitive)
- Medium (general questions)
- Low (casual conversation)

### Step 2: Select Response Template

**For Pricing Inquiries:**
```
Hi [Name]! 👋

Thanks for your interest in [service/product]!

To provide you with an accurate quote, I need a few details:
• [Question 1]
• [Question 2]
• [Question 3]

Once I have this info, I can send you a detailed proposal within 24 hours.

When would be a good time for a quick call to discuss?
```

**For Order/Delivery Questions:**
```
Hi [Name]!

Let me check on that for you right away.

[Provide specific information about order/delivery]

Expected [delivery/completion]: [date/time]

I'll keep you updated on any changes. Anything else I can help with?
```

**For Technical Support:**
```
Hi [Name],

I understand you're experiencing [issue]. Let me help you resolve this.

Can you try these steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Let me know if this works, or if you need further assistance!
```

**For Complaints/Issues:**
```
Hi [Name],

I'm really sorry to hear about [issue]. I completely understand your frustration.

Here's what I'm doing to resolve this:
✅ [Action 1]
✅ [Action 2]
✅ [Action 3]

I'll have an update for you by [specific time].

Thank you for your patience!
```

**For General Inquiries:**
```
Hi [Name]! 👋

Great question!

[Provide clear, concise answer]

Is there anything else you'd like to know?
```

**For Follow-ups:**
```
Hi [Name]!

Just following up on [previous topic].

[Provide update or ask for information]

Let me know if you have any questions!
```

### Step 3: Personalize Response

**Personalization Checklist:**
- Use sender's name
- Reference previous conversations
- Acknowledge specific details from their message
- Match their communication style (formal/casual)
- Add relevant emojis (1-2 per message)
- Keep tone friendly but professional

### Step 4: Determine Approval Requirement

**Requires Approval:**
- First contact with new lead
- Pricing discussions over $100
- Complaints or sensitive issues
- Commitments or promises
- Refunds or compensation
- Anything outside standard templates

**No Approval Needed:**
- Routine questions from existing clients
- Order status updates
- General information
- Acknowledgments
- Meeting confirmations

### Step 5: Handle Escalations

**Escalate to Manual Review if:**
- Message is unclear or ambiguous
- Requires technical expertise beyond scope
- Involves legal or compliance issues
- Sender is angry or threatening
- Request is unusual or suspicious

**Escalation Process:**
1. Create detailed escalation note
2. Flag as "REQUIRES_MANUAL_REVIEW"
3. Notify via Dashboard update
4. Set high priority
5. Provide context and recommendation

---

## 📤 Skill Outputs

- Drafted WhatsApp response
- Approval request (if needed)
- Escalation note (if needed)
- Updated task file with analysis
- Dashboard update

---

## ✅ Success Criteria

- Response is timely (within priority guidelines)
- Message is clear and helpful
- Tone matches brand voice
- All questions answered
- Appropriate approval workflow triggered
- Client satisfaction maintained

---

## 🚨 Error Handling

**If message unclear:**
- Ask clarifying questions
- Don't make assumptions
- Request more details politely

**If outside expertise:**
- Acknowledge the question
- Escalate to appropriate person
- Set clear expectations for response time

**If urgent and complex:**
- Provide immediate acknowledgment
- Create approval request with short expiry
- Offer interim solution if possible

---

## 📊 Performance Metrics

**Target Metrics:**
- Average response time: < 30 minutes
- First response resolution: > 70%
- Client satisfaction: > 4.5/5
- Escalation rate: < 10%

**Quality Metrics:**
- Response accuracy: > 95%
- Template usage: > 80%
- Approval accuracy: > 98%
- Follow-up required: < 20%

---

## 💡 Best Practices

### Do's:
✅ Respond quickly (especially to urgent messages)
✅ Use emojis appropriately (friendly but professional)
✅ Keep messages concise and scannable
✅ Provide specific information and timelines
✅ End with a question or clear next step
✅ Double-check facts before sending

### Don'ts:
❌ Use overly formal language
❌ Send long paragraphs (break into short lines)
❌ Make promises you can't keep
❌ Ignore urgent messages
❌ Use jargon or technical terms unnecessarily
❌ Send without proofreading

---

## 🔗 Related Skills

- `email_triage_skill.md` - Similar triage process
- `approval_request_skill.md` - For creating approvals
- `dashboard_update_skill.md` - For status updates

---

## 📱 WhatsApp-Specific Tips

**Formatting:**
- Use line breaks for readability
- Bullet points with • or emojis
- Bold for emphasis: *text*
- Italic for subtle emphasis: _text_

**Timing:**
- Respond within 30 minutes during business hours
- Set auto-reply for after-hours
- Acknowledge receipt immediately if need time to research

**Tone:**
- More casual than email
- Use emojis (but not excessively)
- Keep it conversational
- Show personality while staying professional

---

## 🕐 Response Time Guidelines

**By Priority:**
- P0 (Critical): < 15 minutes
- P1 (High): < 30 minutes
- P2 (Medium): < 2 hours
- P3 (Low): < 4 hours

**After Hours:**
- Auto-reply: "Thanks for your message! I'll respond first thing tomorrow morning."
- True emergencies: Escalate to manual review

---

**Last Updated:** 2026-02-13
**Skill Owner:** AI Employee System
