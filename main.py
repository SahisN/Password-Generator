from tkinter import *
from panel import *

# Setting up window
window = Tk()
window.title('Password Generator')
window.geometry('450x350+525+80')

# Default Settings
capital_letter = False
include_numbers = False
include_symbols = False
default_text = '10'

# load frame 1
Generate(window, capital_letter, include_numbers, include_symbols, default_text)

# Main loop
window.mainloop()
