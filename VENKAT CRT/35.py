#Student Grades Analyzer 
marks = list(map(int, input("Enter marks : ").split()))
total = sum(marks)
size=len(marks)
average=total/size
print("Average of the total marks :")
print(f"Average: {average:.2f}")  

if average>=40:
    print("Passed")
else:
    print("Failed")