#リスト

scores = [40,50]

print(scores[0])
print(len(scores)) #要素数
scores.append(70) #要素を追加
print(scores)

for score in scores: #全要素ずつ取り出す
	print(score)


for i, score in enumerate(scores): #各要素ずつ取り出す
	print("{0}: {1}".format(i,score))
