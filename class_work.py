"""Класс Privileges определяем без атрибута, атрибут определяется ниже.
Обрати внимание, что как определяется метод - табуляция на одном уровне
"""


class Privileges():
	def __init__(self): 
		self.privileges = [
			'разрешено добавлять сообщения',
			'разрешено удалять пользователей',
			'разрешено банить  пользователей'
			]
	
	def show_privileges(self): 
		print(self.privileges)

	
class Users():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
	
	def describe_user(self):
		print(
		    "Name: " +  self.first_name + ";" +
		    "\nLast name: " + self.last_name + ";" +
		    "\nAge: " + str(self.age) + ";" +
		    "\nLocation: " + self.location + "."
		    )
	def great_user(self):
		print("Hey, " + self.first_name + ", You are Great!\n")

class Admin(Users):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.for_privileges = Privileges()
		
my_users = Admin('Mikhail', 'Voitovich', 31, 'Kazan')
my_users.for_privileges.show_privileges()
