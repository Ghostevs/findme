import csv
import pandas as pd

class Match:
    def __init__(self,fname,lname, username, email, password, upload_picture):
        self.fname= fname
        self.lname= lname
        self.username = username
        self.email = email
        self.password = password
        self.upload_picture = upload_picture 
        
    def sign_up(self):
        new_data = {
        "fname" : str(input("Enter your name: ")),
        "lname" : str(input("Enter your last name: ")),
        "username" : str(input("Create your username: ")),
        "email" : str(input("Enter your email: ")),
        "password" :  str(input("Create password: ")),
        "upload_picture" : str(input("Upload picture: "))
        }
        
        with open('database.csv', 'a', newline='') as csvfile:
            fieldnames = ['fname', 'lname', 'username', 'email', 'password', 'upload_picture']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow(new_data)
    
    def login(self):
        with open('database.csv', 'r'):
            reader = csv.reader(csvfile='database.csv')
            for row in reader:
                print()
        
        
    
    
    
object = Match(1,1,1,1,1,1)
object.sign_up()