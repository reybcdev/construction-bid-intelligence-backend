"""
Mock data for Construction Bid Intelligence Platform Demo
Contains 3 pre-analyzed reports for demonstration
"""

from datetime import datetime, timedelta

# Mock user for demo
DEMO_USER = {
    "id": 1,
    "email": "demo@ntsprint.com",
    "full_name": "John Doe",
    "password": "demo123"
}

# Mock reports data (complete dataset at end of file)

def get_mock_reports():
    """Returns all mock reports"""
    return [
        {
            "id": 1,
            "project_name": "Minneapolis Regional Medical Center",
            "client_name": "Minnesota Department of Health",
            "risk_score": 6.5,
            "risk_level": "MEDIUM-HIGH",
            "budget_avg": 2850000,
            "created_at": (datetime.now() - timedelta(days=2)).isoformat(),
        },
        {
            "id": 2,
            "project_name": "Interstate 35 North Expansion",
            "client_name": "Minnesota Department of Transportation",
            "risk_score": 4.2,
            "risk_level": "LOW-MEDIUM",
            "budget_avg": 1750000,
            "created_at": (datetime.now() - timedelta(days=3)).isoformat(),
        },
        {
            "id": 3,
            "project_name": "Rochester STEM Academy Campus",
            "client_name": "Minnesota Department of Education",
            "risk_score": 8.1,
            "risk_level": "HIGH",
            "budget_avg": 3150000,
            "created_at": datetime.now().isoformat(),
        }
    ]

