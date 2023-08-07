#COMPUTER SCIENCE SUMMER PROJECT.
#PARADISE TRAVEL AND TOURISM.


import turtle 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font 
import math
import random
import PIL.Image
import PIL.ImageTk
import time
import mysql.connector as mys
import smtplib, ssl



def screen(): #Welcome Screen.
    screen = turtle.Screen()
    screen.setup(1200,1050)
    screen.bgpic(r'C:\Users\dalal\OneDrive\Documents\project pics\londonn.gif')
    screen.update()
    time.sleep(3)
    screen.bgpic(r'C:\Users\dalal\OneDrive\Documents\project pics\ny6.gif')
    screen.update()
    time.sleep(3)
    screen.bgpic(r'C:\Users\dalal\OneDrive\Documents\project pics\paris2.gif')

    turtle.color("yellow")
    style = ('Segoe Script', 40, 'bold')
    style2 = ('Segoe Script', 20, 'bold')
    turtle.write('PARADISE TRAVEL\n    & TOURISM\n', font=style, align='center')
    turtle.write('\n', font=style, align='center')
    turtle.write('By Riday Dalal', font = style2, align = 'right')
    turtle.hideturtle()
    turtle.exitonclick()    

screen()




def display():
    
    try:
        myconn=mys.connect(host='localhost', user='root', passwd='adis', database='travel')
        if myconn.is_connected():
            #print("Connection Established Successfully !")
            print()
        mycur=myconn.cursor()
        query='select * from travel_booking;'
        mycur.execute(query)
        rs=mycur.fetchall()
        #count=mycur.rowcount
        print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('NAME', 'MOBILE', 'PASSPORT', 'CITY', 'HOTEL', 'FLIGHT', 'AMOUNT'))
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
        for i in rs:
            print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
        #print("The no. of rows is \t", count)
        
    except Exception as e:
        print(e)
    
    
    '''
    print("NAME\t\t\tMOBILE NUMBER\t   PASSPORT NUMBER\t\tCITY\t\t\tHOTEL\t\t\t\tFLIGHT")
    for i in customer:
    #print(customer)
         print(i, customer[i][0], customer[i][1], customer[i][2], customer[i][3], customer[i][4], sep='\t\t')
    '''


def fnupdate():
    
    global some_variable
    some_variable = 0
    
    def fnsubmit2():
        
        global customer
        fncountry()
        
        
    def fnalert():
        
        global a
        global n
        global l
        
    
        a=txtNAME.get()
        n=txtnewpassno.get()
        l=txtnewmobno.get()
        
        
        fncountry()
           
        #query="update travel_booking set a={}, l={}, n='{}', country = '{}', hotel = '{}', flight = '{}' where NAME={}".format(a, l, n, country, hotel, flight)
        #mycur.execute(query)
        #myconn.commit()
        #display()
                        
        #messagebox.showinfo("Message", "Dear Customer, your credentials have been successfully updated.")
        #display()
            
    root7=tk.Toplevel()
    root7.geometry("1100x900")
    root7.title("UPDATE DETAILS")
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\countryside.png')
    photo=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\countryside.png')
    imagelabel=tk.Label(root7, image=photo)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

    lblhead = tk.Label(root7, text="Update Details.", fg='blue', bg='#CCFFFF', font=('Sergoe Script Bold',28,'bold'))
    lblhead.place(x=300, y=20)
    
    lblNAME = tk.Label(root7, text ="NAME",fg='blue', bg='#CCFFFF', font=("Segoe Script", 20) )
    lblNAME.place(x = 50, y = 150)
    global txtNAME
    txtNAME = tk.Entry(root7, width = 100,fg="blue",font=('Times New Roman', 20))
    txtNAME.place(x = 550, y = 150, width = 450)
    global m
    
    lblnewmobno = tk.Label(root7, text ="MOBILE NUMBER",fg='blue', bg='#CCFFFF',font=("Segoe Script", 20))
    lblnewmobno.place(x = 50, y = 350)
    txtnewmobno = tk.Entry(root7, width = 100, fg="blue", font=('Times New Roman', 20))
    txtnewmobno.place(x = 550, y = 350, width = 450)
    global l
    
    lblnewpassno = tk.Label(root7, text ="PASSPORT NUMBER",fg='blue', bg='#CCFFFF',font=("Segoe Script", 20))
    lblnewpassno.place(x = 50, y = 250)
    txtnewpassno = tk.Entry(root7,width = 100,fg="blue",font=('Times New Roman', 20))
    txtnewpassno.place(x = 550, y = 250, width = 450)
    global n
    
    
    lblemailid = tk.Label(root7, text ="EMAIL ID",bg = '#CCFFFF', fg ='blue',font=("Segoe Script", 20) )
    lblemailid.place(x = 50, y = 450)
    global txtemailid
    txtemailid = tk.Entry(root7, width = 60,fg ='blue',font=("Times New Roman", 20))
    txtemailid.place(x = 550, y = 450, width = 450)
    
    #btnnewcountry = tk.Button(root7, text ="NEW PACKAGE",fg='blue', bg='#CCFFFF',font=("Segoe Script", 10), command=fnsubmit2)
    #btnnewcountry.place(x = 50, y = 400)
    
    btnupdatedetails = tk.Button(root7, text ="PROCEED",fg='blue', bg='#CCFFFF',font=("Segoe Script", 15), command=fnalert)
    btnupdatedetails.place(x = 500, y = 750)
    
    root7.mainloop()
    
    
            
