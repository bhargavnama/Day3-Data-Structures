# n = int(input("Enter the size of the list: "))
# li = [0]*n
# for i in range(n):
#     li[i] = int(input(f"Enter the {i+1}th element: "))
    
# print("Elements of the list are: ", end=" ")
# for num in li: print(num, end=" ")

# # Display negative elements in the list

# li = [12, 32, -23, 43, -32, -34, -98]

# print(f"Negative elements in the list are: {[num for num in li if num < 0]}", end="")

# # Second largest number in the list
# li = [12, 13, 42, 5, 43, 55, 6, 45, 72]

# max = li[0]
# second_max = 0

# for  num in li:
#     if num > max:
#         second_max = max
#         max = num
#     elif num > second_max and num != max:
#         second_max = num
        
# print(f"Second maximum element in the list is: {second_max}")


# # Count number of odd and even numbers in the list

# li = [12, 13, 42, 5, 43, 55, 6, 45, 72]
# odd = 0
# even = 0

# for num in li:
#     if (num & 1) == 1: odd += 1 
#     else: even += 1
    
# print(f"There are {odd} odd numbers and {even} even numbers in the list")


# # Delete element from a specific position

# def delete(l: list, pos):
#     if pos >= len(li):
#         return -1
#     else:
#         return li.pop(pos)

# li = [12, 13, 42, 5, 43, 55, 6, 45, 72]
# pos = int(input("Enter the position: "))
# res = delete(li, pos)
# if res == -1:
#     print("Index out of range")
# else:
#     print(f"Element at {pos} index is deleted")


# # Count frequency of elements in the list

# def countFreq(li):
#     freq = {}
    
#     for num in li:
#         if num not in freq:
#             freq[num] = 1
#         else:
#             freq[num] += 1
            
#     return freq

# li = [21, 23, 41, 21, 34, 54, 34, 34, 91, 23]
# freq = countFreq(li)

# for key, val in freq.items():
#     print(key, "->", val)


# # Print unique elements in the list

# def unique_elements(li: list) -> set:
#     uniques: int = set() 
#     for num in li:
#         uniques.add(num)
#     return uniques

# li = [12, 13, 42, 5, 43, 55, 6, 45, 72]
# uniques = unique_elements(li)
# print("Unique elments in the list are: ", uniques)

def count_duplicates(li: list) -> int:
    uniques: int = set() 
    duplicates = 0
    for num in li:
        if num not in uniques:
            uniques.add(num)
        else:
            duplicates += 1
    return duplicates

li = [21, 23, 41, 21, 34, 54, 34, 34, 91, 23]
duplicates = count_duplicates(li)
print(f"There are {duplicates} duplicates in the list")