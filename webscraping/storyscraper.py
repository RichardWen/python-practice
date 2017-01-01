from lxml import html
import requests
import re

MainPage = requests.get("https://www.carvezine.com/stories/")
tree = html.fromstring(MainPage.content)
links = tree.xpath('//a[@class="summary-title-link"]/@href')

text = ""
text.encode('utf-8').strip()
for link in links:
	testURL = "https://www.carvezine.com" + link
	story = requests.get(testURL)
	storyTree = html.fromstring(story.content)
	storyList = storyTree.xpath('//*[@class="sqs-block-content"]/p//text()')
	storyText = ' '.join(storyList)
	text += storyText

new_txt = re.sub('[^a-zA-Z0-9\'\.\,\!\?\:\;\(\)\"\$\#]', ' ', text)
open('collections.txt', 'w').write(new_txt)