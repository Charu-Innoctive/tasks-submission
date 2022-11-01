'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing
their central elements.
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

'''

def middle_way(arr1,arr2):
    pass
def middle(arr1,arr2):
    # if len(arr1)%2==0:
    #     return None
    if len(arr1)%2!=0:
        middle_elem_index_arr1=len(arr1)//2
        val_of_arr1=arr1[middle_elem_index_arr1]
    if(len(arr2)%2!=0):
        middle_elem_index_arr2=len(arr2)//2
        val_of_arr2=arr2[middle_elem_index_arr2]
    res_list=[val_of_arr1,val_of_arr2]
    print(res_list)
#   l1 = len(arr1)
#   l2=len(arr2)
#   if l1/2:
#     print((arr1[l1//2-1]+arr1[l1//2])//2.0)
#   else:
#     print(arr1[(l1//2-1)//2])
middle([1,2,3],[4, 5, 6])
