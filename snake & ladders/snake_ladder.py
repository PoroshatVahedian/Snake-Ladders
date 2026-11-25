from tkinter import *
from tkinter import ttk
from random import choice


# players_info=Tk()
# players_info.title('Players Information')
# players_info.geometry('500x400')
# players_info.resizable(False,False)
# players_info_canvas=Canvas(players_info,background='light blue',width=500,height=400)


win=Tk()
# f=Frame(win)
# f.pack(expand=True,fill=BOTH)

dice={
1:PhotoImage(file=r'image\one_dice.png'),
2:PhotoImage(file=r'image\two_dice.png'),
3:PhotoImage(file=r'image\three_dice.png'),
4:PhotoImage(file=r'image\four_dice.png'),
5:PhotoImage(file=r'image\five_dice.png'),
6:PhotoImage(file=r'image\six_dice.png')}

blue_piece_pic=PhotoImage(file=r'image\blue_piece.png')
red_piece_pic=PhotoImage(file=r'image\red_piece.png')
green_piece_pic=PhotoImage(file=r'image\green_piece.png')
yellow_piece_pic=PhotoImage(file=r'image\yellow_piece.png')

blue_choice_pic=PhotoImage(file=r'image\blue-choice.png')
red_choice_pic=PhotoImage(file=r'image\red-choice.png')
green_choice_pic=PhotoImage(file=r'image\green-choice.png')
yellow_choice_pic=PhotoImage(file=r'image\yellow-choice.png')

pieces={'blue':blue_choice_pic,
    'red':red_choice_pic,
    'green':green_choice_pic,
    'yellow':yellow_choice_pic}

player_pieces={'blue':blue_piece_pic,
    'red':red_piece_pic,
    'green':green_piece_pic,
    'yellow':yellow_piece_pic}

win.title('Snake & Ladders')
win.geometry('800x600')
win.resizable(False,False)

win.iconbitmap('image\icons8-year-of-snake-50.ico')

Label(win,text='Snake & Ladders',font=('Bauhaus 93',32),foreground='#cd1fd3').place(x=260,y=0)

game_board=Canvas(win,width=500,height=500,bg='light blue')
game_board.pack(side=LEFT,padx=20)

colors=['#a7f2f2','#f9bddc','#f4d2b2','#5bf782','#A9A9A9']


danger=PhotoImage(file='image\icons8-error-48.png')

up=PhotoImage(file='image\icons8-double-up-50.png')

celebrate_pic=PhotoImage(file='image\icons8-confetti-100.png')

