# 讀取留言檔
data = [] #建立空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行 變數命名為line 也可命名為其他變數 
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # % 跟1000求餘數 餘數為0則列印		
			print(len(data)) #len 計算清單長度
print('檔案讀取完畢，總共有', len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #把每一筆留言的長度存進 sum_len
print('留言的平均長度為', sum_len/len(data),'個字')

# 篩選留言長度
new = []
for d in data:
	if len(d) < 100:
		new.append(d) 
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) # 印出第1筆資料
print(new[1]) 

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

good = [d for d in data if 'good' in d] #上面26-29行的快寫法
print(good)

bad = ['bad' in d for d in data]
print(bad) #讀取每一筆留言，判斷運算結果(True/False)後存入清單

bad = []
for d in data:
	bad.append('bad' in d) #等同於上面的寫法


# 文字記數 字典查字
wc = {} # word_count
for d in data:
	words = d.split() # split()預設為空白鍵 且連續空白不會計入空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key進wc字典

for word in wc:
	if wc[word] >1000000:
		print(word,wc[word])

print(len(wc))

while True:
	word = input('請問你想查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔！')

print('感謝使用查詢功能')




