from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Credit Risk Decision API",
    description="API that classifies credit risk decisions based on predicted default probability.",
    version="1.0"
)

class CreditRiskInput(BaseModel):
    probability: float

def decision_engine(probability: float):
    if probability < 0.20:
        return "APPROVE", "Low"
    elif probability < 0.40:
        return "REVIEW", "Medium"
    else:
        return "REJECT", "High"

@app.get("/")
def home():
    return {
        "message": "Credit Risk Decision API is running"
    }

@app.post("/predict")
def predict(input_data: CreditRiskInput):
    decision, risk_level = decision_engine(input_data.probability)

    return {
        "probability": input_data.probability,
        "decision": decision,
        "risk_level": risk_level
    }
