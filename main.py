import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
#first article on the page

first_article = soup.find(name="a", rel="noreferrer")
article_text = first_article.get_text()
article_link = first_article.get("href")
article_upvote = soup.find(name="span", class_="score").get_text()

print(f"First article\nText: {article_text}\nLink: {article_link}\nVotes: {article_upvote}")
print(article_link)
print(article_upvote)

#all articles on the page
artcicles = soup.find_all(name="a", rel="noreferrer")
articles_text=[]
articles_links = []

articles_upvote_span = soup.find_all(name="span", class_="score")
articles_upvote = [int(vote.get_text().split()[0]) for vote in articles_upvote_span]

for article in artcicles:
    articles_text.append(article.get_text())
    articles_links.append(article.get("href"))


print(f"All the articles\nText{articles_text},\nLinks{articles_links},\nVotes{articles_upvote}")

#the article with the most points
index = articles_upvote.index(max(articles_upvote))
voted_art_points = articles_upvote[index]
voted_art_text = articles_text[index]
voted_art_link = articles_links[index]

print(f"The most voted article is \nLink: {voted_art_link}\nText: {voted_art_text}\nVotes: {voted_art_points}")