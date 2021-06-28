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
print('留言的平均長度為',sum_len/len(data),'個字')

# 篩選留言長度
new = []
for d in data:
	if len(d) < 100:
		new.append(d) 
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) # 印出第1筆資料
print(new[1]) 
