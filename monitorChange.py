import time
from bs4 import BeautifulSoup
import requests
import json
import hashlib
import smtplib

def monitor_fifa_by_year(year):
    while True:
        web = "https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
        
        # get current result
        matches = get_response(web)
        currentHash = hashlib.sha224(matches).hexdigest()
        print("running...")
        time.sleep(60)
        
        # get new result
        matches = get_response(web)
        newHash = hashlib.sha224(matches).hexdigest()

        if currentHash == newHash:
            continue

        else:
            send_email(user())
            break
        
def get_response(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "lxml")
    matches = soup.find_all('div', class_='footballbox')
    return matches

def user():
    # read the users setting data
    with open("email.json") as f:
        data = json.load(f)
    return data

def send_email(setting):
    msg = "Subject: This is Huixin\'s script talking, FIFA News!"
    # set the 'from' address,
    fromaddr = setting["from_email"]
    # set the 'to' addresses,
    toaddrs  = setting["to_email"]
    # setup the email server,
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromaddr, setting["from_email_password"])
    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()