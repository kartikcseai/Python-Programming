# Description: Write a Python program to multiply two lists element by element.
# example : multiply([1, 2, 3], [4, 5, 6]) should return [4, 10, 18].

def custom_zip(list1, list2):
    length = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(length)]

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
output1 = custom_zip(list1, list2)
list3 = [1,2,3,4,5,6,7,8]
list4 = [17,23,34,45,6,55,723,45]
output2 = custom_zip(list3, list4)
print(output1)
print(output2)
