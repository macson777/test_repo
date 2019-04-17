# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.


class Window:
    def __init__(self, figure, color, size):
        self.__figure = figure
        self.__color = color
        self.__size = size

    @property
    def open_window(self):
        print('Window open')

    def close_window(self):
        print('Window close')


    @property
    def figure(self):
        return self.__figure

    @figure.setter
    def figure(self, figure):
        self.__figure = figure

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


window = Window('square', 'white', '5x5')
window.open_window
window.close_window()
print(window.figure)
window.figure = 'rectangle'
print(window.figure)
print(window.color)
window.color = 'black'
print(window.color)
print(window.size)
window.size = '10x10'
print(window.size)


class ComputerMouse:
    def __init__(self, type, color, size):
        self.__type = type
        self.__color = color
        self.__size = size

    @property
    def turn_on_mouse(self):
        print('Mouse ON')

    def turn_off_mouse(self):
        print('Mouse OFF')


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


mouse = ComputerMouse('wireless', 'white', '3x3')
mouse.turn_on_mouse
mouse.turn_off_mouse()
print(mouse.type)
mouse.type = 'wire'
print(mouse.type)
print(mouse.color)
mouse.color = 'black'
print(mouse.color)
print(mouse.size)
mouse.size = '1x1'
print(mouse.size)


class NoteBook:
    def __init__(self, model_1, processor, ram):
        self.__model_1 = model_1
        self.__processor = processor
        self.__ram = ram

    @property
    def turn_on(self):
        print('NoteBook ON')

    def turn_off(self):
        print('NoteBook OFF')

    @property
    def model_1(self):
        return self.__model_1

    @model_1.setter
    def model_1(self, model_1):
        self.__model_1 = model_1

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, processor):
        self.__processor = processor

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram):
        self.__ram = ram


note = NoteBook('hp', 'i3', '4gb')
note.turn_on
note.turn_off()
print(note.model_1)
note.model_1 = 'apple'
print(note.model_1)
print(note.processor)
note.processor = 'i7'
print(note.processor)
print(note.ram)
note.ram = '16gb'
print(note.ram)