starter=0
turn=0
x_player1=25
x_player2=25
y_player1=470
y_player2=470
new_dice_player1=0
new_dice_player2=0
check_turn=0
round=0
player1_name_get=''
player2_name_get=''
k=0
h=0
del_pic1_check=False
del_pic2_check=False
y1=False
y2=False
turn_arrow=PhotoImage(file=r'image\arrow.png')
turn_arrow_label1=Label(win)
turn_arrow_label1.place(x=720,y=130)
turn_arrow_label2=Label(win)
turn_arrow_label2.place(x=720,y=500)
blank=PhotoImage(file=r'image\blank.png')
notif_pic1=Label(win,image=blank)
notif_pic2=Label(win,image=blank)
img_piece1=game_board.create_image(0,0,image=blue_piece_pic)
img_piece2=game_board.create_image(0,0,image=red_piece_pic)
notif_pic1.place(x=530,y=120)
notif_pic2.place(x=530,y=500)
def set_the_turn():
    global starter,turn,player1_piece,player2_piece,k,h
    if player1_name['text']!='' and player2_name['text']!='':
        turn_arrow_label1.config(image=turn_arrow)
        player1_piece=game_board.create_image(x_player1,y_player1,image=player_pieces[v1.get()])
        player2_piece=game_board.create_image(x_player2,y_player2,image=player_pieces[v2.get()])
        logo.destroy()
        _dice=Label(win,text=1,image=dice[1],bd=0)
        _dice.place(x=585,y=240)
        def set_turn_player1():
            global new_dice_player1,check_turn,round,turn_arrow,turn_arrow_label1,blank
            for _ in range(1):
                turn_arrow_label1.config(image=blank)
                new_dice_player1=choice(list(dice.keys()))
                set_turn_player1_btn.destroy()
                turn_arrow_label2.config(image=turn_arrow)
            # new_dice_player2=choice(list(dice.keys()))
                _dice.config(text=new_dice_player1,image=dice[new_dice_player1])
                _dice.update()
        set_turn_player1_btn=Button(win,text=f'{player1_name_get} ,roll dice for setting turn',font=('Yu Gothic UI Semilight',12),bd=1,command=set_turn_player1)
        set_turn_player1_btn.place(x=540,y=198)
        # change_dice=Button(win,text='roll the dice',font=('Yu Gothic UI Semilight',14),bd=0,command=set_turn_player1)
        # change_dice.bind('<Button>',set_turn_player1)
        # change_dice.place(x=605,y=400)
        def set_turn_player2():
            global new_dice_player2,check_turn,round,turn_arrow,turn_arrow_label2,blank,starter,turn,player1_piece,player2_piece,k,h,img_piece1,img_piece2,notif_pic1,notif_pic2,celebrate_pic
            for _ in range(1):
                turn_arrow_label2.config(image=blank)
            while True:
                new_dice_player2 = choice(list(dice.keys()))

                if new_dice_player2 != new_dice_player1:
                    break

            set_turn_player2_btn.destroy()
            _dice.config(text=new_dice_player2, image=dice[new_dice_player2])
            _dice.update()

            if new_dice_player1>new_dice_player2:
                turn=1
                starter=1
                turn_arrow_label1.config(image=turn_arrow)
                l1=Label(win,text='       ',width=30,height=6)
                l1.place(x=580,y=0)

                # set_the_turn_btn.destroy()
                # start=Button(win,text='START',font=('Yu Gothic UI Semilight',10),bd=0)
                # start.pack(side=RIGHT)

            elif new_dice_player2>new_dice_player1:
                turn=2
                starter=2
                turn_arrow_label2.config(image=turn_arrow)
                l2=Label(win,text='           ',width=30,height=6)
                l2.place(x=580,y=0)
                # set_the_turn_btn.destroy()


            def roll_dice_func():
                last_check2=0
                last_check1=0
                global new_dice_player1,new_dice_player2,player1_piece,player2_piece,x_player1,x_player2,turn,starter,turn,y_player1,y_player2,h,k,y1,y2,img_piece1,img_piece2
                global del_pic1_check,del_pic2_check,notif_pic1,notif_pic2,celebrate_pic
                notif_pic1.config(image=blank)
                notif_pic2.config(image=blank)
                if starter==1:
                    new_dice_player1=choice(list(dice.keys()))
                    _dice.config(text=new_dice_player1,image=dice[new_dice_player1])
                    _dice.update()
                    game_board.delete(player1_piece)
                    del_pic1_check=True
                    for _ in range(new_dice_player1):
                        k=1
                        x_player1+=50
                    img_piece1=game_board.create_image(x_player1,y_player1,image=player_pieces[v1.get()])
                    starter='none'
                    turn=2
                    turn_arrow_label1.config(image=blank)
                    turn_arrow_label2.config(image=turn_arrow)
                elif starter==2:
                    new_dice_player2=choice(list(dice.keys()))
                    _dice.config(text=new_dice_player2,image=dice[new_dice_player2])
                    _dice.update()
                    game_board.delete(player2_piece)
                    del_pic2_check=True
                    for _ in range(new_dice_player2):
                        h+=1
                        x_player2+=50
                    img_piece2=game_board.create_image(x_player2,y_player2,image=player_pieces[v2.get()])
                    starter='none'
                    turn=1
                    turn_arrow_label2.config(image=blank)
                    turn_arrow_label1.config(image=turn_arrow)
                elif starter=='none':
                    if turn==1:
                        last_check1=x_player1
                        new_dice_player1=choice(list(dice.keys()))
                        _dice.config(text=new_dice_player1,image=dice[new_dice_player1])
                        _dice.update()
                        check_move1=0
                        check_round_1=0
                        for _ in range(new_dice_player1):
                            check_round_1+=1
                            if y_player1==20:
                                for _ in range(new_dice_player1):
                                    last_check1-=50
                                if last_check1==25 and y_player1!=20 and x_player1!=25:
                                    x_player1=last_check1
                                    turn_arrow_label1.config(image=blank)
                                    turn_arrow_label2.config(image=blank)
                                    roll_dice.destroy()
                                    Label(win,text=f'{player1_name_get} Win!',font=('Yu Gothic UI Semilight',25),foreground='#ff1e1e').place(x=600,y=340)
                                    _dice.place(x=620,y=240)
                                    _dice.config(image=celebrate_pic)
                                    game_board.delete(img_piece1)
                                    img_piece1=game_board.create_image(x_player1,y_player1,image=player_pieces[v1.get()])
                                    break
                                if last_check1<25:
                                    new_dice_player1=0
                                    break
                            if check_move1==0:
                                if x_player1==475:
                                    if y_player1!=420 and y_player1!=320 and y_player1!=220 and y_player1!=120 and y_player1!=20:       
                                        y_player1-=50
                                        check_move1+=1
                                        for _ in range(new_dice_player1-check_move1):
                                            x_player1-=50
                                        break
                                    else:
                                        pass
                            if check_move1==0:
                                if x_player1==25:
                                    if y_player1==470 or y_player1==370 or y_player1==270 or y_player1==170 or y_player1==70:
                                        pass
                                    else:
                                        y_player1-=50
                                        check_move1+=1
                                        for _ in range(new_dice_player1-check_move1):
                                            x_player1+=50
                                        break
                            if x_player1==475:
                                if check_move1==new_dice_player1:
                                    break
                                elif y_player1==470 or y_player1==370 or y_player1==270 or y_player1==170 or y_player1==70:
                                    y_player1-=50
                                    check_move1+=1
                                    for _ in range(new_dice_player1-check_move1):
                                        x_player1-=50
                                    break 
                            if y_player1==470 or y_player1==370 or y_player1==270 or y_player1==170 or y_player1==70:
                                if x_player1!=25 and x_player1!=475 or check_round_1==1:
                                    x_player1+=50
                                    check_move1+=1
                                    continue
                            elif y_player1==420 or y_player1==320 or y_player1==220 or y_player1==120 or y_player1==20:
                                if x_player1!=25 and x_player1!=475 or check_round_1==1:
                                    x_player1-=50
                                    check_move1+=1
                                    continue
                            if x_player1==25:
                                if check_move1==new_dice_player1:
                                    break
                                elif y_player1==420 or y_player1==320 or y_player1==220 or y_player1==120 or y_player1==20:
                                    y_player1-=50
                                    check_move1+=1
                                    for _ in range(new_dice_player1-check_move1):
                                        x_player1+=50
                                    break 
                        if x_player1==375 and y_player1==220:
                            notif_pic1.config(image=danger)
                            x_player1=325
                            y_player1=370


                        if x_player1==325 and y_player1==70:
                            notif_pic1.config(image=danger)
                            x_player1=225
                            y_player1=120

                        if x_player1==75 and y_player1==20:
                            notif_pic1.config(image=danger)
                            x_player1=225
                            y_player1=220


                        if x_player1==475 and y_player1==320:
                            notif_pic1.config(image=danger)
                            x_player1=425
                            y_player1=420


                        if x_player1==25 and y_player1==120:
                            notif_pic1.config(image=danger)
                            x_player1=25
                            y_player1=220


                        if x_player1==175 and y_player1==270:
                            notif_pic1.config(image=danger)
                            x_player1=75
                            y_player1=420


                        if x_player1==175 and y_player1==370:
                            notif_pic1.config(image=up)
                            x_player1=275
                            y_player1=170


                        if x_player1==475 and y_player1==70:
                            notif_pic1.config(image=up)
                            x_player1=375
                            y_player1=20


                        if x_player1==375 and y_player1==470:
                            notif_pic1.config(image=up)
                            x_player1=375
                            y_player1=320

                
                        if x_player1==475 and y_player1==270:
                            notif_pic1.config(image=up)
                            x_player1=375
                            y_player1=120


                        if x_player1==125 and y_player1==320:
                            notif_pic1.config(image=up)
                            x_player1=75
                            y_player1=220


                            
                        if del_pic1_check==False:
                            game_board.delete(player1_piece)
                            del_pic1_check=True
                        else:
                            game_board.delete(img_piece1)
                        img_piece1=game_board.create_image(x_player1,y_player1,image=player_pieces[v1.get()])
                        turn=2
                        turn_arrow_label1.config(image=blank)
                        turn_arrow_label2.config(image=turn_arrow)
                        
                    elif turn==2:
                        last_check2=x_player2
                        new_dice_player2=choice(list(dice.keys()))
                        _dice.config(text=new_dice_player2,image=dice[new_dice_player2])
                        _dice.update()
                        check_move2=0
                        check_round_2=0
                        for _ in range(new_dice_player2):
                            if y_player2==20 :
                                for _ in range(new_dice_player2):
                                    last_check2-=50
                                if last_check2==25 and y_player1!=20 and x_player1!=25:
                                    x_player2=last_check2
                                    turn_arrow_label1.config(image=blank)
                                    turn_arrow_label2.config(image=blank)
                                    roll_dice.destroy()
                                    Label(win,text=f'{player2_name_get} Win!',font=('Yu Gothic UI Semilight',25),foreground='#ff1e1e').place(x=600,y=340)
                                    _dice.place(x=620,y=240)
                                    _dice.config(image=celebrate_pic)
                                    game_board.delete(img_piece2)
                                    img_piece2=game_board.create_image(x_player2,y_player2,image=player_pieces[v2.get()])
                                    break
                                if last_check2<25:
                                    new_dice_player2=0
                                    break
                            check_round_2+=1
                            if check_move2==0:
                                if x_player2==475:
                                    if y_player2!=420 and y_player2!=320 and y_player2!=220 and y_player2!=120 and y_player2!=20:       
                                        y_player2-=50
                                        check_move2+=1
                                        for _ in range(new_dice_player2-check_move2):
                                            x_player2-=50
                                        break
                                    else:
                                        pass
                            if check_move2==0:
                                if x_player2==25:
                                    if y_player2==470 or y_player2==370 or y_player2==270 or y_player2==170 or y_player2==70:
                                        pass
                                    else:
                                        y_player2-=50
                                        check_move2+=1
                                        for _ in range(new_dice_player2-check_move2):
                                            x_player2+=50
                                        break
                            if x_player2==475:
                                if check_move2==new_dice_player2:
                                    break
                                elif y_player2==470 or y_player2==370 or y_player2==270 or y_player2==170 or y_player2==70:
                                    y_player2-=50
                                    check_move2+=1
                                    for _ in range(new_dice_player2-check_move2):
                                        x_player2-=50
                                    break 
                            if y_player2==470 or y_player2==370 or y_player2==270 or y_player2==170 or y_player2==70:
                                if x_player2!=25 and x_player2!=475 or check_round_2==1:
                                    x_player2+=50
                                    check_move2+=1
                                    continue
                            elif y_player2==420 or y_player2==320 or y_player2==220 or y_player2==120 or y_player2==20:
                                if x_player2!=25 and x_player2!=475 or check_round_2==1:
                                    x_player2-=50
                                    check_move2+=1
                                    continue
                            if x_player2==25:
                                if check_move2==new_dice_player2:
                                    break
                                elif y_player2==420 or y_player2==320 or y_player2==220 or y_player2==120 or y_player2==20:
                                    y_player2-=50
                                    check_move2+=1
                                    for _ in range(new_dice_player2-check_move2):
                                        x_player2+=50
                                    break 
            

                        if x_player2==375 and y_player2==220:
                                notif_pic2.config(image=danger)
                                x_player2=325
                                y_player2=370

                        if x_player2==325 and y_player2==70:
                                notif_pic2.config(image=danger)
                                x_player2=225
                                y_player2=120

                        if x_player2==75 and y_player2==20:
                                notif_pic2.config(image=danger)
                                x_player2=225
                                y_player2=220

                        if x_player2==475 and y_player2==320:
                                notif_pic2.config(image=danger)
                                x_player2=425
                                y_player2=420

                        if x_player2==25 and y_player2==120:
                                notif_pic2.config(image=danger)
                                x_player2=25
                                y_player2=220

                        if x_player2==175 and y_player2==270:
                                notif_pic2.config(image=danger)
                                x_player2=75
                                y_player2=420

                        if x_player2==175 and y_player2==370:
                                notif_pic2.config(image=up)
                                x_player2=275
                                y_player2=170

                        if x_player2==475 and y_player2==70:
                                notif_pic2.config(image=up)
                                x_player2=375
                                y_player2=20                  

                        if x_player2==375 and y_player2==470:
                                notif_pic2.config(image=up)
                                x_player2=375
                                y_player2=320

                        if x_player2==475 and y_player2==270:
                                notif_pic2.config(image=up)
                                x_player2=375
                                y_player2=120

                        if x_player2==125 and y_player2==320:
                                notif_pic2.config(image=up)
                                x_player2=75
                                y_player2=220



                            

                        if del_pic2_check==False:
                                game_board.delete(player2_piece)
                                del_pic2_check=True
                        else:
                            game_board.delete(img_piece2)
                        img_piece2=game_board.create_image(x_player2,y_player2,image=player_pieces[v2.get()])
                        turn=1
                        turn_arrow_label2.config(image=blank)
                        turn_arrow_label1.config(image=turn_arrow)


            roll_dice=Button(win,text='ROLL THE DICE',bd=1,font=('Yu Gothic UI Semilight',12),command=roll_dice_func)
            roll_dice.place(x=605,y=410)

        set_turn_player2_btn=Button(win,text=f'{player2_name_get} ,roll dice for setting turn',font=('Yu Gothic UI Semilight',12),bd=1,command=set_turn_player2)
        set_turn_player2_btn.place(x=540,y=415)
        

    else:
        player_1_name.insert(0,'!!You have to enter your name!!')
        player_2_name.insert(0,'!!You have to enter your name!!')


