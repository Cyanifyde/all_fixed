"""
Write a subroutine that asks the user for a date in the format dd/mm and hours worked. These details are recorded in a set of serial files, one for each month. New data is appended to the correct file. E.g. if the user enters 22/04 and 5, the file called April.txt will have the number 5 added to it.
Write another subroutine that takes a month as a parameter and outputs the total hours for that month.
"""

import os

loc = "/home/runner/all/School-work-objectives/objective9/timesheet/"


def writes(item, file):
    f = open(loc + file, "a")
    f.write(item + "\n")
    f.close()


def read(file):
    f = open(loc + file, "r")
    f = int(f.read())
    return f


def seefiles(x):
    return sorted([
        (i) for i in list(os.listdir(x)) if i not in
        ".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml"
        if not i.endswith((".json", ".txt"))
    ])


def addhours():
    x = input("what date do you want to add it to?\nenter it like dd/mm\n")
    x, y = x.split("/")
    hours = input("how many hours did you do?")
    writes(hours, y)


def display(map):


    


running = True
while running:
    x = input(
        "would you like to\n1 - add more hours\n2 - output the total hours for the month?\n"
    )
    if x == "1":
        addhours()
    if x == "2":
            x = input(
        "what month do you want to see the hours for (input the month as a number)?\n"
            )
            try:
                v = read(x)
                display(v)
            except:
                print("not a day")
