
s = input("Enter a String: ")
l = []
print("Enter the list of characters:")
for i in range(5):
    l.append(input())
for i in range(5):
    count = 0
    for j in s:
        if l[i] == j:
            count += 1
    print(l[i], "=", count)
