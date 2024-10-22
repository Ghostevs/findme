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
        "fname" : str(input("Enter your name: ")).capitalize(),
        "lname" : str(input("Enter your last name: ")).capitalize(),
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
        def options():
            print("How can we help you")
            print("1. Seek Help")
            print("2. Offer help")
            
            Option = int(input("Choose Option: "))
            
            if Option == 1:
                print("Recover missing document")
                print("Report type of missing document: ")
                print("1. ID")
                print("2. Passport")
                print("3. Credit Card")
                print("4. Election Card")
                opt = int(input("Enter option: "))
                
                if opt == 1:
                    print("ID")
                    
                    id_data = {
                        "fname" : str(input("Enter your name: ")).capitalize(),
                        "lname" : str(input("Enter your last name: ")).capitalize(),
                        "DayOB" : str(input("Enter day of birth: ")),
                        "MonthOB" : str(input("Enter month of birth (in numbers): ")),
                        "YEAROfBirth" : str(input("Enter year of birth: ")),
                        "marital_status" : str(input("Marital status(S or D): ")).capitalize(),
                        "place_of_birth" :  str(input("Place of birth: ")).capitalize(),
                        "upload_picture" : str(input("Upload picture: ")),
                        "contact_cell": str(input("Enter cell number: ")),
                        "email" : str(input("Enter your email: "))
                        
                    }
                    
                    with open('id.csv', 'a', newline='') as csv_file:
                        fieldnames = ['fname', 'lname', 'DayOB', 'MonthOB', 'YEARofBirth', 'marital_status', 'place_of_birth', 'upload_picture', 'contact_cell', 'email']
                        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                        writer.writerow(id_data)
                    
                    
                    
                elif opt == 2:
                    print("Passport")
                    passport_data = {
                        "fname" : str(input("Enter your name: ")).capitalize(),
                        "lname" : str(input("Enter your last name: ")).capitalize(),
                        "dayOfBirth" : str(input("Enter day of birth: ")),
                        "monthOfBirth" : str(input("Enter month of birth (in numbers): ")),
                        "YearOfBirth" : str(input("Enter year of birth: ")),
                        "place_of_birth" :  str(input("Place of birth: ")).capitalize(),
                        "upload_picture" : str(input("Upload picture: ")),
                        "contact_cell": str(input("Enter cell number: ")),
                        "email" : str(input("Enter your email: "))
                        
                    }
                    
                    with open('passport.csv', 'a', newline='') as csv_file:
                        fieldnames = ['fname', 'lname', 'dayOfBirth','monthOfBirth','YearOfBirth', 'place_of_birth', 'upload_picture', 'contact_cell', 'email']
                        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                        writer.writerow(passport_data)
                    
                    
                    
                elif opt == 3:
                    print("Credit Card")
                    creditCard_data = {
                        "fname" : str(input("Enter your name: ")).capitalize(),
                        "lname" : str(input("Enter your last name: ")).capitalize(),
                        "bank" : str(input("Enter name of bank: ")).capitalize(),
                        "contact_cell": str(input("Enter cell number: ")),
                        "email" : str(input("Enter your email: "))
                        
                    }
                    
                    with open('credit_card.csv', 'a', newline='') as csv_file:
                        fieldnames = ['fname', 'lname', 'bank', 'contact_cell', 'email']
                        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                        writer.writerow(creditCard_data)
                    
                    
                elif opt == 4:
                    print("Election Card")
                
                
                
                
                
            elif Option == 2:
                
                print("Report found documents: ")
                print("1. ID")
                print("2. Passport")
                print("3. Credit Card")
                print("4. Election Card ")
                opt = int(input("Enter option: "))
                if opt == 1:
                    print("ID")
                    
                    fname = str(input("Enter Name: ")).capitalize()
                    lname = str(input("Enter last name: ")).capitalize()
                    DayOB = str(input("Enter day of birth: "))
                    MonthOB = str(input("Enter month of birth: "))
                    YearOB = str(input("Enter year of birth: "))
                    Marital_status = str(input("Enter marital status: ")).capitalize()
                    Place_of_birth = str(input("Enter place of birth: ")).capitalize()
                    
                    
                    
                    with open('id.csv', 'r') as csv_file:
                        fieldnames = ['fname', 'lname', 'DayOB', 'MonthOB', 'YEARofBirth', 'marital_status', 'place_of_birth', 'upload_picture', 'contact_cell', 'email']
                        reader = csv.DictReader(csv_file, fieldnames = fieldnames)
                        for row in reader:
                            if (row['fname'] == fname) and (row['lname'] == lname) and (row['DayOB']== DayOB) and (row['MonthOB'] == MonthOB) and (row['YEARofBirth'] == YearOB) and (row['marital_status'] == Marital_status) and (row['place_of_birth'] == Place_of_birth):
                                print(row['fname'])
                                print(row['contact_cell'])
                                print(row['email'])
                        
                    
                    
                    
                    
                elif opt == 2:
                    print("Passport")
                    fname = str(input("Enter the first name: ")).capitalize()
                    lname = str(input("Enter the last name: ")).capitalize()
                    dayOfBirth = str(input("Enter day of birth: "))
                    monthOfBirth = str(input("Enter month of birth (in numbers): "))
                    YearOfBirth = str(input("Enter year of birth: "))
                    place_of_birth = str(input("Place of birth: ")).capitalize()
                    
                    
                    with open('passport.csv', 'r') as csv_file:
                        fieldnames = ['fname', 'lname', 'dayOfBirth', 'monthOfBirth', 'YearOfBirth', 'place_of_birth', 'upload_picture', 'contact_cell', 'email']
                        reader = csv.DictReader(csv_file, fieldnames = fieldnames)
                        for row in reader:
                            
                            if (row['fname'] == fname) and (row['lname'] == lname) and (row['dayOfBirth']== dayOfBirth) and (row['monthOfBirth'] == monthOfBirth) and (row['YEARofBirth'] == YearOfBirth)  and (row['place_of_birth'] == Place_of_birth):
                                print(row['contact_cell'])
                                print(row['email'])

                        
                elif opt == 3:
                    print("Credit Card")
                    
                    fname = str(input("Enter the first name: ")).capitalize()
                    lname = str(input("Enter the last name: ")).capitalize()
                    bank = str(input("Enter the name of the bank: ")).capitalize()
                    
                    with open('credit_card.csv', 'r') as csv_file:
                        fieldnames = ['fname', 'lname', 'bank', 'contact_cell', 'email']
                        reader = csv.DictReader(csv_file, fieldnames = fieldnames)
                        for row in reader:
                            if (row['fname'] == fname) and (row['lname'] == lname) and (row['bank'] == bank):
                                print(row['contact_cell'])
                                print(row['email'])
                        
                        
                elif opt == 4:
                    print("Election Card")
            
            
        
        user_input = str(input("Enter your username: "))
        user_password = str(input("Enter your password: "))
        
        
        with open('database.csv', 'r') as csv_file:
            fieldnames = ['fname', 'lname','user_name','password']
            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            
            for row in reader:
                if (row['user_name'] == user_input and row['password'] == user_password):
                    print("welcome " + row['fname'] + " " + row['lname'])

                    options()

    
    
object = Match(1,1,1,1,1,1)
print("1. Sign Up")
print("2. Login")
choice = int(input("Option: "))
if choice == 1:
    object.sign_up()
elif choice == 2:
    object.login()