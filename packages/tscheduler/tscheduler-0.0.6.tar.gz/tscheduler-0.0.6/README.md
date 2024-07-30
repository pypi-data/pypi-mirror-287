Tscheduler
Tasks Scheduler (Tscheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please.

Among other things, Tscheduler can be used as a cross-platform, application specific replacement to platform specific schedulers, such as the cron daemon or the Windows task scheduler. Please note, however, that Tscheduler is not a daemon or service itself, nor does it come with any command line tools. It is primarily meant to be run inside existing applications. That said, Tscheduler does provide some building blocks for you to build a scheduler service or to run a dedicated scheduler process.

Tscheduler has three built-in scheduling systems you can use:

    Cron-style scheduling

    Interval-based execution (runs jobs on even intervals)

Tscheduler also integrates with several common Python frameworks, like:

    asyncio (PEP 3156)

    gevent

    Tornado

    Twisted

    Qt (using either PyQt , PySide6 , PySide2 or PySide)

There are third party solutions for integrating Tscheduler with other frameworks:

    Django

    Flask

    Fastapi

How to use

First we install the package from pypi.org

    pip install tscheduler

Second we call BackgroundScheduler from the package tscheduler

    from tscheduler.tscheduler import BackgroundScheduler

Python Example 1:

    from tscheduler.tscheduler import BackgroundScheduler

    def hello():
        print("hello")

    scheduler = BackgroundScheduler()
    scheduler.add_job(target=hello,trigger="interval",seconds=5) # line 1
    scheduler.add_job(target=hello,seconds=5) # line 2  line 1 same result with line 2
    scheduler.start()

This example shows the use of the interval

Python Example 2:

    from tscheduler.tscheduler import BackgroundScheduler

    def hello():
        print("hello")

    scheduler = BackgroundScheduler()
    scheduler.add_job(target=hello,trigger="cron",hours=10,minutes=30,seconds=0) # line 1
    scheduler.add_job(target=hello,trigger="cron",day_of_week="mon-tue-wed-thu-fri-sat-sun",hours=10,minutes=30,seconds=0) # line 2   line 1 same result with line 2
                                                                                                                           # day_of_week: With this property you can specify the days on which the job works.
    scheduler.start()

This example shows the use of the cron

Python Example 3: this example using fastapi

    from contextlib import asynccontextmanager
    from time import sleep
    from fastapi import FastAPI
    from tscheduler.tscheduler import BackgroundScheduler


    @asynccontextmanager
    async def lifespan(_: FastAPI):
        print("app started....")
        sch.start()
        yield
        print("app stopped...")
        sch.stop()


    app = FastAPI(lifespan=lifespan)
    sch = BackgroundScheduler()


    def hello():
        print("hello")


    sch.add_job(target=hello, seconds=5)

Note:
The function must not contain args
But there is a solution for it. The function must be wrapped with a function not contain args
Example:

     from tscheduler.tscheduler import BackgroundScheduler

    def hello(name):
        print(f"hello {name}")

    name="taibaoui mohamed"

    def print_name():
        hello(name)
    scheduler = BackgroundScheduler()
    scheduler.add_job(target=print_name,trigger="interval",seconds=5)
    scheduler.start()
