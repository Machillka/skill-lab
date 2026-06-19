# skill-lab

A personal laboratory for reusable AI coding workflows, agent skills, and prompt protocols.

当前仓库用于沉淀可复用的 AI / Agent / Codex 工作流。

## Skills

### Yuki Engineering Loop

Path:

```txt
skills/yuki-engineering-loop/SKILL.md
```

Purpose:

- package a human-reviewed vibe coding workflow
- force repo scan before implementation
- convert requirements into minimal implementation plans
- require approval gates between stages
- record implementation logs, test evidence, review notes, and lessons learned

Recommended use:

```txt
Use the Yuki Engineering Loop skill.
First run repo scan only. Do not modify code.
```

Then continue stage by stage:

```txt
Use the Yuki Engineering Loop skill.
Create the requirement card and minimal plan for this feature. Do not edit code yet.
```

```txt
Use the Yuki Engineering Loop skill.
Implement only Step 1 from the approved plan, then update the implementation log and test report.
```

## Repository Layout

```txt
skills/
  yuki-engineering-loop/
    SKILL.md
    references/
      templates.md
      prompts.md
    examples/
      task-report-example.md
```
