from tkinter import *
from password_generator import *
from tkinter import messagebox
from tkinter import filedialog
import os

# Settings panel gui allows the user to customize password generator
class Settings:

    def __init__(self, window, capital_letter, include_numbers, include_symbols, default_text):
        self.window = window
        self.default_text = default_text

        # Main frame for Settings class
        self.frame = Frame(window, padx=0, pady=50)
        self.frame.pack()

        # Second frame - Sub frame of frame
        check_box_frame = Frame(self.frame)
        button_frame = Frame(self.frame)

        # --------------------

        # Labels
        length_label = Label(self.frame, text='Password Length')
        symbol_label = Label(self.frame, text='Include Symbols')
        upper_label = Label(self.frame, text='Include uppercase')
        number_label = Label(self.frame, text='Include Numbers')

        # Entry Box
        self.length_entry = Entry(self.frame)

        # Set Entry Text
        self.length_entry.insert(0, self.default_text)

        # Buttons
        back_button = Button(self.frame, text='Back', width='10', borderwidth=3, highlightthickness=5,
                             command=self.frame_forget)
        save_button = Button(self.frame, text='Save', width='10', borderwidth=3, highlightthickness=5,
                             command=self.save_changes)
        reset_button = Button(self.frame, text='Reset', width='10', borderwidth=3, highlightthickness=5,
                              command=self.reset_settings)

        # Check boxes variables
        self.symbol_var = BooleanVar()
        self.upper_var = BooleanVar()
        self.number_var = BooleanVar()

        # Check boxes
        self.symbol_check = Checkbutton(self.frame, text='Adds symbols       ', variable=self.symbol_var)
        self.upper_check = Checkbutton(self.frame, text='Adds capital letters', variable=self.upper_var)
        self.number_check = Checkbutton(self.frame, text='Adds numbers       ', variable=self.number_var)

        # Set checkboxes
        if capital_letter is True:
            self.upper_check.select()

        if include_numbers is True:
            self.number_check.select()

        if include_symbols is True:
            self.symbol_check.select()

        # Grid Layout -------------------------

        # Row 1
        length_label.grid(row=0, column=0)
        self.length_entry.grid(row=0, column=1)

        # Row 2
        empty2 = Label(self.frame, text='').grid(row=1, column=0)
        check_box_frame.grid(row=2, column=0)

        # Row 3
        symbol_label.grid(row=3, column=0)
        self.symbol_check.grid(row=3, column=1)

        # Row 4
        empty3 = Label(self.frame, text='').grid(row=4, column=0)

        # Row 5
        upper_label.grid(row=5, column=0)
        self.upper_check.grid(row=5, column=1)

        # Row 6
        empty4 = Label(self.frame, text='').grid(row=6, column=0)

        # Row 7
        number_label.grid(row=7, column=0)
        self.number_check.grid(row=7, column=1)

        # Row 8
        empty5 = Label(self.frame, text='').grid(row=8, column=0)

        # Row 9
        button_frame.grid(row=9, column=0, pady=10)

        # Row 10
        back_button.grid(row=10, column=0)
        # save_button.grid(row=10, column=1, padx=30)
        reset_button.grid(row=10, column=2)

    # ----------------------------------------------

    # This function switches frames from settings to generate
    def frame_forget(self):

        # Calling save_changes class to save before switching panels
        status = self.save_changes()
        print(status)

        # Only switches panel when save_changes does not have any errors
        if status is True:
            self.frame.pack_forget()
            Generate(self.window, self.upper_var.get(), self.number_var.get(), self.symbol_var.get(), self.default_text)

        # If it has errors, it won't switch
        else:
            pass

    # This function saves the changes in Settings class
    def save_changes(self):
        text = self.length_entry.get()

        print(self.upper_var.get())
        print(self.symbol_var.get())
        print(self.number_var.get())
        print(text)

        # Checks for string and accepts digit only
        if text.isdigit():
            print("It's a number")
            number = int(text)

            # Checks numbers and accepts number ranging from 5 to 25
            if 5 <= number <= 40:
                self.default_text = text
                return True

            # Throws an error sign if user inputted string instead of digit
            else:

                # Uses error class and calls show_warning from error class
                Error('Number out of range', 'Enter number between 5 and 40').show_warning()

                # Replaces user's input with default size 5
                self.length_entry.delete(0, END)
                self.length_entry.insert(0, '10')
                self.default_text = '10'

                # Debugging purpose
                print(self.default_text)
                return False

        # If user inputs string or anything not numeric then warning is prompt and length entry field is changed to 10.
        else:
            print("It's a string")
            Error('Invalid Input', 'Enter numbers only').show_error()
            self.length_entry.delete(0, END)
            self.length_entry.insert(0, '5')
            self.default_text = '10'
            return False

    def reset_settings(self):

        # Unselect all the check boxes
        self.upper_check.deselect()
        self.symbol_check.deselect()
        self.number_check.deselect()

        # Delete length_entry and add the default length
        self.length_entry.delete(0, END)
        self.length_entry.insert(0, 10)

        # Save changes
        self.save_changes()


