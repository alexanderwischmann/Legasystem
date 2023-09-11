import tkinter as tk

# Function to update the counter
def update_counter(counter_label, value):
    current_value = int(counter_label["text"])
    current_value += value
    counter_label["text"] = str(current_value)
    update_values_text()

# Function to update the text field displaying counter values
def update_values_text():
    values_text.delete("1.0", "end")
    for i, counter_label in enumerate(counter_labels):
        values_text.insert("end", f"Counter {i+1}: {counter_label['text']} ")
    values_text.update_idletasks()

# Function to finish the program
def finish_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Counter App")

# Set the window size and position it in the center of the screen
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a list of labels for counters
counter_labels = []
for i in range(4):
    counter_label = tk.Label(root, text="0")
    counter_labels.append(counter_label)
    counter_label.grid(row=i, column=0)

# Create a list of labels for displaying counter values
value_labels = []
for i in range(4):
    value_label = tk.Label(root, text="Value: 0")
    value_labels.append(value_label)
    value_label.grid(row=i, column=1)

# Create a list of labels for counter buttons
counter_button_labels = ["Martin", "Stefan", "Mick", "Hendrik"]

# Create and configure buttons for counters
counter_buttons = []
for i in range(4):
    def create_update_function(i):
        def update():
            update_counter(counter_labels[i], 1)
        return update
    
    counter_button = tk.Button(root, text=counter_button_labels[i], command=create_update_function(i))
    counter_buttons.append(counter_button)
    counter_button.grid(row=i, column=2)

# Create and configure the Finish button
finish_button = tk.Button(root, text="Finish", command=finish_program)
finish_button.grid(row=4, column=0, columnspan=3)

# Create a text field to display counter values
values_text = tk.Text(root, height=1, width=30)
values_text.grid(row=5, column=0, columnspan=3)

# Update the initial values text
update_values_text()

# Start the main event loop
root.mainloop()
