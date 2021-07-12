#!/usr/bin/env python3
import os
import getpass
from datetime import date
i = 1

user = str(getpass.getuser())
today_date = str(date.today())


try:
    os.chdir("/home/" + user)
except:
    os.chdir("C:\\Users\\" + user)

def reset_notes():
    notes = open(".NOTEFILE", "w")
    notes.write("")
    notes.close()

try:
    date_file = open(".datefile", "r")
    today_date_from_datefile = str(date_file.read())
    if today_date_from_datefile != today_date:
        reset_notes()
    date_file.close()
except:
    date_file = open(".datefile", "w")
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

def get_help():
    clear_screen()
    print("Commands: ")
    print(":q(uit) - Exit the program")
    print(":r(eset) - Reset all notes")
    print(":d(elete) - Delete last note")
    print(":h(elp) / :? - Get help with commands")

    print("\nTo write to-dos just write out the note and press ENTER")
    input("Press ENTER to continue...")

while i == 1:
    def clear_screen():
        try:
            os.system("clear")
        except:
            os.system("cls")

    clear_screen()
    try:
        def read_notes():
            notes = open(".NOTEFILE", "r")
            print("-------------------------------- TO-DO " + today_date + " --------------------------------")
            print(notes.read() + "\n")
            notes.close()
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
    else:
        append_note(str(note))
