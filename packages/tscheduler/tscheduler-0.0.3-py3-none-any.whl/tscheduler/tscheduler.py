from datetime import datetime
from threading import Thread, Event
from time import sleep


class BackgroundScheduler:

    thread_list = []
    counter = 1

    # -------------------------------------------------------------------------------
    def thread_fun_interval(
        self,
        func=None,
        day_of_week: str = None,
        hours=None,
        minutes=None,
        seconds=None,
        event=None,
        name=None,
    ):
        try:
            print(f"{name} is started...")
            while not event.is_set():
                sleep(seconds)
                func()
            print(f"{name} is stoped...")
        except:
            print(" Exception ERROR")

    # --------------------------------------------------------------------------------
    def thread_fun_cron(
        self,
        func=None,
        day_of_week: str = None,
        hours=None,
        minutes=None,
        seconds=None,
        event=None,
        name=None,
    ):
        try:
            if (
                hours >= 0
                and hours <= 23
                and minutes >= 0
                and minutes <= 59
                and seconds >= 0
                and seconds <= 59
            ):
                hours = str(hours) if hours > 9 else f"0{hours}"
                minutes = str(minutes) if minutes > 9 else f"0{minutes}"
                seconds = str(seconds) if seconds > 9 else f"0{seconds}"
                time = f"{str(hours)}:{str(minutes)}:{str(seconds)}"
                print(f"{name} is started...")
                while not event.is_set():
                    current_time = datetime.now().strftime("%H:%M:%S")
                    if current_time == time:
                        sleep(1)
                        func()
                print(f"{name} is stoped...")
            else:
                print("Make sure you type the hours, minutes and seconds correctly.")
        except:
            print(" Exception ERROR")

    # --------------------------------------------------------------------------------
    def thread_fun_day_of_week(
        self,
        func=None,
        day_of_week: str = None,
        hours=None,
        minutes=None,
        seconds=None,
        event=None,
        name=None,
    ):
        try:
            if (
                hours >= 0
                and hours <= 23
                and minutes >= 0
                and minutes <= 59
                and seconds >= 0
                and seconds <= 59
            ):
                days = day_of_week.split("-")
                hours = str(hours) if hours > 9 else f"0{hours}"
                minutes = str(minutes) if minutes > 9 else f"0{minutes}"
                seconds = str(seconds) if seconds > 9 else f"0{seconds}"
                time = f"{str(hours)}:{str(minutes)}:{str(seconds)}"
                print(f"{name} is started...")
                while not event.is_set():
                    current_time = datetime.now().strftime("%H:%M:%S")
                    if current_time == time:
                        date = datetime.today().strftime("%A")
                        day_index = date[0:3].lower()
                        if day_index in days:
                            sleep(1)
                            func()
                print(f"{name} is stoped...")
            else:
                print("Make sure you type the hours, minutes and seconds correctly.")
        except:
            print(" Exception ERROR")

    # ------------------------------------------------------------------------------------
    def select_func(self, trigger, day_of_week):
        match trigger:
            case "cron":
                if not day_of_week:
                    return self.thread_fun_cron
                else:
                    return self.thread_fun_day_of_week
            case "interval":
                return self.thread_fun_interval

    # -------------------------------------------------------------------------------------
    def add_job(
        self,
        func=None,
        trigger="interval",
        day_of_week: str = None,
        hours: int = None,
        minutes: int = None,
        seconds: int = None,
        name=None,
    ):
        """
        This function takes function that is executed for scheduled time, provided that the function takes variables. If it has variables, it is placed inside a function that does not take variables..

        Parameters:
        func ( function ): function name.
        trigger ( string ): type scheduler "cron or interval".
        day_of_week ( string ): scheduled days "mon-tue-wed-thu-fri-sat-sun".
        hours ( int ): hour of execution.
        minutes ( int ): minute of execution.
        seconds ( int ): second of execution.
        name ( string ): scheduler name.

        Returns:
        run in background
        """
        global thread_list
        global counter
        try:
            exit_event = Event()
            if not name:
                name = f"thread-{self.counter}"
            t = Thread(
                target=self.select_func(trigger, day_of_week),
                kwargs={
                    "func": func,
                    "day_of_week": day_of_week,
                    "hours": hours,
                    "minutes": minutes,
                    "seconds": seconds,
                    "event": exit_event,
                    "name": name,
                },
                name=name,
            )
            self.counter += 1
            self.thread_list.append({"thread": t, "event": exit_event})
        except:
            print(" Exception ERROR")

    # -----------------------------------------------------------------------------
    def start(self, name=None):
        """
        This function for started one job or all jobs

        Parameters:
        name ( string ): The job name : If the job name is entered, only that job will be started. If the name is not entered, all jobs will be started.

        Returns:
        started jobs
        """
        try:
            for t in self.thread_list:
                if t["thread"].name == name:
                    t["thread"].start()
                elif not name:
                    t["thread"].start()
        except:
            print(" Exception ERROR")

    # ------------------------------------------------------------------------------
    def stop(self, name=None):
        """
        This function for stoped one job or all jobs

        Parameters:
        name ( string ): The job name : If the job name is entered, only that job will be stopped. If the name is not entered, all jobs will be stopped..

        Returns:
        stoped jobs
        """

        try:
            for t in self.thread_list:
                if t["thread"].name == name:
                    t["event"].set()
                elif not name:
                    t["event"].set()
            self.thread_list.clear()
        except:
            print(" Exception ERROR")
