
from tkinter import * #Imports everything from tkinter
import os
from time import sleep
from tkinter.font import Font
click = 1

root =Tk()
root.title("TicTacToe")
root.geometry("450x600")
root.config(bg="black")


buttons_frame = Frame(root,bg="red")
buttons_frame.pack(pady = 50)
moves = [0,0,0,0,0,0,0,0,0]



    
myfont = Font(family="Comic Sans MS,",weight='bold')


def show_entry_fields():
    global e1l,e2l,player1,player2,b1
    player1 = e1.get()
    player2 = e2.get()
    
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1l.config(text= "{} : X".format(e1.get()))
    e2l.config(text= "{} : O".format(e2.get()))
    b1.config(state=DISABLED)

    
    e1.destroy()
    e2.destroy()


e1l =Label(root, text="First Player",bg="yellow")
e1l['font']=myfont
e1l.pack()
e2l = Label(root, text="Second Player",bg="yellow")
e2l['font']=myfont
e2l.pack()

e1 = Entry(root)
e2 = Entry(root)
e1.insert(10, "PLAYER 1")
player1 ="PLAYER 1"
player2 ="PLAYER 2"

e2.insert(10, "PLAYER 2")


e1.pack()
e2.pack()


b1 = Button(root, text='Done', command=show_entry_fields,bg="red")
b1.pack()
b2 = Button(root, 
        text='Quit', 
        command=root.quit,bg="red")
b1['font']=myfont
b2['font']=myfont

b2.pack()



def tictactoe():
    root.destroy()
    
    os.system("tictactoe.py")








def check_moves(t,c):
    global click,player2,player1
    
    if check_cols(t) or check_diag(t) or check_rows(t):
        
        try:
            e1.destroy()
            e2.destroy()
        except EXCEPTION:
            pass
        
        for Widget in buttons_frame.winfo_children():
            Widget.destroy()
    
        
        
        
        
        
        if click%2==1:
            
            e1l.config(text="{} Wins".format(player1),bg="orange")
            e1l.place(x = 175,y=100)
            e2l.config(text = "PLAY AGAIN?",bg="orange")
            e2l.place(x=175,y=150)
            b1.config(state=NORMAL,bg='yellow')

            b1.config(text = 'Yes',command =tictactoe,width =5,height =3,bg="yellow")
            b1.place(x=190,y=180)
            b2.config(width =5,height =3,bg="yellow")
            b2.place(x=190,y=250)
            
            
        if click%2==0:
            e1l.config(text = "{} Wins".format(player2),bg="orange")
            e1l.place(x = 175,y=100)

            e2l.config(text = "PLAY AGAIN?",bg="orange")

            e2l.place(x=175,y=150)
            b1.config(state=NORMAL,bg='yellow')

            b1.config(text = 'Yes',command = tictactoe,width = 5,height =3,bg="yellow")
            b1.place(x=190,y=180)
            b2.config(width =5,height =3,bg="yellow")
            b2.place(x=190,y=250)
    elif click>=9:
        e1l.config(text="DRAW")
        e2l.config(text="Play Again")
        b1.config(state=NORMAL,bg='yellow')

        b1.config(text = 'Yes',command =tictactoe,bg="red")
        
        b2.config(bg="red")

    else:
        pass
def check_diag(t):
    if moves[0]==moves[4] and moves[0]==moves[8] and moves[0]==t:

        return(True)    
    elif moves[2]==moves[4] and moves[2]==moves[6] and moves[2]==t:
        return(True) 
    else:
        pass
def check_cols(t):
    global moves
    for i in range(3):
        if moves[i]==t:
            if moves[i]==moves[i+3] and moves[i]==moves[i+6]:
                return(True)
def check_rows(t):
    
    for i in range(0,7,3):
        if moves[i]==t:
            if moves[i]==moves[i+1] and moves[i]==moves[i+2]:
                
                return(True)
        

def button_1():
    global click , moves
    if click%2==1:
        button1.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"
        
    else:
        button1.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[0] = text
    if click>=5:
        check_moves(text,click)
    click += 1


def button_2():
    
    global click, moves
    if click%2==1:
        button2.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"
    else:
        button2.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"

    moves[3] = text
    if click>=5:
        check_moves(text,click)

    click += 1

def button_3():
    
    global click,moves
    if click%2==1:
        button3.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"  
    else:
        button3.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[6] = text
    if click>=5:
        check_moves(text,click)
    click += 1

def button_4():
    
    global click,moves
    if click%2==1:
        button4.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"
    else:
        button4.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[1] = text
    if click>=5:
        check_moves(text,click)
    click += 1
def button_5():
    global click,moves
    if click%2==1:
        button5.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"      
    else:
        button5.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[4] = text
    if click>=5:
        check_moves(text,click)
    click += 1

def button_6():
    
    global click,moves
    if click%2==1:
        button6.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"      
    else:
        button6.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[7] = text
    if click>=5:
        check_moves(text,click)
    click += 1

def button_7():
    
    global click,moves
    if click%2==1:
        button7.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"    
    else:
        button7.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[2] = text
    if click>=5:
        check_moves(text,click)
    click += 1

def button_8():
    
    global click,moves
    if click%2==1:
        button8.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"
    else:
        button8.config(text = "O",state = DISABLED,bg = 'orange')
        #moves.append("O")
        text = "O"
    moves[5] = text
    if click>=5:
        check_moves(text,click)
    


    click += 1


def button_9():
    
    global click,moves
    if click%2==1:
        button9.config(text = "X",state = DISABLED,bg = 'orange')
        text = "X"    
    else:
        button9.config(text = "O",state = DISABLED,bg = 'orange')
        text = "O"
    moves[8] = text
    if click>=5:
        check_moves(text,click)
    click += 1
    


    
button1 = Button(buttons_frame,text = "Press",command = button_1,width = 10,height =5)
button1.grid(row =0,column = 0)
button1['font'] = myfont


button2 = Button(buttons_frame,text = "Press",command = button_2,width = 10,height =5)
button2.grid(row =1,column = 0)
button2['font'] = myfont


button3 = Button(buttons_frame,text = "Press",command = button_3,width = 10,height =5)
button3.grid(row =2,column = 0)
button3['font'] = myfont


button4 = Button(buttons_frame,text = "Press",command = button_4,width = 10,height =5)
button4.grid(row =0,column = 1)
button4['font'] = myfont


button5 = Button(buttons_frame,text = "Press",command = button_5,width = 10,height =5)
button5.grid(row =1,column = 1)
button5['font'] = myfont



button6 = Button(buttons_frame,text = "Press",command = button_6,width = 10,height =5)
button6.grid(row =2,column = 1)
button6['font'] = myfont



button7 = Button(buttons_frame,text = "Press",command = button_7,width = 10,height =5)
button7.grid(row =0,column = 2)
button7['font'] = myfont



button8 = Button(buttons_frame,text = "Press",command = button_8,width = 10,height =5)
button8.grid(row =1,column = 2)
button8['font'] = myfont



button9 = Button(buttons_frame,text = "Press",command = button_9,width = 10,height =5)
button9.grid(row =2,column = 2)
button9['font'] = myfont




root.mainloop()