# Agent Skill: Create Task Plan

**Skill ID:** `create_task_plan`
**Version:** 1.0
**Category:** Planning & Strategy
**Priority:** Medium

---

## 📋 Description

This skill creates detailed action plans for tasks that require approval, complex multi-step processes, or strategic decision-making. Plans are saved in the `/Plans` folder for user review and approval.

---

## 🎯 Purpose

- Break down complex tasks into actionable steps
- Identify risks and dependencies
- Estimate effort and resources needed
- Provide clear approval requests
- Document decision rationale

---

## 📥 Input Requirements

### Required Inputs
- Task description or task file reference
- Task context (what needs to be done and why)
- Access to relevant files and documentation

### Optional Inputs
- Deadline or time constraints
- Specific constraints or requirements
- Preferred approach or methodology
- Risk tolerance level

---

## 📤 Output Format

### Plan Document Structure
```markdown
# Action Plan: [Task Name]

**Plan ID:** [unique_id]
**Created:** [timestamp]
**Status:** Awaiting Approval
**Priority:** [P0/P1/P2/P3]

---

## 📋 Executive Summary

[2-3 sentence overview of what this plan accomplishes]

---

## 🎯 Objectives

- Primary Goal: [main objective]
- Secondary Goals: [supporting objectives]
- Success Criteria: [how we measure success]

---

## 📊 Current Situation

### Context
[What's the current state and why this is needed]

### Constraints
- Time: [deadline or time constraints]
- Resources: [what's available]
- Dependencies: [what this depends on]
- Risks: [potential issues]

---

## 🔧 Proposed Approach

### Option 1: [Approach Name] (Recommended)
**Description:** [What this approach involves]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Option 2: [Alternative Approach]
[Same structure as Option 1]

---

## 📝 Detailed Action Steps

### Phase 1: [Phase Name]
**Goal:** [What this phase accomplishes]

1. **[Step Name]**
   - Action: [What to do]
   - Requires Approval: [Yes/No]
   - Risk Level: [Low/Medium/High]
   - Estimated Effort: [Time estimate]

2. **[Step Name]**
   [Same structure]

### Phase 2: [Phase Name]
[Same structure as Phase 1]

---

## ⚠️ Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| [Risk 1] | [Low/Med/High] | [Low/Med/High] | [How to mitigate] |
| [Risk 2] | [Low/Med/High] | [Low/Med/High] | [How to mitigate] |

---

## ✅ Approval Required For

- [ ] [Action requiring approval 1]
- [ ] [Action requiring approval 2]
- [ ] [Action requiring approval 3]

---

## 📋 Checklist for Execution

- [ ] Pre-requisites completed
- [ ] User approval obtained
- [ ] Resources available
- [ ] Backup created (if applicable)
- [ ] Ready to execute

---

## 📝 Notes & Considerations

[Additional context, assumptions, or important notes]

---

## 🔄 Next Steps

**If Approved:**
1. [What happens next]
2. [Follow-up actions]

**If Rejected:**
1. [Alternative actions]
2. [How to proceed]

---

**Plan Created By:** AI Employee
**Awaiting Approval From:** User
**Plan File:** `[filename]`
```

---

## 🔧 Planning Logic

### Step 1: Analyze Task
```
1. Read task description
2. Identify task type (code change, process, research, etc.)
3. Assess complexity (simple, moderate, complex)
4. Check Company_Handbook for approval requirements
5. Identify stakeholders and dependencies
```

### Step 2: Research Context
```
1. Read relevant files
2. Check existing documentation
3. Review similar past tasks (if any)
4. Identify constraints and requirements
5. Gather necessary information
```

### Step 3: Generate Options
```
1. Brainstorm 2-3 approaches
2. Evaluate pros/cons of each
3. Identify recommended approach
4. Document rationale
```

### Step 4: Break Down Steps
```
1. Divide work into phases
2. List specific actions for each phase
3. Identify approval points
4. Estimate effort for each step
5. Note dependencies between steps
```

### Step 5: Assess Risks
```
1. Identify potential problems
2. Rate likelihood and impact
3. Propose mitigation strategies
4. Flag high-risk items
```

### Step 6: Create Plan Document
```
1. Format plan using template
2. Include all necessary sections
3. Make approval requirements clear
4. Save to /Plans folder
5. Update Dashboard with approval request
```

---

## 💡 Example Usage

### Example 1: Code Modification Plan

**Input:** Task to fix bug in authentication system

