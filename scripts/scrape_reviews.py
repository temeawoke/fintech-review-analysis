import pandas as pd
from google_play_scraper import Sort, reviews
from datetime import datetime

# App package names from Google Play
apps = {
    "Commercial Bank of Ethiopia": "com.combankethio.mobile.android",
    "Bank of Abyssinia": "com.abyssiniasoftware.boaapp",
    "Dashen Bank": "com.mobildev.dashenbank"
}

# Store all reviews
all_reviews = []

# Loop through each app and collect reviews
for bank, package in apps.items():
    print(f"Scraping reviews for {bank}...")
    result, _ = reviews(
        package,
        lang="en",  # you can change to "am" for Amharic if needed
        country="et",
        sort=Sort.NEWEST,
        count=500  # Get more than 400 per bank
    )

    for entry in result:
        all_reviews.append({
            "review": entry['content'],
            "rating": entry['score'],
            "date": entry['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Drop duplicates and handle missing values
df.drop_duplicates(subset=["review", "bank"], inplace=True)
df.dropna(subset=["review", "rating", "date"], inplace=True)

# Save to CSV
df.to_csv("data/bank_reviews_raw.csv", index=False)
print("✅ Reviews scraped and saved to data/bank_reviews_raw.csv")
