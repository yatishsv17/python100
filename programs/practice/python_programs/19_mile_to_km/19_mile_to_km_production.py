"""
Mile to Kilometer Converter - Production Version
===================================================

WHAT THIS PROGRAM DOES (Flow):
1. Create tkinter window with styled layout
2. Add entry field for miles with focus set
3. Add "Calculate" button (Enter key also triggers)
4. Add "Clear" button to reset
5. On calculate:
   a. Validate input (must be numeric)
   b. Convert miles to km (× 1.60934)
   c. Display result formatted to 2 decimal places
   d. Show error message for invalid input
6. On clear: reset entry and result
7. Run GUI main loop

INPUTS:
- Miles (float): entered in GUI text field (integer or decimal)

OUTPUTS:
- Kilometers (float): displayed in GUI label (2 decimal places)
- Error message for invalid inputs (displayed in GUI)

SIDE EFFECTS:
- Opens a tkinter GUI window

RULES:
- Conversion: km = miles × 1.60934
- Input must be a valid number
- Enter key triggers conversion
- Clear button resets all fields

ASSUMPTIONS:
- tkinter available
- User enters numeric values
- Standard conversion factor acceptable

DEPENDENCIES:
- tkinter (standard library)
"""

import tkinter as tk
from tkinter import messagebox

CONVERSION_FACTOR = 1.60934
WINDOW_TITLE = "Mile to Km Converter"
FONT = ("Arial", 12)
FONT_BOLD = ("Arial", 14, "bold")


class MileToKmApp:
    """GUI application for mile to kilometer conversion.

    Attributes:
        window: The tkinter root window.
        miles_entry: Entry widget for miles input.
        result_label: Label widget for displaying result.
    """

    def __init__(self) -> None:
        """Initialize the application window and widgets."""
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.minsize(width=350, height=150)
        self.window.config(padx=30, pady=30)
        self.window.resizable(False, False)

        self._build_widgets()
        self._bind_events()

    def _build_widgets(self) -> None:
        """Create and layout all GUI widgets."""
        # Miles entry
        self.miles_entry = tk.Entry(self.window, width=12, font=FONT,
                                     justify="center")
        self.miles_entry.grid(row=0, column=1, padx=5, pady=5)
        self.miles_entry.focus()

        # Labels
        tk.Label(self.window, text="Miles", font=FONT).grid(
            row=0, column=2, padx=5)
        tk.Label(self.window, text="is equal to", font=FONT).grid(
            row=1, column=0, padx=5)

        self.result_label = tk.Label(self.window, text="0.00",
                                      font=FONT_BOLD, fg="blue")
        self.result_label.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Km", font=FONT).grid(
            row=1, column=2, padx=5)

        # Buttons
        btn_frame = tk.Frame(self.window)
        btn_frame.grid(row=2, column=0, columnspan=3, pady=10)

        tk.Button(btn_frame, text="Calculate", font=FONT,
                  command=self.convert).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", font=FONT,
                  command=self.clear).pack(side="left", padx=5)

    def _bind_events(self) -> None:
        """Bind keyboard shortcuts."""
        self.window.bind("<Return>", lambda e: self.convert())
        self.window.bind("<Escape>", lambda e: self.clear())

    def convert(self) -> None:
        """Convert miles to kilometers and display result."""
        raw = self.miles_entry.get().strip()
        if not raw:
            self.result_label.config(text="0.00", fg="blue")
            return

        try:
            miles = float(raw)
        except ValueError:
            self.result_label.config(text="Invalid!", fg="red")
            return

        km = miles * CONVERSION_FACTOR
        self.result_label.config(text=f"{km:.2f}", fg="blue")

    def clear(self) -> None:
        """Clear input and result."""
        self.miles_entry.delete(0, tk.END)
        self.result_label.config(text="0.00", fg="blue")
        self.miles_entry.focus()

    def run(self) -> None:
        """Start the tkinter main loop."""
        self.window.mainloop()


if __name__ == "__main__":
    app = MileToKmApp()
    app.run()
