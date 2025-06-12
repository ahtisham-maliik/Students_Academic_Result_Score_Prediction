# 🎓 Student Academic Performance Prediction Model

This project aims to predict students' academic performance (exam score) based on key factors such as study habits, attendance, and parental background. A linear regression model has been trained and deployed for prediction.

## 📁 Files Included

| File Name                                 | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `SAP-4000.csv`                            | Dataset containing student data used to train the model.                   |
| `linear_regression_model.pkl`            | Trained linear regression model saved using `joblib`.                      |
| `student-academic-performance-analysis-modeling.ipynb` | Jupyter notebook for data analysis, feature engineering, and model training. |
| `result_score_prediction_model.py`       | Script for taking user input and predicting academic result score.         |

---

## 🧠 Model Information

- **Type:** Linear Regression  
- **Accuracy:** ~92%  
- **Evaluation Metrics Used:** R² Score, RMSE

---

## 🧾 Features Used for Prediction

The model requires the following user inputs:

- **Gender**: Male / Female  
- **Hours Studied per Week**: Numerical input (e.g., 10)  
- **Tutoring Support**: Yes / No  
- **Region**: Urban / Rural  
- **Attendance (%)**: Numerical input (e.g., 85.5)  
- **Parent Education Level**: Primary / Secondary / Tertiary

These inputs are transformed via one-hot encoding to match the format the model was trained on.

---

## 🚀 How to Use

1. Make sure Python is installed.
2. Install required packages:

   ```bash
   pip install pandas scikit-learn joblib



   Run the prediction script:

bash
Copy
Edit
python result_score_prediction_model.py
Enter the required inputs when prompted.

The model will return the predicted exam score based on the provided information.

After prediction, you’ll be asked whether you want to try again.

💬 Example Interaction
plaintext
Copy
Edit
Choose Gender:
A. Male
B. Female
> A

Hours Studied per Week:
> 12

Tutoring:
A. Yes
B. No
> B

Region:
A. Urban
B. Rural
> A

Attendance (%):
> 88.5

Parent Education:
A. Tertiary
B. Primary
C. Secondary
> C

Predicted Exam Score: 82.75
Wanna try again? (Y/N)
📌 Notes
Ensure that the linear_regression_model.pkl is in the same directory as the script.

The model only predicts based on patterns learned from the provided dataset (SAP-4000.csv).

This is a regression model — not a classification system — so it outputs a continuous score (e.g., 74.5).

🏁 Conclusion
This project demonstrates how machine learning can be applied to educational data to generate insights and predictions.
