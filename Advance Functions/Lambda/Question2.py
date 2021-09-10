subject_marks = int(input("Enter Size : "))
tuple = []
for i in range(subject_marks):
    tuple.append([str(input("Enter Subject Name : ")),float(input("Enter Marks : "))])
print(tuple)
tuple.sort(key = lambda x : x[1] )
print(tuple)