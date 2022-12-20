import tkinter as tk
import subprocess

class CPU_Temperature_Gauge(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("CPU Temperature Gauge")

        # Create the temperature gauge
        self.temperature_gauge = tk.Canvas(self, width=200, height=100, bg="white")
        self.temperature_gauge.pack()

        # Create the label to display the temperature
        self.temperature_label = tk.Label(self, text="Temperature: N/A", font=("Helvetica", 16))
        self.temperature_label.pack()

        # Create the update button
        self.update_button = tk.Button(self, text="Turn On", command=self.update_temperature)
        self.update_button.pack()

        # Schedule the update_temperature function to be called every 5 seconds
        self.after(5000, self.update_temperature)

    def update_temperature(self):
        # Get the current CPU temperature
        temperature = self.get_cpu_temperature()

        # Update the temperature label
        self.temperature_label.config(text=f"Temperature: {temperature}°C")

        # Calculate the temperature as a percentage of the maximum temperature
        temperature_percent = temperature / 100.0

        # Update the temperature gauge
        self.temperature_gauge.delete("temp")
        if temperature_percent > 0.75:
            # Temperature is hot (red)
            self.temperature_gauge.create_rectangle(0, 0, 200, 100, fill="red", tags="temp")
        elif temperature_percent > 0.5:
            # Temperature is warm (orange)
            self.temperature_gauge.create_rectangle(0, 0, 200, 100, fill="orange", tags="temp")
        elif temperature_percent > 0.25:
            # Temperature is neutral (yellow)
            self.temperature_gauge.create_rectangle(0, 0, 200, 100, fill="yellow", tags="temp")
        else:
            # Temperature is cold (green)
            self.temperature_gauge.create_rectangle(0, 0, 200, 100, fill="green", tags="temp")

        # Schedule the update_temperature function to be called again in 5 seconds
        self.after(5000, self.update_temperature)

    def get_cpu_temperature(self):
        # Run a command to get the current CPU temperature
        output = subprocess.run(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE)

        # Extract the temperature from the output
        temperature_str = output.stdout.decode("utf-8").strip().split("=")[1].split("'")[0]

        
        # Return the temperature as a float
        return float(temperature_str)

if __name__ == "__main__":
    app = CPU_Temperature_Gauge()
    app.mainloop()