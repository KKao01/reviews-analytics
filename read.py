data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('總共筆數:', len(data))

sum_list = 0
for d in data:
	sum_list += len(d)
print('平均字數是: ', sum_list / len(data))


new_data = []
for d in data:
	if len(d) < 100:
		new_data.append(d)
print('總共有', len(new_data), '筆長度小於100')