# import all Tkinter libraries from the module
from tkinter import *
from tkinter import messagebox
# From the  installed Pytube module, import the youtube library
from pytube import YouTube
# import requests
import requests
# From PIL import Image and ImageTk
from PIL import Image,ImageTk
# import shutil
import shutil
# import urllib
import urllib

def checker():
    try:
        if requests.get('https://google.com').ok:
            print("You're Online")
            link_converter()
    except:
        print("You're Offline")
        messagebox.showwarning('Youtube Downloader','Please Check Your Internet Connection \nAnd \nLink Pasted')
    
def back():
    win.destroy()
    main_page()
    
def download():
    downloading=Label(win,text='Downloading',font='san-serif 16 bold',bg='red',fg='white')
    downloading.place(x=290,y=220)
    type_=download_type.get()
    if type_=='MP4':
        stream = url.streams.get_by_itag(137)
        stream.download() # This is the method with the instruction to download the video.
        downloading.destroy()
        messagebox.showinfo('Youtube Downloader','Succesfully Downloaded MP4 File')
    if type_=='1080p':
        stream = url.streams.get_by_itag(137)
        stream.download() # This is the method with the instruction to download the video.
        downloading.destroy()
        messagebox.showinfo('Youtube Downloader','Succesfully Downloaded 1080p File')
    if type_=='720p':
        stream = url.streams.get_by_itag(22)
        stream.download() # This is the method with the instruction to download the video.
        downloading.destroy()
        messagebox.showinfo('Youtube Downloader','Succesfully Downloaded 720p File')
    if type_=='360p':
        stream = url.streams.get_by_itag(18)
        stream.download() # This is the method with the instruction to download the video.
        downloading.destroy()
        messagebox.showinfo('Youtube Downloader','Succesfully Downloaded 360p File')
    if type_=='MP3':
        stream = url.streams.get_by_itag(140)
        stream.download() # This is the method with the instruction to download the video.
        downloading.destroy()
        messagebox.showinfo('Youtube Downloader','Succesfully Downloaded MP3 File')
    
def link_converter():
    global url
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    thumbnail_url=url.thumbnail_url
    response = requests.get(thumbnail_url)
    if response.status_code:
        fp = open('thumbnail.png', 'wb')
        fp.write(response.content)
        fp.close()
        image=Image.open('thumbnail.png')
        new_image=image.resize((200,150))
        new_image.save('thumbnail.png')
        root.destroy()
        global win
        win=Tk()
        win.geometry('500x300') # Size of the window
        win.resizable(0, 0) # makes the window adjustable with its features
        win.title('Youtube Downloader')
        win.iconbitmap('downloader.ico')
        bg=ImageTk.PhotoImage(Image.open('bg.jpg'))
        Label(win,image=bg).place(x=0,y=25)
        head=Label(win, text="Download Youtube videos And audio", font='san-serif 14 bold',bg='red',fg='white',padx=80).place(x=0,y=0)
        
        thumbnail_img=ImageTk.PhotoImage(Image.open('thumbnail.png'))
        thumbnail=Label(win,image=thumbnail_img).place(x=50,y=70)
        type_=['MP4',
              '1080p',
              '720p',
              '360p',
              'MP3']
        global download_type
        download_type=StringVar()
        download_type.set('MP4')
        download_option=OptionMenu(win,download_type,*type_)
        download_option.place(x=300,y=125)
        download_button=Button(win, text='Download', font='san-serif 12 bold', bg='green2',fg='white', command=download, padx=2)
        download_button.place(x=290,y=170)
        back_button=Button(win, text='<BACK', font='san-serif 10 bold', bg='red',fg='white', command=back, padx=20)
        back_button.place(x=40,y=250)
        win.mainloop()
        
def main_page():
    global root
    root = Tk()
    root.geometry('500x300') # Size of the window
    root.resizable(0, 0) # makes the window adjustable with its features
    root.title('Youtube Downloader')
    root.iconbitmap('downloader.ico')

    bg=ImageTk.PhotoImage(Image.open('bg.jpg'))
    Label(root,image=bg).place(x=0,y=25)
    
    global link
    global way
    global link_enter
    global convert
    head=Label(root, text="Download Youtube videos And audio", font='san-serif 14 bold',bg='red',fg='white',padx=80).place(x=0,y=0)
    link = StringVar() # Specifying the variable type
    way=Label(root, text="Paste your link here", font='san-serif 15 bold')
    way.place(x=150, y=55)
    link_enter = Entry(root, width=50,font='15', textvariable=link)
    link_enter.place(x=30, y=115)

    convert=Button(root, text='Convert', font='san-serif 12 bold', bg='red',fg='white', command=checker, padx=80)
    convert.place(x=150, y=150)
    close_button=Button(root, text='EXIT', font='san-serif 10 bold', bg='red',fg='white', command=root.destroy, padx=20)
    close_button.place(x=40,y=250)
    
    root.mainloop()
main_page()