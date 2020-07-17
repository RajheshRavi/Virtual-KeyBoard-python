'''
This Poject is developed by Rajhesh R
GitHut Link : https://github.com/RajheshRavi
Mail Id : rrajheshgithub@gmail.com
Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
'''

# Module Imports
import tkinter as tk
import keyboard as key
from functools import partial
import time

# GUI
root = tk.Tk()                                      # Creating GUI Object
root.geometry("980x350")                            # Dimention Setup
root.title('Virtual Keyboard')                      # Title Setup
root.iconbitmap('Keyboard.ico')                     # Icon Setup

# Global Variables
capt = False                                        # For Caps Lock
s = ''                                              # To store the entered text
st = tk.StringVar()                                 # To display the entered text if required 

# Functions for Button Command
def setChar(a):                                     # Function to return required Case of alphabets
    global capt
    if capt:
        return chr(ord(a)-ord('a')+ord('A'))
    else:
        return a

def set():                                          # Function to update the case of alphabets in buttons
    for i in range(26):
        butChar[i]['text']=setChar(chr(ord('a')+i))

def caps():                                         # Function to respond the Caps Lock button
    global capt
    capt = not capt
    if capt:
        cap.configure(relief='sunken')
    else:
        cap.configure(relief='raised')
    set()

def sendChar(i):                                    # Function to append corresponding character
    global s
    char = setChar(chr(ord('a')+i))
    s+=char

def sendNum(i):                                     # Function to append corresponding digit
    global s
    s+=str(i)

def sendSpC(i):                                     # Function to append corresponding special character
    global s
    s+=i

def bkSpace():                                      # Function to remove the last character
    global s
    s = s[0:len(s)-1]
    #print(s)

def prev():                                         # Function to display the string in GUI
    global st
    tk.Label(root,textvariable = st).place(x = 460, y = 260)

def preview():                                      # Function to display preview
    global s, st
    st.set(s)
    prev()

def previewClose():                                 # Function to close preview
    global st
    st.set(' ')
    prev()

def send():                                         # Function to write the content in the cursor location
    global s
    time.sleep(10)          # Wait for 10 sec to write in cursor location
    key.write(s)

def support():
    rt = tk.Tk()
    rt.withdraw()
    rt.clipboard_clear()                                                              # Clearing the clipboard
    rt.clipboard_append('https://github.com/RajheshRavi/Virtual-KeyBoard-python')     # Appending the link to the Repositary to th clipboard
    rt.update()                                                                       # Updating the clipboard
    rt.destroy()    
    clip.configure(text = 'Link copied to clipboard')                                 # Updating the Text in the Button

# Caps Lock and Backspace
cap = tk.Button(root,text = "CapsLock",command = caps,width = 9)            # Button for Caps Lock
cap.place(x = 10, y = 40)
tk.Button(root,text = "Backspace",command = bkSpace).place(x = 10, y = 80)  # Button for Backspace

# Characters
butChar = []                                        # List of buttons for Characters
a =40           # Y-Coordinate of Button
b = 100         # X-Coordinate of Button
for i in range(10):
    temp = tk.Button(root, text = chr(ord('a')+i), command = partial(sendChar,i),width = 2)
    temp.place( x = b, y = a)
    #temp.pack()
    butChar.append(temp)
    b+=40
a += 40
b = 100
for i in range(10,20):
    butChar.append(tk.Button(root, text = chr(ord('a')+i), command = partial(sendChar,i),width = 2))
    butChar[-1].place( x = b, y = a)
    #butChar[-1].pack()
    b+= 40
a += 40
b = 100
for i in range(20,26):
    butChar.append(tk.Button(root, text = chr(ord('a')+i), command = partial(sendChar,i),width = 2))
    butChar[-1].place( x = b, y = a)
    #butChar[-1].pack()
    b+= 40

# Numbers
butNum = []                                     # List of buttons for Digits
j = 100
a =40           # Y-Coordinate of Button
b = 500         # X-Coordinate of Button
for i in range(7,10):
    butNum.append(tk.Button(root, text = str(i), command = partial(sendNum,i),width = 2).place( x = b, y = a))
    b+=40
a += 40
b = 500
for i in range(4,7):
    butNum.append(tk.Button(root, text = str(i), command = partial(sendNum,i),width = 2).place( x = b, y = a))
    b+= 40
a += 40
b = 500
for i in range(1,4):
    butNum.append(tk.Button(root, text = str(i), command = partial(sendNum,i),width = 2).place( x = b, y = a))
    b+= 40
a += 40
b = 500
butNum.append(tk.Button(root, text = '0', command = partial(sendNum,0),width = 2).place( x = b, y = a))

