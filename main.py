from tkinter import *


def button_click():    # создаем функцию для выполнения действия после нажатия button
    new_text = input.get()                   # из далее созданного поля для ввода создаем переменную с текстом
    my_label.config(text=new_text)           # меняет label после вызова функции при нажатии кнопки


window = Tk()  # создаем окно через Tkinter.
window.title("My First GUI Program")                                # прописываем название окна
window.minsize(width=500, height=300)                               # прописываем размер окна
window.config(padx=20, pady=20)                                     # делает отступ от поля окна

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))   # создание компонента label и его вида
my_label.config(text="New Text")                                 # и так
my_label.grid(column=0, row=0)         # выводит и центрирует label на экран

#Buttons      # вызываем для отображения и настройки кнопки
button = Button(text="Click me", command=button_click) # вызов функции для выполнения без ()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)         # создаем в окне поле для ввода, устанавливаем ширину
input.get()
input.grid(column=3, row=2)



window.mainloop()      # выводит созданное окно, чтобы оно не исчезало.Прописывается внизу кода.
