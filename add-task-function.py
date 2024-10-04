task = []

# 1. Erstelle einen Feature Branch „feature/add-task-function“ und erweitere dein
# Python-Skript um die Funktion `add_task`.
## Nutze die `input`-Funktion, um den User nach einer Büroaufgabe zu fragen, z.B.: „Bitte gib eine Aufgabe ein,
## die in deiner Aufgabenliste hinzugefügt werden soll“.
### Speichere die Eingabe in der Variablen `task`.
### Füge die Aufgabe zur Liste hinzu.
### Gib eine Meldung aus, dass die Aufgabe zur Liste hinzugefügt wurde.


def add_task():
    task = input("Please add a task to the to do list: ") # asking user to add a task to the to do list
    task.append(task) # add a task to the list
print(f"Task added to the list: {task}") #  # confirmation that the task was added to the to do list

# 2. Erstelle einen Feature Branch „feature/add-show-tasklist-function“ und erweitere dein
# Python-Skript um die Funktion `show_tasklist`:
## Prüfe, ob die Liste leer ist. Wenn ja, gib den Text „Deine Aufgabenliste ist leer“ aus.
### Wenn die Liste nicht leer ist, drucke alle Aufgaben mit einer `for`-Schleife.
#### Gib auch das Fälligkeitsdatum (falls vorhanden) mit aus.

def show_tasklist():
    if len(task) == 0:
        print("Your to do list is empty")
    else:
        for task in task:
            print(f"{task}")

# 3. Erstelle einen Feature Branch „feature/add-main-function“ und erweitere dein
# Python-Skript um die Funktion `main`:
## Erstelle eine `while`-Schleife, die den User fragt, ob er eine Aufgabe
## hinzufügen, die Liste anzeigen oder das Programm beenden möchte.
### Nutze eine `if/elif`-Bedingung, um die Eingabe des Users zu verarbeiten.

def main():
    while True:
        print("----- To do list -----")
        print("1. Would You like to add a task? ")
        print("2. Would You like to show a task? ")
        print("3. Would You like to end a program? ")

        select = input("Choose between 1-3 please:")
        match select:
            case "1":
                add_task()
            case "2":
                show_tasklist()
            case "3":
                print("Program will be closed")
                return

# Füge am Ende deines Skripts folgenden Code ein, um das Programm automatisch zu
# starten, wenn es ausgeführt wird:

if __name__ == "__main__":
    main()

print("Function will be called to action")

        