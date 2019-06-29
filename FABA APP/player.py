from tkinter import *


class Player:
    def __init__(self, root, name, row, image, teampic):
        self.root = root
        self.name = name
        self.row = row
        self.image = image
        self.teampic = teampic

    def playerinfo(self):
        window = Toplevel(self.root)
        window.geometry("900x900+10+10")
        background = PhotoImage(file="ABA2.png")
        bg = Label(window, image=background, bg="grey99")
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        topframe = Frame(window, bg="grey99")
        topframe.pack(side=TOP)

        picture = PhotoImage(file=self.image)
        img = Label(topframe, image=picture, compound="top")
        img.image = picture
        img.pack(side=LEFT)

        info = Label(topframe, text=self.name, fg="Black", height=2, width=70, bg="gold",
                     font=("arial", "30", "bold", "italic"))
        info.pack(side=LEFT, anchor=NW)

        teamimage = PhotoImage(file=self.teampic)
        photo = Label(topframe, image=teamimage, compound="top")
        photo.image = teamimage
        photo.pack(side=LEFT, anchor=SW)

        canvas = Canvas(topframe, width=600, height=212)
        canvas.create_image(0, 0, image=teamimage, anchor=NW)

        canvas.place(x=304, y=55)

        bottomframe = Frame(window, bg="grey99")
        bottomframe.pack()

        head = ["Name", "Team", "PPG", "APG", "RPG", "SPG", "BPG", "Total Points", "Total Assists", "Total Rebounds",
                "Total Steals", "Total Blocks", "Games Played"]
        print("Loading...")
        x = 0
        for t in head:
            header = Label(bottomframe, text=t, bg="grey99", fg="red", font=("arial","12", "bold"))
            header.grid(column=x, row=1, sticky=W)
            x += 1
        x = 0
        for i in self.row:
            a = Label(bottomframe, text=i, fg="blue", bg="grey99", font=("arial", "12", "bold"))
            a.grid(column=x, row=2)
            x += 1


        window.mainloop()

