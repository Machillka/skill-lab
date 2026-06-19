# Yuki Engineering Loop Templates

These templates are used by `Yuki Engineering Loop`.

## 00 Repo Scan

```md
# Repo Scan

## Project Overview

Briefly describe the project, stack, and apparent goal.

## Directory Map

| Path | Purpose | Notes |
|---|---|---|
| `path/` | purpose | notes |

## Core Modules

Describe the important modules, classes, services, components, or packages.

## Entry Points

List program, tool, app, or framework entry points.

## Build and Test Commands

| Command | Purpose | Confidence |
|---|---|---|
| `command` | purpose | confirmed / inferred / unknown |

## Risk Areas

- area: reason

## Unknowns

- unknown item and why it matters
```

## 01 Requirement Card

```md
# Requirement Card

## User Request

Restate the user's request.

## Goal

Define the actual goal of this task.

## Non-goals

- What this task explicitly will not do.

## Acceptance Criteria

- [ ] Observable and testable criterion 1
- [ ] Observable and testable criterion 2
- [ ] Observable and testable criterion 3

## Constraints

- technical constraints
- style constraints
- file/change constraints
- platform constraints

## Related Files

- `path/to/file`

## Open Questions

- question, or `None`
```

## 02 Implementation Plan

```md
# Implementation Plan

## Strategy

Explain the overall approach.

## Step List

### Step 1: Name

Purpose: why this step exists.  
Files: likely files to modify.  
Change: the smallest meaningful change.  
Boundary: what not to do.  
Test: how to verify.  
Rollback: how to revert.

### Step 2: Name

Purpose:  
Files:  
Change:  
Boundary:  
Test:  
Rollback:  

## Change Budget

- Prefer 1 to 3 source files per step.
- Do not perform unrelated refactors.
- Do not change public interfaces unless this plan explicitly says so.
- If the plan becomes invalid, update this document before editing code.

## Risk Control

- risk: mitigation
```

## 03 Implementation Log

```md
# Implementation Log

## Step N: Name

### Modified Files

- `path/to/file`

### What Changed

Describe the actual change.

### Why

Explain the reason.

### Effect

Describe the expected effect on the system.

### Risk

List possible risks.

### Test

List tests or commands run.

### Result

Record actual result.

### Notes

Additional observations.
```

## 04 Test Report

```md
# Test Report

## Automated Tests

| Command | Result | Notes |
|---|---|---|
| `command` | pass / fail / skipped | notes |

## Manual Tests

| Case | Steps | Expected | Actual | Result |
|---|---|---|---|---|
| case | steps | expected | actual | pass / fail / skipped |

## Edge Cases

- [ ] empty / missing input
- [ ] repeated call
- [ ] destroyed / released resource
- [ ] invalid state
- [ ] regression of old behavior

## Known Untested Areas

- area: reason
```

## 05 Review

```md
# Review

## Acceptance Criteria Check

- [ ] criterion: pass / fail / untested

## Diff Summary

Summarize the core diff.

## Out-of-scope Changes

List any changes outside the plan, or `None`.

## Coupling Check

Explain whether new unnecessary coupling was introduced.

## Complexity Check

Explain whether complexity increased and why.

## Regression Risk

List possible regression areas.

## Final Recommendation

Choose one:

- Ready to merge
- Needs manual test
- Needs revision
- Stop and redesign
```

## 06 Lessons Learned

```md
# Lessons Learned

## Project Rules Discovered

- rule

## Reusable Patterns

- pattern

## Anti-patterns

- anti-pattern

## Follow-up Tasks

- [ ] task

## Personal Notes

Write the user's own learning notes, confusions, and insights.
```
