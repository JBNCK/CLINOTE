#!/usr/bin/env python3
import os
import getpass
from datetime import date
loop = 1

user = str(getpass.getuser())
today_date = str(date.today())

try:
    homedir = os.environ["HOME"]
except KeyError:
    homedir = os.environ["UserProfile"]

print(homedir)
os.chdir(homedir)

def read_notes():
        notes = open(".NOTEFILE", "r")
        print("---------------------------- TO-DO " + today_date + " ----------------------------")
        print(notes.read() + "\n")
        notes.close()

def reset_notes():
    notes = open(".NOTEFILE", "w")
    notes.write("")
    notes.close()

def reset_on_day_change_function():
    date_file = open(".DATEFILE", "r")
    today_date_from_datefile = str(date_file.read())
    if today_date_from_datefile != today_date:
        reset_notes()
    else:
        print("Not resetting.")
    date_file.close()

try:
    reset_cycle = open(".DATERESETFILE", "r")
    reset_on_day_change = str(reset_cycle.read())
    print(reset_on_day_change)
    reset_cycle.close()
    if reset_on_day_change == "reset_on_day_change=true":
        reset_on_day_change_function()
    else:
        print("Not true.")
except:
    reset_cycle = open(".DATERESETFILE", "w")
    reset_on_day_change = str("reset_on_day_change=true")
    reset_cycle.write(reset_on_day_change)
    reset_cycle.close()

date_file = open(".DATEFILE", "w")
date_file.write(today_date)
date_file.close()

# Copied from some random website idk how this works but it does:
def remove_last_line():
    notes_old = open(".NOTEFILE", "r")
    notes_new = notes_old.read()
    notes_old.close()
    notes_new_split = notes_new.split("\n")
    notes_new_join = "\n".join(notes_new_split[:-1])
    notes = open(".NOTEFILE", "w+")
    for line in range(len(notes_new_join)):
        notes.write(notes_new_join[line])
    notes.close()

def append_note(note):
    notes = open(".NOTEFILE", "a")
    notes.write("\n- " + note)
    notes.close()

def clear_screen():
    try:
        os.system("clear")
    except:
        os.system("cls")

def get_help():
    clear_screen()
    print("Commands: ")
    print(":q(uit) - Exit the program")
    print(":r(eset) - Reset all notes")
    print(":d(elete) - Delete last note")
    print(":h(elp) / :? - Get help with commands")
    print(":d(ay)c(hange) - Disable/Enable task reset on day change")

    print("\nTo write to-dos just write out the note and press ENTER")
    input("Press ENTER to continue...")

while loop == 1:
    clear_screen()
    try:
        read_notes()
    except FileNotFoundError:
        notes = open(".NOTEFILE", "w")
        notes.close()
        read_notes()


    note = input("Enter a note (type :help for extra commands): ")
    if note == ":quit" or note == ":q":
        exit()
    elif note == ":help" or note == ":h" or note == ":?":
        get_help()
    elif note == ":reset" or note == ":r":
        reset_notes()
    elif note == ":delete" or note == ":d":
        remove_last_line()
    elif note == ":c" or note == ":daychange" or note == ":dc":
        reset_cycle = open(".DATERESETFILE", "r")
        reset_on_day_change = str(reset_cycle.read())
        if reset_on_day_change == "reset_on_day_change=true":
            reset_cycle.close()
            reset_cycle = open(".DATERESETFILE", "w")
            reset_cycle.write("reset_on_day_change=false")
            reset_cycle.close()
            clear_screen()
            print("Tasks will no longer be reset on day change.")
            input("Press ENTER to continue...")
        else:
            reset_cycle.close()
            reset_cycle = open(".DATERESETFILE", "w")
            reset_cycle.write("reset_on_day_change=true")
            clear_screen()
            reset_cycle.close()
            print("All tasks will be reset on day change.")
            input("Press ENTER to continue...")
    elif note == ":jan" or note == ":janbiernacik":
        clear_screen()
        print("011000100110100101100101011100100111 :)")
        input("Press ENTER to continue...")
    elif note == ":amogus":
        print("sus")
        input("Pressus ENTERUS para continuus...")
    else:
        append_note(str(note))
