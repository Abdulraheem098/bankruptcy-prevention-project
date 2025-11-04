import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st

# Load data
df = pd.read_excel('data/bank.xlsx')

# Ensure class labels are 0 for bankruptcy and 1 for non-bankruptcy
df['class'] = df['class'].map({'bankruptcy': 0, 'non-bankruptcy': 1})

# Split data into features and target
X = df[['financial_flexibility', 'competitiveness', 'credibility']]
y = df['class']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize KNN model
knn = KNeighborsClassifier(n_neighbors=4)

# Perform cross-validation
cv_scores = cross_val_score(knn, X_train, y_train, cv=7)

# Train the model
knn.fit(X_train, y_train)

# Streamlit app
st.title('KNN Model Prediction App')

# Sidebar for user input
st.sidebar.header('User Input Parameters')

def user_input_features():
    financialflexibility = st.sidebar.selectbox('Financial Flexibility', (0.0, 0.5, 1.0))
    competitiveness = st.sidebar.selectbox('Competitiveness', (0.0, 0.5, 1.0))
    credibility = st.sidebar.selectbox('Credibility', (0.0, 0.5, 1.0))
    data = {'financial_flexibility': financialflexibility,
            'competitiveness': competitiveness,
            'credibility': credibility}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input
st.subheader('User Input parameters')
st.write(input_df)

# Predict button
if st.button('Predict'):
    # Predict using the trained model
    prediction = knn.predict(input_df)
    
    # Display prediction
    st.subheader('Prediction')
    st.write('Class:', 'Non-Bankruptcy' if prediction[0] == 1 else 'Bankruptcy')

# Display cross-validation scores
#st.subheader('Cross-Validation Scores')
#st.write(cv_scores)
#st.write('Mean CV Score:', cv_scores.mean())