def player1_info(name,piece):
    global player1_name_get
    # global check_1
    # check_1+=1
    a.destroy()
    player1_name_get=name
    player_1_name.destroy()
    player_1_blue.destroy()
    player_1_red.destroy()
    player_1_green.destroy()
    player_1_yellow.destroy()
    player1_name.config(text=name)
    Label(win,image=player_pieces[piece]).place(x=680,y=130)
    confirm1.destroy()



def player2_info(name,piece):
    global player2_name_get
    # global check_2
    # check_2+=1
    b.destroy()
    player2_name_get=name
    player_2_name.destroy()
    player_2_blue.destroy()
    player_2_red.destroy()
    player_2_green.destroy()
    player_2_yellow.destroy()
    player2_name.config(text=name)
    Label(win,image=player_pieces[piece]).place(x=680,y=500)
    confirm2.destroy()



for j in range(10):
    for i in range(10):
        color=choice(colors)
        game_board.create_rectangle(i*50,j*50,(i+1)*50,(j+1)*50, fill=color)
for i in reversed(range(1,101)):
    if i>=91:
        if i ==100:
            x=25
        game_board.create_text(x,25,text=i,font=('Yu Gothic UI Semilight',14))
        x+=50
    elif 91>i>=81:
        if i ==90:
            x=475
        game_board.create_text(x,75,text=i,font=('Yu Gothic UI Semilight',14))
        x-=50
    elif 81>i>=71:
        if i ==80:
            x=25
        game_board.create_text(x,125,text=i,font=('Yu Gothic UI Semilight',14))
        x+=50
    elif 71>i>=61:
        if i ==70:
            x=475
        game_board.create_text(x,175,text=i,font=('Yu Gothic UI Semilight',14))
        x-=50
    elif 61>i>=51:
        if i ==60:
            x=25
        game_board.create_text(x,225,text=i,font=('Yu Gothic UI Semilight',14))
        x+=50
    elif 51>i>=41:
        if i ==50:
            x=475
        game_board.create_text(x,275,text=i,font=('Yu Gothic UI Semilight',14))
        x-=50
    elif 41>i>=31:
        if i ==40:
            x=25
        game_board.create_text(x,325,text=i,font=('Yu Gothic UI Semilight',14))
        x+=50
    elif 31>i>=21:
        if i ==30:
            x=475
        game_board.create_text(x,375,text=i,font=('Yu Gothic UI Semilight',14))
        x-=50
    elif 21>i>=11:
        if i ==20:
            x=25
        game_board.create_text(x,425,text=i,font=('Yu Gothic UI Semilight',14))
        x+=50
    elif 11>i:
        if i ==10:
            x=475
        game_board.create_text(x,475,text=i,font=('Yu Gothic UI Semilight',14))
        x-=50
