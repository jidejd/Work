Input1 = int(input("Enter Value: "))
Calculation = input("*,/,-,+:")
Input2 = int(input("Enter Value: "))
space = ''

if Calculation.upper() == "*":
    print("=:", Input1*Input2)
elif Calculation.upper() == "/":
    print("=:", Input1/Input2)
elif Calculation.upper() == "-":
    print("=:", Input1-Input2)
elif Calculation.upper() == "+":
    print("=", Input1+Input2)
else: print("Error")


CalcNumbI = {CalcNumbS+}