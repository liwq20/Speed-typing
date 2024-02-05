import tkinter as tk
import sys
from tkinter import *
from Gui import *
import datetime
import json


class SelfSpeed:
    '''
    Class SelfSpeed is responsible for events and all interface during the actual game
    param text, time
    text - Text that will be used for the game to write
    time - constant 60 seconds for limited time game_mode
    master is root 
    
    '''
    def __init__(self,text,time = 60,master=None,app=None):
        '''
        Creates a frame with buttons for choosing game mode and leaving to Main Menu 
        '''
        self.counter = 1
        self.root = master
        self.app = app
        self.root.title("Speed Typing")
        self.root.geometry("300x300")
        self.root.resizable(False,False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        with open(text,'r') as file:
            choosen_text = str(file.read().replace('\n', ' '))
            choosen_list= list(filter(None,(choosen_text.split(' '))))
            choosen_text = ' '.join(choosen_list)
            choosen_text = choosen_text + ' '

        self._text = text
        self._time = time
        self.Writeable = True

        self.text = choosen_text
        self.text = self.text.lower()
        self.another_list = []
        self.helplist = []
        self.match2 = 0
        self.word = ''
        self.match4 = 0
        self.word2 = ''
        self.number =0

        self.words = 0
        self.chars = 0
        self.mistakes = 0
        self.time = 0
        self.date = datetime.datetime.now()
        self._text = text
        self.game_mode = ''

        self.page_2 = Leaderboard(master=self.root,app=self)

       
   

        self.limited_time = ttk.Button(self.frame, text = '1 minute',command=self.start_with_limited_pack)  
        self.limited_time.pack(pady =20)

        self.unlimited_time = ttk.Button(self.frame, text = 'unlimited', command=self.start_with_unlimited_pack)  
        self.unlimited_time.pack(pady =20)

        self.backToMenuButton = ttk.Button(self.frame, text=f'Back to Menu', command=self.back_to_menu)
        self.backToMenuButton.pack(pady=20)

    def start_page(self):
        self.frame.pack()



    def greenorred(self):
        '''
        Function for coloring word in GreenorredLabel on right color when right condition is fullfiled
        '''
        try:
            if self.labelLeft.cget('text')[-1] == ' ':
                self.GreenorRedLabel.config(fg="black")
            else:
                res = self.labelLeft.cget('text').split(' ')
                if len(res) <= 1:
                    var1 = len(self.labelLeft.cget('text'))
                    if self.labelLeft.cget('text') == self.GreenorRedLabel.cget('text')[:var1]:
                        self.GreenorRedLabel.config(fg="green")
                    else:
                        self.GreenorRedLabel.config(fg="red")
                else:
                    var2 = self.labelLeft.cget('text').rfind(' ')
                    var3 = len(self.labelLeft.cget('text')[(var2+1):])
                    text4 = self.GreenorRedLabel.cget('text')
                    if self.labelLeft.cget('text')[(var2+1):] == text4[:var3]:
                        self.GreenorRedLabel.config(fg="green")
                    else:
                        self.GreenorRedLabel.config(fg="red")
        except IndexError:
            self.GreenorRedLabel.config(fg="black")

    
    def keyPress(self,event=None):
        '''
        Main function of the game
        Works on keyboard events
        When specific specific key is pressed(Backspace, Enter, Spacebar) it creates special action than do what that key was supposed to do
        But if not then the key is stored in LeftLabel as text with possiblity to delete
        '''
        if event.keycode == 29:
            pass
        if event.keycode == 65:
            if self.word2 != self.labelLeft.cget('text')[(-self.match4):].lower() and self.labelRight.cget('text') != ' ': 
                self.mistakes +=1
                

            if self.labelRight.cget('text').lower() == ' ':
                self.stopTest()
            else:
                match = self.labelRight.cget('text').lower().find(' ')
                self.labelRight.configure(text=self.labelRight.cget('text')[match:].lower())
                self.match2 = (self.labelRight.cget('text').lower().find(' ')-1)
                self.match4 = (self.labelRight.cget('text').lower()[1:]).find(' ')
                self.word = self.labelRight.cget('text')[:self.match2].lower()
                self.GreenorRedLabel.configure(text='')
                self.GreenorRedLabel.configure(text=self.labelRight.cget('text')[1:self.match4+1].lower(), fg="black")
                self.word2 = self.labelRight.cget('text')[1:self.match4+1].lower()
                self.helplist =[]
                self.another_list = []
                for letter in self.word:
                    self.helplist.append(letter)
        if event.keycode == 22:
            if self.labelLeft.cget('text')[-1] == ' ':
                pass
            else:
                if self.labelLeft.cget('text')[-1] in self.helplist:
                    res = list(filter(None,(self.labelLeft.cget('text').split(' '))))
                    if len(res) <= 1:
                        try:
                            if self.another_list[-1] ==  len(self.labelLeft.cget('text')):
                                self.labelRight.configure(text= self.labelLeft.cget('text')[-1]  + self.labelRight.cget('text'))
                                self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                                self.greenorred()
                                self.currentLetterLabel.configure(text=self.labelRight.cget('text')[0])
                                if len(self.another_list) > 1:
                                    del self.another_list[-1]
                                else:
                                    self.another_list = []
                            else:
                                self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                                self.greenorred()
                        except IndexError:
                            self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                            self.greenorred()
                    else:
                        if self.another_list[-1] ==  len(self.labelLeft.cget('text')[:self.match2]):
                            self.labelRight.configure(text= self.labelLeft.cget('text')[-1]  + self.labelRight.cget('text'))
                            self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                            self.greenorred()
                            self.currentLetterLabel.configure(text=self.labelRight.cget('text')[0])
                            if len(self.another_list) > 1:
                                del self.another_list[-1]
                            else:
                                self.another_list = []
                        else:
                            self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                            self.greenorred()
                else:
                    self.labelLeft.configure(text=self.labelLeft.cget('text')[:-1], foreground='black')
                    self.greenorred()
        else:
            if self.labelLeft.cget('text') == '':
                self.match2 = (self.labelRight.cget('text').lower().find(' '))
                self.word = self.labelRight.cget('text')[:self.match2].lower()
                self.match4 = (self.labelRight.cget('text').lower().find(' ') )
                self.word2 = self.labelRight.cget('text')[:self.match4].lower()
                self.helplist =[]
                self.another_list = []
                for letter in self.word:
                    self.helplist.append(letter)



            if self.labelRight.cget('text') == ' ':
                self.labelLeft.configure(text=self.labelLeft.cget('text') + event.char.lower())
                self.GreenorRedLabel.config(fg="red")
            else:
                if event.char.lower() == self.labelRight.cget('text')[0].lower():
                   
                    self.labelRight.configure(text=self.labelRight.cget('text')[1:])
    
                    self.labelLeft.configure(text=self.labelLeft.cget('text') + event.char.lower())

                    self.currentLetterLabel.configure(text=self.labelRight.cget('text')[0])

                    self.another_list.append(len(self.labelLeft.cget('text')[:self.match2].lower()))
                    
                    if self.GreenorRedLabel.cget("fg") =="red":
                        pass
                    else:
                        self.GreenorRedLabel.config(fg="green")
                else:
                    self.labelLeft.configure(text=self.labelLeft.cget('text') + event.char.lower())
                    self.GreenorRedLabel.config(fg="red")

    '''
    Function to write statistics of the game to statystyki.json so they can be read in statistics GUI
    '''
    def write_to_json(self):
        try:
            with open('statystki.json', 'r') as f:
                data = json.load(f)
        except:
            data = {}
        data[len(data)] = {'words': self.words, 'characters': self.chars, 'errors': self.mistakes, 'time': self.time,'date':str(self.date), 'file_path': self._text, 'game_mode':self.game_mode}
        self.data = data
        with open('statystki.json', 'w') as f:
            json.dump(data, f, indent=4)



    '''
    Function to start a game with unlimited time for bigger texts 
    '''
    def start_with_unlimited_time(self):

        self.game_mode = 'unlimited_time'
        
        splitPoint = 0

        self.labelLeft = ttk.Label(self.frame, text=self.text[0:splitPoint], foreground='black',font=('Helventica',30))
        self.labelLeft.place(relx=0.5, rely=0.5, anchor=E)

        
        index_green =(self.text.find(' '))
        self.GreenorRedLabel = tk.Label(self.frame, text=self.text[:index_green], foreground='black',font=('Helventica',30))
        self.GreenorRedLabel.place(relx=0.5, rely=0.4, anchor=CENTER)


        self.labelRight = ttk.Label(self.frame, text=self.text[splitPoint:],font=('Helventica',30))
        self.labelRight.place(relx=0.5, rely=0.5, anchor= W)


        self.currentLetterLabel = ttk.Label(self.frame, text=self.text[splitPoint], foreground='grey',font=('Helventica',30))
        self.currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

        
        self.timeleftLabel = ttk.Label(self.frame, text=f'0 Seconds', foreground='grey',font=('Helventica',30))
        self.timeleftLabel.place(relx=0.5, rely=0.2, anchor=S)

        
        self.writeAble = True
        self.root.bind('<Key>', self.keyPress)

        
        self.ResultButton = ttk.Button(self.frame, text=f'Retry', command=self.restart,width=15)
        self.ResultButton.place(relx=0.5, rely=0.8, anchor=CENTER)


        self.root.after(1000, self.addSecond)

    '''
    Function to change Frame for the game and exceute the function self.start_with_unlimited_time
    '''

    def start_with_unlimited_pack(self):
        self.root.geometry('1024x640')
        self.root.update()
        self.root.resizable(False,False)
        self.unlimited_time.destroy()
        self.limited_time.destroy()
        self.backToMenuButton.destroy()
        rootHeight= self.root.winfo_width()
        rootWidth = self.root.winfo_height()
        self.frame.config(height=rootHeight,width=rootWidth)
        self.start_with_unlimited_time()
        
    
    '''
    Function to start a game with limited time. Made for smaller texts
    '''
    def start_with_limited_time(self):
        self.game_mode = 'unlimited_time'

        splitPoint = 0

        self.labelLeft = ttk.Label(self.frame, text=self.text[0:splitPoint], foreground='black',font=('Helventica',30))
        self.labelLeft.place(relx=0.5, rely=0.5, anchor=E)

        
        index_green =(self.text.find(' '))
        self.GreenorRedLabel = tk.Label(self.frame, text=self.text[:index_green], fg='black',font=('Helventica',30))
        self.GreenorRedLabel.place(relx=0.5, rely=0.4, anchor=CENTER)


        self.labelRight = ttk.Label(self.frame, text=self.text[splitPoint:],font=('Helventica',30))
        self.labelRight.place(relx=0.5, rely=0.5, anchor= W)


        self.currentLetterLabel = ttk.Label(self.frame, text=self.text[splitPoint], foreground='grey',font=('Helventica',30))
        self.currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

        
        self.timeleftLabel = ttk.Label(self.frame, text=f'0 Seconds', foreground='grey',font=('Helventica',30))
        self.timeleftLabel.place(relx=0.5, rely=0.2, anchor=S)

        
        self.writeAble = True
        self.root.bind('<Key>', self.keyPress)

        
        self.ResultButton = ttk.Button(self.frame, text=f'Retry', command=self.restart, width=15)
        self.ResultButton.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.after(1000, self.addSecond)
        self.root.after(60000,self.stopTest)

    
    '''
    Function to change Frame for the game and exceute the function self.start_with_limited_time
    '''


    def start_with_limited_pack(self):
        self.root.geometry('1024x640')
        self.root.update()
        self.root.resizable(False,False)
        self.unlimited_time.destroy()
        self.limited_time.destroy()
        self.backToMenuButton.destroy()
        rootHeight= self.root.winfo_width()
        rootWidth = self.root.winfo_height()
        self.frame.config(height=rootHeight,width=rootWidth)
        self.start_with_limited_time()

    '''
    Function that is responsible for adding seconds and measure the final time of the game
    '''

    def addSecond(self):
        if self.Writeable == True:
            try:
                self.time += 1
                self.timeleftLabel.configure(text=f'{self.time} Seconds')
            except tk.TclError:
                self.timeleftLabel.destroy()
        
        if self.writeAble:
            self.root.after(1000, self.addSecond)

    '''
    Function to delete widgets after the game
    '''

    def delete_labels(self):
        self.timeleftLabel.destroy()
        self.currentLetterLabel.destroy()
        self.labelRight.destroy()
        self.labelLeft.destroy()
        self.ResultButton.destroy()
        self.GreenorRedLabel.destroy()

    '''
    Function to stop the game and execute function to write statistics to statystki.json file and delete labels after the game
    It creates mini interface to redirect 
    '''
            

    def stopTest(self):

        self.root.geometry('320x320')
        rootHeight= self.root.winfo_width()
        rootWidth = self.root.winfo_height()
        self.frame.config(height=rootHeight,width=rootWidth)
        
        self.writeAble = False
        res = list(filter(None,(self.labelLeft.cget('text').split(' '))))
        self.words =  len(res)
        for words in res:
            self.chars += len(words)
        self.mistakes = self.mistakes
        self.time= self.time
        try:
            accuracy = str(round(float(1 - (self.mistakes/self.words)),2) * 100)
        except ZeroDivisionError:
            accuracy = '0.0'

        if self.time <= 0:
            pass
        else:
            self.write_to_json()

        self.delete_labels()
        
    
        self.ResultLabel = ttk.Label(self.frame, text=f'Accuraccy: {accuracy}%', foreground='black',font=('Helventica',19))
        self.ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        
        self.BackToMenuButton = ttk.Button(self.frame, text=f'Back to Menu', command=self.back_to_menu_after, width=15)
        self.BackToMenuButton.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.StatisticsButton = ttk.Button(self.frame, text=f'Show Statistics', command=self.statistics,width=15)
        self.StatisticsButton.place(relx=0.5, rely=0.8, anchor=CENTER)

    def restart(self):
        self.writeAble = False
        self.frame.pack_forget()
        self.speed_game = speed_class.SelfSpeed(self._text,60,master=self.root,app=self)
        self.speed_game.start_page()

    def statistics(self):
        self.root.geometry('1400x500')
        self.frame.pack_forget()
        with open("config.json", 'r') as f:
            data = json.load(f)
        new_text = data['file']
        self.Leaderboard = Leaderboard(new_text,master=self.root,app = self)
        self.Leaderboard.start_page()


    def back_to_menu(self):
        self.frame.pack_forget()
        with open("config.json", 'r') as f:
            data = json.load(f)
        new_text = data['file']
        self.TypeSpeedGui = TypeSpeedGUI(text=new_text,root=self.root)
        self.TypeSpeedGui.main_page()


    def back_to_menu_after(self):
        self.frame.pack_forget()
        with open("config.json", 'r') as f:
            data = json.load(f)
        new_text = data['file']
        self.TypeSpeedGui = TypeSpeedGUI(text=new_text,root=self.root)
        self.TypeSpeedGui.main_page()

       
