# 📊 Telco Customer Churn Prediction & Analysis

An end-to-end **Machine Learning project** predicting customer churn for a telecom company.
Includes **interactive Plotly dashboards**, **REST API integration (Flask)**, **PyTorch Neural Network**, and **SQL-based data handling** — aligning with real-world AI/ML internship requirements.

---

## 🧠 Objective

To predict whether a customer will **churn (leave the service)** based on their demographics, service usage, and contract type.
This project also provides **business insights** through interactive dashboards and deployable APIs.

---

## 🗂️ Dataset

**Source:** [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/blastchar/telco-customer-churn)
**Rows:** 7043  **Columns:** 21
**Target Variable:** `Churn`

**Key Features:**

* `gender`, `SeniorCitizen`, `Partner`, `Dependents`
* `tenure`, `MonthlyCharges`, `TotalCharges`
* `InternetService`, `Contract`, `PaymentMethod`

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing

* Handled missing values (`TotalCharges`)
* OneHotEncoding for categorical variables
* Feature scaling for numerical columns
* Train-test split (80/20)

---

### 2️⃣ Exploratory Data Analysis (EDA)

Interactive **Plotly visualizations** to uncover churn patterns:

* Churn rate by Contract Type
* Churn vs. Monthly Charges & Tenure
* Internet Service type vs. Churn
* Cluster analysis of customer groups

📊 *These insights highlight that short-tenure and month-to-month customers are more likely to churn.*

---

### 3️⃣ Model Building

Models Implemented:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest Classifier
* Basic Neural Network (PyTorch)

**Best Model:** Random Forest (Accuracy ≈ 82%)

**PyTorch Neural Network:**
A simple 3-layer feedforward network trained using Binary Cross Entropy Loss, achieving competitive accuracy.

**Key Features Influencing Churn:**

* Contract Type
* Tenure
* Monthly Charges

---

### 4️⃣ Interactive Dashboards (Plotly)

Built **interactive visualizations** using Plotly Express to make churn analysis dynamic and insightful for business users.
Examples:

```python
fig = px.histogram(df, x='Contract_Two year', color='Churn', barmode='group')
fig.show()
```

---

### 5️⃣ REST API Integration (Flask)

Created a **Flask REST API** to serve the ML model:

**Request (POST):**

```json
{
  "tenure": 5,
  "MonthlyCharges": 80.5,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic"
}
```

**Response:**

```json
{"Churn_Prediction": "Yes"}
```

This allows easy integration with external apps or dashboards.

---

### 6️⃣ SQL Integration

Connected the dataset to **MS SQL / MySQL** using `SQLAlchemy` for:

* Table creation
* Query execution
* Data retrieval for EDA or prediction

---

## 📈 Model Evaluation

|  Metric  | Logistic Regression |  KNN | Random Forest | Neural Net (PyTorch) |
| :------: | :-----------------: | :--: | :-----------: | :------------------: |
| Accuracy |         78%         |  76% |    **82%**    |          75%         |
| F1-Score |         0.79        | 0.77 |    **0.84**   |         0.73         |

---

## 💡 Business Insights

* **Contract Duration:** Long-term contracts significantly reduce churn.
* **Service Type:** Fiber optic users are more prone to churn — consider retention offers.
* **Tenure Impact:** New customers (low tenure) are more likely to leave early.

---

## 🛠️ Tech Stack

| Category        | Tools / Libraries             |
| --------------- | ----------------------------- |
| Language        | Python                        |
| Data Analysis   | Pandas, NumPy                 |
| Visualization   | Plotly, Matplotlib, Seaborn   |
| ML Models       | Scikit-learn                  |
| Deep Learning   | PyTorch                       |
| Deployment      | Flask (REST API)              |
| Database        | MS SQL / MySQL via SQLAlchemy |
| Version Control | Git, GitHub                   |

---

## 🚀 Future Enhancements

* Build a **Streamlit / Dash web app** using API predictions
* Automate weekly churn reports via SQL queries
* Deploy REST API on Render or Azure Web Services
* Add LLM summarizer (Hugging Face) for automated churn insights

---

## 🧩 Folder Structure

```
Telco-Churn-Prediction/
│
├── data/
│   └── telco_churn.csv
│
├── notebooks/
│   └── Telco_Churn_Analysis.ipynb
│
├── app/
│   ├── model.pkl
│   └── app.py  (Flask API)
│
├── README.md
└── requirements.txt
```

---

## 🧑‍💻 Author

**Ritesh Bhadane**
Aspiring Data Scientist | AI/ML | Passionate about Generative AI & Predictive Modeling

📧 Email: [[bhadane009@gmail.com](mailto:bhadane009@gmail.com)]

🌐 GitHub: [github.com/rb7285](https://github.com/rb7285)

---

## 🏁 Conclusion

This project demonstrates:

✅ Strong understanding of data preprocessing & model building

✅ Practical experience with ML and Neural Networks in PyTorch

✅ Ability to visualize insights through interactive dashboards

✅ API deployment skills for ML integration

✅ SQL and REST API knowledge

> “Turning data into decisions through interpretable machine learning.”

