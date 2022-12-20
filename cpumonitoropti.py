import tkinter as tk
import subprocess

# Set the initial temperature thresholds
low_threshold = 24
high_threshold = 30

# Function to get the CPU temperature and update the temperature display
def update_temp():
    # Run the vcgencmd measure_temp command and parse the output to get the temperature
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True).stdout.decode()
    temp = float(output.split('=')[1].split("'")[0])

    # Set the color of the temperature label based on the temperature thresholds
    if temp < low_threshold:
        temp_label.config(fg='green')
    elif temp < high_threshold:
        temp_label.config(fg='yellow')
    else:
        temp_label.config(fg='red')

    # Update the temperature label with the current temperature
    temp_label.config(text=f'Temperature: {temp:.1f}°C')

    # Schedule the update_temp function to be called again after 1000 milliseconds (1 second)
    root.after(1000, update_temp)

# Create the main window
root = tk.Tk()
root.title('CPU Temperature Monitor')

# Create the temperature label
temp_label = tk.Label(root, text='Temp:', font=('Arial', 15))
temp_label.pack()

# Create the input fields for setting the temperature thresholds
low_threshold_entry = tk.Entry(root)
low_threshold_entry.insert(0, low_threshold)
low_threshold_entry.pack()

high_threshold_entry = tk.Entry(root)
high_threshold_entry.insert(0, high_threshold)
high_threshold_entry.pack()

# Create the button for setting the temperature thresholds
def set_thresholds():
    global low_threshold, high_threshold
    low_threshold = float(low_threshold_entry.get())
    high_threshold = float(high_threshold_entry.get())

set_button = tk.Button(root, text='Set Thresholds', command=set_thresholds)
set_button.pack()

# Start the temperature update loop
update_temp()

# Run the Tkinter event loop
root.mainloop()