# Special Char
tk.Button(root,text = '~',command = partial(sendSpC,'~'),width = 2).place(x = 620, y = 40) #1
tk.Button(root,text = '!',command = partial(sendSpC,'!'),width = 2).place(x = 660, y = 40) #2
tk.Button(root,text = '@',command = partial(sendSpC,'@'),width = 2).place(x = 700, y = 40) #3
tk.Button(root,text = '#',command = partial(sendSpC,'#'),width = 2).place(x = 740, y = 40) #4
tk.Button(root,text = '$',command = partial(sendSpC,'$'),width = 2).place(x = 780, y = 40) #5
tk.Button(root,text = '%',command = partial(sendSpC,'%'),width = 2).place(x = 820, y = 40) #6
tk.Button(root,text = '^',command = partial(sendSpC,'^'),width = 2).place(x = 860, y = 40) #7
tk.Button(root,text = '&',command = partial(sendSpC,'&'),width = 2).place(x = 900, y = 40) #8
tk.Button(root,text = '*',command = partial(sendSpC,'*'),width = 2).place(x = 940, y = 40) #9
tk.Button(root,text = '(',command = partial(sendSpC,'('),width = 2).place(x = 620, y = 80) #10
tk.Button(root,text = ')',command = partial(sendSpC,')'),width = 2).place(x = 660, y = 80) #11
tk.Button(root,text = '[',command = partial(sendSpC,'-'),width = 2).place(x = 700, y = 80) #12
tk.Button(root,text = ']',command = partial(sendSpC,'_'),width = 2).place(x = 740, y = 80) #13
tk.Button(root,text = '{',command = partial(sendSpC,'+'),width = 2).place(x = 780, y = 80) #14
tk.Button(root,text = '}',command = partial(sendSpC,'='),width = 2).place(x = 820, y = 80) #15
tk.Button(root,text = '-',command = partial(sendSpC,'{'),width = 2).place(x = 860, y = 80) #16
tk.Button(root,text = '_',command = partial(sendSpC,'}'),width = 2).place(x = 900, y = 80) #17
tk.Button(root,text = '+',command = partial(sendSpC,'['),width = 2).place(x = 940, y = 80) #18
tk.Button(root,text = '=',command = partial(sendSpC,']'),width = 2).place(x = 620, y = 120) #19
tk.Button(root,text = ':',command = partial(sendSpC,':'),width = 2).place(x = 660, y = 120) #20
tk.Button(root,text = ';',command = partial(sendSpC,';'),width = 2).place(x = 700, y = 120) #21
tk.Button(root,text = '<',command = partial(sendSpC,'<'),width = 2).place(x = 740, y = 120) #22
tk.Button(root,text = '>',command = partial(sendSpC,'>'),width = 2).place(x = 780, y = 120) #23
tk.Button(root,text = '/',command = partial(sendSpC,'/'),width = 2).place(x = 820, y = 120) #24
tk.Button(root,text = '|',command = partial(sendSpC,'|'),width = 2).place(x = 860, y = 120) #25
tk.Button(root,text = '\\',command = partial(sendSpC,'\\'),width = 2).place(x = 900, y = 120) #26
tk.Button(root,text = '?',command = partial(sendSpC,'?'),width = 2).place(x = 940, y = 120) #27
tk.Button(root,text = ',',command = partial(sendSpC,','),width = 2).place(x = 620, y = 160) #28
tk.Button(root,text = '.',command = partial(sendSpC,'.'),width = 2).place(x = 660, y = 160) #29
tk.Button(root,text = '`',command = partial(sendSpC,'`'),width = 2).place(x = 700, y = 160) #30
tk.Button(root,text = '"',command = partial(sendSpC,'"'),width = 2).place(x = 740, y = 160) #31
tk.Button(root,text = "'",command = partial(sendSpC,"'"),width = 2).place(x = 780, y = 160) #32

# Space
tk.Button(root,text = "                                                               ",command = partial(sendSpC," ")).place(x = 140, y = 160) # Button for Spacebar

# To Display the content
tk.Button(root, text = 'Click here to preview', command = preview).place(x = 300,y = 210)               # Button to show preiew
tk.Button(root, text = 'Click here to remove preview', command = previewClose).place(x = 460, y = 210)  # Button to close preview
tk.Button(root, text = 'Send the text to cursor in 10 seconds', command = send).place(x = 350, y = 300) # Button to write the text in cursor location
clip = tk.Button(root, text = 'Click here to support', command = support)                               # Button to support in GitHub
clip.place(x = 700, y = 300)
root.mainloop()