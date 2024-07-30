import datetime

class Time_me:
    def __init__(self, start_lap: int = 0) -> None:
        self.start_time = self.start()
        self.last_lap   = None
        self.lap_i      = start_lap

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass

    def __del__(self):
        self.stop()

    def start(self):
        start_time = datetime.datetime.now()
        print("Timer started at:", start_time)
        return start_time

    def stop(self):
        end_time = datetime.datetime.now()
        print("\nTimer stopped at:", end_time)
        print("Time elapsed:", end_time - self.start_time)

    def lap(self):
        now = datetime.datetime.now()
        if not self.last_lap:
            lap_time = now - self.start_time
        else:
            lap_time = now - self.last_lap
        print(f"Lap {self.lap_i} duration: {lap_time}")
        self.last_lap = now
        self.lap_i += 1

if __name__ == "__main__":
    import time
    with Time_me():
        time.sleep(2)
