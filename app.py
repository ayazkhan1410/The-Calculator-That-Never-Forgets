class CalculatorWithHistory:
    file_name = "History.txt"

    def menu(self):
        print("\n1. Perform Calculations")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")
        try:
            return int(input('Enter Choice: '))
        except ValueError:
            return 0

    def add_history(self, subject, operator, second_subject, result):
        with open(self.file_name, 'a') as file:
            file_content = (
                f"{subject} {operator} {second_subject} = {result}\n"
            )
            file.write(file_content)

    def perform_calculations(self):
        print('Input format: 8 + 8 (Include spaces!)')
        user_input = input("Please Enter calculations: ").strip()

        parts = user_input.split()

        if len(parts) != 3:
            print(
                "Error: Please use the format"
                " 'Number Operator Number' (e.g., 8 + 8)"
            )
            return

        try:
            subject = float(parts[0])
            operator = parts[1]
            second_subject = float(parts[2])
            result = None

            if operator == '+':
                result = subject + second_subject
            elif operator == '-':
                result = subject - second_subject
            elif operator == '*':
                result = subject * second_subject
            elif operator == '/':
                if second_subject == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = subject / second_subject
            elif operator == '%':
                if second_subject == 0:
                    print("Error: Modulus by zero.")
                else:
                    result = subject % second_subject
            else:
                print(f"Error: '{operator}' is not a valid operator.")

            if result is not None:
                print(f"Result: {result}")
                self.add_history(subject, operator, second_subject, result)

        except ValueError:
            print("Error: Please enter valid numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_history(self):
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
                if not content.strip():
                    print("\n--- History is empty ---")
                else:
                    print('\n--- History Log ---')
                    print(content.strip())
                    print('-------------------')
        except FileNotFoundError:
            print("\nNo history found. Start calculating!")

    def clear_history(self):
        with open(self.file_name, 'w'):
            pass
        print("History has been cleared!")


calc = CalculatorWithHistory()
while True:
    choice = calc.menu()
    if choice == 1:
        calc.perform_calculations()
    elif choice == 2:
        calc.view_history()
    elif choice == 3:
        calc.clear_history()
    elif choice == 4:
        print('Thank you for using our program!')
        break
    else:
        print('Invalid Input! Please choose 1-4.')