# Generate password gui display the password that being generated and allows user to save their passwords
class Generate:

    def __init__(self, window, capital_letter, include_numbers, include_symbols, default_text):

        # Initializing variables for Generate class
        self.window = window
        self.frame = Frame(window, pady=50, padx=0)
        self.frame.pack()

        # Print default_text for debugging purpose
        print(default_text)

        # Sub frame for text_field
        text_frame = Frame(self.frame, highlightthickness=1)

        # Sub frame for buttons
        button_frame = Frame(self.frame)

        # Scrollbars
        y_scrollbar = Scrollbar(self.frame)

        # Text field & scrollbar
        self.text_field = Text(self.frame, height=13, width=47, yscrollcommand=y_scrollbar.set)
        y_scrollbar.config(command=self.text_field.yview)

        # Change text field to readonly at the beginning
        self.lock_text_field(self.text_field, 0)

        # Buttons for generate GUI
        generate_button = Button(button_frame, text='Generate', width='10', borderwidth=1, highlightthickness=5,
                                 command=lambda: self.display(capital_letter, include_numbers, include_symbols,
                                                              default_text))
        clear_button = Button(button_frame, text='Clear', width='10', borderwidth=1, highlightthickness=5,
                              command=self.clear_text)
        save_button = Button(button_frame, text='Save', width='10', borderwidth=1, highlightthickness=5,
                             command=self.save_file)
        settings_button = Button(button_frame, text='Settings', width=10, borderwidth=1, highlightthickness=5,
                                 command=lambda: self.frame_forget(capital_letter, include_numbers, include_symbols,
                                                                   default_text))

        # Grid layout beginning--------------------

        # Row 0
        self.text_field.grid(row=0, column=0)
        y_scrollbar.grid(row=0, column=1, sticky=N + S)

        # Row 1
        text_frame.grid(row=1, column=0)

        # Row 2
        Label(self.frame, text='').grid(row=2, column=0)

        # Row 3
        button_frame.grid(row=3, column=0)

        # Row 4
        generate_button.grid(row=4, column=0)
        save_button.grid(row=4, column=1, padx=10)
        clear_button.grid(row=4, column=2, padx=10)
        settings_button.grid(row=4, column=3)

    # Grid layout ending -----------------

    # This function displays text string to text field
    def display(self, capital_letter, include_numbers, include_symbols, default_text):
        generate = password_generator

        if default_text.isdigit():
            # Make text_field editable
            self.lock_text_field(self.text_field, 1)

            # Call list class to generate password
            password_list = generate.list_selector(self, capital_letter, include_numbers, include_symbols)
            text = generate.get_password(int(default_text), password_list)

            # Display the generated password to the text_field
            self.text_field.insert('1.0', text + '\n', END)

            # Debug - temp
            print('It is a digit')

            # Make text_field readonly
            self.lock_text_field(self.text_field, 0)

        else:
            self.clear_text()
            self.text_field.insert('1.0', 'Error, no length is selected', END)
            print('It is not a digit')

    # This function clear text in text field
    def clear_text(self):
        # Make text editable
        self.lock_text_field(self.text_field, 1)

        self.text_field.delete('1.0', END)

        # Make text readonly
        self.lock_text_field(self.text_field, 0)

        # Erase the content of console
        os.system('cls')

    # This function switches generate to settings gui and class
    def frame_forget(self, capital_letter, include_numbers, include_symbols, default_text):
        self.frame.pack_forget()
        Settings(self.window, capital_letter, include_numbers, include_symbols, default_text)

    # Save file function
    def save_file(self, event=None):

        # Ask user to chose the save directory
        # Ask user to chose the save directory
        file_extension = [('Text Documents', '*.txt')]
        select_file = filedialog.asksaveasfilename(title="Save", filetypes=file_extension,
                                                   defaultextension=file_extension)

        # Confirms if user wants to save
        if select_file != '':

            # Creates a file with all of content in the notepad where user chose
            save_file = open(select_file, 'w')
            save_file.write(self.get_text())

            # Close file to prevent data leaks
            save_file.close()

            return True

        else:
            pass

    def get_text(self):
        text = self.text_field.get('1.0', END)
        return text

    @classmethod
    def lock_text_field(cls, text_field, case):

        if case == 0:
            text_field.config(state=DISABLED)

        else:
            text_field.config(state=NORMAL)


# Responsible for displaying different type of error or info
class Error:

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show_error(self):
        messagebox.showerror(self.title, self.message)

    def show_warning(self):
        messagebox.showwarning(self.title, self.message)

    def show_info(self):
        messagebox.showinfo(self.title, self.message)
