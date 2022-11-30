# Get FIFA data

## Prerequisite

`pip3 install -r requirements.txt`

## Tech

- request
The data will be obtained by Python request, get to know more (Requests: HTTP for Humans)[https://requests.readthedocs.io/en/latest/]

- BeautifulSoup
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
(Beautiful Soup Documentation)[https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text]

- smtplib
The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. (SMTP protocol client)[https://docs.python.org/3/library/smtplib.html]

# Functions

There are two methods, data from all years or a selected year.

Get historical data, all you need to do is typing:

`python3 main.py`

Get a specific year, adding year after the `main.py`:

`python3 main.py 2018`

Monitor the wikipedia of {year} FIFA World Cup

`python3 main.py m-2022`