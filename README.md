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

# Create .env file from template
cp .env.example .env
# Edit .env with your configuration
```

## 🏃 Running the Server

```bash
# Development mode with auto-reload
python main.py

# Or with uvicorn directly
uvicorn main:app --reload --port 8000
```

Server will be available at: http://localhost:8000

API documentation: http://localhost:8000/docs

## ⚙️ Configuration

The application uses environment variables for configuration. Copy `.env.example` to `.env` and adjust values:

```env
# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# JWT Secret Key (generate with: openssl rand -hex 32)
SECRET_KEY=your-secret-key

# Demo Mode (true for mock data)
DEMO_MODE=true
```

See `.env.example` for all available options.

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
