from task_list import TaskList
from task import Task
from sys import exit
import time
from display import Display


data = TaskList()
displays = Display()

MAIN_MENU = (
	"1: Display Tasks",
	"2: Add Tasks",
	"3: Mark Tasks Completed",
	"4: Remove Tasks",
	"0: Exit Program",
)

#BEGIN DICTIONARY


ADD_MENU = (
	"1: Add a New Task",
	"0: Return to Main Menu",
	)

REMOVE_MENU = (
	"1: Remove Task From List",
	"0: Return to Main Menu",
	)
def main_menu():
	while True:
		menu_selection = get_menu_selection(MAIN_MENU)

		if menu_selection == "1":
			displays.display_tasks(data)
		elif menu_selection == "2":
			add_tasks_menu()
		elif menu_selection == "3":
			pass
		elif menu_selection == "4":
			remove_tasks_menu()
		elif menu_selection == "0":
			exit(0)
		else:
			display_selection_error(menu_selection)

 

def add_tasks_menu():
	while True:
		menu_selection = get_menu_selection(ADD_MENU)

		if menu_selection == "1":
			### committed here
		elif menu_selection == "0":
			break
		else:
			display_selection_error(menu_selection)


#Begin Remove Tasks
def remove_tasks():
	for task in data:
		enumerate(displays.display_tasks(data))

def remove_tasks_menu():


	while True:
		menu_selection = get_menu_selection(REMOVE_MENU)

		if menu_selection == "1":
			remove_tasks()
		elif menu_selection == "0":
			break
		else:
			display_selection_error(menu_selection)	



###### making menu navigation
def main_menu():
	while True:
		menu_selection = get_menu_selection(MAIN_MENU)

		if menu_selection == "1":
			displays.display_tasks(data)
		elif menu_selection == "2":
			add_tasks_menu()
		elif menu_selection == "3":
			pass
		elif menu_selection == "4":
			remove_tasks_menu()
		elif menu_selection == "0":
			exit(0)
		else:
			display_selection_error(menu_selection)

def get_menu_selection(menu_items):
	print("\n")
	for menu_item in menu_items:
		print(menu_item)

	return input("\nPlease select an option from above. \n  >  ")

def display_selection_error(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again"
			.format(menu_selection))
	else:
		print("\n{} is not a number.  Please select from the options above."
			.format(menu_selection))
main_menu()