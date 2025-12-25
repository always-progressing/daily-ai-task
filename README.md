# daily-ai-task
A system that converts daily AI news into executable learning tasks.

## Core Idea
- AI news → actionable tasks
- Focus on "what to do today"

## MVP Scope
- Daily task list
- Task completion tracking
- No learning courses

## Tech Stack
FastAPI / SQLite / LLM API

## Local run (health check)
`uvicorn app.main:app --reload`
visit http://127.0.0.1:8000/health
