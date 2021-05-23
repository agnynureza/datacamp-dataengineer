""" What is efficient """

# fast response(minimal completion time) & minimal resource consumption
# so the goal writing efficient code is still reduce both latency and overhead

#non-pyhtonic 
doubled_numbers = []


for i in range (5):
    doubled_numbers.append(i*2)
    
#Pythonic 
doubled_numbers = [x*2 for x in range (5)]

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

#output = ['Kramer', 'Elaine', 'George', 'Newman']
result = [name for name in names if len(name) >=6]


""" Building with Builtins """
range(start, stop, increment) 
#range(2,11, 2) -> [2,4,6,8,10]
#range(6) -> [0,1,2,3,4,5]

letters = ['a','b','c']
enumerate(letters,start)
#buat kasih pasangan ke indexnya 

#enumerate(letters, start = 5) -> [(5, 'a'), (6, 'b'), (7, 'c')]

nums = range(1,6)
sqrd_num = map(lambda x: x**2, nums)

print(sqrd_num)

""" The Power Of Numpy Arrays """
import numpy as np

nums_np_ints = np.array(range(5))

#list sama kayak numpy array , tpi untuk 2d berbeda 
nums2 =[[1,2,3],[4,5,6]]
nums2_np = np.array(nums2)

#take index 0 then 1 
nums2[0][1]
nums2_np[0,1]

# ambil index ke 0 dari setiap nested nya 
[row[0] for row in nums2]
nums2_np[:,0]

# boolean indexing 
nums = [-2, -1, 0, 1, 2]
nums_np = np.array(nums)

nums_np > 0 # array([false, false, false, true , true]) 

nums_np[nums_np > 0] #array([1,2])


