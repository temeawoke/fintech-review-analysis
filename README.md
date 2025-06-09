# fintech-review-analysis
Customer Experience Analytics for Fintech Apps – Google Play Store Review Analysis

Google Play Review Scraper for Ethiopian Banking Apps

## 1. Introduction & Methodology

This report analyzes customer reviews of three major Ethiopian banks—**Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**—to uncover key sentiment trends, common themes, and 

Goal: Support Ethiopian banks in improving their mobile banking apps to enhance customer retention, satisfaction, and feature competitiveness.

We used a hybrid NLP pipeline combining:
- **DistilBERT** for sentiment classification
- **TF-IDF and spaCy** for keyword extraction
- **Clustering** to group themes
- **Matplotlib & Seaborn** for visualization

✅ Scrape user reviews from the Google Play Store for 3 bank apps.

🧠 Analyze sentiment (positive, negative, neutral) and extract themes (e.g., UI issues, bugs, performance).

🔍 Identify satisfaction drivers (e.g., speed, ease of use) and pain points (e.g., app crashes, login errors).

🗃️ Store cleaned data in an Oracle database.

📊 Deliver a report featuring visualizations and actionable recommendations for product, engineering, and marketing teams.

📌 Overview
This project is part of a real-world data engineering challenge focused on collecting and analyzing customer reviews for three Ethiopian banks' mobile apps:

Commercial Bank of Ethiopia (CBE)

Bank of Abyssinia (BOA)

Dashen Bank

The goal is to scrape reviews from the Google Play Store, preprocess the data, and prepare it for sentiment and thematic analysis.

Folder Structure

project-root/
├── notebooks/
│     └─  bank_reviews_visualization.ipynb 
│     └── oracle_review_loader.ipynb
│     └── scrape_reviews.py   oracle_review_loader.ipynb
│     └── textBlob_sentiment_nalysis.ipynb
│     └── thematic_analysis.ipynb
├── scripts/
│   └── scrape_reviews.py         # Script to scrape and preprocess reviews
│
├── data/
│   └── bank_reviews_sentiment_textblob.csv      # Output of cleaned review data
│
├── requirements.txt
├── .gitignore                     # Dependencies
└── README.md                      # You are her

🚀 How to Run
1. Clone the repository

git clone https://github.com/temeawoke/fintech-review-analysis.git
cd fintech-review-analysis

2. Install dependencies

pip install -r requirements.txt

3. Run the scraper

python scripts/scrape_reviews.py

🧹 Data Preprocessing Steps

Removed duplicate reviews.

Normalized review dates to YYYY-MM-DD format.

Added bank and source columns.

Saved data to bank_reviews_raw.csv.

📊 Output Format
The final CSV contains:

Column	Description
review	User's review text
rating	Integer (1–5 stars)
date	Review posting date (YYYY-MM-DD)
bank	App name (CBE, BOA, Dashen)
source	"Google Play"

✅ Task Status
 Scraped 400+ reviews per bank

 Cleaned and saved data to CSV

 GitHub repo organized and committed to task-1 branch
 1. Sentiment Analysis
    🔄 Steps:
    1. Load and clean review text
    2. Use pre-trained DistilBERT to classify reviews as Positive, Negative, or Neutral
    (If using DistilBERT, map logits to sentiment labels)
    3. Add columns: sentiment_label, sentiment_score
    4. Aggregate sentiment by:
    Bank (mean sentiment scores)

Rating (e.g., what sentiment is dominant in 1-star vs. 5-star reviews?)

💡 2. Thematic Analysis
        ✅ Methods:
        Keyword Extraction:

        TF-IDF (preferred for precision)

        spaCy’s noun chunks or named entities

        Optional: Topic modeling (e.g., LDA, BERTopic)

        💻 Pipeline:
        Tokenize + remove stopwords (use spaCy, NLTK, or scikit-learn)

        Lemmatize tokens (optional, useful for standardization)

        Extract top keywords/phrases (n-grams, e.g., ["login error", "app crashes"])

        Manually cluster related terms into themes
        Example clusters:

        ["login", "login error", "can’t login", "session expired"] → Account Access Issues

        ["crash", "lag", "freeze", "slow transfer"] → Performance & Reliability

 📊 3. Example Themes per Bank
