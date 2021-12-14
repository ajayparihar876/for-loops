for i in range(10):
    print(i)
else:
    print('statment complited')


for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('statment complited')


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
        print(x)
for i in range(10):
    if i == 9           :
        continue
    print(i)
