class Display():
	def display_tasks(self, tasks):
		print("\n")
		index = 1
		for task in tasks:
			print(str(index) + ": " + task.title + " " + str(task.complete))
			index += 1
		


		



