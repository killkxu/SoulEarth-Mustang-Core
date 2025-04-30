import datetime

class MemoryLogger:
    def __init__(self, logfile="soulearth_memory_log.txt"):
        self.logfile = logfile

    def log_event(self, event):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.logfile, "a") as f:
            f.write(f"[{timestamp}] {event}\n")
        print(f"📝 LOGGED: {event}")

memory_logger = MemoryLogger()
