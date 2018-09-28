import requests

def scrape_athletic_net():
    r = requests.get('https://FILLMEIN')

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('span', attrs={'class':'short-desc'})

    records = []
    for result in results:
        X = result.find('PATTERN').text[0:-1] + ', 2018'
        Y = result.contents[1][1:-2]
        Z = results.contents[1][1:-1]

        records.append((date, X,Y,Z))
