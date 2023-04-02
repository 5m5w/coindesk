from bs4 import BeautifulSoup
import requests

url = 'https://www.coindesk.com/policy/2023/03/30/euroclear-finalizing-dlt-bond-settlement-platform-staffer-says/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

contents = soup.find_all('div', 'common-textstyles__StyledWrapper-sc-18pd49k-0 eSbCkN')
paragraph=''
for i in contents:
    content = i.find('div', 'typography__StyledTypography-owin6q-0 bYmaON at-text').text
    if 'Read more:' in content: 
        paragraph = content.split('Read more:')[0]
        print(paragraph)
    elif 'UPDATE (' in content:
        paragraph = content.split('UPDATE (')[0]
        print(paragraph)
    else:
        print(content)