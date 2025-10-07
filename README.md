# Construction Bid Intelligence Platform - Backend

FastAPI backend for AI-powered construction bid document analysis.

## 🚀 Features

- **Authentication API** - JWT-based secure login
- **Dashboard Statistics** - Real-time bid analysis metrics
- **Reports Management** - List, detail, and comparison endpoints
- **Document Upload** - PDF document processing
- **Mock Data** - 3 comprehensive pre-analyzed reports for demo

## 📋 Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

## 🛠️ Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃 Running the Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload --port 8000

# Or using the main script
python main.py
```

Server will be available at: http://localhost:8000

API documentation: http://localhost:8000/docs

## 📚 API Endpoints

### Authentication
- `POST /api/auth/login` - User login (returns JWT token)

### Dashboard
- `GET /api/dashboard/stats` - Get statistics

### Reports
- `GET /api/reports` - List all reports
- `GET /api/reports/{id}` - Get detailed report
- `POST /api/reports/compare` - Compare multiple reports

### Documents
- `POST /api/documents/upload` - Upload bid document

## 🔐 Demo Credentials

- **Email:** demo@ntsprint.com
- **Password:** demo123

## 📊 Sample Data

The backend includes 3 pre-analyzed bid reports:
1. Minneapolis Regional Medical Center (Medium-High Risk)
2. Interstate 35 North Expansion (Low-Medium Risk)
3. Rochester STEM Academy Campus (High Risk)

## 🏗️ Project Structure

```
backend/
├── main.py              # FastAPI application & routes
├── mock_data.py         # Sample report data
├── requirements.txt     # Python dependencies
└── README.md
```

## 🔧 Environment Variables

No environment variables required for demo mode.

For production:
- `OPENAI_API_KEY` - OpenAI API key for AI analysis
- `SECRET_KEY` - JWT secret key
- `DATABASE_URL` - PostgreSQL connection string

## 📝 License

MIT

## 👤 Author

Reynier Bauta Camejo - SDE II
