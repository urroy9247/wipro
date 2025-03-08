score=()
print(type(score))
marks=(23,45,67)
print(marks)
print(type(marks))
#marks[0]=87 # it is immutable can not be modified or added or deleted
#since tuple items can not be modified , we can convert into list, change it 
# again put back to tuple
marks=list(marks)
print(marks)
marks.append(99)  #appending element into list
print(marks)
marks.insert(1,55) #insert method used to insert an element at the specified insdex
print(marks)
print(type(marks))
marks[0]=90
marks=tuple(marks)
print(marks)