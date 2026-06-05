import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("customer_data.csv")

# Remove Name column
data = data.drop("Name", axis=1)

# Encode categorical columns
le_gender = LabelEncoder()
data['Gender'] = le_gender.fit_transform(data['Gender'])

le_purchase = LabelEncoder()
data['Purchase'] = le_purchase.fit_transform(data['Purchase'])

# Features and Target
X = data.drop("Purchase", axis=1)
y = data["Purchase"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest Model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# Prediction
y_pred = rf_model.predict(X_test)

# Results
print("Random Forest Accuracy:",
      accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
new_customer = [[30, 1, 55000, 12, 3]]
# Age, Gender(Male=1/Female=0), Income, WebsiteVisit, PreviousPurchase

prediction = rf_model.predict(new_customer)

if prediction[0] == 1:
    print("Customer will Purchase")
else:
    print("Customer will Not Purchase")