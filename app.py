first_number = int(input('Enter first number: \n'))
second_number = int(input('Enter second number: \n'))
operation = input('Wich one do you want? \n1 - Sum\n2 - Sub\n3 - Multp\n4 - Div\n')

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multp(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

if operation == '1': 
    print(sum(first_number, second_number))

elif operation == '2':
    print(sub(first_number, second_number))

elif operation == '3':
    print(multp(first_number, second_number))
    
elif operation == '4':
    print(div(first_number, second_number))

else: 
    print('Sorry, did not uderstand you. Shutting down...')