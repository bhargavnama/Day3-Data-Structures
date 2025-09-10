A = set()
n: int = int(input("Enter the size of the set: "))

for _ in range(n):
    A.add(input("Enter the element to be added: "))

print("----------------------------------------Set Elments are------------------------------------------------")
for elem in A:
    print(elem, end=" ")