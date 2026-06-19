---
name: Yuki Engineering Loop
description: Use this skill for human-reviewed coding work in a repository. It turns vibe coding into a staged engineering loop: repo scan, requirement card, minimal plan, implementation log, tests, review, and lessons learned. Use it when the user asks to analyze, plan, implement, refactor, debug, or review code with Codex or another coding agent.
---

# Yuki Engineering Loop

This skill packages a human-reviewed coding workflow. It is designed for projects where the user wants AI assistance but still wants to approve each stage manually.

The core idea:

```txt
Read first.
Plan small.
Change one step.
Record evidence.
Review before moving on.
```

## When to use this skill

Use this skill when the user asks for any of the following:

- analyze an unfamiliar repository before coding
- convert a new requirement into small implementation steps
- implement a feature with strict human approval gates
- refactor code while avoiding uncontrolled broad changes
- debug or fix a bug with a written investigation trail
- produce Markdown engineering records for every change
- use Codex / coding agents in a controlled vibe coding workflow

Do not use this skill for casual explanation, pure learning notes, or one-off code snippets that are not tied to a repository.

## Operating modes

### 1. Scan Mode

Goal: understand the repository without changing code.

Allowed:

- read files
- summarize architecture
- identify build and test commands
- identify risk areas
- produce Markdown reports

Forbidden:

- editing source files
- formatting files
- running destructive commands
- changing dependencies

Output:

```txt
.ai/reports/<task>/00_repo_scan.md
```

Human gate:

Stop after producing the report and wait for approval or the next user instruction.

### 2. Planning Mode

Goal: convert the user's requirement into a small, testable implementation plan.

Allowed:

- read existing repo scan and project files
- clarify goals, non-goals, constraints, and acceptance criteria
- split the work into minimal steps
- define test and rollback methods

Forbidden:

- editing source files
- starting implementation
- broad refactor proposals unless explicitly required

Outputs:

```txt
.ai/reports/<task>/01_requirement_card.md
.ai/reports/<task>/02_plan.md
```

Human gate:

Stop after the plan. Do not implement until the user explicitly approves a step.

### 3. Implementation Mode

Goal: implement exactly one approved step.

Allowed:

- modify only files named or implied by the approved step
- run safe build/test commands when available
- update implementation logs and test reports

Forbidden:

- implementing multiple steps at once
- modifying unrelated files
- broad formatting changes
- silent design changes
- changing public interfaces unless the approved plan says so

Outputs:

```txt
.ai/reports/<task>/03_implementation_log.md
.ai/reports/<task>/04_test_report.md
```

Human gate:

Stop after each step. Summarize the diff, tests, risk, and next recommended step.

### 4. Review Mode

Goal: inspect the current diff against the requirement and plan.

Allowed:

- compare changes to acceptance criteria
- identify out-of-scope edits
- identify coupling and complexity risks
- recommend merge, revision, manual test, or redesign

Output:

```txt
.ai/reports/<task>/05_review.md
```

Human gate:

Stop after review. Do not continue implementation unless asked.

### 5. Lessons Mode

Goal: turn the task into reusable project knowledge.

Output:

```txt
.ai/reports/<task>/06_lessons.md
```

Capture:

- project rules discovered
- reusable patterns
- anti-patterns
- follow-up tasks
- personal notes

## Required stage order

Default order:

```txt
0. Repo Scan
1. Requirement Card
2. Minimal Implementation Plan
3. Implementation Log
4. Test Report
5. Review
6. Lessons Learned
```

A later stage may reference an earlier report, but should not skip human approval gates unless the user explicitly asks to compress the workflow.

## Change budget

For each implementation step:

- prefer 1 to 3 source files
- avoid unrelated changes
- avoid mass formatting
- avoid dependency changes
- avoid hidden behavior changes
- update the plan first if the current plan becomes invalid

## Evidence requirements

Every implementation step must record:

- modified files
- what changed
- why it changed
- expected effect
- possible risk
- commands run
- test result
- skipped tests and reasons

Never claim a test passed unless it actually ran and produced that result.

## Output style

Use Markdown. Prefer concise engineering notes over long essays.

Write reports in the user's language unless the repository already uses a different documentation language. For prompt templates and agent-facing instructions, English is acceptable and usually preferred.

## References

Use the templates in:

```txt
references/templates.md
```

Use the reusable prompt entries in:

```txt
references/prompts.md
```
