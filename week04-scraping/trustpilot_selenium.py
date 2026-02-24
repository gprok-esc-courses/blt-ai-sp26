from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
import time
import csv 

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options) 

def get_reviews(company, page):
    url = f"https://www.trustpilot.com/review/{company}?page={page}"
    print(url)

    driver.get(url)
    time.sleep(3) 

    print(f"Scraping page {page} of {company} at Trustpilot")

    reviews_list = driver.find_element(By.XPATH, "//div[@data-reviews-list-start='true']")
    reviews = reviews_list.find_elements(By.TAG_NAME, 'article')

    print(f"{len(reviews)} retrieved")

    data = []

    for review in reviews:
        try:
            title = review.find_element(By.XPATH, ".//h2[@data-service-review-title-typography='true']").text.strip()
            content = review.find_element(By.XPATH, ".//p[@data-service-review-text-typography='true']").text.strip()
            rating = review.find_element(By.XPATH, ".//div[@data-service-review-rating]").get_attribute('data-service-review-rating')
            data.append([title, rating, content])
        except:
            print("One review omitted")

    return data

file = open('trustpilot_selenium.csv', 'w')
out_file = csv.writer(file)

out_file.writerow(['title', 'rating', 'review'])

data = get_reviews("www.greetz.nl", 2)

for row in data:
    out_file.writerow([row[0], row[1], row[2]])

file.close()