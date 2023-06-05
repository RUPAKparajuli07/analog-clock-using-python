import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Analog Clock")

        # Create canvas for clock face
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="white")
        self.canvas.pack()

        # Draw clock face
        self.draw_clock_face()

        # Draw clock hands
        self.hour_hand = self.canvas.create_line(200, 200, 200, 200, width=8, capstyle=tk.ROUND)
        self.minute_hand = self.canvas.create_line(200, 200, 200, 200, width=5, capstyle=tk.ROUND)
        self.second_hand = self.canvas.create_line(200, 200, 200, 200, width=2, capstyle=tk.ROUND)

        # Update clock hands every second
        self.update_clock()
        self.window.mainloop()

    def draw_clock_face(self):
        # Draw clock face
        self.canvas.create_oval(50, 50, 350, 350, width=4, outline='black', fill='white')

        # Draw hour markers
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = 200 + 140 * math.cos(angle)
            y = 200 + 140 * math.sin(angle)
            if i % 3 == 0:
                color = 'red'
            else:
                color = 'blue'
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 16), fill=color)

    def update_clock(self):
        # Get current time
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Calculate hand angles
        hour_angle = math.radians((hour * 30) - 90 + (minute / 2))
        minute_angle = math.radians((minute * 6) - 90)
        second_angle = math.radians((second * 6) - 90)

        # Update clock hands
        self.canvas.coords(self.hour_hand, 200, 200, 200 + 80 * math.cos(hour_angle), 200 + 80 * math.sin(hour_angle))
        self.canvas.coords(self.minute_hand, 200, 200, 200 + 120 * math.cos(minute_angle), 200 + 120 * math.sin(minute_angle))
        self.canvas.coords(self.second_hand, 200, 200, 200 + 140 * math.cos(second_angle), 200 + 140 * math.sin(second_angle))

        # Schedule next update
        self.window.after(1000, self.update_clock)

clock = AnalogClock()
