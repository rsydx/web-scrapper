import requests
from bs4 import BeautifulSoup
import csv


# with open('index.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')


# # to access class tag
# # soup.find('div', class_='footer').text

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

source = requests.get('https://coreyms.com/').content
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# for title in soup.find_all('h2', class_='entry-title'):
#     # a_tag = title.find('a')
#     # print(a_tag.attrs['href'])
#     # # print(title.a.text)

# for content in soup.find_all('div', class_='entry-content'):
#     p_tag = content.find('p').text
#     print(p_tag + "\n\n")

# for vid_content in soup.find_all('iframe', class_='youtube-player'):
#     vid_id = vid_content['src'].split('/')[4]
#     vid_id = vid_id.split('?')[0]
#     # print(vid_id)
#     yt_link = f'https://youtube.com/watch?v={vid_id}'
#     print(yt_link)

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
for article in soup.find_all('article'):
    headline = article.find('h2', class_='entry-title').a.text
    print(headline)
    content = article.find('div', class_='entry-content').p.text
    print(content)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, content, yt_link])

csv_file.close()
