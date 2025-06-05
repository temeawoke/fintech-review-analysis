# fintech-review-analysis
Customer Experience Analytics for Fintech Apps – Google Play Store Review Analysis

Google Play Review Scraper for Ethiopian Banking Apps

Goal: Support Ethiopian banks in improving their mobile banking apps to enhance customer retention, satisfaction, and feature competitiveness.

As a Data Analyst, your responsibilities are to:

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
│
│
├── scripts/
│   └── scrape_reviews.py         # Script to scrape and preprocess reviews
│
├── data/
│   └── bank_reviews_raw.csv      # Output of cleaned review data
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