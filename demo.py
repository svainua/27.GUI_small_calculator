from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")  #отображает стартовый текст, в котором может быть подсказка для пользователя
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)                          #создание большого окна для ввода текста
#Puts cursor in textbox.
text.focus()                                                # устанавливает курсор в этом textbox
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")       #вводим текст, с которым начинаем
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))                                 # берем вводимый текст для использования. 1.0 для использования текста от первой буквы до последней
text.pack()

#Spinbox
def spinbox_used():                                                 # окошко с бегунком. Выбор чего-либо. .get берет выбранное действие для пользования
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale                                                          # бегунок, который изменяет что-то. берет инфу,на которой юзер остановился
#Called with current scale value.
def scale_used(value):                                          # через value передается значение, на котором юзер остановился
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton                                                    # при нажатии делается какой-то выбор.
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)  #variable берет на себя выбор, эта переменная распознается через класс IntVar(),
# т.е. это на самом деле класс. И когда мы создаем из этого класса Объект checked_state, мы можем вставить ее в checkbutton.
# И эта переменная будет содержать в себе выбор пользователя
checked_state.get()
checkbutton.pack()

#Radiobutton                                    # для выбора между несколькими опциями
def radio_used():
    print(radio_state.get())                        #когда опция определена, берет значение для использования
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()                              #создаем класс, определяем объект, который потом используется ниже в variable
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)     #используем, чтобы вызвать функцию listbox_used
listbox.pack()
window.mainloop()

