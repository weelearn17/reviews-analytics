# 讀取留言檔
data = [] #建立空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行 變數命名為line 也可命名為其他變數 
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # % 跟1000求餘數 餘數為0則列印		
			print(len(data)) #len 計算清單長度
print(data[0])
print('---------------------')
print(data[5])
