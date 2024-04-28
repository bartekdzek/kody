import tkinter as tk  # Importing tkinter library for GUI
from tkinter import filedialog, messagebox  # Importing specific modules for file dialog and message box
import pandas as pd  # Importing pandas library for data manipulation
import matplotlib.pyplot as plt  # Importing matplotlib library for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importing FigureCanvasTkAgg for embedding matplotlib figures in tkinter

class HistogramApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Histogram Generator")

        # Creating the main frame
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Button for loading data
        self.btn_load_data = tk.Button(self.frame, text="Load Data", command=self.load_data)
        self.btn_load_data.pack(fill=tk.X)

        # Button for generating histogram
        self.btn_generate_histogram = tk.Button(self.frame, text="Generate Histogram", command=self.generate_histogram)
        self.btn_generate_histogram.pack(fill=tk.X)

        # Creating an area for drawing the histogram
        self.figure = plt.figure(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def load_data(self):
        # File dialog window for selecting CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            try:
                # Loading data from CSV file using pandas library
                self.data = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Data has been successfully loaded!")
            except Exception as e:
                messagebox.showerror("Error", f"Error while loading data: {str(e)}")

    def generate_histogram(self):
        # Checking if data has been loaded
        if hasattr(self, 'data'):
            try:
                # Clearing the previous histogram
                plt.clf()
                # Generating histogram of the data
                self.data.hist(ax=self.figure.gca())
                # Setting title and axis labels
                self.figure.gca().set_title('Height of children aged 0-14')
                self.figure.gca().set_ylabel('Frequency')
                self.figure.gca().set_xlabel('Values')
                # Refreshing the drawing area
                self.canvas.draw()
            except Exception as e:
                messagebox.showerror("Error", f"Error while generating histogram: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please load the data first.")

def main():
    root = tk.Tk()
    app = HistogramApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
