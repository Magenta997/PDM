import json
import re


# 读取爬取的json文件
# 存储为摘要+字典，供模型训练用
def readJson(magazine):
	path = 'data/srcData/' + magazine + '_data.json'
	sumPath = 'data/Clean/' + magazine + '_summary.txt'
	dictPath = 'data/Dicts/' + magazine + '_dict.txt'

	paperList = []
	dictSet = set()

	content = json.load(open(path, 'r', encoding='utf-8'))
	for paper in content:
		article = re.sub('[a-zA-Z0-9’!"#$%&\'()*+./（）《》’‘-‘ ；]+', '', paper[0]['summary'])
		paperList.append(article.split(","))
		for word in paper[0]['keywords']:
			dictSet.add(word)
	print(paperList)

	file = open(dictPath, 'w', encoding='utf-8')
	count = 1
	for i in dictSet:
		count += 1
		file.write(i)
		file.write('\n')
	print('共有%d个关键词' % count)

	file = open(sumPath, 'w', encoding='utf-8')
	count_2 = 1
	for i in paperList:
		count_2 += 1
		for j in i:
			if j != "":
				file.write(j + '\n')
	print('共有%d篇摘要' % count_2)
	print("保存完毕")


def readPaperData(paperName):
	file = open('data/Clean/压力容器_summary.txt', 'a+', encoding='utf-8')
	with open(paperName, encoding="utf-8") as paper:
		content = paper.read()
		article = re.sub('[a-zA-Z0-9’!"#$%&\'()*+./（）《》￥’‘-‘ ]+', '', content)
		for item in article.split(","):
			if "。" in item:
				for sentence in item.split("。"):
					file.write(sentence + "\n")
			else:
				file.write(item + "\n")


if __name__ == '__main__':
	readJson("压力容器")
	readPaperData("data/论文聚合.txt")
