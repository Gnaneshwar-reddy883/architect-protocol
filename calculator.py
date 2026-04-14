num1 = float(input())
num2 = float(input())
operator = input("choose an operator(+ - * /): ")
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)