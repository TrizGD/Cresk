from tkinter import *
import time

ver=0.1
space=' '
bg_color=None
if bg_color == None:
      bg_color='#161616'
else:
      pass

clr_check='lime'

txt_fg_clr=clr_check



file_name=None
def open_file():
      try:
            global file_name
            global file_ins
            global in_file
            write_in_file=file_ins.get()
            file_name=file.get()
            if file_name == None:
                  msg=Label(root, bg=bg_color, fg=txt_fg_clr, text='Bad file name or unkown type').pack(side=TOP)
                  time.sleep(1)
                  msg.destroy()
            in_file=open(file_name, 'w')
            if '.txt' in file_name:
                  in_file.write(time.asctime()+
'''
''')
      except:
            dis_txt=Label(root, bg=bg_color, fg=txt_fg_clr, text='Missing or unknown file').pack(side=TOP)
      in_file.write(str(write_in_file))

def display():
      try:
            global file_name
            global in_file
            global dis_txt
            file_name=file.get()
            in_file=open(file_name, 'r')
            dis_txt=Label(root, bg=bg_color, fg=txt_fg_clr, text=in_file.read())
            dis_txt.pack(side=TOP)
            btn2['state']=DISABLED
            btn3['state']=NORMAL
      except:
            dis_txt=Label(root, bg=bg_color, fg=txt_fg_clr, text='Missing or unknown file').pack(side=TOP)

def clear():
      dis_txt.pack_forget()
      btn2['state']=NORMAL

root = Tk()
root.title('Cresk - '+str(ver))
root.geometry('500x400')
root.config(bg=bg_color)
txt1=Label(root, bg=bg_color, fg=txt_fg_clr, text='Load or Save:')
txt1.pack(side=TOP)
file=Entry(root, bg=bg_color, fg=txt_fg_clr, borderwidth="5", relief="flat")
file.pack(side=TOP)
txt2=Label(root, bg=bg_color, fg=txt_fg_clr, text='Save in file(file name)')
txt2.pack(side=TOP)
file_ins=Entry(root, bg=bg_color, fg=txt_fg_clr, borderwidth="5", relief="flat")
file_ins.pack(side=TOP)
btn1=Button(root, bg=bg_color, fg=txt_fg_clr, text='Save', command=open_file)
btn1.pack(side=BOTTOM)
btn2=Button(root, bg=bg_color, fg=txt_fg_clr, text='Display', command=display)
btn2.pack(side=BOTTOM)
btn3=Button(root, bg=bg_color, fg=txt_fg_clr, text='Clear', command=clear)
btn3.pack(side=BOTTOM)
root.mainloop()