def fnemployee(): #Employee Login 
    
    def fnlogin():
        global password
        global username
        password = txtpass.get()
        username = txtUser.get()
        if username == 'Paradise' and password == '42069':
            
            messagebox.showinfo("Message", "Login Successful!")
            root5.destroy()
            display()
            
            #if customer != {}:
             #   display()
            
            #else:
             #   messagebox.showinfo("ALERT", "Nothing to display!")
                
        else:
            messagebox.showinfo("Message", "Invaild Login Credentials. Please try again!")
    
    #Design of Login Page
            
    root5 = tk.Toplevel()
    root5.geometry("770x600")
    root5.configure(bg='green')
    root5.title("LOGIN PAGE")
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\lock.png')
    photo=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\lock.png')
    imagelabel=tk.Label(root5, image=photo)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

    
    lblmenu = tk.Label(root5, text ="EMPLOYEE LOGIN", bg='#FF6666', fg = 'yellow', font=('Sergoe Script Bold',28,'bold'))
    lblmenu.place(x = 150, y = 20)
    
    lbluser = tk.Label(root5, text ="EMPLOYEE ID",bg='#FF6666', fg="yellow",font=("Segoe Script", 20) )
    lbluser.place(x = 50, y = 200)
    txtUser = tk.Entry(root5, width = 200, fg="blue",font=("Times New Roman", 20))
    txtUser.place(x = 400, y = 200, width = 200)
    
    lblpass = tk.Label(root5, text ="PASSWORD", bg='#FF6666', fg="yellow",font=("Segoe Script", 20))
    lblpass.place(x = 50, y = 300)
    txtpass = tk.Entry(root5,show="*", width = 200, fg="blue",font=("Times New Roman", 20))
    txtpass.place(x = 400, y = 300, width = 200)
    
    loginbtn = tk.Button(root5, text ="Login", bg='#FF6666', fg ='yellow', font=("Segoe Script", 20), command = fnlogin)
    loginbtn.place(x = 300, y = 400, width = 200)
    
    root5.mainloop()
  
      

                
