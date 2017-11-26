from tkinter import *
import tkinter.messagebox
import time

def WinnerCheck(i):
      global counter
      x=0
      while x<=6:
            if list[x]["text"] == list[x+1]["text"] == list[x+2]["text"] != "     " :
                  FinishedGame(1)
            x+=3
      x=0
      while x<=2 :
            if list[x]["text"] == list[x+3]["text"] == list[x+6]["text"] != "     " :
                  FinishedGame(1)
            x+=1
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " :
            quit()
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
            quit()
      if counter == 8:
            FinishedGame(0)
            
def checked(i) :
      global player
      global counter
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            WinnerCheck(i)
            button["bg"] = "yellow"
            
      else :
            player = "X"
            WinnerCheck(i)
            button["bg"] = "lightgreen"
      counter+=1

def FinishedGame(i) :
      global player
      if i == 0:
            tkinter.messagebox.showinfo("END.","무승부")
      if i == 1:
            if player == "X" :
                  player = "O"
            else:
                  player = "X"
            
            tkinter.messagebox.showinfo("END.",player+"의 승리")         
      quit()
      
window = Tk()
counter=0
player = "X"
list= []
window.geometry('180x170+10+10')
window.title("Tic-Tac-Toe")

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k),height=3,width=4)
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


