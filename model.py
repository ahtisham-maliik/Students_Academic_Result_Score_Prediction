import joblib
import pandas as pd

# --- Load the trained model ---
model = joblib.load('linear_regression_model.pkl')

# --- Define expected input features (one-hot encoded form) ---
all_columns = [
    'HoursStudied_Week', 'Attendance(%)',
    'Gender_Male',
    'Tutoring_Yes',
    'Region_Urban',
    'Parent Education_Secondary',
    'Parent Education_Tertiary'
]

print("--------------------------------------------------")
print("📊 This prediction model has approximately 90% accuracy.")
print("It uses your input to predict your expected exam score.")
print("--------------------------------------------------\n")

while True:
    print("Please enter the following information:\n")

    gender = input("Choose Gender:\nA. Male\nB. Female\n> ").strip().upper()
    gender_male = 1 if gender == 'A' else 0

    hours = float(input("Hours Studied per Week (e.g., 10):\n> "))

    tutoring = input("Tutoring:\nA. Yes\nB. No\n> ").strip().upper()
    tutoring_yes = 1 if tutoring == 'A' else 0

    region = input("Region:\nA. Urban\nB. Rural\n> ").strip().upper()
    region_urban = 1 if region == 'A' else 0

    attendance = float(input("Attendance (%):\n> "))

    parent_edu = input("Parent Education:\nA. Tertiary\nB. Primary\nC. Secondary\n> ").strip().upper()
    parent_tertiary = 1 if parent_edu == 'A' else 0
    parent_secondary = 1 if parent_edu == 'C' else 0

    # --- Construct input DataFrame ---
    input_data = pd.DataFrame([{
        'HoursStudied_Week': hours,
        'Attendance(%)': attendance,
        'Gender_Male': gender_male,
        'Tutoring_Yes': tutoring_yes,
        'Region_Urban': region_urban,
        'Parent Education_Tertiary': parent_tertiary,
        'Parent Education_Secondary': parent_secondary
    }])

    # Add any missing columns with default 0
    for col in all_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns
    input_data = input_data[all_columns]

    # --- Predict ---
    predicted_score = model.predict(input_data)[0]
    print(f"\n🎯 Predicted Exam Score: {predicted_score:.2f}")

    # --- Ask to continue ---
    try_again = input("\nDo you want to try again? (yes/no):\n> ").strip().lower()
    if try_again != 'yes':
        print("\n✅ Thank you for using the Exam Score Predictor! Best wishes and good luck! 🍀")
        break