Theme	Example Keywords/Phrases
Account Access Issues	login error, session expired, can’t login
Transaction Performance	transfer delay, failed transaction, timeout
UI & UX	confusing design, clean interface, font size
Customer Support	no reply, poor support, help not available
Feature Requests	fingerprint login, dark mode, ATM locator

   Task 3

✅ Step 1: Oracle XE Setup

Install Oracle XE:

Download from: https://www.oracle.com/database/technologies/xe-downloads.html

Install and verify it runs (default service name: XE)

Install Oracle Python Driver:

pip install oracledb
Ensure Oracle Instant Client is installed if using thick mode (optional). oracledb also supports thin mode.

✅ Step 2: Create Schema and Tables

A. Connect to Oracle as SYS:

sqlplus sys/your_sys_password@XE as sysdba

B. Create Schema (User):
bank_reviews

C. Login as the bank_reviews user:
sqlplus bank_reviews/your_password@XE


✅ Step 3: Define Tables

-- Banks Table
CREATE TABLE Banks (
    bank_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    bank_name VARCHAR2(100) NOT NULL,
    headquarters VARCHAR2(100),
    established_year NUMBER(4),
    website VARCHAR2(255)
);

-- Reviews Table
CREATE TABLE Reviews (
    review_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    bank_id NUMBER NOT NULL,
    review_date DATE,
    rating NUMBER(2,1),
    review_text CLOB,
    sentiment VARCHAR2(20),
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);
✅ Step 4: Insert Cleaned Data Using Python
Install Required Library:
pip install oracledb
Python Script

## 2. Key Insights

### 🔍 Drivers and Pain Points

| Bank          | Driver                          | Pain Point                           |
|---------------|----------------------------------|----------------------------------------|
| CBE           | Fast navigation and UI layout   | Frequent app crashes, poor error handling |
| BOA           | Extensive ATM network access    | Slow customer support via app chat      |
| Dashen Bank   | Quick loan application process  | Complicated and inconsistent interface  |

### 📊 Visualizations Summary

1. **Sentiment Distribution by Bank**: CBE had the highest negative sentiment skew.  
2. **Average Sentiment Score**: Dashen scored highest, BOA lowest.  
3. **Word Clouds**: "Crash", "support", "login", and "loan" were dominant themes.  
4. **Rating vs. Sentiment Heatmap**: Clear positive correlation, but CBE had a cluster of low-rated reviews with mixed sentiment.

---

## 3. Recommendations

### ✅ Feature Improvements
- **Crash analytics + bug reporting tool** for CBE to improve stability.
- **In-app AI assistant** for BOA to reduce support wait time.
- **UI walkthrough/tutorial** for Dashen to improve onboarding.

### 💡 New Features
- **Budgeting and expense tracker**: Many users ask for financial planning tools.
- **Push notification manager**: Control alerts, especially for login and security.

---

## 4. Ethical Considerations

- **Bias in Reviews**: Negative experiences are more likely to be shared, leading to skewed data.
- **Model Limitations**: Sentiment models may misclassify sarcasm or culturally nuanced language.
- **Theme Overlap**: Some complaints touch on multiple themes (e.g., login issues tied to UI and support), which may be underrepresented in clustering.

To address these, we suggest human validation and triangulating findings with **qualitative feedback** (e.g., interviews or surveys).

---

## 📎 Appendix: Visualizations

> *(Insert exported plots here from your notebook as images or figures)*  
You can export plots using:

```python
plt.savefig("plots/sentiment_distribution.png")
```

Then include them in your report.
