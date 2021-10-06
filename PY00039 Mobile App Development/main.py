from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior 
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

'''Connection with python'''
Builder.load_file('design.kv')

'''Login Screen'''
class LoginScreen(Screen):  # LoginScreen is from kivi file line 1 Screen is an object which is imported
    def sign_up(self): # signup button is in login so we are assigning (42 lin in kivi) functionality to it from here
        self.manager.current = "sign_up_screen" # on pressing signup button it will move to other page line 44 in kivi file

    def login(self, uname, pword): # aassigning functionality to login button 21 line in kivi
        with open("users.json", 'r') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success' # (line 109 in kivi) will move to Login_Screen_Success screen
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

class RootWidget(ScreenManager): # RootWidget is from kivi file, ScreenManager is an object which is imported
    pass

'''Signup screen'''
class SignUpScreen(Screen): # Screen is parent SignUpScreen is child
    def add_user(self, uname, pword): # (line 60) assigning functionality
        with open("users.json") as file: # Json format file will be loaded
            users = json.load(file)

        users[uname] = {'username': uname, 'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open ("users.json", 'w') as file: # To add entered data into json file
            json.dump(users, file) # Dumping occurs to the file
        self.manager.current = "submit_screen_success"

'''Signup success screen'''
class SubmitScreenSuccess(Screen): # (line 44)
    def go_to_login(self): # (line 69)
        self.manager.transition.direction = "left" # Moving direction of screen
        self.manager.current = "login_screen"

'''Login Success screen'''
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right" 
        self.manager.current = "login_screen" # move to log in page (line 104)

    def get_quote(self, feel): # (line 92) user will pass his mood
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt") # it open quotes folder and checks with use passed mood
        
        available_feelings = [Path(filename).stem for filename in available_feelings] # if file name avialable 

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding='utf-8') as file:
                quotes = file.readlines() # lines will be read by quotes
            self.ids.quote.text = random.choice(quotes) # randomly displayed
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class GiriApp(App):
    def build(self): #build is a attribute of App
        return RootWidget()

if __name__ == "__main__":
    GiriApp().run()