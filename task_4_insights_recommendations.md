
# Task 4 Report: Insights and Recommendations

**Project Title:** Sentiment and Thematic Analysis of Bank App Reviews  
**Team/Analyst:** [Your Name]  
**Date:** [Insert Date]  

---

## 1. Introduction & Methodology

This report analyzes customer reviews of three major Ethiopian banks—**Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**—to uncover key sentiment trends, common themes, and actionable recommendations.

We used a hybrid NLP pipeline combining:
- **DistilBERT** for sentiment classification
- **TF-IDF and spaCy** for keyword extraction
- **Clustering** to group themes
- **Matplotlib & Seaborn** for visualization

Cleaned data was stored in **Oracle DB**, simulating enterprise financial workflows.

---

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
