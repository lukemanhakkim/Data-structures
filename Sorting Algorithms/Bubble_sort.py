"""
Author: Lukeman Hakkim Sheik Alavudeen
Description: Bubble sort
Time complexity: 
Avg case - O(n2)
Best case - O(n)
"""


def bubble_sort(array):
    flag=True
    while flag:
        flag=False
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag=True
    return array

array = [5,7,77,1,3,4,9]
s = bubble_sort(array)
print(s)
