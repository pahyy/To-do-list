import json

class Todo:
    def __init__(self, title, opis='', done=False):
        self.title = title
        self.opis = opis
        self.done = done

    def mark_done(self):
        self.done = True

    def ispis(self):
        return f"{self.title}|{self.opis}|{self.done}"

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split('|')
        title = parts[0]
        opis = parts[1] if len(parts) > 1 else ''
        done = parts[2].lower() == 'true' if len(parts) > 2 else False
        return cls(title, opis, done)

    def __str__(self):
        status = "DONE" if self.done else "TODO"
        return f"[{status}] {self.title}: {self.opis}"


class ToDoList:
    def __init__(self, file='lista.txt'):
        self.tasks = []
        self.file = file
        self.load()

    def add_task(self, task):
        self.tasks.append(task)
        self.save()

    def remove_task(self, i):
        if 0 <= i < len(self.tasks):
            del self.tasks[i]
            self.save()

    def show_tasks(self):
        if(not self.tasks):
            print("Prazna todo lista!")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def done(self, i):
        if(0 <= i < len(self.tasks)):
            self.tasks[i].mark_done()
            self.save()

    def save(self):
        with open(self.file, 'w') as f:
            for task in self.tasks:
                f.write(task.ispis() + '\n')

    def load(self):
        try:
            with open(self.file, 'r') as f:
                self.tasks = [Todo.from_line(line) for line in f]
        except FileNotFoundError:
            self.tasks = []


def main():
    todo = ToDoList()

    while True:
        print("")
        print("=== Todo lista ===")
        print("1. Dodaj\n2. Prikazi\n3. Oznaci kao uradjen\n4. Ukloni\n5. Quit")
        choice = input("Izaberi opciju: ")

        if(choice=="1"):
            title = input("Ime: ")
            opis = input("Opis: ")
            todo.add_task(Todo(title, opis))
        elif(choice=="2"):
            todo.show_tasks()
        elif(choice=="3"):
            todo.show_tasks()
            if(todo.tasks):
                id = int(input("Broj zadatka koji zelis oznaciti: "))
                todo.done(id)
        elif(choice=="4"):
            todo.show_tasks()
            if(todo.tasks):
                id = int(input("Broj zadatka koji zelis ukloniti: "))    
                todo.remove_task(id)
        elif(choice=="5" or choice=="q"):
            break
        else:
            print("Nope.")

if(__name__ == "__main__"):
    main()
