import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.text import Text
from kivy.core.text.markup import *
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import os
import sqlite3 as sql







class Mainscreen(Screen):
    
    def btn(self):
        show_popup()

    class P(FloatLayout):
        pass
    
    

class Secondscreen(Screen):
    pass

class Thirdscreen(Screen):
    pass

class Fourthscreen(Screen):
    pass

class Fifthscreen(Screen):
	task1 = ObjectProperty(None)
	task2 = ObjectProperty(None)

	

		



	def ref(self):
		

		con = sql.connect('task.db')
		cur = con.cursor()

		
		

		query = "SELECT name, description FROM Todolist WHERE no=1"
		cur.execute(query)
		for (name,description) in cur:

			self.task1.text = name
			

				

		query = "SELECT name, description FROM Todolist WHERE no=2"
		cur.execute(query)

		for (name,description) in cur:
						
			self.task2.text = name
		

							
		query = "SELECT name, description FROM Todolist WHERE no=3"
		cur.execute(query)

		for (name,description) in cur:
					

			self.task3.text = name
			


		query = "SELECT name, description FROM Todolist WHERE no=4"
		cur.execute(query)

		for (name,description) in cur:
												

			self.task4.text = name
			

		query = "SELECT name, description FROM Todolist WHERE no=5"
		cur.execute(query)

		for (name,description) in cur:
															

			self.task5.text = name
			


							







################## ADD POP UP ###################################################################################

	def taskinfo1(self):
	    show = a1()
	    

	    popupWindow = Popup(title="Add Task 1", content=show, size_hint=(None,None),size=(600,700))
		

	    popupWindow.open()
	    

	def taskinfo2(self):
	    show = a2()

	    popupWindow = Popup(title="Add Task 2", content=show, size_hint=(None,None),size=(600,700))

	    popupWindow.open()
	    


	def taskinfo3(self):
	    show = a3()

	    popupWindow = Popup(title="Add Task 3", content=show, size_hint=(None,None),size=(600,700))

	    popupWindow.open()
	    

	def taskinfo4(self):
	    show = a4()

	    popupWindow = Popup(title="Add Task 4", content=show, size_hint=(None,None),size=(600,700))

	    popupWindow.open()
	    


	def taskinfo5(self):
	    show = a5()

	    popupWindow = Popup(title="Add Task 5", content=show, size_hint=(None,None),size=(600,700))

	    popupWindow.open()
	    

######################### ADD classes ####################################

class a1(FloatLayout):
	t1 = ObjectProperty(None)
	d1 = ObjectProperty(None)



	def fill1(self):
		con=sql.connect("task.db")
		cur=con.cursor()
		query = "SELECT name, description FROM Todolist WHERE no=1"
		cur.execute(query)
		for (name,description) in cur:
			self.t1.text = name
			self.d1.text = description
	


	def addtask1(self):
		if self.t1.text =="" and self.d1.text == "":
			self.t1.text = "Input Task"
			self.d1.text = "Input Description"
		else:

			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=1",(self.t1.text, self.d1.text))
			con.commit()
			con.close()

	def delpop1(self):

	    show = d1()

	    popupWindow = Popup(title="Delete task 1", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()


class a2(FloatLayout):
	t2 = ObjectProperty(None)
	d2 = ObjectProperty(None)


	def fill2(self):
		con=sql.connect("task.db")
		cur=con.cursor()
		query = "SELECT name, description FROM Todolist WHERE no=2"
		cur.execute(query)
		for (name,description) in cur:
			self.t2.text = name
			self.d2.text = description

	def addtask2(self):
		if self.t2.text =="" and self.d2.text == "":
			self.t2.text = "Input Task"
			self.d2.text = "Input Description"
		else:
			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=2",(self.t2.text, self.d2.text))
			con.commit()
			con.close()

	def delpop2(self):
	    show = d2()

	    popupWindow = Popup(title="Delete task 2", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()


class a3(FloatLayout):
	t3 = ObjectProperty(None)
	d3 = ObjectProperty(None)

	def fill3(self):
		con=sql.connect("task.db")
		cur=con.cursor()
		query = "SELECT name, description FROM Todolist WHERE no=3"
		cur.execute(query)
		for (name,description) in cur:
			self.t3.text = name
			self.d3.text = description

	def addtask3(self):
		if self.t3.text =="" and self.d3.text == "":
			self.t3.text = "Input Task"
			self.d3.text = "Input Description"
		else:
			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=3",(self.t3.text, self.d3.text))
			con.commit()
			con.close()

	def delpop3(self):
	    show = d3()

	    popupWindow = Popup(title="Delete task  3", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()


class a4(FloatLayout):
	t4 = ObjectProperty(None)
	d4 = ObjectProperty(None)

	def fill4(self):
		con=sql.connect("task.db")
		cur=con.cursor()
		query = "SELECT name, description FROM Todolist WHERE no=4"
		cur.execute(query)
		for (name,description) in cur:
			self.t4.text = name
			self.d4.text = description

	def addtask4(self):
		if self.t4.text =="" and self.d4.text == "":
			self.t4.text = "Input Task"
			self.d4.text = "Input Description"
		else:
			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=4",(self.t4.text, self.d4.text))
			con.commit()
			con.close()


	def delpop4(self):
	    show = d4()

	    popupWindow = Popup(title="Delete task  4", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

class a5(FloatLayout):
	t5 = ObjectProperty(None)
	d5 = ObjectProperty(None)

	def fill5(self):
		con=sql.connect("task.db")
		cur=con.cursor()
		query = "SELECT name, description FROM Todolist WHERE no=5"
		cur.execute(query)
		for (name,description) in cur:
			self.t5.text = name
			self.d5.text = description

	def addtask5(self):
		if self.t5.text =="" and self.d5.text == "":
			self.t5.text = "Input Task"
			self.d5.text = "Input Description"
		else:
			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=5",(self.t5.text, self.d5.text))
			con.commit()
			con.close()

	def delpop5(self):
	    show = d5()

	    popupWindow = Popup(title="Delete task  5", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()





##########################  DELETE classes ####################################
class d1(FloatLayout):
	


	def deltask1(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=1",("Task 1", "Description 1"))
		con.commit()
		con.close()


class d2(FloatLayout):

	def deltask2(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=2",("Task 2", "Description 2"))
		con.commit()
		con.close()

class d3(FloatLayout):
	def deltask3(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=3",("Task 3", "Description 3"))
		con.commit()
		con.close()


class d4(FloatLayout):
	def deltask4(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=4",("Task 4", "Description 4"))
		con.commit()
		con.close()

class d5(FloatLayout):
	def deltask5(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=5",("Task 5", "Description 5"))
		con.commit()
		con.close()





    



		

class CalcGridLayout(GridLayout):
    
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "ERROR"







class WindowManager(ScreenManager):
    pass

class Widgets(FloatLayout):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass





kv = Builder.load_file('my.kv')



class Toolkit(App):
	icon = 'toolkit.png'

	def build(self):
	    return kv


	con = sql.connect('task.db')
	cur = con.cursor()  
	con.commit()
	con.close()
       
def show_popup():
    show = P()

    popupWindow = Popup(title="About us", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


    

if __name__ == "__main__":
    Toolkit().run()
