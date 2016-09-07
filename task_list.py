class TaskList: 
	def __init__(self):
		self.my_list = []
	def add_task(self, task):
		self.my_list.append(task)

	def remove_task(self,task):
		self.my_list.remove(task)