logo_label=PhotoImage(file='image\snakeladderslogo.png')
logo=Label(win,image=logo_label)
logo.place(x=570,y=238)



player1_name=Label(win,text='',font=('Yu Gothic UI Semilight',19))
player1_name.place(x=582,y=130)
player2_name=Label(win,text='',font=('Yu Gothic UI Semilight',19))
player2_name.place(x=582,y=500)
a=Label(win,text='Player name 1',bd=1,font=('Yu Gothic UI Semilight',14),foreground='#e73485')
a.place(x=603,y=100)
player_1_name=Entry(win,bd=1,font=('Yu Gothic UI Semilight',10),width=29,bg='#f9bddc')
player_1_name.place(x=562,y=128)
v1=StringVar()
v1.set('blue')
player_1_blue=Radiobutton(win,image=blue_choice_pic,variable=v1,value='blue')
player_1_blue.place(x=563,y=160)
player_1_red=Radiobutton(win,image=red_choice_pic,variable=v1,value='red')
player_1_red.place(x=613,y=160)
player_1_green=Radiobutton(win,image=green_choice_pic,variable=v1,value='green')
player_1_green.place(x=663,y=160)
player_1_yellow=Radiobutton(win,image=yellow_choice_pic,variable=v1,value='yellow')
player_1_yellow.place(x=713,y=160)
confirm1=Button(win,text='confirm',font=('Yu Gothic UI Semilight',10),bd=1,command=lambda:player1_info(player_1_name.get(),v1.get()))
confirm1.place(x=638,y=200)

