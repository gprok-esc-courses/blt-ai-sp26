import requests
from bs4 import BeautifulSoup
import csv 
import time 

def get_reviews(company, page):
    url = f"https://www.trustpilot.com/review/{company}?page={page}"
    print(url) 

    page = requests.get(url).text 

    soup = BeautifulSoup(page, 'html.parser')

    reviews_list = soup.select("div[data-reviews-list-start='true']")[0]

    reviews = reviews_list.find_all("article")

    data = []

    for review in reviews: 
        try:
            title = review.select("h2[data-service-review-title-typography='true']")[0].text
            content = review.select("p[data-service-review-text-typography='true']")[0].text
            rating = review.select("div[data-service-review-rating]")[0]['data-service-review-rating']
            data.append([title, rating, content])
        except:
            print("One review ignored")
    
    return data


file = open("truestpilot.csv", "w")
out_file = csv.writer(file)

out_file.writerow(['title', 'rating', 'review'])

print("Starting scraping")
time.sleep(5)
data = get_reviews("www.greetz.nl", 2)

for row in data:
    out_file.writerow([row[0], row[1], row[2]])

file.close()