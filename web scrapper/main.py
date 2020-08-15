# # using the requests module, we can use get function
from bs4 import BeautifulSoup as BS
import requests
from bs4 import BeautifulSoup
# # provides access to webpage as in argument

# result = requests.get("https://www.whitehouse.gov/briefings-statements/")

# # to ensure website is accessible, if output is 200 then ok
# print(result.status_code)

# # print(result.headers)

# src = result.content    # to store page source
# # create BeautifulSoup object based on the source above
# soup = BeautifulSoup(src, 'lxml')
# links = soup.find_all("h2")

# # urls = []
# # for h2_tag in links:
# #     a_tag = h2_tag.find('a')
# #     urls.append(a_tag.attrs['href'])
# # print(urls)
data = '''<div class='test'>
  I Like
  <span class='unwanted'> to punch </span>
   your face
 </div>'''


soup = BS(data, 'html.parser')

external_span = soup.find('div', class_='test')

print("1 HTML:", external_span)
print("1 TEXT:", external_span.text.strip())

unwanted = external_span.find('span')
unwanted.extract()

print("2 HTML:", external_span)
print("2 TEXT:", external_span.text.strip())
