'''
Hey!

In the next lecture, Windows or ARM Mac(M1, M2, etc) users might encounter a small issue.

Due to the way these systems work you must make sure that the code that starts a process is surrounded by if __name__ == "__main__".

Otherwise when we start new processes, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.

So in the next video, when you see something like process.start(), make sure to do:

if __name__ == "__main__":
    process.start()
    ...
    process.join()
It's important that all the code in between starting the process and joining the process is inside the if statement.

Kind regards,

Jose
'''