
data = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
for index in range(len(data)):
    if(index + 1) % 3 == 0:
        data[index] = data[index]*2
print(data)
