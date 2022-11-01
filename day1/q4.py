'''
Given a Matrix, convert it into the dictionary with keys as row numbers and
values as a nested list.
Input : test_list = [[5, 6, 7], [8, 3, 2]]
Output : {1: [5, 6, 7], 2: [8, 3, 2]}
Explanation: Matrix rows are paired with row numbers in order.

'''
test_list = [[5, 6, 7], [8, 3, 2],[2,3,4,5]]
keys=range(1,len(test_list)+1)
dict_res=dict(zip(keys,test_list))
print(dict_res)