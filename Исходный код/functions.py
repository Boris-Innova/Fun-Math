from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import threading
from random import randint

class GIU():
	
	def __init__(self, window, top, event=None):
		"""Инициализация атрибутов"""
		self.window = window
		self.top = top
		
		self.x = self.window.winfo_screenwidth() # ширина экрана
		self.y = self.window.winfo_screenheight() # высота экрана
		
		# список для хранения изображений в памяти для быстрого извлечения
		self.images = []
		self.content = []
		self.memes = []
		self.devops = []
		self.sets = []
		self.practice1 = []
		self.practice2 = []
		self.practice3 = []
		self.practice4 = []
		self.practice5 = []
		self.practice6 = []
		self.practice = {1:'',2:'',3:'',4:'',5:'',6:''}
		self.faile_memes = []
		self.true_memes = []

		self.download_pictures() # загружаем изображения в списки
		
		# виджеты родительского окна
		self.canvas = self.create_canvas(self.window)
		self.buttons = self.create_buttons(self.window)
		self.check_button(event)
		
		# виджеты дочернего окна
		self.canvas_of_top = self.create_canvas(self.top, "top")
		
		self.num_theory = 0
		self.num_practice = 0
		self.index = 0
		self.get_meme = True
	

		
	def download_pictures(self):
		path = {0 :"all_pictures\\bg\\holly.png", 1 :"all_pictures\\active_picture\\book.png", 2 :"all_pictures\\active_picture\\fire.png", 3 :"all_pictures\\active_picture\\back.png", 4 :"all_pictures\\active_picture\\forward.png", 5:"all_pictures\\active_picture\\check.png", 6:"all_pictures\\active_picture\\choice.png", 7:"all_pictures\\active_picture\\smile.png", 8:"all_pictures\\active_picture\\homer.png"}
		x = { 0:self.x, 1:self.x, 2:int(self.x*0.3), 3:int(self.y*0.1), 4:int(self.y*0.1), 5:int(self.y*0.1), 6:int(self.y*0.1), 7:int(self.y*0.25), 8:int(self.y*0.75)}
		y = { 0:self.y, 1:self.y, 2:int(self.y*0.1), 3:int(self.y*0.1), 4:int(self.y*0.1), 5:int(self.y*0.1), 6:int(self.y*0.1), 7:int(self.y*0.25), 8:int(self.y*0.75)}
		for i in range(0,9): # загружаем изображения: фон и кнопки
			self.change_image(path[i], x[i], y[i])
			
		self.change_image("all_pictures\\main_mem.jpg", int(self.x*0.36), int(self.y*0.77))
		self.change_image("all_pictures\\settings\\1.jpg", int(self.x*0.8), int(self.y*0.8), "set")

		path = {1:"all_pictures\\1.jpg", 2:"all_pictures\\2.jpg", 3:"all_pictures\\3.jpg", 4:"all_pictures\\4.jpg", 5:"all_pictures\\5.jpg", 6:"all_pictures\\6.jpg"}
		for i in range(1,7): # загружаем мемы
			self.change_image(path[i], int(self.x*0.36), int(self.y*0.77), "memes")
		
		nums = {1:3, 2:5, 3:6, 4:3, 5:3, 6:3}
		for i in range(1,7):
			for k in range(1, nums[i]+1):
				path = {i:f"all_pictures\\limit\\{i}\\{i}_{k}.jpg"}
				self.change_image(path[i], int(self.x*0.8), int(self.y*0.8), "content")
		
		nums = {1:4, 2:5, 3:6, 4:4, 5:8, 6:5}
		flags = {1:self.practice1, 2:self.practice2, 3:self.practice3, 4:self.practice4, 5:self.practice5, 6:self.practice6}
		for i in range(1,7):
			for k in range(1,nums[i]):
				path = f"all_pictures\\practice\\{i}\\{k}.jpg"
				self.change_image(path, int(self.x*0.4), int(self.y*0.2), f"p{i}")
				for n in range(1, 6):
					path = f"all_pictures\\practice\\{i}\\{k}{n}.jpg"
					self.change_image(path, int(self.x*0.375), int(self.y*0.08), f"p{i}")
			self.practice[i] = flags[i]
			
		for i in range(1, 14):
			path = f"all_pictures\\faile\\{i}.jpg"
			self.change_image(path, int(self.x*0.36), int(self.y*0.77), "faile")
		
		for i in range(1, 10):
			path = f"all_pictures\\true\\{i}.jpg"
			self.change_image(path, int(self.x*0.36), int(self.y*0.77), "true")
		
		for i in range(1, 4):	
			path = f"all_pictures\\about_me\\{i}.png"
			picture = self.change_image(path, int(self.x*0.13), int(self.y*0.225), "devops")
			
							
	def read_txt(self, path): # читает текстовый файл и возвращает информацию
		with open(path, encoding="utf-8") as file_object:
			message = file_object.read()
		return message
		
	def change_image(self, path, x, y, flag=None): # обработка изображения и возвращение его
		image = Image.open(path)
		image = image.resize((x, y))
		image = ImageTk.PhotoImage(image)
		if flag == "content":
			self.content.append(image) # фон
		elif flag == "memes":
			self.memes.append(image)
		elif flag == "p1":
			self.practice1.append(image)
		elif flag == "p2":
			self.practice2.append(image)
		elif flag == "p3":
			self.practice3.append(image)
		elif flag == "p4":
			self.practice4.append(image)
		elif flag == "p5":
			self.practice5.append(image)
		elif flag == "p6":
			self.practice6.append(image)
		elif flag == "true":
			self.true_memes.append(image)
		elif flag == "faile":
			self.faile_memes.append(image)
		elif flag == "devops":
			self.devops.append(image)
		elif flag == "set":
			self.sets.append(image)
		else:
			self.images.append(image)
		return image
					
	def create_canvas(self, window, flag="window"): # создаем холст на весь экран и размещаем на нем изображение
		canvas = Canvas(window, width=self.x, height=self.y)
		canvas.grid(row=0, column=0)
		if flag == "top":
			return canvas
		canvas.create_image(0, 0, anchor=NW, image=self.images[0])
		canvas.create_image(self.x, self.y, anchor=SE, image=self.images[7])
		canvas.create_image(0, self.y, anchor=SW, image=self.images[7])
		canvas.create_text(int(self.x*0.5), int(self.y*0.1), anchor=CENTER, text="МАТЕМАТИЧЕСКИЙ АНАЛИЗ", font="Courier 48", fill="white")
		return canvas
				
	def create_buttons(self, window): # создание кнопок в родительском окне
		buttons = []
		texts = {0:"Анализировать", 1:"Помощь", 2:"Настройки", 3:"Разработчики", 4:"Выход"}
		x, y = self.x*0.5, self.y*0.2
		for i in range(0,5):
			button = Button(window, width=int(self.x*0.3), height=int(self.y*0.1), anchor=CENTER, bg="black", fg="black", text=texts[i], bd=5, font="Arial 22", image=self.images[2], compound=CENTER)
			self.canvas.create_window(x, y, anchor=CENTER, window=button) # размещаем кнопки на холсте
			y += self.y*0.1575
			buttons.append(button)
		return buttons
			
	def check_button(self, event): # обрабатывает события в родительском окне
		cmds = {0:self.eval_math, 1:self.about_app, 2:self.settings, 3:self.developers, 4:sys.exit}
		for button in self.buttons:
			self.bind_check(event, button, cmds[self.buttons.index(button)])
			
	def but_motion(self, event, button): # конфигурация кнопки при наведении на нее
		button.config(bd=10, fg="white")
	
	def but_leave(self, event, button): # конфигурация кнопки при покидании ее курсором
		button.config(bd=5, fg="black")
	
	def focus_on_window(self, event=None): # меняет фокус на род.окно и очищает дочернее окно
		self.canvas_of_top.delete("all")
		self.window.focus()
				
	def update_top(self, event=None): # меняет содержимое дочернего окна
		self.canvas_of_top.delete("all")
		self.canvas_of_top.create_image(0, 0, anchor=NW, image=self.images[1])
	
	def func_bf(self, event, cmd, flag=None): # функция для кнопки вперед
		self.update_top(event)
		self.num_theory += 1
		self.num_practice += 1
		cmd(event)
		
	def func_bb(self, event, cmd): # функция для кнопки назад
		self.update_top(event)
		if self.check_current_theory(self.index) == False:
			self.num_theory -= 1
		if self.check_current_practice(self.index) == False:
			self.num_practice -= 1
		cmd(event)
		
	def bind_check(self, event, button, command, flag=False): # обрабатывает нажатие кнопки для дочерних окон.
		if flag == False:
			button.bind("<ButtonRelease-1>", command)
		elif flag == "forward":
			button.bind("<ButtonRelease-1>", lambda event, cmd=command: self.func_bf(event, cmd))
		elif flag == "back":
			button.bind("<ButtonRelease-1>", lambda event, cmd=command: self.func_bb(event, cmd))
			
		button.bind("<Motion>", lambda event, but=button: self.but_motion(event, but))
		button.bind("<Leave>", lambda event, but=button: self.but_leave(event, but))

	def button_back(self, event, cmd): # создает кнопку "Назад" на холсте с обработкой событий
		button = Button(self.top, width=int(self.y*0.1), height=int(self.y*0.1), image=self.images[3], bg="black", compound=CENTER)
		self.canvas_of_top.create_window(int(self.x*0.08), int(self.y*0.89), anchor=CENTER, window=button) # размещаем кнопку на холсте
		self.bind_check(event, button, cmd, "back")
		self.get_meme = True
	
	def button_forward(self, event, cmd): # создает кнопку "Вперед" на холсте с обработкой событий
		button = Button(self.top, width=int(self.y*0.1), height=int(self.y*0.1), image=self.images[4], bg="black", compound=CENTER)
		self.canvas_of_top.create_window(int(self.x*0.95), int(self.y*0.89), anchor=CENTER, window=button) # размещаем кнопку на холсте
		self.bind_check(event, button, cmd, "forward")
		self.get_meme = True
	
	def developers(self, event): # обработка кнопки "Разработчики"
		self.update_top(event)
		self.button_back(event, self.focus_on_window) # кнопка назад
		y = {0:0.175, 1:0.475, 2:0.775}
		for i in range(0, 3):
			self.canvas_of_top.create_image(self.x*0.32, self.y*y[i], anchor=CENTER, image=self.devops[i])

		path = "all_pictures\\about_me\\about_me.txt"
		content = self.read_txt(path)
		self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, text=content, font=32, width=int(self.x*0.33))
		self.top.focus()
		
	def settings(self, event): # обработка кнопки "Настройки
		self.update_top(event)
		self.canvas_of_top.create_text(self.x*0.5, self.y*0.065, anchor=CENTER, text="АХАХАХАХА, ВЫ ХОТЕЛИ ПОМЕНЯТЬ НАСТРОЙКИ?🤣🤣🤣🤣🤣", fill="black", font=72)
		self.canvas_of_top.create_image(self.x*0.515, self.y*0.5, anchor=CENTER, image=self.sets[0])
		self.button_back(event, self.focus_on_window) # кнопка назад
		self.top.focus()

	def about_app(self, event): # обработка кнопки "Помощь"
		self.update_top(event)
		self.button_back(event, self.focus_on_window) # кнопка назад
		content = self.read_txt("all_pictures\\help\\help.txt")
		self.canvas_of_top.create_text(self.x*0.32, self.y*0.45, anchor=CENTER, text=content, font='Arial 12', width=int(self.x*0.33))
		self.canvas_of_top.create_image(self.x*0.725, self.y*0.5, anchor=CENTER, image=self.images[8])
		self.top.focus()
		
	def eval_math(self, event): # обработка кнопки "Анализировать"
		self.update_top(event)
		self.button_back(event, self.focus_on_window) # кнопка назад
		self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.images[-1])
		texts = {
					"Ⅰ":"Числовая последовательность", 
					"Ⅱ":"Функция одной переменной", 
					"Ⅲ":"Предел числовой последовательности и функции",
					"Ⅳ":"Непрерывность функции и точки ее разрыва",
					"Ⅴ":"Раскрытие простейших неопределенностей",
					"Ⅵ":"Асимптоты графика функции"
				}
		nums = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ"]
		y = self.y*0.14
		for i in range(1, 7):
			self.canvas_of_top.create_text(int(self.x*0.32), int(y-self.y*0.07), text=f"{nums[i-1]}", font="Arial 26")
			but = Button(self.top, width=int(self.x*0.3), height=int(self.y*0.06), anchor=CENTER, bg="black", fg="black", text=texts[nums[i-1]], bd=5, font="Arial 14", image=self.images[2], compound=CENTER)
			self.canvas_of_top.create_window(int(self.x*0.32), int(y), anchor=CENTER, window=but)
			self.bind_check(event, but, lambda event, index=i: self.choice_practice_theory(event, index)) # связывает каждую кнопку с событием
			y += self.y*0.14
		self.top.focus()
	
		
	def choice_practice_theory(self, event, index): # выбор теория/практика
		self.update_top(event)
		self.index = index
		self.num_theory = self.return_num(index)
		self.num_practice = self.return_num_practice(index)
		self.button_back(event, self.eval_math)	
		cmds = {1:lambda event, index=index: self.get_theory(event, index), 2:lambda event, index=index: self.get_practice(event, index)}
		texts = {1:"Теория", 2:"Практика"}
		y = self.y*0.3
		for i in range(1, 3):
			but = Button(self.top, width=int(self.x*0.3), height=int(self.y*0.1), anchor=CENTER, bg="black", fg="black", text=texts[i], bd=5, font="Arial 26", image=self.images[2], compound=CENTER)
			self.canvas_of_top.create_window(int(self.x*0.32), int(y), anchor=CENTER, window=but)
			self.bind_check(event, but, cmds[i]) # связывает каждую кнопку с событием
			y += self.y*0.3
		self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.memes[index-1])
		self.top.focus()
		
	def check_end_theory(self, index): # проверка окончания теории
		nums = {1:0, 2:3, 3:8, 4:14, 5:17, 6:20}
		if (index == 1 and self.num_theory == 2):
			return False
		elif (index == 2 and self.num_theory == 7):
			return False
		elif (index == 3 and self.num_theory == 13):
			return False
		elif (index == 4 and self.num_theory == 16):
			return False
		elif (index == 5 and self.num_theory == 19):
			return False
		elif (index == 6 and self.num_theory == 22):
			return False
		else:
			return True
	
	def check_current_theory(self, index): # проверка текущего положения теория
		if (index == 1 and self.num_theory > 0):
			return False
		elif (index == 2 and self.num_theory > 3):
			return False
		elif (index == 3 and self.num_theory > 8):
			return False
		elif (index == 4 and self.num_theory > 14):
			return False
		elif (index == 5 and self.num_theory > 17):
			return False
		elif (index == 6 and self.num_theory > 20):
			return False
		else:
			return True		
	
	def return_num(self, index): 
		if index == 1:
			return 0
		elif index == 2:
			return 3
		elif index == 3:
			return 8
		elif index == 4:
			return 14
		elif index == 5:
			return 17
		elif index == 6:
			return 20			
				
	def get_theory(self, event, index): # теория
		self.update_top(event)
		
		if self.check_end_theory(index) == True:
			self.button_forward(event, lambda event, i=index: self.get_theory(event, i))
		else:
			self.create_button_to_choice(event, index)
			
		if self.check_current_theory(index) == False:
			commanda = lambda event, i=index:self.get_theory(event, index)		
		else:
			commanda = lambda event, i=index:self.choice_practice_theory(event, i)
			
		self.button_back(event, commanda)
		self.canvas_of_top.create_image(int(self.x*0.515), int(self.y*0.5), anchor=CENTER, image=self.content[self.num_theory])


	def check_end_practice(self, index): # проверка окончания практики
		if (index == 1 and self.num_practice == 2):
			return False
		elif (index == 2 and self.num_practice == 6):
			return False
		elif (index == 3 and self.num_practice == 11):
			return False
		elif (index == 4 and self.num_practice == 14):
			return False
		elif (index == 5 and self.num_practice == 21):
			return False
		elif (index == 6 and self.num_practice == 25):
			return False
		else:
			return True

	def check_current_practice(self, index): # проверка текущего положения практика
		if (index == 1 and self.num_practice > 0):
			return False
		elif (index == 2 and self.num_practice > 3):
			return False
		elif (index == 3 and self.num_practice > 7):
			return False
		elif (index == 4 and self.num_practice > 12):
			return False
		elif (index == 5 and self.num_practice > 15):
			return False
		elif (index == 6 and self.num_practice > 22):
			return False
		else:
			return True	
	
	def return_num_practice(self, index):
		if index == 1:
			return 0
		elif index == 2:
			return 3
		elif index == 3:
			return 7
		elif index == 4:
			return 12
		elif index == 5:
			return 15
		elif index == 6:
			return 22	
	
	
	def create_radio(self, event, index):
		k = {0:0, 1:6, 2:12, 3:0, 4:6, 5:12, 6:18, 7:0, 8:6, 9:12, 10:18, 11:24, 12:0, 13:6, 14:12, 15:0, 16:6, 17:12, 18:18, 19:24, 20:30, 21:36, 22:0, 23:6, 24:12, 25:18}
		self.canvas_of_top.create_image(int(self.x*0.32), int(self.y*0.15), anchor=CENTER, image=self.practice[index][k[self.num_practice]])
		self.canvas_of_top.create_text(int(self.x*0.32), int(self.y*0.3), anchor=CENTER, text="Выберите один из вариантов", font="Courier 16")
		global int_var
		int_var = IntVar()
		int_var.set(0)
		for i in range(1,6):
			radiobutton = Radiobutton(self.top, width=int(self.x*0.375), height=int(self.y*0.08), bg="white", image=self.practice[index][k[self.num_practice]+i], compound=CENTER, variable=int_var, value=i)
			self.canvas_of_top.create_window(int(self.x*0.32), int(self.y*(0.3+i*0.1)), anchor=CENTER, window=radiobutton)		
	
	def create_checkbutton(self, event, index):
		k = {0:0, 1:6, 2:12, 3:0, 4:6, 5:12, 6:18, 7:0, 8:6, 9:12, 10:18, 11:24, 12:0, 13:6, 14:12, 15:0, 16:6, 17:12, 18:18, 19:24, 20:30, 21:36, 22:0, 23:6, 24:12, 25:18}
		self.canvas_of_top.create_image(int(self.x*0.32), int(self.y*0.15), anchor=CENTER, image=self.practice[index][k[self.num_practice]])
		self.canvas_of_top.create_text(int(self.x*0.32), int(self.y*0.3), anchor=CENTER, text="Выберите верные варианты ответов", font="Courier 16")
		global var1, var2, var3, var4, var5
		var1, var2, var3, var4, var5 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
		global varss
		varss = {1:var1, 2:var2, 3:var3, 4:var4, 5:var5}
		for i in range(1,6):
			checkbutton = Checkbutton(self.top, width=int(self.x*0.375), height=int(self.y*0.08), bg="white", image=self.practice[index][k[self.num_practice]+i], compound=CENTER, variable=varss[i], onvalue=i, offvalue=0)
			self.canvas_of_top.create_window(int(self.x*0.32), int(self.y*(0.3+i*0.1)), anchor=CENTER, window=checkbutton)		
	
	def check_true_false(self, event, index): # проверяет правильный ответ или нет
		k = {0:1, 1:4, 2:1, 3:1, 4:2, 5:4, 6:1, 7:1, 8:2, 9:3, 10:1, 11:5, 12:[3], 13:[1,2], 14:[4,5], 15:3, 16:3, 17:5, 18:2, 19:3, 20:2, 21:1, 22:[4], 23:[1,4], 24:[2,4,5], 25:[2,3]}

		if (index != 4 and index !=6):
			if k[self.num_practice] == int_var.get():
				try:
					self.canvas_of_top.delete("my_tag")
				except:
					None
				try:
					self.canvas_of_top.delete("my_tag2")
				except:
					None
				self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="ВЕРНО!", font="Courier 48", fill="green")
				self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.true_memes[randint(0,8)])
				button_check.unbind("<ButtonRelease-1>")
				self.get_meme = True
			elif int_var.get() == 0:
				self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="Выберите вариант ответа!", font="Courier 16", fill="black", tags="my_tag2")
			else:
				if self.get_meme == True:
					self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="НЕВЕРНО!", font="Courier 48", fill="red", tags="my_tag")
					self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.faile_memes[randint(0,12)], tags="my_tag")
					self.get_meme = False
		else:
			my_list = []
			for i in range(1,6):
				if varss[i].get() != 0:
					my_list.append(varss[i].get())
			if k[self.num_practice] == my_list:
				try:
					self.canvas_of_top.delete("my_tag")
				except:
					None
				try:
					self.canvas_of_top.delete("my_tag2")
				except:
					None							
				self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="ВЕРНО!", font="Courier 48", fill="green")
				self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.true_memes[randint(0,8)])
				button_check.unbind("<ButtonRelease-1>")
				self.get_meme = False
			elif len(my_list) == 0:
				self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="Выберите вариант ответа!", font="Courier 16", fill="black", tags="my_tag2")
			else:
				if self.get_meme == True:
					self.canvas_of_top.create_text(int(self.x*0.725), int(self.y*0.08), anchor=CENTER, text="НЕВЕРНО!", font="Courier 48", fill="red", tags="my_tag")
					self.canvas_of_top.create_image(int(self.x*0.725), int(self.y*0.5), anchor=CENTER, image=self.faile_memes[randint(0,12)], tags="my_tag")
					self.get_meme = False
	
	def create_button_to_choice(self, event, index):
		button = Button(self.top, width=int(self.y*0.1), height=int(self.y*0.1), bd=5, anchor=CENTER, bg="black", image=self.images[6], compound=CENTER)
		self.bind_check(event, button, lambda event, i=index:self.choice_practice_theory(event, i))
		self.canvas_of_top.create_window(int(self.x*0.95), int(self.y*0.89), anchor=CENTER, window=button) # размещаем кнопки на холсте
		
				
	def get_practice(self, event, index): # практика
		self.update_top(event)
		if self.check_end_practice(index) == True:
			self.button_forward(event, lambda event, i=index: self.get_practice(event, i))
		else:
			self.create_button_to_choice(event, index)
			
		if self.check_current_practice(index) == False:
			commanda = lambda event, i=index:self.get_practice(event, index)		
		else:
			commanda = lambda event, i=index:self.choice_practice_theory(event, i)
		self.button_back(event, commanda)
		if (index == 4 or index == 6):
			self.create_checkbutton(event, index)
		else:
			self.create_radio(event, index)
		
		global button_check
		button_check = Button(self.top, width=int(self.y*0.1), height=int(self.y*0.1), anchor=CENTER, bg="black", fg="black", bd=5, font="Arial 22", image=self.images[5], compound=CENTER)
		self.bind_check(event, button_check, lambda event, i=index: self.check_true_false(event, i))
		self.canvas_of_top.create_window(self.x*0.5, self.y*0.9, anchor=CENTER, window=button_check) # размещаем кнопку на холсте