def fnsearch():
    try:
        myconn=mys.connect(host='localhost', user='root', passwd='adis', database='travel')
        if myconn.is_connected():
            print()
            #print("Connection Established Successfully !")
        mycur=myconn.cursor()
        query='select * from travel_booking;'
        mycur.execute(query)
        rs=mycur.fetchall()
        #count=mycur.rowcount
        print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15}".format('NAME', 'MOBILE', 'PASSPORT', 'CITY', 'HOTEL', 'FLIGHT' ))
        print("-----------------------------------------------------------------------------------------------------------------")
        for i in rs:
            if txtname.get() == i[0] or txtmobno.get() == i[1] or txtpassno.get() == i[2]:
                print ("{:<25} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print()
        print("-----------------------------------------------------------------------------------------------------------------")
        #print("The no. of rows is \t", count)
        
    
    except Exception as e:
        print(e)
        
        
        
        
        
            
def fndelete():
    
    x=messagebox.askyesno("ALERT!", "Are you sure you want to cancel this booking?")
    
    if x == True:
        myconn=mys.connect(host='localhost', user='root', passwd='adis', database='travel')
        if myconn.is_connected():
            print()
            #print("Connection Established Successfully !")
        mycur = myconn.cursor()
        you_are_fired = txtname.get()
        
        if you_are_fired == '':
            
            messagebox.showinfo("ALERT!", "Enter the name of the record you want to delete!")
            
        else:
            
            query='select * from travel_booking;'
            mycur.execute(query)
            rs=mycur.fetchall()
            
            for i in rs:
                
                if you_are_fired == i[0]:
            
                    query="delete from travel_booking where NAME='{}'".format(you_are_fired)
                    mycur.execute(query)
                    myconn.commit()
                    display()
                    messagebox.showinfo("Message", "Dear Customer, your record has been successfully deleted.")
                    break
            
            else:
                messagebox.showinfo("ALERT!", "There is no such record in the database!")
            
            
            #del customer[full_name]
            
        
    else:
        messagebox.showinfo("ALERT", "Invalid Credentials. Please try again!")
    
    
    
def menu(): #Main Menu
    
    def fnsubmit():
        global full_name
        global mobno
        global passno
        global list2
        list2=[]
        full_name = txtname.get()
        mobno = txtmobno.get()
        passno = txtpassno.get()
        
        if full_name == '' or mobno == '' or passno == '':
            msg = messagebox.askyesno("ALERT", "All the details have not been entered. Do you want to search for this record on the database?")
            if msg:
                fnsearch()
                
            else:
                messagebox.showinfo("ALERT", "Dear Customer, please enter the complete credentials.")
            
            
        else:
            list2.extend([full_name, mobno, passno])
            messagebox.showinfo("Message", "Dear Customer, your credentials have been successfully submitted.")
        
        #except NameError:
        #    messagebox.showinfo("ALERT", "Dear Customer, please enter the complete credentials.")
    
    
    def fnback():
        root.destroy()
        fnprojectmenu()
    
    
    
    def fncheck():
        try:
            if full_name == '' or mobno == '' or passno == '':
                messagebox.showinfo("ALERT", "Dear Customer, please enter the complete credentials.")
        
            else:
                fncountry()
                
        except NameError:
            messagebox.showinfo("ALERT", "Dear Customer, please enter the complete credentials.")
        
       
        
    # Design of the main menu
    
    root6.destroy()
    
    
    root=tk.Tk()
    root.geometry("1000x900")
    root.title("MAIN MENU")
    global photo
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\rr.png')
    photo=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\rr.png')
    imagelabel=tk.Label(root, image=photo)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblmenu = tk.Label(root, text ="MAIN MENU", bg='#52522E', fg = 'light green', font=('Segoe Script Bold',28,'bold'))
    lblmenu.place(x = 300, y = 20)
    
    lblname = tk.Label(root, text ="NAME",bg = '#52522E', fg ='light green',font=("Segoe Script", 20) )
    lblname.place(x = 50, y = 200)
    global txtname
    txtname = tk.Entry(root, width = 60,fg ='black',font=('Times New Roman', 20))
    txtname.place(x = 550, y = 200, width = 400)
    
    lblmobno = tk.Label(root, text ="MOBILE NUMBER",bg = '#52522E', fg ='light green',font=("Segoe Script", 20))
    lblmobno.place(x = 50, y = 300)
    global txtmobno
    txtmobno = tk.Entry(root, width = 60,fg ='black',font=("Times New Roman", 20))
    txtmobno.place(x = 550, y = 300, width = 400)
    
    
    lblpassno = tk.Label(root, text ="PASSPORT NUMBER",bg = '#52522E', fg ='light green',font=("Segoe Script", 20) )
    lblpassno.place(x = 50, y = 400)
    global txtpassno
    txtpassno= tk.Entry(root, width = 60,fg ='black',font=("Times New Roman", 20))
    txtpassno.place(x = 550, y = 400, width = 400)
    
    lblemailid = tk.Label(root, text ="EMAIL ID",bg = '#52522E', fg ='light green',font=("Segoe Script", 20) )
    lblemailid.place(x = 50, y = 500)
    global txtemailid
    txtemailid = tk.Entry(root, width = 60,fg ='black',font=("Times New Roman", 20))
    txtemailid.place(x = 550, y = 500, width = 400)
    
    btnsubmit=tk.Button(root, text ="SUBMIT", bg = '#52522E', fg ='light green',font=("Times New Roman Bold", 10), command=fnsubmit)
    btnsubmit.place(x = 100, y = 600, width = 100)
    
    btnupdate=tk.Button(root, text ="UPDATE", bg = '#52522E', fg ='light green',font=("Times New Roman Bold", 10), command=fnupdate)
    btnupdate.place(x = 400, y = 600, width = 100)
    #btnupdate.place(x = 300, y = 600, width = 100)
    
    
    btninsert = tk.Button(root, text ="--->", bg = '#52522E', fg ='light green',font=("Segoe Script", 10), command=fncheck)
    btninsert.place(x = 800, y = 700, width = 100)
    
    btndelete = tk.Button(root, text ="DELETE", bg = '#52522E', fg ='light green',font=("Times New Roman Bold", 10), command=fndelete)
    btndelete.place(x = 700, y = 600, width = 100)
    
    #btnsearch = tk.Button(root, text ="SEARCH", bg = '#52522E', fg ='light green',font=("Times New Roman Bold", 10), command=fnsearch)
    #btnsearch.place(x = 500, y = 700, width = 100)
    
    btnback = tk.Button(root, text ="<---", bg = '#52522E', fg ='light green',font=("Segoe Script", 10), command=fnback)
    btnback.place(x = 100, y = 700, width = 100)
    
    #btndisplay = tk.Button(root, text='DISPLAY', bg = '#52522E', fg ='light green',font=("Times New Roman Bold", 10), command=display)
    #btndisplay.place(x = 500, y = 600, width = 100)
    


      
def fnflight(): #Flight Selection 
    
    
    def T1():
        global flight_time
        flight_time = '00.15'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
        
    def T2():
        global flight_time
        flight_time = '04.00'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
        
    def T3():
        global flight_time
        flight_time = '09.45'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
    
    def T4():
        global flight_time
        flight_time = '13.30'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
        
    def T5():
        global flight_time
        flight_time = '17.55'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
    
    def T6():
        global flight_time
        flight_time = '21.15'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)
    
    def T7():
        global flight_time
        flight_time = '23.00'
        
        if flight == 'Air India':
            
            string = "Dear Customer, you have chosen Air India as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
            messagebox.showinfo("Message", string)
            
        elif flight == 'Etihad':
            
            string = "Dear Customer, you have chosen Etihad as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2500 Dhs"
            messagebox.showinfo("Message", string)

        elif flight == 'Emirates':
            
            string = "Dear Customer, you have chosen Emirates as your flight.\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
            messagebox.showinfo("Message", string)

    
    
    def AI():
        global flight
        global FLIGHT_
        global p
        global cost
        #global flight_time
        p=str(random.randrange(1000,9999))
        FLIGHT_='AI '+ p
        flight = 'Air India'                     #'Air India (2000 Dhs)'
        cost += 2000
        #string = "Dear Customer, you have chosen Air India as your flight.\nFlight number is : AI " + p + "\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 2000 Dhs"
        list2.append(FLIGHT_)
        if len(list3) > 4:
            del list3[4]
        list3.append(flight)
        #messagebox.showinfo("Message", string)
   
    def EK():
        global flight
        global FLIGHT_
        global p
        global cost
        #global flight_time
        p=str(random.randrange(1000,9999))
        FLIGHT_='EK ' + p
        flight = 'Emirates'                #'Emirates (3000 Dhs)'
        cost +=  3000
        list2.append(FLIGHT_)
        #string = "Dear Customer, you have chosen Emirates as your flight.\nFlight number is : EK " + p + "\nTime of Departure : " + flight_time + "\nSeat : Economy Class\nRate : 3000 Dhs"
        if len(list3) > 4:
            del list3[4]
        list3.append(flight)
        #messagebox.showinfo("Message", string)
   
    def EY():
        global flight
        global FLIGHT_
        global p
        global cost
        #global flight_time
        p=str(random.randrange(1000,9999))
        FLIGHT_='EY '+ p
        flight = 'Etihad'                               #'Etihad (2500 Dhs)'
        cost += 2500
        list2.append(FLIGHT_)
        #string = "Dear Customer, you have chosen Etihad Airways as your flight.\nFlight number is : EY " + p + "\nTime of Departure : 00.15\nSeat : Economy Class\nRate : 2500 Dhs"
        if len(list3) > 4:
            del list3[4]
        list3.append(flight)
        #messagebox.showinfo("Message", string)
        
    
    
    def fnnext3(): #Conclusion of Booking.
        
        if flight == 'Etihad' or flight == 'Emirates' or flight == 'Air India':
            
            global list2
            global flight_time
            global list4
            #global flight
            global customer_update
            global txtemailid
            #global some_variable
            global a
            global n
            global l
            global cost
            global previous_mobile
            global start
            global end
            global room
            root2.destroy()
            list4=list2.copy()
            #dept = txt_departure.get()
            #print(some_variable)
            #print(a,n,l)
            list_updated = []
            
            try:
                if some_variable == 0:
                
                    list_updated.extend([a,l,n])
                    list_updated.extend([list2[0], list2[1], list2[2], cost])
                    list4 = list_updated.copy()
                    print(list4)       
                    
                                   
                    myconn=mys.connect(host='localhost', user='root', passwd='adis', database='travel')
                    if myconn.is_connected():
                        print()
                    mycur=myconn.cursor()
                
                    NAME, MOBILE, PASSPORT, CITY, HOTEL, FLIGHT, AMOUNT = list4[0], list4[1], list4[2], list4[3], list4[4], list4[5], list4[6] 
                
                    query="update travel_booking set MOBILE ='{}', PASSPORT ='{}', CITY = '{}', HOTEL = '{}', FLIGHT = '{}', AMOUNT = '{}' where NAME ='{}'".format(list4[1], list4[2], list4[3], list4[4], list4[5], list4[6], list4[0])
                    mycur.execute(query)
                    myconn.commit()
                    
                    
                    
                    port = 465
                    password = "fgcvvnpsvsktargn"
                    #password = "Ariyd0106&&&" #APP PASSSWORD (CHANGE EVERY TIME)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                        server.login("info.paradise.travels2021@gmail.com", password)

                    port = 465
                    smtp_server = "smtp.gmail.com"
                    sender_email = "info.paradise.travels2021@gmail.com"  #sender's address
                    receiver_email = txtemailid.get()  # receiver address
                
                    message1 = "from: Paradise Travel & Tourism\nto: " + receiver_email + "\nsubject: UPDATED TRAVEL BOOKING DETAILS"
                
                    message2 = """\nDear Customer,\n\nThank you for booking your holiday with Paradise Travel & Tourism. Your details have been successfully updated and are mentioned below in this email.\nContact us on info.paradise.travels2021@gmail.com in case you have any queries or face any problems.\n"""
                
                    message3 = "\nFULL NAME: " + list4[0] + "\nMOBILE NUMBER: " + list4[1] + "\nPASSPORT NUMBER: " + list4[2] + "\nCITY TO VISIT: " + list4[3] + "\nHOTEL: " + list4[4] + "\nCHECK-IN: " + start + "\nCHECK-OUT: " + end + "\nROOM: " + room + "\nFLIGHT: " + list4[5] + "\nTOTAL AMOUNT: " + str(cost) + "Dhs"
                
                    message4 = "\n\nWe hope you enjoy your trip to the fullest!\nWill Watson\nParadise Travel & Tourism"
                
                    message = message1 + "\n\n" + message2 + "\n" + message3 + message4
                
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                    
                    
                
                    messagebox.showinfo("Message", "Dear Customer, your credentials have been successfully updated.")
                    display()
                       
                    #some_variable = 1
            
                    #print(list4, list_updated)
            
            
            
            
            except NameError:
                
                list4.append(cost)
                myconn=mys.connect(host='localhost', user='root', passwd='adis', database='travel')
                if myconn.is_connected():
                    print()
                    #print("Connection Established Successfully !")
                
                mycur=myconn.cursor()
            
            
                NAME, MOBILE, PASSPORT, CITY, HOTEL, FLIGHT, AMOUNT = list4[0], list4[1], list4[2], list4[3], list4[4], list4[5] , list4[6]
            
            
                query=f"insert into travel_booking values('{NAME}', '{MOBILE}', '{PASSPORT}', '{CITY}', '{HOTEL}', '{FLIGHT}', '{AMOUNT}')"
                mycur.execute(query)
                myconn.commit()

                #customer[full_name] = list4
                #customer_update=customer.copy()
            
                messagebox.showinfo("Message","Dear Customer, thank you for booking your trip with Paradise Travel and Tourism.\nYour booking details have been sent to you on your email ID.\nFor further queries, contact us on 0502356126\nEmail us on info.paradise.travels2021@gmail.com\n\nENJOY YOUR TRIP!!")
                
                '''
                port = 535  # For SSL
                password = "Paradise//" #input("Type your password and press enter: ")
                # Create a secure SSL context
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login("info.paradise.travels2021@gmail.com", password)
                '''
                
                print(txtemailid.get())
                
                port = 465
                #port = 535
                password = "fgcvvnpsvsktargn"
                #password = "Ariyd0106&&&" # APP PASSSWORD (CHANGE EVERY TIME)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login("info.paradise.travels2021@gmail.com", password)

                port = 465
                #port = 535
                smtp_server = "smtp.gmail.com"
                sender_email = "info.paradise.travels2021@gmail.com"  #sender's address
                receiver_email = txtemailid.get()  # receiver address
                
                message1 = "from: Paradise Travel & Tourism\nto: " + receiver_email + "\nsubject: TRAVEL BOOKING DETAILS"
                
                message2 = """\nDear Customer,\n\nThank you for booking your holiday with Paradise Travel & Tourism. The details of your booking are mentioned below in this email.\nContact us on info.paradise.travels2021@gmail.com in case you have any queries or face any problems.\n"""
                
                message3 = "\nFULL NAME: " + list4[0] + "\nMOBILE NUMBER: " + list4[1] + "\nPASSPORT NUMBER: " + list4[2] + "\nCITY TO VISIT: " + list4[3] + "\nHOTEL: " + list4[4] + "\nCHECK-IN: " + start + "\nCHECK-OUT: " + end + "\nROOM: " + room + "\nFLIGHT: " + list4[5] + "\nTOTAL AMOUNT: " + str(cost) + "Dhs"
                
                message4 = "\n\nWe hope you enjoy your trip to the fullest!\nWill Watson\nParadise Travel & Tourism"
                
                message = message1 + "\n\n" + message2 + "\n" + message3 + message4
                
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                
                list2.clear()
                
                
        
            
            
            # Boarding Pass.
            
            global photo10
            root10=tk.Toplevel()
            root10.geometry('1400x600')
            pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\BPASS.png')
            photo10=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\BPASS.png')
            imagelabel=tk.Label(root10, image=photo10)
            imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

            y1=list4[0]
            y=str(y1)
            
            lblName = tk.Label(root10, text=y, bg='white', font=('Times New Roman',15))
            lblName.place(x=180, y=230)
            lblName2 = tk.Label(root10, text=y, bg='white', font=('Times New Roman',10))
            lblName2.place(x=1080, y=180)
            
            
            z1 = start #txt_departure.get()
            #str(random.randrange(1,32))+'/'+str(random.randrange(1,13))+'/'+'2021'
            
            z = str(z1)
            lbldate = tk.Label(root10, text=z, bg='white', font=('Times New Roman',15))
            lbldate.place(x=580, y=230)
            lbldate2 = tk.Label(root10, text=z, bg='white', font=('Times New Roman',10))
            lbldate2.place(x=1070, y=298)
            
            
            if FLIGHT_ == 'AI '+ p:
                x=flight_time
                lbltime = tk.Label(root10, text=x, bg='white', font=('Times New Roman',15))
                lbltime.place(x=780, y=230)
                lbltime2 = tk.Label(root10, text=x, bg='white', font=('Times New Roman',10))
                lbltime2.place(x=1245, y=298)
                
                t='Abu Dhabi'
                lblC = tk.Label(root10, text=t, bg='white', font=('Times New Roman',15))
                lblC.place(x=180, y=330)
                lblC2 = tk.Label(root10, text=t, bg='white', font=('Times New Roman',10))
                lblC2.place(x=1080, y=223)
                
                lblName = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',15))
                lblName.place(x=580, y=440)
                lblName2 = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',10))
                lblName2.place(x=1080, y=445)
                
            elif FLIGHT_ == 'EK '+ p:
                x=flight_time
                lbltime = tk.Label(root10, text=x, bg='white', font=('Times New Roman',15))
                lbltime.place(x=780, y=230)
                lbltime2 = tk.Label(root10, text=x, bg='white', font=('Times New Roman',10))
                lbltime2.place(x=1245, y=298)
                
                t='Dubai'
                lblC = tk.Label(root10, text=t, bg='white', font=('Times New Roman',15))
                lblC.place(x=180, y=330)
                lblC2 = tk.Label(root10, text=t, bg='white', font=('Times New Roman',10))
                lblC2.place(x=1080, y=223)
                
                lblName = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',15))
                lblName.place(x=580, y=440)
                lblName2 = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',10))
                lblName2.place(x=1080, y=445)
                
            elif FLIGHT_ == 'EY '+ p:
                
                x=flight_time
                lbltime = tk.Label(root10, text=x, bg='white', font=('Times New Roman',15))
                lbltime.place(x=780, y=230)
                lbltime2 = tk.Label(root10, text=x, bg='white', font=('Times New Roman',10))
                lbltime2.place(x=1245, y=298)
                
                t='Abu Dhabi'
                lblC = tk.Label(root10, text=t, bg='white', font=('Times New Roman',15))
                lblC.place(x=180, y=330)
                lblC2 = tk.Label(root10, text=t, bg='white', font=('Times New Roman',10))
                lblC2.place(x=1080, y=223)
                
                lblName = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',15))
                lblName.place(x=580, y=440)
                lblName2 = tk.Label(root10, text=FLIGHT, bg='white', font=('Times New Roman',10))
                lblName2.place(x=1080, y=445)
                
            
            w1=str(random.randrange(1,9))
            lblgate = tk.Label(root10, text=w1, bg='white', font=('Times New Roman',15))
            lblgate.place(x=580, y=330)
            lblgate2 = tk.Label(root10, text=w1, bg='white', font=('Times New Roman',10))
            lblgate2.place(x=1080, y=376)
            
            u=str(chr(random.randrange(65,76))) + ' ' + str(random.randrange(1,10))
            lblseat = tk.Label(root10, text=u, bg='white', font=('Times New Roman',15))
            lblseat.place(x=780, y=330)#x=1245, y=376
            lblseat2 = tk.Label(root10, text=u, bg='white', font=('Times New Roman',10))
            lblseat2.place(x=1245, y=376)
            
            t=str(country)
            lblcountry = tk.Label(root10, text=t, bg='white', font=('Times New Roman',15))
            lblcountry.place(x=180, y=440)
            lblcountry = tk.Label(root10, text=t, bg='white', font=('Times New Roman',10))
            lblcountry.place(x=1080, y=256)
        
        else:
            messagebox.showinfo("ALERT", "Please select one of the options.")
            
            
    # Design of flight selection page.
    
    root2=tk.Toplevel()
    root2.geometry("1700x800")
    #root2.title("FLIGHT SELECTION")
    
    global photo2
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\Emirates.png')
    photo2=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\Emirates.png')
    imagelabel=tk.Label(root2, image=photo2)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblhead = tk.Label(root2, text="Select your flight.", bg='light green', font=('Sergoe Script Bold',28,'bold'))
    lblhead.place(x=120, y=20)
    
    btnAI = tk.Button(root2, text='Air India', width = 20, bg='light green', fg ='brown', font=("Segoe Script", 20), command=AI)
    btnAI.place(x=100, y=100)
    
    btnEM = tk.Button(root2, text='Emirates', width = 20, bg='light green', fg = 'brown', font=("Segoe Script", 20), command=EK)
    btnEM.place(x=100, y=250)
    
    btnET = tk.Button(root2, text='Etihad', width = 20, bg='light green', fg ='brown',font=("Segoe Script", 20), command=EY) 
    btnET.place(x=100, y = 400)
    
    btnnext = tk.Button(root2, text='FINISH', width = 10, bg='light green', fg='brown', font=("Segoe Script", 10), command=fnnext3)
    btnnext.place(x=1500, y=650)
    
    global txt_departure
    lbl_departure = tk.Label(root2, text="Departure Date", bg='light green', font=('Sergoe Script Bold',15,'bold'))
    lbl_departure.place(x=900, y=20)
    txt_departure = tk.Entry(root2, bg='light green', font=('Sergoe Script Bold',15,'bold'))
    txt_departure.place(x=1200, y=20)
    #txt_departure.get()
    
    
    #global txt_arrival
    lbl_arrival = tk.Label(root2, text="Arrival Date", bg='light green', font=('Sergoe Script Bold',15,'bold'))
    lbl_arrival.place(x=900, y=120)
    txt_arrival = tk.Entry(root2, bg='light green', font=('Sergoe Script Bold',15,'bold'))
    txt_arrival.place(x=1200, y=120)
    
    
    lbl_time = tk.Label(root2, text="Select a flight time", bg='light green', font=('Sergoe Script Bold',15,'bold'))
    lbl_time.place(x=900, y=220)
    
    # Flight Timings
    
    btn1 = tk.Button(root2, text='00.15', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T1)
    btn1.place(x=900, y=320)
    btn2 = tk.Button(root2, text='04.00', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T2)
    btn2.place(x=1000, y=320)
    btn3 = tk.Button(root2, text='09.45', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T3)
    btn3.place(x=1100, y=320)
    btn4 = tk.Button(root2, text='13.30', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T4)
    btn4.place(x=1200, y=320)
    btn5 = tk.Button(root2, text='17.55', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T5)
    btn5.place(x=1300, y=320)
    btn6 = tk.Button(root2, text='21.15', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T6)
    btn6.place(x=1400, y=320)
    btn7 = tk.Button(root2, text='23.00', width = 5, bg='light green', fg ='brown', font=("Segoe Script Bold", 10), command=T7)
    btn7.place(x=1500, y=320)

    
    lbl_departure = tk.Label(root2, text="Please choose flight FIRST and then enter the details on the right", bg='light green', font=('Sergoe Script Bold',15,'bold'))
    lbl_departure.place(x=100, y=750)







