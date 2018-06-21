import sample
from tkinter import *

my_first = sample.samp
print(my_first)
x = 0
y = 0
x0 = 0
y0 = 0
z = False
class main:
    def __init__(self):  # - конструктор, позволяющий создавать
        # экземпляры во время выполнения программы

        self.master = root
        self.master.title('parent')
        self.master.geometry('1000x400')
        self.xer = 1
        self.sp = my_first
        self.label = Label(self.master)
        self.label.configure(text='null')
        self.label.pack(side=BOTTOM)

        self.canva = Canvas(self.master,
                            width=1000,
                            height=300,
                            bg="gray",)

        #def in_rect_check(self):
        a = self.canva.create_rectangle(50, 50, 200, 100, tags="namba_one", fill = "purple")
        print(a)
        a = self.canva.create_rectangle(220, 50, 400, 100, tags="namba_one")
        print(a)
        a = self.canva.create_rectangle(50, 100, 200, 150, tags="namba_two", fill="purple")
        print(a)
        a = self.canva.create_rectangle(220, 100, 400, 150, tags="namba_two")
        print(a)
        self.canva.pack()

        def mouse_coord(event):
            global x, y, x0, y0, z
            if z == True:
                x, y = event.x, event.y
                self.canva.move(CURRENT, x - x0, y - y0)
                x, y = event.x, event.y
                x0 = x
                y0 = y



        self.canva.bind("<Motion>", mouse_coord)
# определяем нажатие в область прямоугольника
        def get_item(event):
            global x0, y0, z
            if self.canva.find_withtag(CURRENT):
                x, y = event.x, event.y
                x0 = x
                y0 = y
                z = True
                print("yoyo")
                self.label.configure(text="{},{}".format(x0, y0))
# определяем отпускание поднятого элемента
        def drop_item(event):
            global z
            z = False
        self.canva.bind("<ButtonRelease-1>", drop_item)

        self.canva.bind("<Button-1>", get_item)
        self.myText = Text(self.master,
                           background='white',
                           height=10,
                           width=25)
        self.myText.pack(side=LEFT, fill=NONE)
        self.master.mainloop()
    def resize_rect(self):
        pass
    def move_rect(self):
        pass


root = Tk()
main()