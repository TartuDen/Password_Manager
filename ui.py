from tkinter import *
import random
from savingClass import ToSave


class UI():
    def __init__(self):
        
        self.basic_color = "lightblue"
        self.window = Tk()
        self.window.config(bg="lightblue")

        canvas = Canvas(width=200, height=224,background=self.basic_color, highlightthickness=0)
        img = PhotoImage(file=".\\logo.png")
        canvas.create_image(103, 100, image = img)
        canvas.grid(row=2, column=2, pady=10)


        website_label = Label(text="Website: ",background=self.basic_color)
        website_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.entry_website = Entry(width=40)
        self.entry_website.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
        self.entry_website.focus_set()


        email_user_label = Label(text="Email/Username: ",background=self.basic_color)
        email_user_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.entry_email = Entry(width=40)
        self.entry_email.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

        pasword_label = Label(text="Password: ",background=self.basic_color)
        pasword_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.password_entry = Entry(width=17)
        self.password_entry.grid(row=5, column=2, padx=10, pady=10)

        self.button_generatePassword = Button(text = "Generate Password",command=self.password_generator)
        self.button_generatePassword.grid(row=5, column=3, padx=10, pady=10)

        self.button_add = Button(text = "Add",width=30, command=self.to_add_button)
        self.button_add.grid(row=6, column=2, columnspan=2, pady=10)


        self.window.mainloop()

    def popup_window(self,message):
        popup = Toplevel()
        popup.title("Popup Window")
        popup.geometry("200x100")
        popup_label = Label(popup, text=message)
        popup_label.pack(pady=20)
        close_button = Button(popup, text="Close", command=popup.destroy)
        close_button.pack()

    def validator(self, str_to_validate):
        if isinstance(str_to_validate,str):
            if len(str_to_validate)>1:
                return(True)
            else:
                self.popup_window(ValueError("Field cannot be empty"))
                raise ValueError("Field cannot be empty")

        else:
            self.popup_window(KeyError(f"Expected a {str} key, but got {type(str_to_validate)} instead."))
            raise KeyError(f"Expected a {str} key, but got {type(str_to_validate)} instead.")


    def to_add_button(self):
        wb = self.entry_website.get()
        em = self.entry_email.get()
        ps = self.password_entry.get()
        if self.validator(wb) and self.validator(em) and self.validator(ps):
            self.database(f"{wb} | {em} | {ps}")
    
    def password_generator(self):
        l1="abcdefghijklmnopqrstuvwxqzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*)(0123456789"
        new_pass = ""
        for i in range(7):
            new_pass = new_pass + random.choice(l1)
        self.password_entry.delete(0,END)
        self.password_entry.insert(0,new_pass)
    
    def database(self,dataToSave):
        saveClass = ToSave(data_to_be_added =  dataToSave)
        saveClass.add_data()


















