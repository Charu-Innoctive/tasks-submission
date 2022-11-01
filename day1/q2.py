'''
Given an array of ints, return True if 6 appears as either the first or last element
in the array. The array will be length 1 or more.
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''
import numpy as np

def first_last_6(arr_inp):
    if(arr_inp[0]==6 or arr_inp[-1]==6):
        return print(True)
    else:
        return print(False)

first_last_6([1, 2, 6])
first_last_6([6, 1, 2, 3])
first_last_6([13, 6, 1, 2, 3])

# first_last6=[1, 2, 6]
# frst_trial=np.array(first_last6)

# first_last6_ex2=[6, 1, 2, 3]
# sec_trial=np.array(first_last6_ex2)

# first_last6_ex3=[13, 6, 1, 2, 3]
# thrd_trial=np.array(first_last6_ex3)




