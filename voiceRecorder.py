import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory

add = ""

def file_path():
    global add
    add = askdirectory()
    print(add)

def save_file():
    global add 
    try:
         time = int(sec.get())
         addr = add + "/" + "demo.wav"
         # Record audio
         showinfo(title="Start", message="Recording started")
         recd = sd.rec(int(time*44100), samplerate=44100, channels=2)
         print("Waiting for recording to finish...")
         sd.wait()
         print("Saving file...")
         # Save recorded audio to a WAV file
         write(addr, 44100, recd)
         showinfo(title="End",message="Recording stopped")

    except:
        showwarning(title="Time", message="Wrong time format")


def main_window():
    global sec
    win = Tk()
    win.geometry("500x600")
    win.resizable(False,False)
    win.title("Wscube Tech")
    win.config(bg="pink")

    img1 =PhotoImage(file="voice-record1.png")
    l1= Label(win,image=img1)
    l1.place(x=150,y=20,height=200,width=200)

    sec = Entry(win,font=(20),)
    sec.place(x=150, y=230, height=50,width=200)

    l2 = Label(win,text="Time in sec :", font =("Time New Roman ",20),bg="pink")
    l2.place(x=100, y=290, height=50, width= 300)

    b= Button(win,text="Path",font=("Time New Roman",20),command= file_path)
    b.place(x=150,y=350,height=50,width=200)

    img2= PhotoImage(file="recording mic.png")

    start = Button(win,image=img2, command=save_file)
    start.place(x=170,y=410,height=150,width=150)

    win.mainloop()
main_window()
