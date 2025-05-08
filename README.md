
# 📊 Customer Churn Prediction

This project predicts whether a customer is likely to **churn** based on behavioral and service-related features using an **XGBoost** model. It provides a simple REST API built with **Flask** to serve predictions.

---

## 🚀 Features

- Machine learning model (XGBoost) trained on telecom customer data
- REST API using Flask to serve predictions
- API test script with sample input
- Well-documented, modular structure for easy deployment

---

## 🏗️ Project Structure

```
customer-churn-prediction/
├── app.py                           # Flask API to serve predictions
├── churn_model.pkl                 # Saved machine learning model
├── main.ipynb                      # Jupyter notebook for training and evaluation
├── test_api.py                     # API testing script
├── requirements.txt                # List of dependencies
├── customer_churn_dataset-training-master.csv   # Training dataset
├── customer_churn_dataset-testing-master.csv    # Testing dataset
```

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask API**:
   ```bash
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5005/predict`

---

## 📡 API Usage

### Endpoint

- `POST /predict`

### Sample Request

```json
{
  "features": [0.8, 1.5, 3.9, 1.1, 2.0, 1.3, 0.9, 0.6, 0.5, 1.9, 0.8]
}
```

### Sample Response

```json
{
  "prediction": 1,
  "churn_probability": 0.76
}
```

- `prediction`: `1` (will churn), `0` (will not churn)
- `churn_probability`: Probability score between 0 and 1

---

## 🧪 Testing

Use the provided script to test the API:

```bash
python test_api.py
```

---

## 📚 Model Training

- Open `main.ipynb` to view:
  - Data preprocessing steps
  - Model training and evaluation
  - Saving the final model to `churn_model.pkl`

---

## ✅ Requirements

- Python 3.x
- Flask
- NumPy
- scikit-learn
- XGBoost
- Joblib
- Gunicorn (optional for production)

Install via:

```bash
pip install -r requirements.txt
```

---
