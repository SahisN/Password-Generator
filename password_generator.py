import random


class password_generator:

    def list_selector(self, capital_letter, include_numbers, include_symbols):

        # All of the password generator options are stored as variable
        numbers = '0123456789'
        alphabets = 'abcdefghijklmnopqrstuvxwyz'
        symbols = '!@_-#$'
        capital = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
        package = []
        package += alphabets

        # Using if statements, the program filters selected options

        # All false and true -------------
        if not include_numbers and not include_symbols and not capital_letter:

            print('all false')

        elif include_numbers and include_symbols and capital_letter:
            package += numbers
            package += symbols
            package += capital

            print('all true')

        # -----------------------------------

        # Single false and all true -----------------------

        # Number is false
        elif not include_numbers and include_symbols and capital_letter:
            package += symbols
            package += capital
            print('Number is false')

        # Symbols is false
        if not include_symbols and include_numbers and capital_letter:
            package += numbers
            package += capital
            print('Symbol is false')

        # capital is false
        elif not capital_letter and include_symbols and include_numbers:
            package += symbols
            package += numbers
            print('Capital is false')

        # ------------------------------

        # 2 false and 1 true --------------------

        # number and capital is false
        elif not include_numbers and not capital_letter and include_symbols:
            package += symbols
            print('number and capital is false')

        # number and include symbol is false
        elif not include_numbers and not include_symbols and capital_letter:
            package += capital
            print('number and symbol is false')

        # capital and include symbol false
        elif not capital_letter and not include_symbols and include_numbers:
            package += numbers
            print('capital and include_symbols is false')

        # -----------------------------------------

        # After storing list selector returns list including the options user selected
        return package

    @classmethod
    def get_password(cls, length, list):

        # This function randomly chooses characters from the list and returns it as a string
        def random_generate(list):
            index = random.randint(0, len(list) - 1)
            return list[index]

        # random_generate function gets called in a for loop depending on the length of the list
        password = ''
        for index in range(0, length):
            password += random_generate(list)

        # Final product is saved in variable password and returned to panel.py, generate class
        return password
