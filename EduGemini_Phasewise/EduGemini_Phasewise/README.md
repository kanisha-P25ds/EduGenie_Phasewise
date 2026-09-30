# EDUGENIE – 8-PHASE PROJECT DOCUMENTATION

Team Members:
1.Kanisha P (Team Leader)
2.Janavikaa G.J
3.Sathana S
4.Suvitha S


## Project Overview
EduGenie is an AI-powered learning assistant that brings Question Answering, Concept Explanation, Quiz Generation, Text Summarization, and Learning Path Generation into one web application.

The documented implementation uses FastAPI as the backend, HTML/CSS for the web interface, Gemini 3.5 Flash for cloud-based generation functions, and LaMini-Flan-T5-783M locally for concept explanation.

## Phase 1: Brainstorming & Ideation
The project identifies learning-support needs around academic questions, difficult concepts, self-assessment, revision and structured learning. These needs are mapped to five core modules.

## Phase 2: Requirement Analysis
Functional requirements cover the five learning modules, web interface and FastAPI routing. Non-functional requirements cover usability, maintainability, credential security, availability, performance considerations and extensibility.

## Phase 3: Project Design
EduGenie follows a modular client-server architecture. The browser communicates with FastAPI, which routes requests to the appropriate learning module. Gemini 3.5 Flash handles cloud-based generation functions while LaMini-Flan-T5-783M handles local concept explanation.

## Phase 4: Project Planning
The project is organized into ideation, requirements, design, planning, development, testing, documentation and demonstration milestones.

## Phase 5: Project Development
The implementation is divided into `main.py`, `gemini_client.py`, `qna.py`, `explanation_module.py`, `quiz_module.py`, `summary_module.py`, and `learning_path.py`, with `templates/index.html` and `static/style.css` providing the frontend.

## Phase 6: Project Testing
Testing covers application startup, interface loading, each learning module, AI response availability, local model requirements and configuration safety. The source documentation does not provide numerical benchmark measurements, so none are invented here.

## Phase 7: Project Documentation
The documentation set includes the project aim, algorithm, results, setup instructions, project structure, technology stack, AI model setup, core modules and future enhancements.

## Phase 8: Project Demonstration
The recommended demonstration sequence introduces the project and then demonstrates Q&A, concept explanation, quiz generation, summarization and learning-path generation, followed by architecture and future-scope explanation.

## Setup:
```bash
python -m venv venv
pip install -r requirements.txt
```

Configure the Gemini key locally:
```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run:
```bash
uvicorn main:app --reload
```

Open:
```text
http://127.0.0.1:8000
```

## Conclusion:
EduGenie provides a modular foundation for an intelligent digital learning assistant. Its documented architecture separates frontend interaction, FastAPI routing, learning modules and AI services, allowing the application to support multiple educational workflows within one interface.

## Security Note:
The real `.env` file/API key is intentionally not included in this package. Use `.env.example` and configure the actual credential locally.
