# 2
print("2. Print numbers from 0 to 6 except 3 and 6:")
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")
print("\n")