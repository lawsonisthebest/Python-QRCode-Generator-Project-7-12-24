from tkinter import *
import customtkinter
from tkinter.font import Font
import qrcode
from PIL import Image
import os
import sys
cwd = os.getcwd()

QRSize = 50
URL = ''
BoarderWidth = 2

path = os.getcwd()
fileName = "Image.png"
fullDir = os.path.join(path,fileName)

#Tkinter Setup
root = customtkinter.CTk()

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
root.title("QR Code Generator")
root.geometry('500x600')

def Reset():
    os.execl(sys.executable, sys.executable, *sys.argv)

def DownloadImage():
    URL = URLInp.get()
    BoarderWidth = 2
    QRSize = 45
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=QRSize, border=BoarderWidth)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=ColorInp.get(), back_color=BackgroundColorInp.get())
    img.save(fullDir)
    QRImage = customtkinter.CTkImage(light_image=Image.open("Image.png"), size=(int(QRSize) * 5, int(QRSize) * 5))
    QRText = customtkinter.CTkLabel(root, text='', image=QRImage)
    QRText.pack(pady=10)
    ResetButton = customtkinter.CTkButton(root, text='Reset App', width=150, height=30,
                                             command=Reset, font=inpFieldFont)
    ResetButton.pack(pady=10)

TitleFont = customtkinter.CTkFont(family='Helvetica', weight='bold', size=40)
Title = customtkinter.CTkLabel(root, text='QR Code Generator!', width=500, height=60, font=TitleFont)
Title.pack(pady=5)

ConfigureFont = customtkinter.CTkFont(family='Helvetica', weight='bold', size=30)
SettingsText = customtkinter.CTkLabel(root, text='Configure:', width=500, height=50, font=ConfigureFont)
SettingsText.pack()

inpFieldFont = customtkinter.CTkFont(family='Helvetica', weight='bold', size=15)
URLInp = customtkinter.CTkEntry(root,placeholder_text='Paste URL Here:', width=350, height=35, font=inpFieldFont)
URLInp.pack()

BackgroundColorInp = customtkinter.CTkEntry(root,placeholder_text='Background Color (Default: White):', width=350, height=35, font=inpFieldFont)
BackgroundColorInp.pack(pady=10)

ColorInp = customtkinter.CTkEntry(root,placeholder_text='QR Color (Default: Black):', width=350, height=35, font=inpFieldFont)
ColorInp.pack()

DownloadButton = customtkinter.CTkButton(root, text='Download QR Code!', width=250, height=30, command=DownloadImage, font=inpFieldFont)
DownloadButton.pack(pady=10)

root.mainloop()