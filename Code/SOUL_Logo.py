from tkinter import *
from tkinter import Tk
import tkinter
import tkinter as tk
import turtle
import SOUL_Title_Song
import start_setup


root = Tk()

canvas = tk.Canvas(root,width=500,height=500)
canvas.pack()

#__________________S____________________

s = turtle.RawTurtle(canvas)

s.penup()
s.setx(-100)
s.sety(100)
s.pendown()

s.left(180)
s.forward(50)

s.left(90)
s.forward(100)

s.left(90)
s.forward(50)

s.right(90)
s.forward(100)

s.right(90)
s.forward(50)

#__________________O____________________

o = turtle.RawTurtle(canvas)
o.shape("circle")

o.penup()
o.setx(-80)
o.sety(100)
o.pendown()

o.right(90)
o.forward(200)

o.left(90)
o.forward(50)
o.left(90)
o.forward(100)
o.forward(100)
o.left(90)
o.forward(50)

#__________________U____________________

u = turtle.RawTurtle(canvas)
u.shape("circle")

u.penup()
u.setx(-10)
u.sety(100)
u.pendown()

u.right(90)
u.forward(200)

u.left(90)
u.forward(50)

u.left(90)
u.forward(200)

#__________________L____________________

l = turtle.RawTurtle(canvas)

l.penup()
l.setx(60)
l.sety(100)
l.pendown()

l.right(90)
l.forward(200)

l.left(90)
l.forward(50)

#SOUL_Title_Song.main()

l.forward(200)
s.forward(200)

root.destroy()
start_setup.main()

root.mainloop()
