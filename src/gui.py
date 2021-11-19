import tkinter as tk
from tkinter import Variable, filedialog
from tkinter.constants import SINGLE
import mood_ai as audio
import audio_analysis as stat
from playsound import playsound

#<--------Initial Variables--------->

file_path = "No audio file selected"
b_w = 17
b_h = 9


#<--------Main Functions--------->

#Play the audio file
def play():
    try:
        name,extension =file_path.split(".")
        if extension == "wav":
            playsound(str(file_path))
        else:
            play_win = tk.Tk()
            play_lab = tk.Label(play_win,text="Error: Files must be wav")
            play_lab.pack()
    except:
        play_win = tk.Tk()
        play_lab = tk.Label(play_win,text="Hm, something went wrong")
        play_lab.pack()


    
#File browsing
def select_audio():
    global file_path
    file_path = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Audio files",
                                                    "*.wav*"),
                                                    ("all files",
                                                    "*.*")))
    file_choice.config(text="File: " +str(file_path))
      
#Returns Pitch (Hz)
def pitch():
    pitch_win = tk.Tk()
    pitch_lab = tk.Label(pitch_win)
    try:
        pitch_lab.configure(text=audio.get_pitch(file_path))
    except ValueError:
        pitch_lab.configure(text="Error: Invalid file name")
    except FileNotFoundError:
        pitch_lab.configure(text="Error: No file selected")
    except RuntimeError:
        pitch_lab.configure(text="Error: No file selected")
    except:
        pitch_lab.configure(text="Hm, something went wrong")
    pitch_lab.pack()

#Returns Amplitude (Db)
def amp():
    amp_win = tk.Tk()
    amp_lab = tk.Label(amp_win)
    try:
        amp_lab.configure(text=audio.get_amp(file_path))
    except ValueError:
        amp_lab.configure(text="Error: Invalid file name")
    except FileNotFoundError:
        amp_lab.configure(text="Error: No file selected")
    except:
        amp_lab.configure(text="Hm, something went wrong")

    amp_lab.pack()

#Return Audio Stats
def show_stats():
    try:
        stat.analyse(str(file_path))
    except:
        err_win = tk.Tk()
        err_win.configure(bg="red")
        err_lab = tk.Label(err_win,text="Hm, something went wrong")
        err_lab.pack()

#Get the mood based on audio variables eg:pitch
def mood_calc():
    try:
        for i in gender_box.curselection():
            mood_win = tk.Tk()
            mood_win.geometry('100x50')
            mood_lab = tk.Label(mood_win,text=audio.get_mood(file_path,gender_box.get(i),age_box.get()))
            mood_lab.pack()
    except:
        err_win = tk.Tk()
        err_lab = tk.Label(err_win,text="Hm, something went wrong")
        err_lab.pack()
        err_win.configure(bg="red")

#<--------Gui setup--------->

root = tk.Tk()

root.title("Mood Analysis")
root.geometry("500x500")
root.configure(bg="black")

analysis= tk.Button(root,text="Mood",width=b_w,height=b_h,command = mood_calc)
stats= tk.Button(root,text="Statistics",width=b_w,height=b_h,command = show_stats)
audio_choose= tk.Button(root,text="Select Audio",width=b_w,height=b_h,command = select_audio)
pitch_button= tk.Button(root,text="Pitch",width=b_w,height=b_h,command = pitch)
amp_button= tk.Button(root,text="Amplitude",width=b_w,height=b_h,command = amp)
file_choice = tk.Label(root, text=str(file_path))
play_audio = tk.Button(root,text="Play Audio",width=b_w,height=b_h,command = play)
age_box = tk.Entry(root,text="age")
gender_box = tk.Listbox(root,selectmode=SINGLE,height=2)

gender_box.insert(1,"Male")
gender_box.insert(2,"Female")

analysis.place(x=0,y=0)
stats.place(x=168,y=0)
audio_choose.place(x=337,y=0)
pitch_button.place(x=0,y=168)
amp_button.place(x=168,y=168)
file_choice.place(x=0,y=480)
play_audio.place(x=337,y=168)
age_box.place(x=0,y=337)
gender_box.place(x=167,y=337)


root.mainloop()