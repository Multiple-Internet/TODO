from sys import exit
import time
from display import Display

### Defines Main Menu
class TODO():
	def __init__(self):
		self.data = {}
		self.displays = Display()

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

	def add_tasks(self):
		task_input = input("What do you need to do? \n >")
		self.data[task_input] = time.time()
		#example d['mynewkey'] = 'mynewvalue'


	def add_tasks_menu(self):
		while True:
			menu_selection = self.get_menu_selection(self.ADD_MENU)

			if menu_selection == "1":
				self.add_tasks()
			elif menu_selection == "0":
				break
			else:
				display_selection_error(menu_selection)
	


	###### making menu navigation
	def main_menu(self):
		while True:
			menu_selection = self.get_menu_selection(self.MAIN_MENU)

			if menu_selection == "1":
				self.displays.display_tasks(self.data)
			elif menu_selection == "2":
				self.add_tasks_menu()
			elif menu_selection == "3":
				pass
			elif menu_selection == "4":
				pass
			elif menu_selection == "0":
				exit(0)
			else:
				display_selection_error(menu_selection)

	def get_menu_selection(self, menu_items):
		print("\n")
		for menu_item in menu_items:
			print(menu_item)

		return input("\nPlease select an option from above. \n  >  ")

	def display_selection_error(self, menu_selection):
		if menu_selection.isdigit():
			print("\n{} is an invalid option, please try again"
				.format(menu_selection))
		else:
			print("\n{} is not a number.  Please select from the options above."
				.format(menu_selection))