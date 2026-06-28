````markdown
# Production AI Todo Assistant

This project is a production-ready AI-powered Todo Assistant developed using Python and Flask. It started as a simple Todo API and was gradually improved by adding AI reasoning, context management, confidence evaluation, source tracking, error handling, and production validation.

The main goal of this project is not just to retrieve todo items, but to demonstrate how an AI agent can process information responsibly by maintaining context, checking confidence, tracking data provenance, and deciding whether a response should be accepted or escalated.

---

## Features

- REST API built using Flask
- AI Agent for processing todo requests
- Context management
- Confidence scoring
- Source attribution (Provenance)
- Escalation decision support
- Failure handling
- Structured API responses
- Unit testing
- Production scenario testing

---

# Project Structure

```
Production-AI-Todo-Assistant/
│
├── app/
│   ├── models/
│   │   └── todo.py
│   │
│   ├── routes/
│   │   └── todos.py
│   │
│   ├── services/
│   │   └── todo_service.py
│   │
│   ├── ai_agent.py
│   ├── action_checker.py
│   ├── case_facts.py
│   ├── confidence.py
│   ├── context_manager.py
│   ├── escalation.py
│   ├── errors.py
│   ├── failure_handler.py
│   ├── provenance.py
│   └── responses.py
│
├── tests/
│   ├── test_api.py
│   └── scenarios.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Project Workflow

### Step 1

A request is received through the Flask API.

↓

### Step 2

The Todo Service retrieves the requested Todo item.

↓

### Step 3

The AI Agent processes the Todo.

↓

### Step 4

Case facts are generated.

↓

### Step 5

Relevant context is collected.

↓

### Step 6

Source attribution is stored using the Provenance module.

↓

### Step 7

Confidence score is calculated.

↓

### Step 8

Action Checker verifies whether the AI response is acceptable.

↓

### Step 9

Escalation module determines whether human review is required.

↓

### Step 10

A structured JSON response is returned.

---

# Modules

## Todo Model

Represents each todo item with

- ID
- Title
- Completion Status

---

## Todo Service

Responsible for retrieving todo information.

---

## AI Agent

Acts as the central controller.

It combines outputs from every module and produces the final response.

---

## Context Manager

Maintains contextual information used by the AI.

Example

- Retrieved Todo 1
- Retrieved Todo 2
- Retrieved Todo 3

---

## Case Facts

Converts todo information into structured facts.

Example

```
Todo ID
Title
Completed Status
```

---

## Provenance

Tracks where information came from.

Example

```
TodoService
TodoService
TodoService
```

This improves transparency and explainability.

---

## Confidence

Calculates confidence for every AI response.

Example

```
Approved : True

Score : 0.95

Threshold : 0.80
```

---

## Action Checker

Determines whether the generated response should be accepted.

Returns

```
True
```

or

```
False
```

---

## Escalation

Checks whether human intervention is required.

Returns

```
True
```

or

```
False
```

---

## Failure Handler

Provides graceful handling for unexpected situations.

---

## Response Formatter

Creates a structured JSON response containing

- Todo
- Case Facts
- Context
- Sources
- Confidence
- Action
- Escalation

---

# API Response Example

```json
{
  "ok": true,
  "data": {
    "todo": {
      "id": "1",
      "title": "Learn Claude Code",
      "completed": false
    },
    "case_facts": "...",
    "context": [
      "Retrieved Todo 1"
    ],
    "sources": [
      "TodoService"
    ],
    "confidence": {
      "approved": true,
      "score": 0.95,
      "threshold": 0.80
    },
    "action": true,
    "escalate": false
  }
}
```

---

# Installation

Clone the project

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Production-AI-Todo-Assistant
```

Create virtual environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask server

```bash
python app.py
```

Server

```
http://127.0.0.1:5000
```

---

# API Endpoints

Retrieve Todo

```
GET /todos/<id>
```

Example

```
http://127.0.0.1:5000/todos/1
```

---

# Running Unit Tests

```bash
python -m unittest tests.test_api
```

---

# Running Production Workflow

```bash
python -m tests.scenarios
```

---

# Expected Outputs

### API Response

Returns structured JSON containing

- Todo
- Case Facts
- Context
- Sources
- Confidence
- Action
- Escalation

---

### Unit Test

```
Ran 2 tests

OK
```

---

### Scenario Execution

Runs all production scenarios and prints the AI processing results.

Final output

```
All 8 production scenarios completed successfully.
```

---

# Technologies Used

- Python
- Flask
- REST API
- Object-Oriented Programming
- JSON
- unittest

---

# Author
## J. Deepakkumar