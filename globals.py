from tkinter import *

init_pos_limit = 200
sheeps = []

window = Tk()
window.title('Wolf&Sheep')
window.geometry(str(3 * init_pos_limit) + 'x' + str(3 * init_pos_limit + 40) + '+500-100')
window.resizable(False, False)

canvas = Canvas(window, width=3 * init_pos_limit, height=3 * init_pos_limit, bg="#42F058")
canvas.pack()

var = StringVar()
sheep_label = Label(window, width=init_pos_limit//10, textvariable=var).place(x=2 * init_pos_limit, y=3 * init_pos_limit + init_pos_limit//21)


def update_sheep_label():
    var.set('Current sheep amount: ' + str(len(sheeps)))


def last_sheep_eaten():
    eaten_sheep_window = Toplevel(window)
    eaten_sheep_window.geometry('310x50+400-100')
    eaten_sheep_window.title('Wolf ate all sheep!')
    display = Label(eaten_sheep_window, text="There are no more sheep on map.")
    display.config(font=("Courier", 12))
    display.pack()
    eaten_sheep_window.focus_set()
    eaten_sheep_window.grab_set()


def create_circle(x, y, r, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, outline='')