def fnhotel(): #Hotel selection.
    
    def HI():
        global hotel
        global cost
        hotel = 'Hilton'                                     #'Hilton (800 Dhs)'
        cost = 800
        list2.append(hotel)
        if len(list3) > 3:
            del list3[3]
        list3.append(hotel)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to stay at The Hilton.")#\nRoom Type : Double bed Suite\n\nRate : 800 Dhs (Including Breakfast).")
    
    def BR():
        global hotel
        global cost
        hotel = 'Radisson'                              #'Radisson (1000 Dhs)'
        cost = 1000
        list2.append(hotel)
        if len(list3) > 3:
            del list3[3]
        list3.append(hotel)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to stay at Radisson.")#\nRoom Type : Double bed Suite\n\nRate : 1000 Dhs (Including Breakfast and Lunch).")
    
    def SR():
        global hotel
        global cost
        hotel = 'Sheraton'                              #'Sheraton (1200 Dhs)'
        cost = 1200
        list2.append(hotel)
        if len(list3) > 3:
            del list3[3]
        list3.append(hotel)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to stay at Sheraton.")#\nRoom Type : Double bed Suite with Jacuzzi\n\nRate : 1200 Dhs (All meals)")
    
    def fnnext2():
        if hotel == '':
            messagebox.showinfo("ALERT", "Please select one of the options.")
            
        else:
            root3.destroy()
            fnhotel_2()
            #fnflight()
        
    # Design of Hotel Selection Page.
    
    root3=tk.Toplevel()
    root3.geometry("1200x700")
    #root3.title("HOTEL SELECTION")
    
    global photo4
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\hotels.png')
    photo4=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\hotels.png')
    imagelabel=tk.Label(root3, image=photo4)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblhead = tk.Label(root3, text="Select your hotel.", bg = 'light blue', font=('Sergoe Script Bold',28,'bold'))
    lblhead.place(x=120, y=20)
    btnHI = tk.Button(root3, text='Hilton', width = 20, bg='light blue', fg ='red', font=("Segoe Script", 20), command=HI)
    btnHI.place(x=100, y=100)
    btnBR = tk.Button(root3, text='Radisson', width = 20, bg='light blue', fg = 'red', font=("Segoe Script", 20), command=BR)
    btnBR.place(x=100, y=250)
    btnSR = tk.Button(root3, text='Sheraton', width = 20, bg='light blue', fg ='red',font=("Segoe Script", 20), command=SR) 
    btnSR.place(x=100, y = 400)
    btnnext = tk.Button(root3, text='--->', width = 10, bg='light blue', fg='red', font=("Segoe Script", 10), command=fnnext2)
    btnnext.place(x=700, y=550)




