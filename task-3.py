import requests
from bs4 import BeautifulSoup

#url of web page to scrape
url = 'https://www.amazon.in/'

#sending request to web page
response = requests.get(url)

#check if request is successful
if response.status_code ==200:

    #parse html content
    soup = BeautifulSoup(response.text,'html.parser')

    #extract all text from web page
    page_text = soup.get_text()

    #extract all links from web page
    links = [a['href'] for a in soup.find_all('a',href=True)]

    #extract all images from the web page
    images = [img['src'] for img in soup.find_all('img',src=True)]

    #print extracted data
    print('Text:')
    print(page_text)

    print('\nLinks:')
    for link in links:
        print(link)

    print('\nImages')
    for image in images:
        print(image)

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")