from asyncio.windows_events import NULL
from cProfile import label
from cgitb import text
from ctypes import sizeof
from ctypes.wintypes import SIZE
import tkinter as tk
import random
from tkinter import Label, font
import ctypes

OFF_WHITE = "#F8FAFF"
box_color = "#141414"
LABEL_COLOR = "#25265E"

def stars(x, y):            #function to create safe zones (star places)
    points = [
        x,y,            #1                                  1
        x-5, y+10,      #2                                
        x-15, y+10,     #3                           3    2    10   9
        x-10, y+20,     #4                               
        x-10, y+30,     #5                               4      8
        x, y+25,        #6                                   6
        x+10, y+30,     #7                           5              7
        x+10, y+20,     #8
        x+15, y+10,     #9
        x+5, y+10]  
    return points

     

class LUDO:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("900x900")
        #self.window.resizable(0, 0)
        self.window.title("L U D O")

        self.create_canvas = tk.Canvas(self.window, bg = box_color, width = 750, height = 750)
        self.create_canvas.pack(fill = tk.BOTH, expand = 1)

        self.create_canvas.l1 = tk.Label(self.window,  font = ("Helvetica", 50))

        self.for_red_coin = []
        self.for_blue_coin = []
        self.for_yellow_coin = []
        self.for_green_coin = []

        
        self.pos_r1 = 0
        self.pos_r2 = 0
        self.pos_r3 = 0
        self.pos_r4 = 0

        self.pos_b1 = 0
        self.pos_b2 = 0
        self.pos_b3 = 0
        self.pos_b4 = 0

        self.pos_y1 = 0
        self.pos_y2 = 0
        self.pos_y3 = 0
        self.pos_y4 = 0

        self.pos_g1 = 0
        self.pos_g2 = 0
        self.pos_g3 = 0
        self.pos_g4 = 0
        
        self.n_dice = []

        self.total_players = []

        self.board()
        self.create_canvas.dice_buttons = self.dice_button()
      
 
    
    
    def dice_label(self):
        n = ['\u2680', '\u2681','\u2682', '\u2683','\u2684', '\u2685']
        int_no = {'\u2680' : 1, '\u2681' : 2,'\u2682' : 3, '\u2683' : 4,'\u2684' : 5, '\u2685' : 6}
        mn = 0
        mm = 48-1
        nm = 0
        nn = -48
        
        coin_clr = 'red'
        
        txt = random.choice(n)
        self.create_canvas.l1.config(text = txt)
        
        '''
        if(txt == '\u2685'): 
            if(coin_clr == 'red'):
                mm += 46
                mm *= 6
                self.create_canvas.move(self.r1, -1, 250)
            elif(coin_clr == 'blue'):
                self.create_canvas.move(self.b1, 232, 135)
            elif(coin_clr == 'yellow'):
                self.create_canvas.move(self.y1, 125, -94)
            elif(coin_clr == 'green'):
                self.create_canvas.move(self.g1, -94, 10)
                '''

        if(coin_clr == 'red'):
            j = 0
                #self.pos_r1 += 4
                #mm *= 4
                #nn -= 45
            if(txt == '\u2680'):
                j = 1
            if(txt == '\u2681'):
                j = 2
            if(txt == '\u2682'):
                j = 3
            if(txt == '\u2683'):
                j = 4
            if(txt == '\u2684'):
                j = 5
            if(txt == '\u2685'):
                j = 0
        
            for i in range(j):
                if(self.pos_r1 < 4):
                    self.pos_r1 += 1
                    nn = 0
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 4):
                    self.pos_r1 += 1
                    nn = -47
                    self.create_canvas.move(self.r1, mm, nn)    
                elif(self.pos_r1 > 4 and self.pos_r1 < 10):
                    self.pos_r1 += 1
                    mm = 0
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 10 or self.pos_r1 == 11):
                    self.pos_r1 += 1
                    mm = 43
                    nn = 0
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 11 and self.pos_r1 < 17):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    nn += 48
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 17):
                    self.pos_r1 += 1
                    nn = 0
                    nn += 47
                    mm = 0
                    mm = 45
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 17 and self.pos_r1 < 23):
                    self.pos_r1 += 1
                    nn = 0
                    mm = 0
                    mm += 46
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 23 or self.pos_r1 == 24):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    nn += 40
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 24 and self.pos_r1 < 30):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    mm -= 47
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 30):
                    self.pos_r1 += 1
                    nn = 0
                    nn += 47
                    mm = 0
                    mm -= 40
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 30 and self.pos_r1 < 36):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    nn += 47
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 36 or self.pos_r1 == 37):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    mm -= 43
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 37 and self.pos_r1 < 43):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    nn -= 48
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 43):
                    self.pos_r1 += 1
                    nn = 0
                    nn -= 42
                    mm = 0
                    mm -= 46
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 43 and self.pos_r1 < 49):
                    self.pos_r1 += 1
                    mm = 0
                    nn = 0
                    mm -= 47
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 == 49):
                    self.pos_r1 += 1
                    nn = 0
                    mm = 0
                    nn -= 42
                    self.create_canvas.move(self.r1, mm, nn)
                elif(self.pos_r1 > 49 and self.pos_r1 < 56):
                    self.pos_r1 += 1
                    nn = 0
                    self.create_canvas.move(self.r1, mm, nn)




            
        print(self.pos_r1)
        
        
        
        self.create_canvas.l1.pack() 
        
        #mm += 45
        #self.create_canvas.move(self.r1, mm, 250)

        return txt
    
    def dice_button(self):
        count = self.n_dice
        for i in range(1,3):
            if(self.dice_label == '\u2685'):
                count += 1                
            #if(count < 4):
           # else:

        
                
        
        b1 = tk.Button(self.create_canvas, text = "Roll the Dice", bg = OFF_WHITE, fg = "blue", command = self.dice_label)
        b1.place()
        b1.pack(side = tk.RIGHT)


    def coin_button(self):
        b1 = tk.Button(self.create_canvas, command = self.coin_move)
        b1.pack()
        #b1.grid(row=0, column = 1)
    
    def coin_move(self):
        self.create_canvas.move(v, -1, 250)

    
    def board(self):
        self.create_canvas.create_rectangle(5, 5, 700, 700, width = 0, fill = "white")  # for main box
        #self.create_canvas.create_rectangle(850, 325, 800, 375, width = 0, fill = "white")  # for dice box

        self.create_canvas.create_rectangle(5, 5, 290, 300, width=2, fill="#ff0000") # for red box
        self.create_canvas.create_rectangle(5 , (5 + 695), 290, (120 + 300), width=2, fill="blue") # for blue box
        self.create_canvas.create_rectangle(420, 5, 700, 300, width=2, fill="#00ff00") # for green box
        self.create_canvas.create_rectangle(420, (5 + 415), 700, 700, width=2, fill="yellow") # for yellow box
        
        #red-blue-zone
        self.create_canvas.create_rectangle(5, 300, 290, (300 + 40), width=3)
        self.create_canvas.create_rectangle(54, 380, 290, (300 + 40), width=3, fill = "#ff0000")
        self.create_canvas.create_rectangle(5, 420, 290, (300 + 80), width=3)

        #yellow-green-zone
        self.create_canvas.create_rectangle(420, 300, 700, 340, width=3)
        self.create_canvas.create_rectangle(420, 340, 652, 380, width=3, fill = "yellow")
        self.create_canvas.create_rectangle(420, 380, 700, 420, width=3)

        #green-red-zone
        self.create_canvas.create_rectangle(290, 5, 335, 299, width=3)
        self.create_canvas.create_rectangle(335, 55, 380, 299, width=3, fill="#00FF00")
        self.create_canvas.create_rectangle(380, 5, 100 + 319, 299, width=3)

        #blue-yellow-zone
        self.create_canvas.create_rectangle(290, 421, 335, 699, width=3)
        self.create_canvas.create_rectangle(335, 421, 380, 653, width=3, fill="#0000FF")
        self.create_canvas.create_rectangle(380, 421, 420, 699, width=3)

        #lines for red-blue zone
        start_x = 5
        start_y = 299
        end_x = 5
        end_y = 420
        for _ in range(6):
            self.create_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x += 48
            end_x += 48

        #lines for yellow-green zone
        start_x = 464
        start_y = 299
        end_x = 464
        end_y = 420
        for _ in range(6):
            self.create_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x += 47
            end_x += 47

        #lines for red-green zone
        start_x = 289
        start_y = 5
        end_x = 419
        end_y = 5
        for _ in range(6):
            self.create_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 50
            end_y += 50

        #lines for blue-yellow zone
        start_x = 289
        start_y = 468
        end_x = 419
        end_y = 468
        for _ in range(6):
            self.create_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 46
            end_y += 46

        #self inside red box (holder)
        self.create_canvas.create_rectangle(50, 45, 109, 100, width = 3, fill = "white")
        self.create_canvas.create_rectangle(180, 45, 245, 100, width = 3, fill = "white")
        self.create_canvas.create_rectangle(50, 245, 110, 185, width = 3, fill = "white")
        self.create_canvas.create_rectangle(180, 185, 245, 245, width = 3, fill = "white")
        
        #self inside green box (holder)
        self.create_canvas.create_rectangle(465, 45, 525, 100, width = 3, fill = "white")
        self.create_canvas.create_rectangle(605, 45, 665, 100, width = 3, fill = "white")
        self.create_canvas.create_rectangle(465, 245, 525, 185, width = 3, fill = "white")
        self.create_canvas.create_rectangle(605, 185, 665, 245, width = 3, fill = "white")
        
        #self inside blue box (holder)
        self.create_canvas.create_rectangle(50, 465, 112, 525, width = 3, fill = "white")
        self.create_canvas.create_rectangle(180, 465, 245, 525, width = 3, fill = "white")
        self.create_canvas.create_rectangle(50, 605, 110, 665, width = 3, fill = "white")
        self.create_canvas.create_rectangle(180, 605, 245, 665, width = 3, fill = "white")
        
        #self inside yellow box (holder)
        self.create_canvas.create_rectangle(475, 465, 535, 525, width = 3, fill = "white")
        self.create_canvas.create_rectangle((180 + 475 - 50), 465, 665, 525, width = 3, fill = "white")
        self.create_canvas.create_rectangle((50 + 475 - 50), 605, 535, 665, width = 3, fill = "white")
        self.create_canvas.create_rectangle((180 + 475 - 50), 605, 665, 665, width = 3, fill = "white")

        #red start position
        self.create_canvas.create_rectangle(54, 300, 101, 340, width=3, fill="#ff0000")

        #Blue start position
        self.create_canvas.create_rectangle(290, 605, 335, 653, width=3, fill="#0000FF")

        #yellow start position
        self.create_canvas.create_rectangle(605, 380, 652, 420, width=3, fill="yellow")

        #green start position
        self.create_canvas.create_rectangle(380, 55, 419, 105, width=3, fill="#00FF00")

        #Home
        self.create_canvas.create_polygon(291, 300, 291, 420, 355.5, 355.5, width=3, fill="#ff0000", outline = "#000000")
        self.create_canvas.create_polygon(300 + 120, 300, 120 + 300, 420, 355.5, 355.5, width=3, fill="yellow", outline = "#000000")
        self.create_canvas.create_polygon(291, 420, 422, 420, 355.5, 355.5, width=3, fill="#0000ff", outline = "#000000")
        self.create_canvas.create_polygon(291, 300, 420, 300, 355.5, 355.5, width=3, fill="#00ff00", outline = "#000000")

        self.create_canvas.create_text(355.5, 355.5, text = "HOME", font= ("algerian 18 bold"), fill="#000000", activefill="#ffffff")       

        #star
        x = 78
        y = 305
        points = stars(x, y)    #red1
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#ff0000", width = 3)

        x = 125
        y = 385
        points = stars(x, y)    #red2
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#ff0000", width = 3)

        x = 312
        y = 614
        points = stars(x, y)     #blue1
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#1122ff", width = 3)

        x = 400
        y = 568
        points = stars(x, y)     #blue2
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#0000ff", width = 3)

        x = 628
        y = 385
        points = stars(x, y)     #yellow1
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "yellow", width = 3)

        x = 578
        y = 305
        points = stars(x, y)     #yellow2
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "yellow", width = 3)

        x = 400
        y = 63
        points = stars(x, y)     #green1
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#00ff00", width = 3)

        x = 313
        y = 114
        points = stars(x, y)     #green2
        self.create_canvas.create_polygon(points, outline = "#000000", fill = "#00ff00", width = 3)


        # red-coins
        self.r1 = self.create_canvas.create_oval(67, 58, 91, 83, width=3, fill="#ff0000", activewidth=4, activefill="#ff0000")
        self.create_canvas.move(self.r1, -1, 250)
        #self.create_canvas.move(self.r1, 47*5, 0)
        #self.create_canvas.move(self.r1, 0, -45)
        
        self.r2 = self.create_canvas.create_oval(200, 60, 225, 85, width=3, fill="#ff0000", activewidth=4, activefill="#ff0000")
        self.r3 = self.create_canvas.create_oval(67, 202, 93, 227, width=3, fill="#ff0000", activewidth=4, activefill="#ff0000")
        self.r4 = self.create_canvas.create_oval(200, 200, 225, 225, width=3, fill="#ff0000", activewidth=4, activefill="#ff0000")
        self.for_red_coin.append(self.r1)
        self.for_red_coin.append(self.r2)
        self.for_red_coin.append(self.r3)
        self.for_red_coin.append(self.r4)
        
        
        # blue-coins
        self.b1 = self.create_canvas.create_oval(69, (58 + 425), 93, (83 + 425), width=3, fill="#0000ff", activewidth=4, activefill="#0000ff")
        self.b2 = self.create_canvas.create_oval(200, (60 + 425), 225, (85 + 425), width=3, fill="#0000ff", activewidth=4, activefill="#0000ff")
        self.b3 = self.create_canvas.create_oval(68, (202 + 422), 92, (227 + 422), width=3, fill="#0000ff", activewidth=4, activefill="#0000ff")
        self.b4 = self.create_canvas.create_oval(200, (200 + 422), 225, (225 + 422), width=3, fill="#0000ff", activewidth=4, activefill="#0000ff")
        self.for_blue_coin.append(self.b1)
        self.for_blue_coin.append(self.b2)
        self.for_blue_coin.append(self.b3)
        self.for_blue_coin.append(self.b4)

        # yellow-coins
        self.y1 = self.create_canvas.create_oval((67 + 425), (58 + 425), (91 + 425), (83 + 425), width=3, fill="yellow", activewidth=4, activefill="yellow")
        self.y2 = self.create_canvas.create_oval((200 + 425), (60 + 425), (225 + 425), (85 + 425), width=3, fill="yellow", activewidth=4, activefill="yellow")
        self.y3 = self.create_canvas.create_oval((67 + 425), (202 + 425), (93 + 425), (227 + 425), width=3, fill="yellow", activewidth=4, activefill="yellow")
        self.y4 = self.create_canvas.create_oval((200 + 425), (200 + 425), (225 + 425), (225 + 425), width=3, fill="yellow", activewidth=4, activefill="yellow")
        self.for_yellow_coin.append(self.y1)
        self.for_yellow_coin.append(self.y2)
        self.for_yellow_coin.append(self.y3)
        self.for_yellow_coin.append(self.y4)

        # green-coins
        self.g1 = self.create_canvas.create_oval((67 + 415), 58, (91 + 415), 83, width=3, fill="#00ff00", activewidth=4, activefill="#00ff00")
        self.g2 = self.create_canvas.create_oval((200 + 425), 60, (225 + 425), 85, width=3, fill="#00ff00", activewidth=4, activefill="#00ff00")
        self.g3 = self.create_canvas.create_oval((67 + 415), 202, (93 + 415), 227, width=3, fill="#00ff00", activewidth=4, activefill="#00ff00")
        self.g4 = self.create_canvas.create_oval((200 + 425), 200, (225 + 425), 225, width=3, fill="#00ff00", activewidth=4, activefill="#00ff00")
        self.for_green_coin.append(self.g1)
        self.for_green_coin.append(self.g2)
        self.for_green_coin.append(self.g3)
        self.for_green_coin.append(self.g4)

        
        #1st position or )th position of all coins
        
        #self.create_canvas.move(r1, -1, 250)
        #self.create_canvas.move(r2, -135, 250)
        #self.create_canvas.move(r3, -1, 107)
        #self.create_canvas.move(r4, -134, 108)
        '''
        self.create_canvas.move(self.b1, 232, 135)
        self.create_canvas.move(b2, -1, 250)
        self.create_canvas.move(b3, -1, 250)
        self.create_canvas.move(b4, -1, 250)

        self.create_canvas.move(self.y1, 125, -94)
        self.create_canvas.move(y2, -1, 250)
        self.create_canvas.move(y3, -1, 250)
        self.create_canvas.move(y4, -1, 250)

        self.create_canvas.move(self.g1, -94, 10)
        self.create_canvas.move(g2, -1, 250)
        self.create_canvas.move(g3, -1, 250)
        self.create_canvas.move(g4, -1, 250)
        '''
       
        
    
    def game_start(self):
        top = tk.Toplevel()
        top.geometry("600x600")
        top.maxsize("600x600")
        top.minsize("600x600")
        #top.
  
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    LUDO_GAME = LUDO()
    LUDO_GAME.run()