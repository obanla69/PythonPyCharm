
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in range(len(data)):
    if(index + 1) % 3 == 0:
        data[index] = data[index]*2
print(data)
