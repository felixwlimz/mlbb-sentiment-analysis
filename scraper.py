from google_play_scraper import  Sort, reviews_all 
import csv
import pandas as pd

scrap_review = reviews_all(
    'com.mobile.legends',
    lang='en',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=1000
)

with open('review.csv', mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrap_review:
        writer.writerow([review['content']])
        
mlbb_reviews = pd.DataFrame(scrap_review)
print(mlbb_reviews.shape)
mlbb_reviews.to_csv('mlbb_reviews.csv', index=False)
