from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Credit Risk Decision App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: #111827;
                padding: 35px;
                border-radius: 16px;
                width: 420px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            }

            h1 {
                margin-bottom: 10px;
                font-size: 26px;
            }

            p {
                color: #cbd5e1;
                font-size: 14px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin-top: 15px;
                border-radius: 8px;
                border: none;
                font-size: 16px;
            }

            button {
                width: 100%;
                padding: 12px;
                margin-top: 15px;
                border-radius: 8px;
                border: none;
                font-size: 16px;
                font-weight: bold;
                background: #2563eb;
                color: white;
                cursor: pointer;
            }

            button:hover {
                background: #1d4ed8;
            }

            .result {
                margin-top: 25px;
                padding: 15px;
                border-radius: 10px;
                background: #1e293b;
                display: none;
            }

            .approve {
                color: #22c55e;
            }

            .review {
                color: #facc15;
            }

            .reject {
                color: #ef4444;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Credit Risk Decision App</h1>
            <p>Enter a predicted probability of default between 0 and 1.</p>

            <input id="probability" type="number" step="0.01" min="0" max="1" placeholder="Example: 0.35">

            <button onclick="predictRisk()">Predict</button>

            <div id="result" class="result">
                <p><strong>Probability:</strong> <span id="probabilityResult"></span></p>
                <p><strong>Decision:</strong> <span id="decisionResult"></span></p>
                <p><strong>Risk Level:</strong> <span id="riskResult"></span></p>
            </div>
        </div>

        <script>
            async function predictRisk() {
                const probability = parseFloat(document.getElementById("probability").value);

                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        probability: probability
                    })
                });

                const data = await response.json();

                document.getElementById("result").style.display = "block";
                document.getElementById("probabilityResult").innerText = data.probability;
                document.getElementById("decisionResult").innerText = data.decision;
                document.getElementById("riskResult").innerText = data.risk_level;

                const decisionSpan = document.getElementById("decisionResult");
                decisionSpan.className = "";

                if (data.decision === "APPROVE") {
                    decisionSpan.classList.add("approve");
                } else if (data.decision === "REVIEW") {
                    decisionSpan.classList.add("review");
                } else {
                    decisionSpan.classList.add("reject");
                }
            }
        </script>
    </body>
    </html>
    """

@app.post("/predict")
def predict(input_data: CreditRiskInput):
    decision, risk_level = decision_engine(input_data.probability)

    return {
        "probability": input_data.probability,
        "decision": decision,
        "risk_level": risk_level
    }
