from .invoice_matching import router as invoice_matching_router
from .procurement_assistant import router as procurement_assistant_router
from .risk_assessment import router as risk_assessment_router
from .demand_forecasting import router as demand_forecasting_router
from .fraud_detection import router as fraud_detection_router

__all__ = [
    "invoice_matching_router",
    "procurement_assistant_router",
    "risk_assessment_router",
    "demand_forecasting_router",
    "fraud_detection_router",
]