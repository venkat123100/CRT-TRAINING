b = input("Enter the employee's attendance record: ")
a = b.upper()
abcount = a.count("A")
lacount = a.count("L")

if a.isalpha():
    if abcount > 5 or lacount > 3:
        print("Not Eligible")
    else:
        print("Eligible")
else:
    print("Invalid")