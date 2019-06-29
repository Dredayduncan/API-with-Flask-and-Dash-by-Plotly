from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class AllPlayers:
    def __init__(self, root, ABA_obj):
        self.ABA_obj = ABA_obj
        self.scope = ['https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name("ABAStats.json", self.scope)
        self.client = gspread.authorize(self.credentials)
        self.stats = self.client.open("ABA stats NEW").sheet1
        self.playernames = self.stats.col_values(1)
        self.rows = {}
        self.main = Toplevel(root)
        self.main.title("All Players")
        self.main.geometry("1920x1080+10+10")
        self.list_lstboxes = []
        self.reslist = []
        self.scrll = Scrollbar(orient=VERTICAL, command=self.moving)
        self.scrll.pack(side=RIGHT, fill=Y)
        self.sroll = Scrollbar(orient=HORIZONTAL, command=self.moving)
        self.sroll.pack(side=BOTTOM, fill=X)
        self.topframe = Frame(self.main)
        self.topframe.pack(side=TOP)
        self.bottomframe = Frame(self.main)
        self.bottomframe.pack(side=BOTTOM)
        self.notice = Label(self.topframe, text="Take a look at the stats and select the names of your 12 players "
                                                "and click Next", background="grey22", width=120,
                       font=("Roboto", "25", "bold", "italic"), fg="Royalblue")
        self.notice.pack(fill="x")
        self.initialize()

    def moving(self, *args):
        for widget in self.list_lstboxes:
            widget.yview(*args)

    def Teampic(self, name):
        if name == "AshKnights":
            return "Ashknights.png"
        elif name == "Berekuso Warriors":
            return "Warriors.png"
        elif name == "LongShots":
            return "Longshots.png"
        elif name == "Los Ashtros":
            return "Los Ashtros.png"
        elif name == "HillBlazers":
            return "Hillblazers.png"

    def Points(self, players):
        total = 0
        numbers = [float(i) for i in players[7:12] if i != ""]
        for cat in numbers:
            point = cat / 2
            total += point
        self.rows[players[0]] = total

    def initialize(self):
        a = 1
        print("Initial Listboxes")
        for i in range(13):
            values = StringVar()
            values.set(self.stats.col_values(a))

            if a == 1:
                def OnMouseWheel(event):
                    for widget in self.list_lstboxes:
                        widget.yview("scroll", event.delta, "units")
                    # this prevents default bindings from firing, which
                    # would end up scrolling the widget twice
                    return "break"
                self.lstbox1 = Listbox(self.main, listvariable=values, selectmode=MULTIPLE, background="grey22", fg="Royalblue",
                             font=("Roboto", "20", "bold", "italic"), height=33, width=15, yscrollcommand=self.scrll.set)
                self.lstbox1.bind("<MouseWheel>", OnMouseWheel)
                self.lstbox1.pack(side=LEFT)
                self.list_lstboxes.append(self.lstbox1)


                def select(self):
                    selection = self.lstbox1.curselection()
                    if len(selection) == 12:
                        for i in selection:
                            name = self.lstbox1.get(i)
                            if name in self.playernames:
                                row_index = self.playernames.index(name)
                                row = self.stats.row_values(row_index + 1)
                                self.Points(row)
                                teamname = row[1]
                                info = (name, row, self.Teampic(teamname))
                                self.reslist.append(info)
                        self.ABA_obj.FABA(self.reslist, self.rows, self)
                    else:
                        warning = Toplevel(self.main)
                        warning.title("Error!")
                        warning.geometry("300x150+10+10")
                        notice = Message(warning, fg="red", text="You picked less or more than 12 players", font=("Roboto", "16", "bold", "italic"))
                        close = Button(warning, text="Close", command=warning.destroy, font=("Roboto", "20", "bold", "italic"))
                        close.pack()
                        notice.pack()

                next = Button(self.bottomframe, text="Next",fg="red", width=120, command=lambda: select(self),
                              font=("Roboto", "20", "bold", "italic"))
                next.pack()
                a += 1
            else:
                def OnMouseWheel(event):
                    event.widget.yview("scroll", event.delta, "units")
                    for widget in self.list_lstboxes:
                        widget.yview("scroll", event.delta, "units")
                    # this prevents default bindings from firing, which
                    # would end up scrolling the widget twice
                    return "break"
                lstbox = Listbox(self.main, listvariable=values, background="grey22", fg="floral white",
                                 font=("Roboto", "20", "bold", "italic"), height=33, width=9, yscrollcommand=self.scrll.set)
                lstbox.bind("<MouseWheel>", OnMouseWheel)
                lstbox.pack(side=LEFT)
                self.list_lstboxes.append(lstbox)
                a += 1


        self.main.mainloop()


