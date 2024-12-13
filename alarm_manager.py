class AlarmManager:
    def __init__(self):
        self.alarms = []
        self.alarm_callback = None

    def add_alarm(self, alarm_time):
        self.alarms.append(alarm_time)
        print(f"Alarm set for {alarm_time}")

    def check_alarms(self):
        while True:
            now = datetime.datetime.now().time()
            for alarm in self.alarms:
                if now.hour == alarm.hour and now.minute == alarm.minute and now.second == 0:
                    if self.alarm_callback:
                        self.alarm_callback(alarm)
            time.sleep(1)

    def start(self, callback):
        self.alarm_callback = callback
        thread = Thread(target=self.check_alarms)
        thread.daemon = True
        thread.start()
