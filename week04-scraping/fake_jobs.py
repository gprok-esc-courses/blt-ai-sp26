import requests 
from bs4 import BeautifulSoup 
# pip install beautifulsoup4
import csv 


page = requests.get('https://realpython.github.io/fake-jobs/') 
file = open('fake_jobs.csv', 'w')
out_file = csv.writer(file)

out_file.writerow(['title', 'company', 'location'])

soup = BeautifulSoup(page.text, 'html.parser')

job_cards = soup.find_all("div", class_="card")

print(len(job_cards))

for card in job_cards:
    title = card.find("h2", class_="title").text.strip()
    company = card.find("h3", class_="company").text.strip()
    location = card.find("p", class_="location").text.strip()

    out_file.writerow([title, company, location]) 

file.close()