**Plan Created:**
```markdown
# Action Plan: Fix Authentication Bug

**Plan ID:** plan_auth_fix_20260211
**Created:** 2026-02-11 16:00:00
**Status:** Awaiting Approval
**Priority:** P1 - High

---

## 📋 Executive Summary

Fix critical authentication bug causing users to be logged out unexpectedly.
Requires modifying auth.py and session_manager.py with proper testing.

---

## 🎯 Objectives

- Primary Goal: Resolve logout bug affecting 15% of users
- Secondary Goals: Add logging to prevent future issues
- Success Criteria: Zero unexpected logouts in 24hr test period

---

## 🔧 Proposed Approach

### Option 1: Fix Session Timeout Logic (Recommended)

**Description:** Modify session timeout calculation in session_manager.py
to properly handle timezone differences.

**Pros:**
- Minimal code changes
- Low risk of side effects
- Can be deployed quickly

**Cons:**
- Doesn't address root cause of timezone handling

**Steps:**
1. Modify session timeout calculation
2. Add timezone normalization
3. Update unit tests
4. Deploy to staging for testing

---

## 📝 Detailed Action Steps

### Phase 1: Code Changes
1. **Modify session_manager.py**
   - Action: Update timeout calculation (lines 45-52)
   - Requires Approval: YES (code modification)
   - Risk Level: Medium
   - Estimated Effort: 30 minutes

2. **Add logging**
   - Action: Insert debug logging for session events
   - Requires Approval: YES (code modification)
   - Risk Level: Low
   - Estimated Effort: 15 minutes

### Phase 2: Testing
1. **Run unit tests**
   - Action: Execute test suite
   - Requires Approval: NO
   - Risk Level: Low
   - Estimated Effort: 10 minutes

---

## ⚠️ Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Breaking existing sessions | Low | High | Test thoroughly in staging first |
| Timezone edge cases | Medium | Medium | Add comprehensive timezone tests |

---

## ✅ Approval Required For

- [ ] Modify session_manager.py (lines 45-52)
- [ ] Modify auth.py (add logging)
- [ ] Deploy to staging environment

---

**Awaiting User Approval**
```

### Example 2: Process Improvement Plan

**Input:** Task to automate weekly report generation

**Plan Created:**
```markdown
# Action Plan: Automate Weekly Reports

**Plan ID:** plan_weekly_reports_20260211
**Created:** 2026-02-11 16:30:00
**Status:** Awaiting Approval
**Priority:** P2 - Medium

---

## 📋 Executive Summary

Create automated system to generate weekly activity reports every Friday,
reducing manual effort from 2 hours to 5 minutes.

---

## 🎯 Objectives

- Primary Goal: Automate weekly report generation
- Secondary Goals: Improve report consistency and accuracy
- Success Criteria: Reports generated automatically with <5% error rate

---

## 🔧 Proposed Approach

### Option 1: Python Script + Scheduler (Recommended)

**Description:** Create Python script that aggregates data from logs
and generates markdown report, scheduled via cron/Task Scheduler.

**Pros:**
- Fully automated
- Easy to modify and extend
- Uses existing log data

**Cons:**
- Requires initial setup time
- Needs scheduler configuration

**Steps:**
1. Create report generation script
2. Test with historical data
3. Set up scheduler
4. Monitor first few runs

---

## 📝 Detailed Action Steps

### Phase 1: Script Development
1. **Create report_generator.py**
   - Action: Write script to parse logs and generate report
   - Requires Approval: NO (new file, no system changes)
   - Risk Level: Low
   - Estimated Effort: 2 hours

### Phase 2: Scheduling
1. **Configure Task Scheduler**
   - Action: Set up weekly execution
   - Requires Approval: YES (system configuration)
   - Risk Level: Low
   - Estimated Effort: 30 minutes

---

## ✅ Approval Required For

- [ ] Configure Windows Task Scheduler for weekly execution
- [ ] Email reports automatically (if desired)

---

**Awaiting User Approval**
```

---

## 🚨 Error Handling

### Insufficient Information
```
- Request additional details from user
- Document assumptions made
- Flag uncertainties in plan
- Provide multiple options
```

### Conflicting Requirements
```
- Identify conflicts clearly
- Present trade-offs
- Request user decision
- Document chosen approach
```

### High Risk Task
```
- Highlight risks prominently
- Require explicit approval
- Suggest safer alternatives
- Recommend testing strategy
```

---

## 📊 Success Criteria

- ✅ Plan is clear and actionable
- ✅ All approval points identified
- ✅ Risks assessed and documented
- ✅ Multiple options provided (when applicable)
- ✅ Steps are specific and measurable
- ✅ Plan saved to /Plans folder
- ✅ Dashboard updated with approval request

---

## 🔄 Integration Points

### Reads From:
- `/Needs_Action/*.md` - Task files
- `Company_Handbook.md` - Approval rules
- Relevant source files for context

### Writes To:
- `/Plans/*.md` - Plan documents
- `Dashboard.md` - Approval notifications
- `/Logs/*.md` - Planning activity

### Triggers:
- Task requires approval (per handbook)
- Complex multi-step task detected
- User explicitly requests plan
- High-risk action identified

---

## 📝 Notes

- Always provide at least 2 options when feasible
- Be realistic about effort estimates
- Highlight approval requirements clearly
- Document assumptions and constraints
- Keep plans concise but complete
- Use clear, non-technical language when possible

---

**Last Updated:** 2026-02-11
