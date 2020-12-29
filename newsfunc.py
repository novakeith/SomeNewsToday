# news grabber
import requests

def news_search(API, term, lang = "en", country = "us"):
	content = requests.get('https://gnews.io/api/v4/search?q='+term+'&token='+API+'&lang='+lang+'&country='+country)
	return content.text

def news_top(API, lang = "en", country = "us"):
	content = requests.get('https://gnews.io/api/v4/top-headlines?lang='+lang+'&token='+API+'&country='+country)
	return content.text
	
# to do - template library (Quik or Jinja2) - iterate over results to print out data into a template, then email that to end user