b=Label(win,text='Player name 2',bd=1,font=('Yu Gothic UI Semilight',14),foreground='#313131')
b.place(x=603,y=458)
player_2_name=Entry(win,bd=1,font=('Yu Gothic UI Semilight',10),width=29,bg='#A9A9A9')
player_2_name.place(x=562,y=485)

v2=StringVar()
v2.set('red')
player_2_blue=Radiobutton(win,image=blue_choice_pic,variable=v2,value='blue')
player_2_blue.place(x=563,y=518)
player_2_red=Radiobutton(win,image=red_choice_pic,variable=v2,value='red')
player_2_red.place(x=613,y=518)
player_2_green=Radiobutton(win,image=green_choice_pic,variable=v2,value='green')
player_2_green.place(x=663,y=518)
player_2_yellow=Radiobutton(win,image=yellow_choice_pic,variable=v2,value='yellow')
player_2_yellow.place(x=713,y=518)
confirm2=Button(win,text='confirm',font=('Yu Gothic UI Semilight',10),bd=1,command=lambda:player2_info(player_2_name.get(),v2.get()))
confirm2.place(x=638,y=558)



set_the_turn_btn=Button(win,text='set the turn',font=('Yu Gothic UI Semilight',14),bd=0,command=set_the_turn)
set_the_turn_btn.pack(anchor=NE)

