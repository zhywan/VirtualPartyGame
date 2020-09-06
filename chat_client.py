# import all the required  modules
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
import json
# import all functions /
#  everthing from chat.py file
#from chat import *

PORT = 5000
SERVER = "192.168.2.13"  # need to change the IP address of your server
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
TEXT_HEIGHT = 25
TEXT_WIDTH = 100
# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(ADDRESS)


# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self):

        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()

        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Cher Ami")
        self.login.resizable(width=True,
                             height=True)
        self.login.configure(width=400,
                             height=600)
        # create a Label
        self.pls = Label(self.login,
                         text="Welcome to Cher Ami!",
                         justify=CENTER,
                         font="Helvetica 14 bold")

        self.pls.place(height=TEXT_HEIGHT,
                       x=100,
                       y=60)

        # create a Label for Name
        self.labelName = Label(self.login,
                               text="Name: ",
                               font="Helvetica 14")

        self.labelName.place(height=TEXT_HEIGHT,
                             x=50,
                             y=130)

        # create a entry box for typing the message for Name
        self.entryName = Entry(self.login,
                               font="Helvetica 14")

        self.entryName.place(width=TEXT_WIDTH,
                             height=TEXT_HEIGHT,
                             x=160,
                             y=130)

        # create a Label for Gender
        self.labelGender = Label(self.login,
                                 text="Gender: ",
                                 font="Helvetica 14")

        self.labelGender.place(height=TEXT_HEIGHT,
                               x=50,
                               y=180)

        # create a radiobutton for selecting Gender
        gender = IntVar()
        Radiobutton(self.login, text="Male", font="Helvetica 14", padx=5, variable=gender, value=1)\
            .place(x=160, y=180)
        Radiobutton(self.login, text="Female", font="Helvetica 14", padx=20, variable=gender, value=0)\
            .place(x=270, y=180)

        # create a Label for Age
        self.labelAge = Label(self.login,
                              text="Age: ",
                              font="Helvetica 14")

        self.labelAge.place(height=TEXT_HEIGHT,
                            x=50,
                            y=230)

        # create a entry box for typing the message for Age
        self.entryAge = Entry(self.login,
                              font="Helvetica 14")

        self.entryAge.place(width=TEXT_WIDTH,
                            height=TEXT_HEIGHT,
                            x=160,
                            y=230)

        ##this creates 'Label' widget for Zodiac and uses place() method.
        self.labelZodiac = Label(self.login, text="Zodiac: ", font="Helvetica 14")
        self.labelZodiac.place(x=50, y=280)

        # this creates list of countries available in the dropdownlist.
        list_of_zodiac = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座',
                          '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']

        # the variable 'c' mentioned here holds String Value, by default ""
        zodiac = StringVar()
        droplist = OptionMenu(self.login, zodiac, *list_of_zodiac)
        zodiac.set('Select your Zodiac')
        droplist.place(x=160, y=280)

        ##this creates 'Label' widget for Music Taste and uses place() method.
        self.MusicTaste = Label(self.login, text="MusicTaste: ", font="Helvetica 14")
        self.MusicTaste.place(x=50, y=330)

        # the variable 'music1' mentioned here holds Integer Value, by default 0
        music1 = IntVar()
        # this creates Checkbutton widget and uses place() method.
        Checkbutton(self.login, text="嘻哈说唱", variable=music1).place(x=160, y=330)

        # the variable 'music2' mentioned here holds Integer Value, by default 0
        music2 = IntVar()
        Checkbutton(self.login, text="摇滚", variable=music2).place(x=270, y=330)

        # the variable 'music1' mentioned here holds Integer Value, by default 0
        music3 = IntVar()
        # this creates Checkbutton widget and uses place() method.
        Checkbutton(self.login, text="流行", variable=music3).place(x=50, y=380)

        # the variable 'music2' mentioned here holds Integer Value, by default 0
        music4 = IntVar()
        Checkbutton(self.login, text="民谣", variable=music4).place(x=160, y=380)

        # the variable 'music1' mentioned here holds Integer Value, by default 0
        music5 = IntVar()
        # this creates Checkbutton widget and uses place() method.
        Checkbutton(self.login, text="原声", variable=music5).place(x=270, y=380)

        # the variable 'music2' mentioned here holds Integer Value, by default 0
        music6 = IntVar()
        Checkbutton(self.login, text="电子", variable=music6).place(x=50, y=430)

        # the variable 'music1' mentioned here holds Integer Value, by default 0
        music7 = IntVar()
        # this creates Checkbutton widget and uses place() method.
        Checkbutton(self.login, text="轻音乐", variable=music7).place(x=160, y=430)

        # the variable 'music2' mentioned here holds Integer Value, by default 0
        music8 = IntVar()
        Checkbutton(self.login, text="爵士", variable=music8).place(x=270, y=430)

        # create a Label for Profile_URL
        self.labelProfile = Label(self.login,
                              text="Profile URL: ",
                              font="Helvetica 14")

        self.labelProfile.place(height=TEXT_HEIGHT,
                            x=50,
                            y=480)

        # create a entry box for typing the message for Age
        self.entryProfile = Entry(self.login,
                              font="Helvetica 14")

        self.entryProfile.place(width=TEXT_WIDTH * 2,
                            height=TEXT_HEIGHT,
                            x=160,
                            y=480)

        # set the focus of the curser
        self.entryName.focus()

        # pact all info
        info = {
            "name": self.entryName.get(),
            "gender": gender,
            "age": self.entryAge.get(),
            "zodiac": zodiac,
            "music_taste": [music1, music2, music3, music4, music5, music6, music7, music8],
            "profile_url": self.entryProfile.get()
        }
        # create a Register Button along with action
        self.go = Button(self.login,
                         text="SIGN IN",
                         font="Helvetica 14 bold",
                         command=lambda: self.goAhead(self.entryName.get(),
                                                      gender.get(),
                                                      self.entryAge.get(),
                                                      zodiac.get(),
                                                      [music1.get(), music2.get(), music3.get(), music4.get(),
                                                       music5.get(), music6.get(), music7.get(), music8.get()],
                                                      self.entryProfile.get()))

        self.go.place(x=50,
                      y=530)

        # create a Continue Button along with action
        self.go = Button(self.login,
                         text="SIGN UP",
                         font="Helvetica 14 bold",
                         command=lambda: self.goAhead(self.entryName.get(),
                                                      gender.get(),
                                                      self.entryAge.get(),
                                                      zodiac.get(),
                                                      [music1.get(), music2.get(), music3.get(), music4.get(),
                                                       music5.get(), music6.get(), music7.get(), music8.get()],
                                                      self.entryProfile.get()))

        self.go.place(x=250,
                      y=530)
        self.Window.mainloop()

    def goAhead(self, name, gender, age, zodiac, music_taste, profile_url):
        self.login.destroy()
        self.layout(name, gender, age, zodiac, music_taste, profile_url)

        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

        # The main layout of the chat

    def layout(self, name, gender, age, zodiac, music_taste, profile_url):

        self.name = name
        info = {
            "name": name,
            "gender": gender,
            "age": age,
            "zodiac": zodiac,
            "music_taste": music_taste,
            "profile_url": profile_url
        }
        self.info = info
        # to show chat window
        self.Window.deiconify()
        self.Window.title("GAME ROOM")
        self.Window.resizable(width=True,
                              height=True)
        self.Window.configure(width=400,
                              height=500,
                              bg="#17202A")
        self.labelHead = Label(self.Window,
                               bg="#17202A",
                               fg="#EAECEE",
                               text=self.name,
                               font="Helvetica 13 bold",
                               pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,
                          width=450,
                          bg="#ABB2B9")

        self.line.place(relwidth=1,
                        rely=0.07,
                        relheight=0.012)

        self.textCons = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=5,
                             pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.labelBottom = Label(self.Window,
                                 bg="#ABB2B9",
                                 height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                              bg="#2C3E50",
                              fg="#EAECEE",
                              font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74,
                            relheight=0.06,
                            rely=0.008,
                            relx=0.011)

        self.entryMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text="Send",
                                font="Helvetica 10 bold",
                                width=20,
                                bg="#ABB2B9",
                                command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.06,
                             relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

        # function to basically start the thread for sending messages

    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

        # function to receive messages

    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                # if the messages from the server is NAME send the client's name
                if message == 'INFO':
                    info_string = json.dumps(self.info)
                    client.send(info_string.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END,
                                         message + "\n\n")

                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break

                # function to send messages

    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

        # create a GUI class object


g = GUI()