def fnhotel_2():
    
    def fnnext4():
        global root50
        
        if txt_start_date.get() != '' and txt_end_date.get() != '':
            fnflight()
            root50.destroy()
            
        else:
            messagebox.showinfo("ALERT", "Dear Customer, please enter all the details.")
        
        
            
    def SB():
        global start
        global end
        global room
        start = txt_start_date.get()
        end = txt_end_date.get()
        room = "Single Bed Standard"
        string = "Dear Customer, your hotel stay is booked from " + txt_start_date.get() + " to " + txt_end_date.get() + ".\nYour room is a Single Bed Standard." 
        messagebox.showinfo("MESSAGE", string)
    
    def DB():
        global start
        global end
        global room
        start = txt_start_date.get()
        end = txt_end_date.get()
        room = "Double Bed Standard"
        string = "Dear Customer, your hotel stay is booked from " + txt_start_date.get() + " to " + txt_end_date.get() + ".\nYour room is a Double Bed Standard." 
        messagebox.showinfo("MESSAGE", string)
        
    def DBJ():
        global start
        global end
        global room
        start = txt_start_date.get()
        end = txt_end_date.get()
        room = "Double Bed Suite"
        string = "Dear Customer, your hotel stay is booked from " + txt_start_date.get() + " to " + txt_end_date.get() + ".\nYour room is a Double Bed Suite." 
        messagebox.showinfo("MESSAGE", string)
    
    
    global root50
    root50=tk.Toplevel()
    root50.geometry("1200x700")
    global photo4
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\hotels.png')
    photo4=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\hotels.png')
    imagelabel=tk.Label(root50, image=photo4)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblhead = tk.Label(root50, text="HOTEL BOOKING.", bg = 'light blue', font=('Sergoe Script Bold',28,'bold'))
    lblhead.place(x=120, y=20)
        
    
    global txt_start_date
    lbl_start_date = tk.Label(root50, text = "Enter Check-in date.", bg = 'light blue', font=('Sergoe Script Bold',15,'bold'))
    lbl_start_date.place(x=120, y=220)
    txt_start_date = tk.Entry(root50, bg = 'light blue', font=('Sergoe Script Bold',15,'bold'))
    txt_start_date.place(x = 520, y = 220)
    
    
    global txt_end_date
    lbl_end_date = tk.Label(root50, text = "Enter Checkout date.", bg = 'light blue', font=('Sergoe Script Bold', 15, 'bold'))
    lbl_end_date.place(x=120, y=320)
    txt_end_date = tk.Entry(root50, bg = 'light blue', font=('Sergoe Script Bold',15,'bold'))
    txt_end_date.place(x = 520, y = 320)
    
    
    
    lbl_type = tk.Label(root50, text = "Choose the type of room you want.", bg = 'light blue', font=('Sergoe Script Bold',15,'bold'))
    lbl_type.place(x=120, y=420)
    
    btnSB = tk.Button(root50, text='Single Bed Standard', width = 20, bg='light blue', fg ='red',font=("Segoe Script", 10), command=SB) 
    btnSB.place(x=120, y = 500)
    btnDB = tk.Button(root50, text='Double Bed Standard', width = 20, bg='light blue', fg ='red',font=("Segoe Script", 10), command=DB) 
    btnDB.place(x=450, y = 500)
    btnDBJ = tk.Button(root50, text='Double Bed Suite', width = 20, bg='light blue', fg ='red',font=("Segoe Script", 10), command=DBJ) 
    btnDBJ.place(x=750, y = 500)    

    btnNEXT = tk.Button(root50, text='--->', width = 10, bg='light blue', fg='red', font=("Segoe Script", 10), command=fnnext4)
    btnNEXT.place(x=700, y=610)





