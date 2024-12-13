import tkinter as tk
from tkinter import ttk
import datetime
from alarm_manager import AlarmManager
from tkinter import messagebox
from threading import Thread


class AlarmApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.alarm_manager = AlarmManager()
        self.setup_ui()
        self.root.configure(bg='#F0F8FF')

    def run(self):
        self.alarm_manager.start(self.alarm_triggered)
        self.root.mainloop()

    def setup_ui(self):
        frame = tk.Frame(self.root, bg='#F0F8FF')
        frame.pack(pady=20)

        tk.Label(frame, text="Hour", font=('Helvetica', 14), bg='#F0F8FF').grid(row=0, column=0, padx=10)
        self.hour_spin = ttk.Spinbox(frame, from_=0, to=23, wrap=True, width=5, font=('Helvetica', 24))
        self.hour_spin.grid(row=1, column=0, padx=10)

        tk.Label(frame, text="Minute", font=('Helvetica', 14), bg='#F0F8FF').grid(row=0, column=1, padx=10)
        self.minute_spin = ttk.Spinbox(frame, from_=0, to=59, wrap=True, width=5, font=('Helvetica', 24))
        self.minute_spin.grid(row=1, column=1, padx=10)

        tk.Label(frame, text="Second", font=('Helvetica', 14), bg='#F0F8FF').grid(row=0, column=2, padx=10)
        self.second_spin = ttk.Spinbox(frame, from_=0, to=59, wrap=True, width=5, font=('Helvetica', 24))
        self.second_spin.grid(row=1, column=2, padx=10)

        self.status_label = tk.Label(self.root, text="Set your alarm!", font=('Helvetica', 24), bg='#F0F8FF')
        self.status_label.pack(pady=10)

        set_button = tk.Button(self.root, text="Set", font=('Helvetica', 24), bg='green', command=self.set_alarm)
        set_button.pack(side=tk.LEFT, padx=20, pady=20)

        start_button = tk.Button(self.root, text="Start", font=('Helvetica', 24), bg='blue', command=self.start_timer)
        start_button.pack(side=tk.LEFT, padx=20, pady=20)

        pause_button = tk.Button(self.root, text="Pause", font=('Helvetica', 24), bg='red', command=self.pause_timer)
        pause_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.time_label = tk.Label(self.root, font=('Helvetica', 48), bg='#F0F8FF', fg='black')
        self.time_label.pack(pady=20)

        self.update_time()

    def set_alarm(self):
        hour = int(self.hour_spin.get())
        minute = int(self.minute_spin.get())
        second = int(self.second_spin.get())
        alarm_time = datetime.time(hour, minute, second)
        self.alarm_manager.add_alarm(alarm_time)
        self.status_label.config(text=f"Alarm set for {alarm_time}")

    def alarm_triggered(self, alarm):
        self.status_label.config(text=f"Alarm! Time: {alarm}")
        messagebox.showinfo("Alarm", f"Alarm triggered at {alarm}")

    def start_timer(self):
        print("Timer started")

    def pause_timer(self):
        print("Timer paused")

    def update_time(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    app = AlarmApp()
    app.run()
