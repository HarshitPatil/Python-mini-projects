#importing all the needed modules
import requests
from bs4 import BeautifulSoup as bs4

#getting the user name from command line input
user_name = input('Enter username : ')

#concatinating github link to the username to get full link
url = "https://github.com/"+user_name

#getting the webpage
r = requests.get(url)

#getting the html code of the full webpage
soup = bs4(r.content, 'html.parser')

#finding the html code for profile image and then extracting the src from it
image = soup.find('img', {'alt':'Avatar'})['src']

print(image)