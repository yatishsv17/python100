"""
Mile to Kilometer Converter - Simple Version
==============================================

WHAT THIS PROGRAM DOES (Flow):
1. Create tkinter window with title
2. Add entry field for miles input
3. Add "Calculate" button
4. On click: read miles, multiply by 1.60934, display result
5. Run the GUI main loop

INPUTS:
- Miles (float): entered in GUI text field

OUTPUTS:
- Kilometers (float): displayed in GUI label (2 decimal places)

SIDE EFFECTS:
- Opens a tkinter GUI window

RULES:
- Conversion: km = miles × 1.60934
- Input must be a valid number

ASSUMPTIONS:
- tkinter is available
- User enters numeric values

DEPENDENCIES:
- tkinter (standard library)
"""

import tkinter as tk

CONVERSION_FACTOR = 1.60934


def convert():
    try:
        miles = float(miles_entry.get())
        km = miles * CONVERSION_FACTOR
        result_label.config(text=f"{km:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=20, pady=20)

# Miles entry
miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0, column=1)

# Labels
miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = tk.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

# Button
calc_button = tk.Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)

window.mainloop()
