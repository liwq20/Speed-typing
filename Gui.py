import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import speed_class
import ttkbootstrap
from tkinter import ttk
import json



class TypeSpeedGUI:
    '''
    Main Class of the programm
    To start takes no parameters
    It is the main control panel to choose the path where do u want to go
    It has redirection to Class Settings, Class Statistics, Class SelfSpeed
    '''
    def __init__(self,text=None,time=60,root=None):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        ttk.Label(self.frame, text='Main Page',font=('Helventica',19)).pack(pady=20)
       
        self.text = text
        ttk.Button(self.frame, text='Start', command=self.make_page_3,bootstyle="success",width=15).pack()
        
        ttk.Label(self.frame, text='').pack()
        ttk.Button(self.frame, text='Statistics', command=self.make_page_2,bootstyle="warning",width=15).pack()
        ttk.Label(self.frame, text='').pack()
        ttk.Button(self.frame, text='Upload a file', command=self.make_page_1,width=15).pack()
        self.page_1 = Settings(master=self.root,app=self)
        self.page_2 = Leaderboard(master=self.root,app=self)
       
        self.root.geometry("320x320")
        self.root.title("TypeSpeed")


        self.settings = Settings(master=self.root,app = self)

    def start(self):
        self.text = self.text

    def main_page(self,text= None):
        self.text = text
        self.frame.pack()

    def make_page_1(self):
        self.frame.pack_forget()
        self.settings.start_page()

    def make_page_2(self):
        self.root.geometry('1400x500')
        self.frame.pack_forget()
        self.Leaderboard = Leaderboard(self.text,master=self.root,app=self)
        self.Leaderboard.start_page()

    def make_page_3(self):
        try:
            data = "config.json"
            with open("config.json", 'r') as f:
                data = json.load(f)
            new_text = data['file']
            self.frame.pack_forget()
            self.speed_game = speed_class.SelfSpeed(new_text,60,master=self.root,app=self)
            self.speed_game.start_page()
        except:
            messagebox.showerror('Error', 'Please upload a file first')


                


class Settings:
    '''
    Class Settings is responsible to open filedialog and save path of chosen file to config.json
    param: master, app
    master takes a role of root to open this class
    '''
    def __init__(self,master=None, app=None):
        self.master = master
        self.app = app
        self.frame = ttk.Frame(self.master)
    

        self.file = ''
        self.conf = None
 
        ttk.Label(self.frame, text='Settings',font=('Helventica',19)).pack(pady=20)
        
        ttk.Button(self.frame, text='Choose file', command=self.get_file,bootstyle="warning",).pack()
        ttk.Label(self.frame, text='').pack(pady=10)
        ttk.Button(self.frame, text='Save & Go back', command=self.go_back,width=15).pack()
        self.entry_file = ttk.Entry(self.master)
        self.file_dialog_open = False
   

    def get_file(self):
        '''
        Function get_file is the main function of the class settings. With it u can choose what text u want to write
        It also save the path of the file to config.json so the SpeedClass can read it
        '''
        if not self.file_dialog_open:
            self.file_dialog_open = True
            self.file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
            self.entry_file.insert(0, self.file)

            self.conf = self.file
            global Leaderboard_text
            Leaderboard_text = self.file
            self.file_dialog_open = False
            #write to json file
            data = "config.json"
            dict2= {'file': self.file}
            with open(data, 'w') as f:
                json.dump(dict2, f)
        else:
            self.master.withdraw()
            print('filedialog is open')

    '''
    Indirect function to display GUI of Class Settings and leave to Main Menu
    '''

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page(self.file)

class Leaderboard:
    '''
    Class Leaderboard
    takes one unnecessary param to store path to file of class TypespeedGui
    when created it loads data from file from .json file and creates GUI 
    with Treeview to display statistics of previous games
    text - text neccesary to start a game
    data - data to display statistics
    index - number of the game
    words - number of words written by user during the game
    characters -  number of characters written by user during the game
    errors - number of mistakes made by user during the game
    time - number of seconds, it took user to end the game
    date - day, month, year, hour, minutes, seconds of ending the game
    file_path - path to .txt file that was used for the game
    game_mode - chosen game_mode
    '''
    def __init__(self, text=None, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.text = text

        '''       
        Loading the data from file statystki.json 
        Creating gui to display the statistics
        '''

        data = "statystki.json"
        with open(data, 'r') as f:
            data = json.load(f) 
        self.data = data
        ttk.Label(self.frame, text='Stats',font=('Helventica',19)).pack(pady=20)

        '''
        Creating Treeview to display values of certain statistics to right column
        Creating button go_back to comeback to the Main Menu
        '''
        
        self.tree = ttk.Treeview(self.frame, columns=('index','words', 'characters', 'errors', 'time','date','file_path','game_mode'), show='headings')
        self.tree.heading('index', text='game')
        self.tree.heading('words', text='words')
        self.tree.heading('characters', text='characters')
        self.tree.heading('errors', text='errors')
        self.tree.heading('time', text='time')
        self.tree.heading('date', text='time')
        self.tree.heading('file_path', text='file_path')
        self.tree.heading('game_mode', text='game_mode')

        self.tree.column('index', width=130, anchor='center')
        self.tree.column('words', width=130, anchor='center')
        self.tree.column('characters', width=130, anchor='center')
        self.tree.column('errors', width=130, anchor='center')
        self.tree.column('time', width=140, anchor='center')
        self.tree.column('date', width=160, anchor='center')
        self.tree.column('file_path', width=160, anchor='center')
        self.tree.column('game_mode', width=140, anchor='center')
        self.tree.pack()

        for i in range(len(self.data)):
            self.tree.insert('', 'end', values=(i +1, self.data[str(i)]['words'], self.data[str(i)]['characters'], self.data[str(i)]['errors'], self.data[str(i)]['time'],self.data[str(i)]['date'],self.data[str(i)]['file_path'],self.data[str(i)]['game_mode']))

        ttk.Button(self.frame, text='Go back', command=self.go_back,width=15,bootstyle="warning").pack(pady=20)
    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.master.geometry('320x320')
        self.frame.pack_forget()
        data = "config.json"
        with open("config.json", 'r') as f:
            data = json.load(f)
        new_text = data['file']
        self.TypeSpeedGui = TypeSpeedGUI(text=new_text,time=60,root=self.master)
        self.TypeSpeedGui.main_page()

if __name__ == '__main__':
    root = tk.Tk()
    app = TypeSpeedGUI(root=root)
    root.mainloop()
    data = "config.json"
    with open(data, 'w') as f:
        json.dump({}, f)


 
     