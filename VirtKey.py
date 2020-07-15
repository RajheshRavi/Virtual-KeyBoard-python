'''
Icon Form Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
'''

# Module Imports
import tkinter as tk
import keyboard as key
from functools import partial
import time

# GUI
root = tk.Tk()
root.geometry("980x350")
root.title('Virtual Keyboard')
#root.iconbitmap()

# Global Variables
capt = False
s = ''
st = tk.StringVar()

'''
# Values
di = {'!':'shift + 1','@':'shift + 2','#':'shift + 3','$':'shift + 4','%':'shift + 5','^':'shift + 6','&':'shift + 7','*':'shift + 8','(':'shift + 9',')':'shift + 0'}
sy = {'~':'shift + `','{':'shift + [', '}':'shift + ]','|':'shift + \\',':':'shift + ;','\":"shift +\'','<':'shift + <','>':'shift + .','?':'shift + ?','_':'shift + _',',':'<'}
'''

# Functions for Button Command
def setChar(a):
    global capt
    if capt:
        return chr(ord(a)-ord('a')+ord('A'))
    else:
        return a
def set():
    for i in range(26):
        butChar[i]['text']=setChar(chr(ord('a')+i))

def caps():
    global capt
    capt = not capt
    if capt:
        cap.configure(relief='sunken')
    else:
        cap.configure(relief='raised')
    #print(capt)
    set()

def sendChar(i):
    global s
    char = setChar(chr(ord('a')+i))
    # print in cursor location
    #print(char)
    s+=char
    #print(s)
    #key.write(char)

def sendNum(i):
    global s
    #print(i)
    s+=str(i)
    #print(s)

def sendSpC(i):
    global s
    #print(i)
    s+=i
    #print(s)

def bkSpace():
    global s
    s = s[0:len(s)-1]
    #print(s)

def prev():
    global st
    tk.Label(root,textvariable = st).place(x = 460, y = 260)

def preview():
    global s, st
    #rt = tk.Tk()
    #rt.title('Preview')
    st.set(s)
    #print(st.get())
    prev()
    #rt.mainloop()

def previewClose():
    global st
    st.set(' ')
    prev()

def send():
    global s
    time.sleep(10)
    # Wait for 10 sec to sends
    key.write(s)
    '''
    for i in s:
        if i in di:
            key.send(di[i])
        elif i in sy:
            key.send(sy[i])
        elif ord(i) >= 'A' and ord(i) <= 'Z':
            key.send('shift + '+i)
        elif i == ' ':
            key.send()
        else:
            key.send(i)
        print(i)
    '''


# Caps Lock and Backspace
cap = tk.Button(root,text = "CapsLock",command = caps,width = 9)
cap.place(x = 10, y = 40)
tk.Button(root,text = "Backspace",command = bkSpace).place(x = 10, y = 80)

# Characters
butChar = []
j = 100
a =40
b = 100
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
butNum = []
j = 100
a =40
b = 500
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
tk.Button(root,text = "                                                               ",command = partial(sendSpC," ")).place(x = 140, y = 160) #33



# To Display the content
tk.Button(root, text = 'Click here to preview', command = preview).place(x = 300,y = 210)
tk.Button(root, text = 'Click here to remove preview', command = previewClose).place(x = 460, y = 210)
tk.Button(root, text = 'Send the text to cursor in 10 seconds', command = send).place(x = 350, y = 300)


root.mainloop()
