def main():    
    first_number = int(input('Enter first number: \n'))
    second_number = int(input('Enter second number: \n'))
    chosen_operation = int(input('Wich one do you want? \n1 - Sum\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Potentiation\n'))

    def sum(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def multp(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2
    
    def potentiation(num1, num2):
        return num1 ** num2

    operations = {
        1: sum,
        2: sub,
        3: multp,
        4: div,
        5: potentiation
    }

    if chosen_operation in operations:
        result = operations[chosen_operation](first_number, second_number)
        print()
        print('Result: '+result)
        print()
        main()
        
    else: 
        print('Sorry, did not uderstand you. Shutting down...')

main()