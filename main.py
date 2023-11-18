from tkinter import *
from tkinter import ttk

# Global Variables
counter = 0
window = Tk()
benched_count = 0

l = [Label(window, text = "Player 1:")]
e = [Entry(window)]
l[0].grid(row = 1, column = 2, sticky = W, pady = 2)
e[0].grid(row = 1, column = 3, pady = 2)

lbl = Label(window, text = "Active Players")
lbl.grid(row=0, column = 2, columnspan=2, pady = 2)

lbl2 = Label(window, text = "Benched Players")
lbl2.grid(row=0, column = 5, columnspan=2, pady = 2)

# Button Click Functions
def add_player():
    global counter, l, e, window
    counter += 1

    l.append(Label(window, text = "Player " + str(counter + 1) + ": "))
    l[counter].grid(row = counter+1, column = 2, sticky = W, pady = 2)

    e.append(Entry(window))
    e[counter].grid(row = counter+1, column = 3, pady = 2)

def remove(i, rb):
    global benched_count
    benched_count += 1

    for p in [p for p in range(len(e) - 1, -1, -1) if (e[p].grid_info()['column'] == 3)]:
        rb[-1].destroy()
        rb.pop()

    for p in [p for p in range(i, len(e)) if (e[p].grid_info()['column'] == 3)]:
        e[p].grid(row=e[p].grid_info()['row']-1)    
        l[p].grid(row=l[p].grid_info()['row']-1)    
    
    l[i].grid(row=benched_count, column=5, sticky=W, pady=2)
    e[i].grid(row=benched_count, column=6, pady=2)

def remove_player():
    rb = []

    for i in [i for i in range(len(e)) if (e[i].grid_info()['column'] == 3)]:
        rb.append(Button(window, text = "Bench", command=lambda k=(i): remove(k, rb)))
        rb[-1].grid(row = e[i].grid_info()['row'], column = 4, sticky = E)

def unremove(i, urb):
    global benched_count
    benched_count -= 1

    for p in [p for p in range(len(e) - 1, -1, -1) if (e[p].grid_info()['column'] == 6)]:
        urb[-1].destroy()
        urb.pop()

    for p in [p for p in range(i, len(e)) if (e[p].grid_info()['column'] == 6)]:
        e[p].grid(row=e[p].grid_info()['row']-1)    
        l[p].grid(row=l[p].grid_info()['row']-1)    
    
    l[i].grid(row=len([x for x in e for i in range(len(e) - 1) if e[i].grid_info()['column'] == 3]), column=2, sticky=W, pady=2)
    e[i].grid(row=len([x for x in e for i in range(len(e) - 1) if e[i].grid_info()['column'] == 3]), column=3, pady=2)

def unremove_player():
    urb = []

    for i in [i for i in range(len(e)) if (e[i].grid_info()['column'] == 6)]:
        urb.append(Button(window, text = "Unbench", command=lambda k=(i): unremove(k, urb)))
        urb[-1].grid(row = e[i].grid_info()['row'], column = 7, sticky = E)

img = PhotoImage(file = r"turt.png")
img1 = img.subsample(1, 1)
Label(window, image = img1).grid(row = 0, column = 1,
       columnspan = 1, rowspan = 20, padx = 5, pady = 5)

b = [Button(window, text = "Add Player", command=add_player)]
b[0].grid(row = 0, column = 0, sticky = E)
b.append(Button(window, text = "Bench Player", command=remove_player))
b[1].grid(row = 1, column = 0, sticky = E)
b.append(Button(window, text = "Unbench Player", command=unremove_player))
b[2].grid(row = 2, column = 0, sticky = E)

window.mainloop()