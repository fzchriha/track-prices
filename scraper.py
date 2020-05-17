import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.otto.de/p/adidas-performance-t-shirt-mh-bo-reg-tee-700368581/#variationId=780736620"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

def check_price():
	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find(id = "")
	price = soup.find(id ="reducedPriceAmount").get_text()
	converted_price = float(price[0:5])
	if (converted_price < 4):
		send_email()



def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('fatimazahra.chriha@gmail.com', 'vehxlqpckdogtkny')
	subject = 'Price fell down'
	body = 'Check the otto link: https://www.otto.de/p/adidas-performance-t-shirt-mh-bo-reg-tee-700368581/#variationId=780736620'
	msg = f"subject: {subject}\n\n{body}"
	server.sendmail(
		'fatimazahra.chriha@gmail.com',
		'fatimazahra.chriha@gmail.com',
		msg
		)
	print("You've got mail!")


while(True):
	check_price()
	time.sleep(3600)