
# SMS Spam Detection Using Machine Learning

## Project Overview
This project classifies SMS messages into two categories:
- Ham: Normal messages
- Spam: Unwanted messages

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Matplotlib
- Seaborn
- Streamlit

## Dataset
UCI SMS Spam Collection

Original records: 5572
Records after cleaning: 5169

## Machine Learning Algorithms
1. Multinomial Naive Bayes
2. Logistic Regression
3. Tuned Multinomial Naive Bayes

## Final Model Performance
- Accuracy: 98.07%
- Precision: 95.12%
- Recall: 89.31%
- F1 Score: 92.13%

## How to Run the Application

1. Install Python.
2. Install required libraries:

   pip install -r requirements.txt

3. Run the application:

   streamlit run app.py

4. Open the local address displayed in the terminal.

## Project Structure

SMS_Spam_Detection/
    dataset/
    notebooks/
    models/
    graphs/
    reports/
    app.py
    requirements.txt
    README.md

## Conclusion
The project demonstrates how machine learning and NLP
can classify SMS messages as spam or normal.
