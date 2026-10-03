# Saudi Legal AI Platform

## Overview
A smart legal platform tailored for the Saudi legal environment. It combines:
- 3D courtroom simulation
- legal case analysis
- AI-powered strategy generation
- training scenarios
- responsive dashboards
- multi-input legal processing

## Features
- Case intake via text, audio, video, images, and documents
- Three AI modes:
  - Full AI
  - AI Assisted
  - User Only
- Legal classification and risk analysis
- Linkage to Saudi legal frameworks and precedents
- 3D courtroom visual experience
- Training scenarios for legal education
- Dashboard with analytics and reporting

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- AI layer: Python + Anthropic API compatible integration
- Data: JSON/SQLite ready structure
- 3D visuals: CSS-based mockup + extensible for Three.js

## Project Structure
```text
saudi-law-3d-courtroom/
├── README.md
├── package.json
├── .env.example
├── .gitignore
├── index.html
├── styles.css
├── script.js
├── docs/
│   ├── system-spec.md
│   └── INSTALLATION.md
├── frontend/
│   ├── dashboard.html
│   ├── dashboard.css
│   ├── dashboard.js
│   └── assets/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── legal_ai_system.py
│   ├── api/
│   │   └── client.js
│   └── data/
│       └── saudi_legal_db.json
├── tests/
│   ├── test_case_analysis.py
│   └── test_input_processing.py
└── screenshots/
    └── .gitkeep
```

## Quick Start
1. Clone the repo
2. Create a virtual environment
3. Install backend dependencies
4. Copy `.env.example` to `.env`
5. Update your API key
6. Run:

```bash
python backend/app.py
```

Then open:

```text
http://localhost:5000
```

## AI Modes
### Full AI
System makes decisions independently.

### AI Assisted
System suggests and user reviews/adjusts.

### User Only
System provides information and the user makes the decision.

## Deployment Notes
This project is structured for local development and can be extended to production deployment with:
- secure API layer
- persistent database
- auth system
- cloud deployment
- production AI configuration

## Legal Scope
This is a conceptual platform prototype for legal workflow and smart assistance. It does not replace legal counsel or official legal advisement.

## License
MIT
