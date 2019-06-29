from tkinter import *
from All_Players import AllPlayers
import gspread
from player import Player
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("ABAStats.json", scope)
client = gspread.authorize(creds)

stats = client.open("ABA stats NEW").sheet1


class ABA:
    def __init__(self):
        self.mainroot = Tk()
        self.mainroot.withdraw()
        self.welcomescreen()

    # This creates the welcome screen
    def welcomescreen(self):
        self.root = Toplevel(self.mainroot)
        self.root.title("Fantasy Ashesi Basketball League")
        self.root.geometry("1080x1080+10+10")

        # To create a background image
        back = PhotoImage(file="ABA.png")
        backg = Label(self.root, image=back)
        backg.place(x=0, y=0, relwidth=1, relheight=1)

        intro = Label(self.root, text="Welcome to Fantasy Ashesi Basketball League", fg="red")
        intro.pack(side=TOP)
        next1 = Button(self.root, text="Pick Your Team", fg="Black", height=2, width=20,
                       command=self.to_next)

        next1.place(relx=0.42, rely=0.2)

        self.root.mainloop()


    def to_next(self):
        self.root.destroy()
        AllPlayers(self.mainroot, self)

    # To open the page of players set up on the court
    def c_window(self):
        name, row, teampic = self.mylist[0]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    #To display the stats of the players on the court when picked
    def sg_window(self):
        name, row, teampic = self.mylist[1]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def pf_window(self):
        name, row, teampic = self.mylist[2]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def sf_window(self):
        name, row, teampic = self.mylist[3]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def pg_window(self):
        name, row, teampic = self.mylist[4]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    # To open the stats of the subs when clicked
    def subs1_window(self):
        name, row, teampic = self.mylist[5]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs2_window(self):
        name, row, teampic = self.mylist[6]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs3_window(self):
        name, row, teampic = self.mylist[7]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs4_window(self):
        name, row, teampic = self.mylist[8]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs5_window(self):
        name, row, teampic = self.mylist[9]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs6_window(self):
        name, row, teampic = self.mylist[10]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    def subs7_window(self):
        name, row, teampic = self.mylist[11]
        self.name, self.row, self.teampic = name, row, teampic
        p = Player(self.mainroot, self.name, self.row, "stencil2.png", self.teampic)
        p.playerinfo()

    #Top create the window of the players displayed on the court
    def FABA(self, mylist, points, Allplayers_obj):
        self.mylist = mylist

        Allplayers_obj.main.destroy()

        master = Toplevel(self.mainroot)
        master.title("Fantasy Ashesi Basketball League")
        master.geometry("1920x1080+10+10")

        #To create and place the background picture
        background_image = PhotoImage(file="543489be84aafafe500002af.png")
        bg = Label(master, image=background_image, bg="brown")
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        totalpoints = 0
        for i in range(12):
            playerpoint = points[self.mylist[i][0]]
            totalpoints += float(playerpoint)


        #To create the points labels at the top of the window
        # pastweek = Button(master, text="Previous points", fg="red")
        current = Label(master, text="Totalpoints are: " + str(totalpoints), fg="Royalblue", font=("Roboto", "20", "bold", "italic"))
        # best = Button(master, text="highest points", fg="purple")

        # pastweek.place(relx=.001, rely=0)
        current.place(relx=0.46, rely=0)
        # best.place(relx=0.93, rely=0)

        # To open the stats of the players on the court when clicked
        player_image = PhotoImage(file="stencil1.png")

        # To create the subs at the bottom

        sub1 = Button(master, text=points[self.mylist[5][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs1_window)
        sub2 = Button(master, text=points[self.mylist[6][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs2_window)
        sub3 = Button(master, text=points[self.mylist[7][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs3_window)
        sub4 = Button(master, text=points[self.mylist[8][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs4_window)
        sub5 = Button(master, text=points[self.mylist[9][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs5_window)
        sub6 = Button(master, text=points[self.mylist[10][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs6_window)
        sub7 = Button(master, text=points[self.mylist[11][0]], font=("Roboto", "19", "bold", "italic"),
                      fg="blue", image=player_image, compound="top", command=self.subs7_window)

        subs = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
        x = 0.15
        for i in subs:
            i.place(relx=x, rely=0.85)
            x += 0.1

        # To create the players on the court
        c = Button(master, text=points[self.mylist[0][0]], font=("Roboto", "20", "bold", "italic"),
                   fg="orange", image=player_image, compound="top", command=self.c_window)
        pf = Button(master, text=points[self.mylist[1][0]], font=("Roboto", "20", "bold", "italic"),
                    fg="orange", image=player_image, compound="top", command=self.pf_window)
        sf = Button(master, text=points[self.mylist[2][0]], font=("Roboto", "20", "bold", "italic"),
                    fg="orange", image=player_image, compound="top", command=self.sf_window)
        pg = Button(master, text=points[self.mylist[3][0]], font=("Roboto", "20", "bold", "italic"),
                    fg="orange", image=player_image, compound="top", command=self.pg_window)
        sg = Button(master, text=points[self.mylist[4][0]], font=("Roboto", "20", "bold", "italic"),
                    fg="orange", image=player_image, compound="top", command=self.sg_window)

        c.place(relx=0.45, rely=0.2)
        pf.place(relx=0.2, rely=0.4)
        sf.place(relx=0.7, rely=0.4)
        pg.place(relx=0.6, rely=0.6)
        sg.place(relx=0.3, rely=0.6)

        master.mainloop()


main = ABA()
# main.FABA(main, list)














