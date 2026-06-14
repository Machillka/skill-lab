---
name: learning-note
description: Turn a technical, conceptual, creative, or learning topic into Machillka's structured learning note. Use when the user asks what something is, why it exists, how to use it, how it differs from similar concepts, how it fits into a workflow, or asks to form notes. Do not use for email rewriting, translation-only tasks, debugging logs, git diff review, image critique, or implementation planning.
license: MIT
metadata:
    author: Machillka
    version: "0.1.0"
---

# Learning Note

## Purpose

Transform a concept into a structured learning note.

This skill is for understanding and note formation, not for project implementation, debugging, or code review.

## When To Use

Use this skill when the request is about:

- explaining a concept
- forming notes
- understanding "what / why / how"
- comparing similar concepts
- building a learning path
- connecting a concept to a personal workflow

Typical inputs:

- "KV Cache 是什么？形成笔记"
- "Agent Runtime 和 Tool / MCP 有什么区别？"
- "FOV 和视锥体的关系是什么？"
- "pyproject.toml 是什么规范？"

## When Not To Use

Do not use this skill when the task is mainly:

- rewriting an email or message
- translating a paragraph only
- debugging compiler errors or runtime logs
- reviewing git diff
- analyzing an image
- writing implementation code
- making a full project plan

If the user asks for implementation planning, use a task-brief or implementation-planning workflow instead.

## Output Contract

Always output with these sections:

### 1. 是什么

Give a direct definition.

### 2. 为什么需要它

Explain the pain point or problem that makes the concept necessary.

### 3. 它解决了什么问题

Explain the concrete problem it solves.

### 4. 怎么使用

Give a practical usage path.

### 5. 和相似概念的区别

Compare it with nearby concepts.

### 6. 常见误区

List common misunderstandings.

### 7. 最小练习

Give one small exercise that can be completed quickly.

## Style Rules

- Use Chinese by default.
- Be structured and direct.
- Prefer concrete examples over vague descriptions.
- Do not flatter.
- Do not expand into a full project plan unless explicitly asked.
- If the topic is too broad, reduce it to the smallest useful learning slice.
