x = int(input("Введите  начальные координаты по оси Х(по горизонтали): "))
y  = int(input("Введите начальные координаты по оси Y(по вертикали): "))
s = int(input("Введите количество клеток хода: "))

class Turtle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        
        
    def go_up(self):
        turtle.y+=s
        return turtle.y

    def go_down(self):
        turtle.y-=s
        return turtle.y

    def go_left(self):
        turtle.x -=s
        return turtle.x

    def go_right(self):
        turtle.x+=s
        return turtle.x

    def evolve(self):
        turtle.s+=1
        return turtle.s

    def degrade(self):
        if turtle.s <= 0:
            print('Error')
        else:
            turtle.s-=1
        return turtle.s

    def count_moves(self,x2, y2):
        return turtle.x -x2, turtle.y -y2


turtle = Turtle(x,y,s)
x2 = int(input("введите конечные координаты по оси Х: "))
y2 = int(input("Введите конечные координаты по оси Y: "))


print(f'Черепашка поднялась вверх  по оси Y  до точки {turtle.go_up()}')
print(f"Черепашка опустилась вниз по оси Y до точки {turtle.go_down()}")
print(f"Черепашка переместилась влево по оси Х до точки {turtle.go_left()}")
print(f"Черепашка переместилась вправо по оси Х до точки {turtle.go_right()}")
print(turtle.evolve())
print(turtle.degrade())
print(f'Минимальное сделанное количество ходов: {turtle.count_moves(x2,y2)}')