ladder1_pic=PhotoImage(file='image\ladder1.png')
ladder1=game_board.create_image(222,273,image=ladder1_pic)

ladder2_pic=PhotoImage(file='image\ladder2.png')
ladder2=game_board.create_image(425,45,image=ladder2_pic)

ladder3_pic=PhotoImage(file='image\ladder3.png')
ladder3=game_board.create_image(337,420,image=ladder3_pic)

ladder4_pic=PhotoImage(file='image\ladder4.png')
ladder4=game_board.create_image(424,190,image=ladder4_pic)

# ladder5_pic=PhotoImage(file='image\ladder5.png')
# ladder5=game_board.create_image(125,88,image=ladder5_pic)

ladder6_pic=PhotoImage(file='image\ladder6.png')
ladder6=game_board.create_image(70,282,image=ladder6_pic)

snake1_pic=PhotoImage(file='image\snake1img_prev_ui.png')
snake1=game_board.create_image(330,300,image=snake1_pic)

snake2_pic=PhotoImage(file='image\snake2.png')
snake2=game_board.create_image(275,100,image=snake2_pic)

snake3_pic=PhotoImage(file='image\snake_prev_ui (1).png')
snake3=game_board.create_image(150,130,image=snake3_pic)

snake4_pic=PhotoImage(file='image\snake4.png')
snake4=game_board.create_image(458,370,image=snake4_pic)

snake5_pic=PhotoImage(file='image\snake5.png')
snake5=game_board.create_image(40,168,image=snake5_pic)

snake6_pic=PhotoImage(file='image\snake6_prev_ui.png')
snake6=game_board.create_image(125,350,image=snake6_pic)

# game_board.create_image(525,470,image=blank)



win.mainloop()

