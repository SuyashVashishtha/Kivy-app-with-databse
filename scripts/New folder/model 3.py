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
	desc1 = ObjectProperty(None)

	task2 = ObjectProperty(None)
	desc2 = ObjectProperty(None)

	task3 = ObjectProperty(None)
	desc3 = ObjectProperty(None)

	task4 = ObjectProperty(None)
	desc4 = ObjectProperty(None)

	task5 = ObjectProperty(None)
	desc5 = ObjectProperty(None)

	task6 = ObjectProperty(None)
	desc6 = ObjectProperty(None)

	addt = ObjectProperty(None)
	addd = ObjectProperty(None)

	



	def ref(self):
		

		con = sql.connect('task.db')
		cur = con.cursor()

		
		

		query = "SELECT name, description FROM Todolist WHERE no=1"
		cur.execute(query)
		for (name,description) in cur:

			self.task1.text = name
			self.desc1.text = description

				

			query = "SELECT name, description FROM Todolist WHERE no=2"
			cur.execute(query)

			for (name,description) in cur:
						
				self.task2.text = name
				self.desc2.text = description

							
				query = "SELECT name, description FROM Todolist WHERE no=3"
				cur.execute(query)

				for (name,description) in cur:
					

					self.task3.text = name
					self.desc3.text = description


					query = "SELECT name, description FROM Todolist WHERE no=4"
					cur.execute(query)

					for (name,description) in cur:
												

						self.task4.text = name
						self.desc4.text = description


						query = "SELECT name, description FROM Todolist WHERE no=5"
						cur.execute(query)

						for (name,description) in cur:
															

							self.task5.text = name
							self.desc5.text = description


							query = "SELECT name, description FROM Todolist WHERE no=6"
							cur.execute(query)

							for (name,description) in cur:
																		

								self.task6.text = name
								self.desc6.text = description







################## ADD POP UP ###################################################################################

	def addpop1(self):
	    show = a1()
	    

	    popupWindow = Popup(title="Add Task 1", content=show, size_hint=(None,None),size=(600,400))
		

	    popupWindow.open()
	    

	def addpop2(self):
	    show = a2()

	    popupWindow = Popup(title="Add Task 2", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    


	def addpop3(self):
	    show = a3()

	    popupWindow = Popup(title="Add Task 3", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

	def addpop4(self):
	    show = a4()

	    popupWindow = Popup(title="Add Task 4", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    


	def addpop5(self):
	    show = a5()

	    popupWindow = Popup(title="Add Task 5", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

	def addpop6(self):
	    show = a6()

	    popupWindow = Popup(title="Add Task 6", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()



######################### DELETE POP UP ########################################################################################
	    
	def delpop1(self):
	    show = d1()

	    popupWindow = Popup(title="Delete task 1", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

	def delpop2(self):
	    show = d2()

	    popupWindow = Popup(title="Delete task 2", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    


	def delpop3(self):
	    show = d3()

	    popupWindow = Popup(title="Delete task  3", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

	def delpop4(self):
	    show = d4()

	    popupWindow = Popup(title="Delete task  4", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    


	def delpop5(self):
	    show = d5()

	    popupWindow = Popup(title="Delete task  5", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    

	def delpop6(self):
	    show = d6()

	    popupWindow = Popup(title="Delete task  6", content=show, size_hint=(None,None),size=(600,400))

	    popupWindow.open()
	    
################################## Classes for pop ups ###################################

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


class d6(FloatLayout):
	def deltask6(self):

		con=sql.connect("task.db")
		cur=con.cursor()
		
		cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=6",("Task 6", "Description 6"))
		con.commit()
		con.close()

######################### ADD classes ####################################

class a1(FloatLayout):
	t1 = ObjectProperty(None)
	d1 = ObjectProperty(None)
	assd = ObjectProperty(None)


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





class a2(FloatLayout):
	t2 = ObjectProperty(None)
	d2 = ObjectProperty(None)

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



class a3(FloatLayout):
	t3 = ObjectProperty(None)
	d3 = ObjectProperty(None)

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


class a4(FloatLayout):
	t4 = ObjectProperty(None)
	d4 = ObjectProperty(None)

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

class a5(FloatLayout):
	t5 = ObjectProperty(None)
	d5 = ObjectProperty(None)

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


class a6(FloatLayout):
	t6 = ObjectProperty(None)
	d6 = ObjectProperty(None)

	def addtask6(self):
		if self.t6.text =="" and self.d6.text == "":
			self.t6.text = "Input Task"
			self.d6.text = "Input Description"
		else:
			con=sql.connect("task.db")
			cur=con.cursor()
			
			cur.execute("UPDATE Todolist SET name=?, description=? WHERE no=6",(self.t6.text, self.d6.text))
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



class MyMainApp(App):
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

#Window.size = (720, 1440)
    

if __name__ == "__main__":
    MyMainApp().run()
