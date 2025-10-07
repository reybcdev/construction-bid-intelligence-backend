"""
FastAPI Backend for Construction Bid Intelligence Platform Demo
Mock implementation for demonstration purposes
"""

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import mock_data

app = FastAPI(title="Construction Bid Intelligence API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    user: dict

# Routes

@app.get("/")
def root():
    return {"message": "Construction Bid Intelligence API", "status": "running"}

@app.post("/api/auth/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """Mock login endpoint"""
    if request.email == "demo@ntsprint.com" and request.password == "demo123":
        return {
            "access_token": "mock_jwt_token_12345",
            "user": {
                "id": 1,
                "email": "demo@ntsprint.com",
                "full_name": "John Doe"
            }
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/api/dashboard/stats")
def get_dashboard_stats():
    """Get dashboard statistics"""
    return {
        "total_documents": 3,
        "analyzed": 3,
        "pending": 0,
        "average_risk_score": 6.3
    }

@app.get("/api/reports")
def get_reports():
    """Get all reports"""
    return {"reports": mock_data.get_mock_reports(), "total": 3}

@app.get("/api/reports/{report_id}")
def get_report(report_id: int):
    """Get specific report details"""
    report = mock_data.get_report_detail(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@app.post("/api/reports/compare")
def compare_reports(report_ids: List[int]):
    """Compare multiple reports"""
    if len(report_ids) < 2 or len(report_ids) > 5:
        raise HTTPException(status_code=400, detail="Must compare 2-5 reports")
    
    reports = [mock_data.get_report_detail(rid) for rid in report_ids]
    reports = [r for r in reports if r]  # Filter None values
    
    if len(reports) != len(report_ids):
        raise HTTPException(status_code=404, detail="Some reports not found")
    
    return {"reports": reports, "count": len(reports)}

@app.post("/api/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    """Mock document upload"""
    return {
        "message": "Document uploaded successfully",
        "document_id": 4,
        "status": "processing",
        "filename": file.filename
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
