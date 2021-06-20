import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import csv
def youtube():
	quote = {} 
	quotes=[]
	video_url = "https://www.youtube.com/watch?v=OqsM0hw6B-c"
	content = requests.get(video_url)
	soup = bs(content.content, "html.parser")
	try:
		quote['Title'] = soup.find("span", attrs={"class": "watch-title"}).text
	except:
		pass
	try:
		quote['description'] = soup.find("p", attrs={"id": "eow-description"}).text
	except:
		pass
	try:
		quote['views'] = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))
	except:
		pass
	try:
		quote['date_published']= soup.find("strong", attrs={"class": "watch-time-text"}).text
	except:
		pass
	try:
		data = quote['likes'] = str(int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", "")))
		print(type(data))
	except:
		pass
	try:
		quote['dislikes'] = str(int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", "")))
	except:
		pass
	try:
		quote['channel_tag'] = soup.find("a", attrs={"class": "yt-uix-sessionlink spf-link"}).text
	except:
		pass
	try:
		quote['subscribers'] = soup.find("span", attrs={"class": "yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count"}).text
	except:
		pass
	quotes.append(quote)
	print(quotes)
	filename = 'youtube.csv'
	with open(filename, 'w',encoding='utf-8') as f: 
	    w = csv.DictWriter(f,['Title','description','views','date_published','likes','dislikes','subscribers','channel_name']) 
	    w.writeheader() 
	    for quote in quotes: 
	        w.writerow(quote) 	
if __name__ == '__main__':
	youtube()