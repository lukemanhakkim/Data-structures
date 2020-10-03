"""
Author: Lukeman Hakkim Sheik Alavudeen
Description: All sorting algorithms

1. Bubble sort
	Time complexity: Avg case - O(n2), Best case - O(n)
2. Selection sort
	Time complexity: Avg case - O(n2), Best case - O(n)
"""

#######################
#Bubble sort
#######################

def bubble_sort(array):
    flag=True
    while flag:
        flag=False
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag=True
    return array

########################
#Selection sort
########################
def selection_sort(array):
    
    for i in range(len(array)):
        min=i
        for j in range(i+1, len(array)):
            if array[j]<array[min]:
                array[j], array[min]=array[min], array[j]              
    return array
    

def insertion_sort(array):

    for i in range(1, len(array)):
		key_insert_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_insert_item:
			array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_insert_item
    return array


if __name__ == '__main__':

	array = [5,7,77,1,3,4,9]
	s1 = bubble_sort(array)
	s2 = selection_sort(array)
	s3 = insertion_sort(array)
	print(s1)                
	print(s2)
	print(s3) 