def fncountry(): #City selection
    
    def NYC():
        global country
        country = 'New York'
        list2.append(country)
        if len(list3) > 2:
            del list3[2]
        list3.append(country)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to visit New York.")
    
    def LON():
        global country
        country = 'London'
        list2.append(country)
        if len(list3) > 2:
            del list3[2]
        list3.append(country)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to visit London.")
    
    def PAR():
        global country
        country = 'Paris'
        list2.append(country)
        if len(list3) > 2:
            del list3[2]
        list3.append(country)
        messagebox.showinfo("Message", "Dear Customer, you have chosen to visit Paris.")
    
    def fnnext():
        if country == 'New York' or country == 'Paris' or country == 'London':
            root4.destroy()
            fnhotel()
            
        else:
            messagebox.showinfo("ALERT", "Please select one of the options.")
            
        
    # Design of the City Selection Page.    
    
    root4=tk.Toplevel()
    root4.geometry("1500x1000")
    #root4.title("CITY SELECTION")
    
    global photo3
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\kkk.png')
    photo3=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\kkk.png')
    imagelabel=tk.Label(root4, image=photo3)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    lblhead = tk.Label(root4, text="Select the city you want to visit.", font=('Sergoe Script Bold',28,'bold'))
    lblhead.place(x=420, y=120)
    btnNYC = tk.Button(root4, text='New York', width = 20, fg ='purple', font=("Segoe Script", 20), command=NYC)
    btnNYC.place(x=500, y=300)
    btnLON = tk.Button(root4, text='London', width = 20, fg = 'purple', font=("Segoe Script", 20), command=LON)
    btnLON.place(x=500, y=500)
    btnPAR = tk.Button(root4, text='Paris', width = 20, fg ='purple',font=("Segoe Script", 20), command=PAR) 
    btnPAR.place(x=500, y = 700)
    btnnext = tk.Button(root4, text='--->', width = 10, fg='purple', font=("Segoe Script", 10), command=fnnext)
    btnnext.place(x=1000, y=850)

         

