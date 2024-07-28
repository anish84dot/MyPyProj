day = input("Enter a day:")
'''
if day == "Monday" or day == 'Tuesday' or day == 'Wednesday'or day == 'Thursday' or day == 'Friday':
    print(f"{day} is a weekday")
else:
    print(f"{day} is a weekend")
'''

'''if day == "Sunday" or day == 'Saturday':
    print(f"{day} is a weekend")
else:
    print(f"{day} is a weekday")'''
if day == 'Sunday':
    print(f"{day} is a weekend")
elif day == "Monday":
    print(f"{day} is a weekday")
elif day == 'Tuesday':
    print(f"{day} is a weekday")
elif day == 'Wednesday':
    print(f"{day} is a weekday")    
elif day == 'Thursday':
    print(f"{day} is a weekday")
elif day == 'Friday':
    print(f"{day} is a weekday")    
elif day == 'Saturday':
    print(f"{day} is a weekend")
else:
    print(f"{day} is not a day")
