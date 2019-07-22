num_1 = input("Enter first digit")
num_2 = input("Enter second digit")
operator = input("Enter operator")

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)

result = None
if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    result = num_1 / num_2
else:
    print("Unknown operator")
if result != None:
    print("{} {} {} = {}".format(
        num_1,
        operator,
        num_2,
        result))
#end
