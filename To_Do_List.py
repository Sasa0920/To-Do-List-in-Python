#Step 1 : Enter the date and add the tasks
#Step 2 : get the tasks after completion
#Step 3 : Display the to do list in a list format
#Step 4 : Save the tasks in a text file

def add_task():

  tasks = []
  name = input("Enter your name: ")
  print(f"Hi {name} , Let's add your today' tasks!")

  date = input("Enter the date (dd-mm-yyyy) : ")
  no_of_tasks = int(input("how many tasks do you want to add? "))

  for i in range(no_of_tasks):
    task = input(f"Enter the task {i+1}: ")
    tasks.append(task)

  completion=complete_task(tasks)
  display_to_do_list(date,tasks,completion)
  save_to_file(name,date,tasks,completion)
 

def complete_task(tasks):
  completion=[]
  
  for task in tasks:
    done =input(f"is {task} completed? (yes/no) : ").lower()

    if done =="yes":
      completion.append(task)
  
  return completion
  
def display_to_do_list(date,tasks,completion):
  print("To Do List")
  print("===========")
  print(f"Date : {date}")
  print(f"Tasks : {tasks}")
  print(f"Completed Tasks : {completion}")


def save_to_file(name,date,tasks,completion):
  with open("To_Do_List.json","a") as file: # open the file in append mode
    file.write(f"Name : {name}\n")
    file.write(f"Date : {date}\n")
    file.write(f"Tasks\n")
    for t in tasks:
      file.write(f"* {t}\n")
    file.write(f"Completed Tasks\n")
    for c in completion:
      file.write(f"* {c}\n")
  

add_task()


  