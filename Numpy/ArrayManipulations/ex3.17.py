# Sorting of ndarray in numpy

import numpy as np

myarr1 = np.array([45,34,68,34,67,26,9,98,35])
print(f"Original array is: {myarr1}")
print(f"sorted 1-D array in ascending order is{np.sort(myarr1)}") # default sorting is ascending
print(f"sorted 1-D array in descending order is {-np.sort(-myarr1)}") # default sorting is ascending
print('-'*50)
myarr2 =np.array(['mat','hat','rat','bat','cat'])
print(f"String sorted 1-D array in ascending order is {np.sort(myarr2)}") # default sorting is ascending
print(f"String sorted 1-D array in descending order is {np.sort(myarr2)[::-1]}")
print('-'*50)
myarr3 = np.array([[78,35,98],[21,11,9],[87,35,65]])
print(f"Sorted 2-D array in ascending order is{np.sort(myarr3)}")
print(f"Sorted 2-D array in descending order is {-np.sort(-myarr3)}")
print('-'*50)
print("Sorting based on same marks of Students and correct questions attempted in ascendong order")
mydata = [('name', 'S10'), ('marks', float),
('correct_questions', int)]
myvalues = [('Saurabh', 89.5, 52), ('Pallavi', 67,
38),('Priyanka', 89.5, 53),('Yathartha', 88, 51)]
mydatatype = np.array(myvalues, dtype=mydata)
mysort_marks_correct = np.sort(mydatatype,
order=['marks', 'correct_questions'])
print(f"Original Array is :\n {mydata}")
print(f"Sorting carried out based on correct_questions :\n {mysort_marks_correct}")

# Original array is: [45 34 68 34 67 26  9 98 35]
# sorted 1-D array in ascending order is[ 9 26 34 34 35 45 67 68 98]
# sorted 1-D array in descending order is [98 68 67 45 35 34 34 26  9]
# --------------------------------------------------
# String sorted 1-D array in ascending order is ['bat' 'cat' 'hat' 'mat' 'rat']
# String sorted 1-D array in descending order is ['rat' 'mat' 'hat' 'cat' 'bat']
# --------------------------------------------------
# Sorted 2-D array in ascending order is[[35 78 98]
#  [ 9 11 21]
#  [35 65 87]]
# Sorted 2-D array in descending order is [[98 78 35]
#  [21 11  9]
#  [87 65 35]]
# --------------------------------------------------
# Sorting based on same marks of Students and correct questions attempted in ascendong order
# Original Array is :
#  [('name', 'S10'), ('marks', <class 'float'>), ('correct_questions', <class 'int'>)]
# Sorting carried out based on correct_questions :
#  [(b'Pallavi', 67. , 38) (b'Yathartha', 88. , 51) (b'Saurabh', 89.5, 52)
#  (b'Priyanka', 89.5, 53)]