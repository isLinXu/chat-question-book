import requests
from bs4 import BeautifulSoup


url = 'https://www.zhihu.com/question/587680799'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

question = soup.find("h1", {"class": "QuestionHeader-title"}).text
print("问题：", question)

answers = soup.find_all("div", {"class": "RichContent-inner"})
print("answer:", len(answers))
for answer in answers:
    print("回答：", answer.text.strip())
    print("--------------------------------------------------")

