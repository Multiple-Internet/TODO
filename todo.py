from task_list import TaskList
from task import Task
from sys import exit
import time
from display import Display


my_task_list = TaskList()
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

COMPLETE_MENU = (
	"1: Mark Task Complete",
	"0: Return to Main Menu",
	)

def main_menu():
	while True:
		menu_selection = get_menu_selection(MAIN_MENU)

		if menu_selection == "1":
			displays.display_tasks(my_task_list.my_list)
		elif menu_selection == "2":
			add_tasks_menu()
		elif menu_selection == "3":
			complete_task()
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
			my_task_list.add_task(input("What task would you like to add? \n >"))
		elif menu_selection == "0":
			break
		else:
			display_selection_error(menu_selection)

def remove_tasks_menu():
	while True:
		menu_selection = get_menu_selection(REMOVE_MENU)

		if menu_selection == "1":
			displays.display_tasks(my_task_list.my_list)
			my_task_list.remove_task(my_task_list.my_list[int(input("What number would you like to remove? \n >")) - 1])
		elif menu_selection == "0":
			break
		else:
			display_selection_error(menu_selection)	

def complete_task():
	while True:
		menu_selection = get_menu_selection(COMPLETE_MENU)

		if menu_selection == "1":
			displays.display_tasks(my_task_list.my_list)
			complete_answer = int(input("What number would you like to mark as complete? \n >")) - 1
			my_task_list.my_list[complete_answer].complete = True
			print(my_task_list.my_list)
		elif menu_selection == "0":
			break
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