# Design of introduction page.

def fnprojectmenu():
    
    def button():
        messagebox.showinfo("Message", 'Contact Details\nMobile Number: +971 503489856\nLandline: +971 26267669\nEmail ID: info.paradise.travels2021@gmail.com\nDon\'t forget to follow us on our instagram account\n@paradise.travels')
    
    
    
    def send_concern():
        
        if txtname_person.get() != '' and txtEMAIL.get() != '' and txtconcerns.get() != '':
            
            port = 465  # For SSL
            password = "Sample#0#0#" #input("Type your password and press enter: ")
            # Create a secure SSL context
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("riday.sc12@gmail.com", password)

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "riday.sc12@gmail.com"  # Enter your address
            receiver_email = "info.paradise.travels2021@gmail.com"  # Enter receiver address
            password = "Sample#0#0#" #input("Type your password and press enter: ")
            message = txtconcerns.get() + "\n\n\n This email is sent by " + txtname_person.get() + " whose email ID is " + txtEMAIL.get()

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            
            
            root20.destroy()
            

        elif txtconcerns.get() == '' and txtname_person.get() != '' and txtEMAIL.get() != '':
            messagebox.showinfo("ALERT", "Type your concern/question/feedback.")

        else:
            messagebox.showinfo("ALERT", "Please enter the complete details.")
    
    
    
    def concerns():
        
        global root20
        root20=tk.Tk()
        root20.geometry("1500x930")
        root20.configure(bg = "Pink")

        #pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\world2.png')
        #photo20=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\world2.png')
        #imagelabel=tk.Label(root20, image=photo20)
        #imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

        lbl = tk.Label(root20, bg='Pink', text='QUESTIONS / CONCERNS / FEEDBACK', fg='black',  font=("Algerian", 35))
        lbl.place(x=120 ,y=200)

        global txtname_person
        lblname_person = tk.Label(root20, text = "NAME", bg='Pink', fg ='black', font=("Segoe Script", 15))
        lblname_person.place(x=100, y=350)
        txtname_person = tk.Entry(root20, bg='white', fg ='black', font=("Times New Roman", 15))
        txtname_person.place(x = 300, y = 350, width = 400)
        
        
        global txtEMAIL
        lblEMAIL = tk.Label(root20, text = "EMAIL ID", bg='Pink', fg ='black', font=("Segoe Script", 15))
        lblEMAIL.place(x=100, y=450)
        txtEMAIL = tk.Entry(root20, bg='white', fg ='black', font=("Times New Roman", 15))
        txtEMAIL.place(x = 300, y = 450, width = 400)
        
        
        global txtconcerns
        lblconcern = tk.Label(root20, text = "How can I help?", bg='Pink', fg ='black', font=("Segoe Script", 15))
        lblconcern.place(x=100, y=550)
        txtconcerns = tk.Entry(root20, bg='white', fg ='black', font=("Times New Roman", 15))
        txtconcerns.place(x=100, y=600, width = 1000)
    
        btnsend = tk.Button(root20, text='Send', bg='Pink', fg ='black', font=("Times New Roman", 10), command=send_concern)
        btnsend.place(x=150, y=750)
        root20.mainloop()
        
        

    global list3
    global list2
    list2=[]
    list3=[]
    
    global root6
    root6=tk.Tk()
    root6.geometry("1500x930")
    
    pic=PIL.Image.open(r'C:\Users\dalal\OneDrive\Documents\project pics\world2.png')
    photo=PIL.ImageTk.PhotoImage(file=r'C:\Users\dalal\OneDrive\Documents\project pics\world2.png')
    imagelabel=tk.Label(root6, image=photo)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

    lbl = tk.Label(root6, bg='#CCFFFF', text='WELCOME TO \nPARADISE TRAVEL & TOURISM', fg='red',  font=("Algerian", 40))
    lbl.place(x=150 ,y=200)

    btndisplay2 = tk.Button(root6, bg='#CCFFFF', text ="Login as employee", fg ='red',font=("Segoe Script", 20), command=fnemployee)
    btndisplay2.place(x = 150, y = 600)

    btntrip = tk.Button(root6, text='Book your trip', bg='#CCFFFF', fg ='red', font=("Segoe Script", 20), command=menu)
    btntrip.place(x=900, y=600)
    
    btnbutton = tk.Button(root6, text='Contact Us', bg='#CCFFFF', fg ='red', font=("Segoe Script", 15), command=button)
    btnbutton.place(x=150, y=800)
   
    
    btnquestions = tk.Button(root6, text='Questions', bg='#CCFFFF', fg ='red', font=("Segoe Script", 15), command=concerns)
    btnquestions.place(x=800, y=800)
    root6.mainloop()

    
fnprojectmenu()






