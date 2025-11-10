import os
from datetime import datetime

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)


def create_note():
    title=input("\n Enter title for notes")
    title=title.lower()
    content=input("\n Enter your notes")

    filename=f"{NOTES_DIR}/{title}.md"

    f=open(filename,"w")
    f.write(f"# {title}\n")
    f.write(f"Created on: {datetime.now()}\n\n")
    f.write(content)
    f.close()
    print("Notes added successfully!")

def view_all():
    files=os.listdir(NOTES_DIR)
    print("\n ---Saved Notes---")
    for x in files:
        print("-",x)#.replace(".md",""))

def search():
    title=input("\nEnter title to search")
    title=title.lower()
    filename=f"{NOTES_DIR}/{title}.md"

    if os.path.exists(filename):
        f=open(filename,"r")
        print("\n---Content---")
        print(f.read())
        f.close()
    else:
        print("File not found!")

def delete_note():
    title=input("\nEnter title of notes")
    filename=f"{NOTES_DIR}/{title}.md"

    if os.path.exists(filename):
        os.remove(filename)
        print("\nNotes deleted")
    else:
        print("File not found")


print("-----Command Line markdown notes manager-----")

while True:
    print("\nPress '1' to add new note")
    print("\nPress '2' to view all saved notes")
    print("\nPress '3' to search note by title")
    print("\nPress '4' to remove a note")
    print("\nPress '5' to exit")

    choice=int(input("\nEnter your choice"))

    match choice:
        case 1:
            create_note()
        case 2:
            view_all()
        case 3:
            search()
        case 4:
            delete_note()
        case 5:
            break
        case _:
            print("Invalid choice!")