def get_report_detail(report_id: int):
    """Get detailed report data by ID"""
    reports_detail = {
        1: {
            "id": 1,
            "project_name": "Minneapolis Regional Medical Center",
            "client_name": "Minnesota Department of Health",
            "location": "Minneapolis, Minnesota",
            "project_type": "Healthcare Infrastructure",
            "budget_min": 2500000,
            "budget_max": 3200000,
            "duration_months": 18,
            "risk_score": 6.5,
            "risk_level": "MEDIUM-HIGH",
            "participation_recommendation": "CONDITIONAL",
            "deadline_date": "2025-11-15",
            "award_date": "2025-12-10",
            "start_date": "2026-01-05",
            "created_at": (datetime.now() - timedelta(days=2)).isoformat(),
            "executive_summary": {
                "description": "Construction of a 120-bed regional medical center with emergency services, surgical areas, and diagnostic facilities in compliance with Minnesota Department of Health standards.",
                "requirements": [
                    "ISO 9001:2015 certification",
                    "Minimum 5 years healthcare construction experience",
                    "Financial capacity: $500,000 minimum",
                    "Technical team: min 3 registered engineers"
                ],
                "selection_method": "Best Value"
            },
            "cost_analysis": {
                "budget_breakdown": [
                    {"category": "Direct Costs", "amount": 1750000, "percentage": 70},
                    {"category": "Indirect Costs", "amount": 500000, "percentage": 20},
                    {"category": "Contingency", "amount": 250000, "percentage": 10}
                ],
                "guarantees": [
                    {"type": "Bid Bond", "amount": 50000, "percentage": 2},
                    {"type": "Performance Bond", "amount": 250000, "percentage": 10},
                    {"type": "Advance Payment Bond", "amount": 125000, "percentage": 5}
                ],
                "payment_terms": {
                    "advance": 30,
                    "progress": 65,
                    "retention": 5
                },
                "pricing_strategy": "Recommended competitive pricing at 15-18% markup. Market analysis suggests strong competition. Consider value-add services to differentiate rather than lowest price."
            },
            "risk_assessment": {
                "categories": [
                    {
                        "name": "Technical Risks",
                        "level": "MEDIUM",
                        "items": [
                            "Complex foundation requirements",
                            "Specialized medical equipment specifications",
                            "Seismic zone construction requirements"
                        ]
                    },
                    {
                        "name": "Financial Risks",
                        "level": "HIGH",
                        "items": [
                            "High guarantee requirements ($425,000 total)",
                            "Long payment cycle (18 months)",
                            "5% retention until project completion"
                        ]
                    },
                    {
                        "name": "Legal Risks",
                        "level": "LOW",
                        "items": [
                            "Standard government contract terms",
                            "Clear dispute resolution process"
                        ]
                    },
                    {
                        "name": "Schedule Risks",
                        "level": "MEDIUM",
                        "items": [
                            "Tight 60-day proposal preparation deadline",
                            "Weather constraints during rainy season",
                            "Coordination with ongoing hospital operations"
                        ]
                    },
                    {
                        "name": "Execution Risks",
                        "level": "MEDIUM",
                        "items": [
                            "Specialized subcontractor availability",
                            "Medical equipment procurement lead times",
                            "Site access limitations"
                        ]
                    }
                ],
                "red_flags": [
                    "Tight deadline: Only 60 days to prepare proposal",
                    "Penalty clause: 2% per day delay (very aggressive)",
                    "Unclear scope in Section 4.2: 'Additional works as required'"
                ],
                "mitigation_actions": [
                    "Schedule pre-bid clarification meeting",
                    "Engage geotechnical consultant early",
                    "Request scope clarification in writing",
                    "Build 15% time buffer into schedule",
                    "Review penalty terms with legal team"
                ]
            },
            "recommendations": {
                "strategic_advice": "Bid participation is recommended ONLY if your team can: (1) Secure specialized healthcare contractor, (2) Obtain scope clarification on Section 4.2, (3) Accept aggressive penalty terms. Budget is attractive and client reputable, but timeline and penalties present significant execution risk.",
                "priority_actions": [
                    "Contact MN Dept of Health for pre-bid meeting (within 7 days)",
                    "Engage ABC Medical Contractor as subcontractor",
                    "Get legal review of penalty clauses",
                    "Site visit to assess foundation needs"
                ]
            }
        },
        2: {
            "id": 2,
            "project_name": "Interstate 35 North Expansion",
            "client_name": "Minnesota Department of Transportation",
            "location": "Duluth, Minnesota",
            "project_type": "Road Infrastructure",
            "budget_min": 1600000,
            "budget_max": 1900000,
            "duration_months": 12,
            "risk_score": 4.2,
            "risk_level": "LOW-MEDIUM",
            "participation_recommendation": "YES",
            "deadline_date": "2025-11-20",
            "award_date": "2025-12-15",
            "start_date": "2026-01-10",
            "created_at": (datetime.now() - timedelta(days=3)).isoformat(),
            "executive_summary": {
                "description": "Expansion of Interstate 35 North for 5.3 miles including two bridges, drainage systems, and safety infrastructure in accordance with MnDOT standards.",
                "requirements": [
                    "Highway construction experience (minimum 3 projects)",
                    "Bridge construction capability",
                    "ISO 9001 certification",
                    "Environmental management certification"
                ],
                "selection_method": "Lowest Price"
            },
            "cost_analysis": {
                "budget_breakdown": [
                    {"category": "Earthworks", "amount": 480000, "percentage": 30},
                    {"category": "Pavement", "amount": 560000, "percentage": 35},
                    {"category": "Bridges", "amount": 400000, "percentage": 25},
                    {"category": "Other", "amount": 160000, "percentage": 10}
                ],
                "guarantees": [
                    {"type": "Bid Bond", "amount": 32000, "percentage": 2},
                    {"type": "Performance Bond", "amount": 160000, "percentage": 10}
                ],
                "payment_terms": {
                    "advance": 20,
                    "progress": 75,
                    "retention": 5
                },
                "pricing_strategy": "Lowest price selection method. Recommend aggressive pricing at 8-12% markup to win. Project scope is clear and well-defined, reducing execution risk."
            },
            "risk_assessment": {
                "categories": [
                    {
                        "name": "Technical Risks",
                        "level": "LOW",
                        "items": [
                            "Standard highway construction methods",
                            "Well-defined bridge specifications"
                        ]
                    },
                    {
                        "name": "Financial Risks",
                        "level": "LOW",
                        "items": [
                            "Moderate guarantee requirements",
                            "Reasonable payment schedule"
                        ]
                    },
                    {
                        "name": "Legal Risks",
                        "level": "LOW",
                        "items": [
                            "Standard contract terms",
                            "No unusual penalty clauses"
                        ]
                    },
                    {
                        "name": "Schedule Risks",
                        "level": "MEDIUM",
                        "items": [
                            "Weather dependency (rainy season)",
                            "Material delivery logistics to remote area"
                        ]
                    },
                    {
                        "name": "Execution Risks",
                        "level": "LOW",
                        "items": [
                            "Experienced workforce available",
                            "Standard equipment required"
                        ]
                    }
                ],
                "red_flags": [],
                "mitigation_actions": [
                    "Plan for weather delays in schedule",
                    "Secure material suppliers early",
                    "Establish on-site storage for materials"
                ]
            },
            "recommendations": {
                "strategic_advice": "HIGHLY RECOMMENDED opportunity. Low risk profile, clear scope, reputable client, and fair terms. Lowest price selection favors efficient operators. This is an ideal project for your portfolio.",
                "priority_actions": [
                    "Begin cost estimation immediately",
                    "Secure asphalt and concrete suppliers",
                    "Schedule site visit for measurements",
                    "Prepare aggressive but realistic pricing"
                ]
            }
        },
        3: {
            "id": 3,
            "project_name": "Rochester STEM Academy Campus",
            "client_name": "Minnesota Department of Education",
            "location": "Rochester, Minnesota",
            "project_type": "Educational Infrastructure",
            "budget_min": 2800000,
            "budget_max": 3500000,
            "duration_months": 24,
            "risk_score": 8.1,
            "risk_level": "HIGH",
            "participation_recommendation": "NO",
            "deadline_date": "2025-11-10",
            "award_date": "2025-12-05",
            "start_date": "2026-01-15",
            "created_at": datetime.now().isoformat(),
            "executive_summary": {
                "description": "Construction of STEM academy campus including 3 school buildings, sports facilities, laboratories, and administrative areas for 1,200 students with cold climate considerations.",
                "requirements": [
                    "Educational facility experience (minimum 2 projects)",
                    "Cold climate engineering certification",
                    "Environmental impact assessment capability",
                    "Minimum team of 5 professional engineers"
                ],
                "selection_method": "Quality and Cost Based Selection (QCBS)"
            },
            "cost_analysis": {
                "budget_breakdown": [
                    {"category": "Buildings", "amount": 2100000, "percentage": 60},
                    {"category": "Infrastructure", "amount": 700000, "percentage": 20},
                    {"category": "Equipment", "amount": 525000, "percentage": 15},
                    {"category": "Other", "amount": 175000, "percentage": 5}
                ],
                "guarantees": [
                    {"type": "Bid Bond", "amount": 70000, "percentage": 2},
                    {"type": "Performance Bond", "amount": 350000, "percentage": 10},
                    {"type": "Warranty Bond", "amount": 175000, "percentage": 5}
                ],
                "payment_terms": {
                    "advance": 10,
                    "progress": 80,
                    "retention": 10
                },
                "pricing_strategy": "QCBS selection requires balance between technical quality and price. High guarantees and long duration increase financial risk. Not recommended unless you have significant working capital."
            },
            "risk_assessment": {
                "categories": [
                    {
                        "name": "Technical Risks",
                        "level": "HIGH",
                        "items": [
                            "Cold climate construction requirements",
                            "Complex multi-building coordination",
                            "Specialized laboratory installations",
                            "Sports facility standards compliance"
                        ]
                    },
                    {
                        "name": "Financial Risks",
                        "level": "VERY HIGH",
                        "items": [
                            "Very high guarantee requirements ($595,000 total)",
                            "Low advance payment (only 10%)",
                            "Long project duration (24 months)",
                            "10% retention until warranty period"
                        ]
                    },
                    {
                        "name": "Legal Risks",
                        "level": "MEDIUM",
                        "items": [
                            "Environmental compliance requirements",
                            "Community consultation obligations",
                            "Multiple regulatory approvals needed"
                        ]
                    },
                    {
                        "name": "Schedule Risks",
                        "level": "HIGH",
                        "items": [
                            "VERY tight proposal deadline (only 30 days)",
                            "Academic calendar constraints",
                            "Weather impacts (24-month duration)",
                            "Permit approval uncertainties"
                        ]
                    },
                    {
                        "name": "Execution Risks",
                        "level": "HIGH",
                        "items": [
                            "Coordination of multiple specialized subcontractors",
                            "Remote location material delivery",
                            "Skilled labor availability",
                            "Quality control across multiple buildings"
                        ]
                    }
                ],
                "red_flags": [
                    "CRITICAL: Only 30 days to prepare proposal",
                    "CRITICAL: Very low advance payment (10% vs industry standard 30%)",
                    "HIGH: Penalty clause of 3% per day delay",
                    "HIGH: Vague scope in Sections 3.4 and 5.2",
                    "MEDIUM: Requirement for specialized cold climate consultant not clearly funded"
                ],
                "mitigation_actions": [
                    "Request deadline extension (unlikely to be granted)",
                    "Secure $595,000 in guarantee bonds immediately",
                    "Engage cold climate engineering firm for proposal support",
                    "Request written clarification on scope ambiguities",
                    "Consider partnering with experienced educational contractor"
                ]
            },
            "recommendations": {
                "strategic_advice": "NOT RECOMMENDED. This project presents excessive risk across all categories: (1) Extremely tight deadline makes thorough proposal preparation nearly impossible, (2) Very high financial requirements with low cash flow, (3) Multiple technical complexities for cold climate construction, (4) Aggressive penalties, (5) Scope ambiguities. Unless you have extensive experience with similar projects and strong financial backing, this opportunity should be declined.",
                "priority_actions": [
                    "DECLINE participation",
                    "If must bid: Immediately secure financial guarantees",
                    "Request scope clarifications within 48 hours",
                    "Engage experienced educational construction partner"
                ]
            }
        }
    }
    return reports_detail.get(report_id)
