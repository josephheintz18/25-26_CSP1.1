num1 = 6
num2 = 6

# Header: of booleanStatement
if num1 > num2:
    # Body: holds the statement to execute
    # Everything in the same tab level is in the body
    print("Num1 is bigger bro")
# Elif: stands for else if. Check the first condition then check them in the order shown
elif num2 > num1:
    print("Num2 is bigger bro")
else:
    print("The nums are equal bro")