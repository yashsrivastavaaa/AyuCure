import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import os

def disease(combobox_var):
    disease_name = combobox_var.get()

    if(disease_name == "Allergies"):
        os.startfile(r".\data\Diseases\Allergies.pdf")

    elif(disease_name == "Asthma"):
        os.startfile(r".\data\Diseases\Asthma.pdf")

    elif(disease_name == "Cataract"):
        os.startfile(r".\data\Diseases\Cataract.pdf")
    
    elif(disease_name == "Chickenpox"):
        os.startfile(r".\data\Diseases\Chickenpox.pdf")

    elif(disease_name == "Cholera"):
        os.startfile(r".\data\Diseases\Cholera.pdf")

    elif(disease_name == "Dengue"):
        os.startfile(r".\data\Diseases\Dengue.pdf")

    elif(disease_name == "Diarrhea"):
        os.startfile(r".\data\Diseases\Diarrhea.pdf")

    elif(disease_name == "Heart Disease"):
        os.startfile(r".\data\Diseases\HEART DISEASES.pdf")

    elif(disease_name == "Kidney Disease"):
        os.startfile(r".\data\Diseases\Kidney Disease.pdf")

    elif(disease_name == "Monkeypox"):
        os.startfile(r".\data\Diseases\Monkeypox.pdf")

    elif(disease_name == "Myopia"):
        os.startfile(r".\data\Diseases\Myopia.pdf")

    elif(disease_name == "Piles"):
        os.startfile(r".\data\Diseases\Piles.pdf")

    elif(disease_name == "Pneumonia"):
        os.startfile(r".\data\Diseases\Pneumonia.pdf")

    elif(disease_name == "Typhoid"):
        os.startfile(r".\data\Diseases\Typhoid.pdf")
        
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x768")
app.title("Medicine Prediction")

image1=ImageTk.PhotoImage(Image.open("./data/Pattern.png"))
label1=customtkinter.CTkLabel(master=app,image=image1)
label1.pack()

frame=customtkinter.CTkFrame(master=label1, width=320, height=360, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label2=customtkinter.CTkLabel(master=frame, text="Select the Disease",font=('Century Gothic',25))
label2.place(relx=0.25,y=20,x=-3)

combo_list = ["Allergies", "Asthma", "Cataract","Chickenpox","Cholera","Dengue","Diarrhea","Heart Disease","Kidney Disease","Monkeypox","Myopia","Piles","Pneumonia","Typhoid"]
combobox_var = StringVar(value="Select Disease")
status_combobox = customtkinter.CTkComboBox(frame,variable=combobox_var ,values=combo_list,state="readonly",font=("Century Gothic",20),dropdown_hover_color="green",dropdown_font=("Century Gothic",20),width = 220)
status_combobox.grid(row=0, column=0, padx=100, pady=70,  sticky="ew")

button1 = customtkinter.CTkButton(master=frame, width=220,font=("Century Gothic",20), text="Select", corner_radius=20,command=lambda : disease(combobox_var))
button1.place(relx=0.25,rely=0.5,y=34)

app.mainloop()
