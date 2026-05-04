# Credit Risk Prediction

Machine learning project to predict credit default risk and improve identification of high-risk clients in a banking context.

Focus: Risk Management | Credit Analysis | Banking

---

## Key Results

* Accuracy: ~75%
* Recall (default class): improved from 24% to 54%
* Better identification of high-risk clients

---

## Model

* Logistic Regression
* StandardScaler
* Class imbalance handling (class_weight)

---

## Key Insights

* Payment history (PAY_0, PAY_2, PAY_3) is the strongest predictor
* Behavioural variables are more relevant than static financial variables
* Model significantly improves detection of risky clients

---

## Feature Importance

![Feature Importance](feature_importance.png)

---

## Run the Project

Open in Google Colab:
https://colab.research.google.com/github/ricardoserodio/credit-risk-prediction/blob/main/credit_risk_prediction.ipynb

---

## How to Use

1. Open the notebook in Google Colab
2. Upload the dataset (`credit_default.csv`) when prompted
3. Run all cells to train the model, evaluate performance and view feature importance

---

## Use Case

This model can be used by financial institutions to:

* Identify high-risk clients before granting credit
* Improve credit approval decisions
* Support risk management and compliance processes

---

## Files

* `credit_risk_prediction.ipynb` – main notebook
* `feature_importance.png` – model insights

---


---

## Decision Engine

The project includes a simple credit decision engine based on predicted default probability:

- Probability < 20%: Approve
- Probability between 20% and 40%: Review
- Probability > 40%: Reject
## Model Output

### Credit Decision Distribution
![Decision Distribution](decision_distribution.png)

### Sample Results

| Probability | Decision | Risk Level |
|------------|--------|-----------|
| 0.28       | REVIEW | Medium    |
| 0.45       | REJECT | High      |
| 0.09       | APPROVE| Low       |
## Author

Ricardo Serôdio
