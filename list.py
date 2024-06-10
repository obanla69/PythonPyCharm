



outer_list = []

for i in range(4):
    inner_list = []
    for j in range(5):
        inner_list.append(i * j )
    outer_list.append(inner_list)
    print(inner_list)