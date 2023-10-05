import functions
import time

time_today = time.strftime("%b %d, %Y %H:%M:%S")
print("Today is :", time_today)


while True:
   user_action = input("Select: add, show, complete, or exit: ")
   user_action = user_action.strip()

   if user_action.startswith("add"):
      todo = user_action[4:]

      todos = functions.get_todos()

      todos.append(todo + '\n')

      functions.write_todos(todos)

   elif user_action.startswith("show"):

         todos = functions.get_todos()

         for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}:{item}"
            print(row)

   elif user_action.startswith("edit"):
       try:
            todo = user_action[5:]
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()
            print("this are the existing todos: ", todos)

            new_todo = input("Enter the new todo: ")

            todos[number] = new_todo + "\n"
            print("This are are new todos", todos)

            functions.write_todos(todos)

       except ValueError:
           print("your command is not Valid!!")
           continue

   elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
                 print("There is item with this number")
                 continue

   elif user_action.startswith("exit"):
          print("Bye!!!")
          break
   else:
          print("You have entered invalid option!!!")

