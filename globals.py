from tkinter import *

init_pos_limit = 200

window = Tk()
window.title('HeRb')
window.geometry(str(3 * init_pos_limit) + 'x' + str(3 * init_pos_limit + 40) + '+500-100')
window.resizable(False, False)

canvas = Canvas(window, width=3 * init_pos_limit, height=3 * init_pos_limit, bg="#42F058")
canvas.pack()

var = StringVar()
sheep_label = Label(window, textvariable=var).place(x=3 * init_pos_limit - 200, y=3 * init_pos_limit + 7)


def create_circle(x, y, r, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, outline='')
