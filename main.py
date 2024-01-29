import conversions
import operations
import os

# Textual is the way to go
# https://textual.textualize.io

# Blessed
# https://blessed.readthedocs.io/en/latest/

# Check out rich
# https://github.com/Textualize/rich

# Utilize Bubble Tea
# https://www.reddit.com/r/commandline/comments/w30ppv/any_guide_to_creating_a_terminal_application/

# Test issue on line 110 and division by zero errors

number_list = []
state = True
while state:
    os.system("clear")
    print("Welcome to the digital math convertor and calculator!")
    print("Please select an option and press enter:")
    print("1. Conversions")
    print("2. Operations")
    print("3. See previous calculations")
    print("4. Exit")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > 4 or choice < 1:
                1/0
            break
        except ValueError:
            print("Please enter a number")
        except ZeroDivisionError:
            print("Please enter a number between 1 and 4")

    if choice == 1:
        os.system("clear")
        print("Please select an option and press enter")
        print("1. From decimal to base")
        print("2. From base to decimal")
        print("3. From base to base")
        print("4. Return to menu")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice > 4 or choice < 1:
                    1/0
                break
            except ValueError:
                print("Please enter a number")
            except ZeroDivisionError:
                print("Please enter a number between 1 and 4")

        if choice == 1:
            while True:
                try:
                    decimal = float(input("Enter an integer or decimal: "))
                    if decimal.is_integer():
                        decimal = int(decimal)
                    base = int(input("Enter a desired base: "))
                    if base > 16:
                        1/0
                    break
                except ValueError:
                    print("Please enter a number")
                except ZeroDivisionError:
                    print("Please enter a valid base")

            number = conversions.decimal_to_base(decimal, base)
            print(f"\n{number}\n")
            choice = ''
            input("Press enter to continue")

        if choice == 2:
            while True:
                try:
                    number = float(input("Enter a number: "))
                    if number.is_integer():
                        number = int(number)
                    base = int(input("Enter your number's base: "))
                    if base > 16:
                        1/0
                    break
                except ValueError:
                    print("Please enter a number")
                except ZeroDivisionError:
                    print("Please enter a valid base")

            number = conversions.base_to_decimal(number, base)
            print(f"\n{number}\n")
            choice = ''
            input("Press enter to continue")

        if choice == 3:
            while True:
                try:
                    number = float(input("Enter a number: "))
                    if number.is_integer():
                        number = int(number)
                    base1 = int(input("Enter your number's base: "))
                    base2 = int(input("Enter a desired base: "))
                    if base1 > 16 or base2 > 16:
                        1/0
                    break
                except ValueError:
                    print("Please enter a number")
                except ZeroDivisionError:
                    print("Please enter a valid base")

            number = conversions.decimal_to_base(conversions.base_to_decimal(number, base1), base2)
            print(f"\n{number}\n")
            choice = ''
            input("Press enter to continue")

        if choice == 4:
            choice = ''

        number_list.append(number)
        choice = ''

    if choice == 3:
        print()
        for i in range(len(number_list)):
            print(f"{i+1}. {number_list[i]}")
        print()
        choice = ''
        input("Press enter to continue")

    if choice == 4:
        state = False
