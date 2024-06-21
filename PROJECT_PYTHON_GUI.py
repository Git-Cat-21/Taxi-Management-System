import mysql.connector
from tkinter import * 
import random as r
import time
a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
cur=a.cursor()
cur.execute('select password from admin')
fetch1=cur.fetchone()
fetch=list(tuple(fetch1))
window=Tk();window.title("WELCOME PAGE");window.config(bg='#6497b1')
window.geometry('1475x445')
def msg():
   top=Tk();top.title('submit')
   def submit():
        from geopy.geocoders import Nominatim
        from geopy import distance
        rr=r.randint(1,100);name=name_en.get();sd=sd_en.get();ed=ed_en.get();source=source_en.get()
        destination=destination_en.get();phno=phno_en.get();num_of_cars=numve_en.get();n=numppl_en.get()
        mem=mem_en.get()
        stat="taken"
        geocoder = Nominatim(user_agent='khushi')
        l1=source
        l2=destination
        c1=geocoder.geocode(l1)
        c2=geocoder.geocode(l2)
        lat1,long1=(c1.latitude),(c1.longitude)
        lat2,long2=(c2.latitude),(c2.longitude)
        place1=(lat1,long1);place2=(lat2,long2)
        a=(distance.distance(place1,place2))
        b=str(a);bb=((b[:8]));bbf=float(bb)
        nsd=sd.replace('-','/'); esd=ed.replace('-','/')
        from datetime import datetime
        start_date = datetime.strptime(nsd, "%Y/%m/%d")
        end_date = datetime.strptime(esd, "%Y/%m/%d")
        tot=(abs((end_date-start_date).days))
        cost=0
        import mysql.connector
        a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
        cur=a.cursor()
        cur.execute('select Name_of_Vehicle from car_det where S_No={}'.format(sn_en.get()))
        m=cur.fetchone()
        car_taken=m[0]
        cur.execute('insert into cust_det values({},"{}","{}","{}","{}","{}","{}",{},{},"{}","{}",{},{},{},"{}")'.format(rr,name,sd,ed,stat,source,destination,bbf,tot,phno,car_taken,num_of_cars,n,cost,mem))
        a.commit()  
        
        msg=name+' your unique id is  '+str(rr)+"  you are travelling for a total of   "+str(tot)+'  days'+"  from  "+source+"   to "+destination+ "  you are travelling for a distance of   "+str(bbf)+'  kms  '+m[0]+' is successfully booked under you name'
        from twilio.rest import Client 
        SID='AC6a99b05cf6256f3c2a793d519b0241e9'
        Auth_Token='15cdd6c9cd1a1876f89ee912df2a9751'
        cl=Client(SID,Auth_Token)
        cl.messages.create(body=msg,from_='+14352535685',to=str(phno))
        print("message sent successfully :)")
        print(name,' please check your messages for the invoice')
   def showcars():
        from tkinter import ttk
        r=Tk();r.geometry('500x200');r.title('cars')
        cur.execute('select * from car_det')
        tree=ttk.Treeview(r)
        tree["columns"]=('S_No','Name_of_Vehicle','Number_of_Vehicle','Cost_of_Vehicle')
        tree['show']='headings'
        s=ttk.Style(r)
        s.theme_use("clam")
        s.configure(".",font=("Helvetica",11))
        s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))
        tree.column("S_No",width=100,minwidth=50,anchor=CENTER)
        tree.column("Name_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
        tree.column("Number_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
        tree.column("Cost_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
        tree.heading("S_No",text="S_No",anchor=CENTER)
        tree.heading("Name_of_Vehicle",text="Name_of_Vehicle",anchor=CENTER)
        tree.heading("Number_of_Vehicle",text="Number_of_Vehicle",anchor=CENTER)
        tree.heading("Cost_of_Vehicle",text="Cost_of_Vehicle",anchor=CENTER)
        i=0
        for ro in cur:
            tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
            i=i+1
        tree.pack()
        r.mainloop()
    
   def invoice():
        invoice=Tk();invoice.title('BOOKING INVOICE')
        import mysql.connector
        a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
        cur=a.cursor()
        cur.execute('select Name_of_Vehicle from car_det where S_No={}'.format(sn_en.get()))
        m=cur.fetchone()
        car_taken=m[0]
        
        l=Label(invoice, text="Tours and Travels",font=('Consolas', '25'))
        l.grid(row=1,column=1)
        
        a=time.ctime()
        t=Label(invoice, text=a, font=('Consolas', '15'))
        t.grid(row=1, column=2)

        l1a=Label(invoice, text="Name: " , font=('Consolas', '20'))
        l1a.grid(row=2, column=1, sticky=W)
        l1b=Label(invoice, text=name_en.get(), font=('Consolas', '20'))
        l1b.grid(row=2, column=2,sticky=W)

        l2a=Label(invoice, text="Phone Number: " , font=('Consolas', '20'))
        l2a.grid(row=3, column=1, sticky=W)
        l2b=Label(invoice, text=phno_en.get(), font=('Consolas', '20'))
        l2b.grid(row=3, column=2,sticky=W)

        l3a=Label(invoice, text="Travelling from: " , font=('Consolas', '20'))
        l3a.grid(row=4, column=1, sticky=W)
        l3b=Label(invoice, text=source_en.get(), font=('Consolas', '20'))
        l3b.grid(row=4, column=2,sticky=W)

        l4a=Label(invoice, text="Travelling to: " , font=('Consolas', '20'))
        l4a.grid(row=5, column=1, sticky=W)
        l4b=Label(invoice, text=destination_en.get(), font=('Consolas', '20'))
        l4b.grid(row=5, column=2,sticky=W)

        l5a=Label(invoice, text="Start Date of Travel: " , font=('Consolas', '20'))
        l5a.grid(row=6, column=1, sticky=W)
        l5b=Label(invoice, text=sd_en.get(), font=('Consolas', '20'))
        l5b.grid(row=6, column=2,sticky=W)

        l6a=Label(invoice, text="End Date of Travel: " , font=('Consolas', '20'))
        l6a.grid(row=7, column=1, sticky=W)
        l6b=Label(invoice, text=ed_en.get(), font=('Consolas', '20'))
        l6b.grid(row=7, column=2,sticky=W)

        l7a=Label(invoice, text="Vehicle Booked: " , font=('Consolas', '20'))
        l7a.grid(row=8, column=1, sticky=W)
        l7b=Label(invoice,text=car_taken, font=('Consolas', '20'))
        l7b.grid(row=8, column=2,sticky=W)

        l8a=Label(invoice, text="Number of Vehicles Booked: " , font=('Consolas', '20'))
        l8a.grid(row=9, column=1, sticky=W)
        l8b=Label(invoice, text=numve_en.get(), font=('Consolas', '20'))
        l8b.grid(row=9, column=2,sticky=W)

        l9a=Label(invoice, text="Number of People Travelling: " , font=('Consolas', '20'))
        l9a.grid(row=10, column=1, sticky=W)
        l9b=Label(invoice, text=numppl_en.get(), font=('Consolas', '20'))
        l9b.grid(row=10, column=2,sticky=W)

        invoice.title("Invoice")
        invoice.mainloop()
    
    
    
   l1=Label(top, text="Enter your Name", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l1.grid(row=3, column=1, sticky=W)
   name_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   name_en.grid(row=3, column=2)

   l2=Label(top, text="Enter Phone Number", font=("Consolas", 20), fg='red', bg='light yellow')
   l2.grid(row=4, column=1,sticky=W)
   phno_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   phno_en.grid(row=4, column=2)

   l3=Label(top, text="Enter Start Location", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l3.grid(row=5, column=1,sticky=W)
   source_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   source_en.grid(row=5, column=2, sticky=W)

   l4=Label(top, text="Enter Final Destination", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l4.grid(row=6, column=1,sticky=W)
   destination_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   destination_en.grid(row=6, column=2)

   l5=Label(top, text="Enter Start Date in YY-MM-DD Format", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l5.grid(row=7,column=1,sticky=W)
   sd_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   sd_en.grid(row=7, column=2)

   l6=Label(top, text="Enter End Date in YY-MM-DD Format", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l6.grid(row=8,column=1, sticky=W)
   ed_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   ed_en.grid(row=8, column=2)

   l7=Label(top, text="Enter the Serial Number of the Vehicle", font=('Consolas', '20'), fg='Red', bg='light yellow')
   l7.grid(row=9,column=1,sticky=W)
   sn_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   sn_en.grid(row=9, column=2)

   l8=Label(top, text="Enter Number of Vehicles", font=("Consolas", 20), fg='red', bg='light yellow')
   l8.grid(row=10, column=1, sticky=W)
   numve_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   numve_en.grid(row=10, column=2)

   l9=Label(top, text="Enter Number of People Travelling", font=("Consolas", 20), fg='red', bg='light yellow')
   l9.grid(row=11, column=1,sticky=W)
   numppl_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   numppl_en.grid(row=11, column=2)

   l10=Label(top, text="Enter Y(YES)/ N(NO) for Permanent Membership", font=('Consolas', 20, 'bold'), fg='red', bg='light blue')
   l10.grid(row=12, column=1,sticky=W)
   mem_en=Entry(top, font=('Consolas', '20'), fg='blue', bg='yellow')
   mem_en.grid(row=12, column=2)

   button1=Button(top,text="CLICK HERE TO VIEW CARS", font=('Consolas', '20'), fg='pink', bg='black',command=showcars)
   button1.grid(row=13,column=1, sticky=W)

   button2=Button(top,text="SUBMIT",font=('Consolas', '20'), fg='pink', bg='black', command=submit,width=24)
   button2.grid(row=14,column=1, sticky=W)

   button3=Button(top, text="GENERATE INVOICE", font=('Consolas','20'), fg='pink', bg='black', command=invoice,width=23)
   button3.grid(row=15,column=1, sticky=W)
   top.mainloop()

def retur():
    windowret=Tk();windowret.title("RETURNING VEHICLE")
    def retve():
        retvebill=Tk();retvebill.title('BILL')
        import mysql.connector
        a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
        cur=a.cursor()
        st='select NAME,start_date,end_date,start,end,tot_dist,tot_num_day,car_taken,number_of_vehicles_taken,membership from cust_det where Customer_id={}'.format(cusid_en.get())
        cur.execute(st);m=cur.fetchone()
        print(m[-1])
        st1='select Cost_of_Vehicle from car_det where Name_of_Vehicle ="{}"'.format(m[7])
        cur.execute(st1); m1=cur.fetchone()
        if m[-1] in 'Yy':
            totcost=m[5]*12+10*m[6]+m1[0]*m[8]
            disc_cost=totcost*0.20
            totcost1=totcost-disc_cost
            st2='update cust_det set cost={} where Customer_id={}'.format(totcost1,cusid_en.get())
            cur.execute(st2); a.commit()
            st3='update cust_det set status="{}" where Customer_id={}'.format("returned",cusid_en.get())
            cur.execute(st3); a.commit()
            l=Label(retvebill, text="Tours and Travels",font=('Consolas', '25'))
            l.grid(row=1,column=1)
            
            a=time.ctime()
            t=Label(retvebill, text=a, font=('Consolas', '15'))
            t.grid(row=1, column=2)

            l1a=Label(retvebill, text="Name: " , font=('Consolas', '20'))
            l1a.grid(row=2, column=1, sticky=W)
            l1b=Label(retvebill, text=m[0], font=('Consolas', '20'))
            l1b.grid(row=2, column=2,sticky=W)

            l3a=Label(retvebill, text="Travelling from: " , font=('Consolas', '20'))
            l3a.grid(row=4, column=1, sticky=W)
            l3b=Label(retvebill, text=m[3], font=('Consolas', '20'))
            l3b.grid(row=4, column=2,sticky=W)

            l4a=Label(retvebill, text="Travelling to: " , font=('Consolas', '20'))
            l4a.grid(row=5, column=1, sticky=W)
            l4b=Label(retvebill, text=m[4], font=('Consolas', '20'))
            l4b.grid(row=5, column=2,sticky=W)

            l5a=Label(retvebill, text="Start Date of Travel: " , font=('Consolas', '20'))
            l5a.grid(row=6, column=1, sticky=W)
            l5b=Label(retvebill, text=m[1], font=('Consolas', '20'))
            l5b.grid(row=6, column=2,sticky=W)

            l6a=Label(retvebill, text="End Date of Travel: " , font=('Consolas', '20'))
            l6a.grid(row=7, column=1, sticky=W)
            l6b=Label(retvebill, text=m[2], font=('Consolas', '20'))
            l6b.grid(row=7, column=2,sticky=W)

            l7a=Label(retvebill, text="Vehicle Booked: " , font=('Consolas', '20'))
            l7a.grid(row=8, column=1, sticky=W)
            l7b=Label(retvebill,text=m[7], font=('Consolas', '20'))
            l7b.grid(row=8, column=2,sticky=W)

            l8a=Label(retvebill, text="Number of Vehicles Booked: " , font=('Consolas', '20'))
            l8a.grid(row=9, column=1, sticky=W)
            l8b=Label(retvebill, text=m[-2], font=('Consolas', '20'))
            l8b.grid(row=9, column=2,sticky=W)

            l9a=Label(retvebill, text="COST: " , font=('Consolas', '20'))
            l9a.grid(row=10, column=1, sticky=W)
            l9b=Label(retvebill, text='₹'+str(totcost1), font=('Consolas', '20'))
            l9b.grid(row=10, column=2,sticky=W)
            import mysql.connector
            a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
            cur=a.cursor()
            st2='select phone_number from cust_det where Customer_id ="{}"'.format(cusid_en.get())
            cur.execute(st2); m2=cur.fetchone()
            msg=m[0]+' you have travelled from  '+m[3]+"  to   "+m[4]+ " a total distance of   "+str(m[5])+'  kms  '+"taken together for  "+str(m[6])+"  days your final bill is "+"₹"+str(totcost1)[:8]
            from twilio.rest import Client 
            SID='AC6a99b05cf6256f3c2a793d519b0241e9'
            Auth_Token='15cdd6c9cd1a1876f89ee912df2a9751'
            cl=Client(SID,Auth_Token)
            cl.messages.create(body=msg,from_='+14352535685',to=str(m2[0]))
            print("message sent successfully :)")
            print(m[0],' please check your messages for the invoice')
            
        elif m[-1] in 'Nn':
            totcost=m[5]*12+10*m[6]+m1[0]*m[8]
            print(totcost)
            st2='update cust_det set cost={} where Customer_id={}'.format(totcost,cusid_en.get())
            cur.execute(st2); a.commit()
            l=Label(retvebill, text="Tours and Travels",font=('Consolas', '25'))
            l.grid(row=1,column=1)
            st3='update cust_det set status="{}" where Customer_id={}'.format("returned",cusid_en.get())
            cur.execute(st3); a.commit()
            a=time.ctime()
            t=Label(retvebill, text=a, font=('Consolas', '15'))
            t.grid(row=1, column=2)

            l1a=Label(retvebill, text="Name: " , font=('Consolas', '20'))
            l1a.grid(row=2, column=1, sticky=W)
            l1b=Label(retvebill, text=m[0], font=('Consolas', '20'))
            l1b.grid(row=2, column=2,sticky=W)

            l3a=Label(retvebill, text="Travelling from: " , font=('Consolas', '20'))
            l3a.grid(row=4, column=1, sticky=W)
            l3b=Label(retvebill, text=m[3], font=('Consolas', '20'))
            l3b.grid(row=4, column=2,sticky=W)

            l4a=Label(retvebill, text="Travelling to: " , font=('Consolas', '20'))
            l4a.grid(row=5, column=1, sticky=W)
            l4b=Label(retvebill, text=m[4], font=('Consolas', '20'))
            l4b.grid(row=5, column=2,sticky=W)

            l5a=Label(retvebill, text="Start Date of Travel: " , font=('Consolas', '20'))
            l5a.grid(row=6, column=1, sticky=W)
            l5b=Label(retvebill, text=m[1], font=('Consolas', '20'))
            l5b.grid(row=6, column=2,sticky=W)

            l6a=Label(retvebill, text="End Date of Travel: " , font=('Consolas', '20'))
            l6a.grid(row=7, column=1, sticky=W)
            l6b=Label(retvebill, text=m[2], font=('Consolas', '20'))
            l6b.grid(row=7, column=2,sticky=W)

            l7a=Label(retvebill, text="Vehicle Booked: " , font=('Consolas', '20'))
            l7a.grid(row=8, column=1, sticky=W)
            l7b=Label(retvebill,text=m[7], font=('Consolas', '20'))
            l7b.grid(row=8, column=2,sticky=W)

            l8a=Label(retvebill, text="Number of Vehicles Booked: " , font=('Consolas', '20'))
            l8a.grid(row=9, column=1, sticky=W)
            l8b=Label(retvebill, text=m[-2], font=('Consolas', '20'))
            l8b.grid(row=9, column=2,sticky=W)

            l9a=Label(retvebill, text="COST: " , font=('Consolas', '20'))
            l9a.grid(row=10, column=1, sticky=W)
            l9b=Label(retvebill, text='₹'+str(totcost), font=('Consolas', '20'))
            l9b.grid(row=10, column=2,sticky=W)
            import mysql.connector
            a=mysql.connector.connect(host='localhost',user='root',password='mysql@123',database='customer')
            cur=a.cursor()
            st2='select phone_number from cust_det where Customer_id ="{}"'.format(cusid_en.get())
            cur.execute(st2); m2=cur.fetchone()
            msg=m[0]+' you have travelled from  '+m[3]+"  to   "+m[4]+ " a total distance of  "+str(m[5])+'  kms  '+"taken together "+str(m[6])+" days your final bill is "+"₹"+str(totcost)[:8]
            from twilio.rest import Client 
            SID='AC6a99b05cf6256f3c2a793d519b0241e9'
            Auth_Token='15cdd6c9cd1a1876f89ee912df2a9751'
            cl=Client(SID,Auth_Token)
            cl.messages.create(body=msg,from_='+14352535685',to=str(m2[0]))
            print("message sent successfully :)")
            print(m[0],' please check your messages for the invoice')
            
        cur.execute(st)


        retvebill.mainloop()
    l1=Label(windowret, text="Enter your Customter ID", font=('Consolas', '20'), fg='Red', bg='light yellow')
    l1.grid(row=0, column=0, sticky=W)
    cusid_en=Entry(windowret, font=('Consolas', '20'), fg='blue', bg='yellow')
    cusid_en.grid(row=0, column=1)
    subbut=Button(windowret,text='GENERATE BILL',font=('Consolas', '20'),command=retve)
    subbut.grid(row=1,column=1)
    windowret.mainloop()
def exitn():
    window.destroy()

def adminpg():
    window1=Tk()
    def grant():
        if (pass_entry.get()) in fetch:
            window2=Tk()
            def exitpg():
                window2.destroy()
            def changeava():
                windowava=Tk(); windowava.title('CHANGE AVAILABILITY AND COST'); windowava.geometry('1500x270');windowava.config(bg='#9EA1D4')
                def exitt():
                    windowava.destroy()
                def submit():
                    numve=entry_ch_veava.get();vesno=entry_ch_ava.get();cost=entry_ch_cost.get()
                    cur.execute('update car_det set Number_of_Vehicle={} where S_No ={}'.format(numve,vesno))
                    a.commit()
                    cur.execute('update car_det set Cost_of_Vehicle={} where S_No ={}'.format(cost,vesno))
                    a.commit()
                    print("changed successfully")
                def showcars():
                    from tkinter import ttk
                    r=Tk();r.geometry('500x200');r.title('cars')
                    cur.execute('select * from car_det')
                    tree=ttk.Treeview(r)
                    tree["columns"]=('S_No','Name_of_Vehicle','Number_of_Vehicle','Cost_of_Vehicle')
                    tree['show']='headings'
                    s=ttk.Style(r)
                    s.theme_use("clam")
                    s.configure(".",font=("Helvetica",11))
                    s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))
                    tree.column("S_No",width=100,minwidth=50,anchor=CENTER)
                    tree.column("Name_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Number_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Cost_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.heading("S_No",text="S_No",anchor=CENTER)
                    tree.heading("Name_of_Vehicle",text="Name_of_Vehicle",anchor=CENTER)
                    tree.heading("Number_of_Vehicle",text="Number_of_Vehicle",anchor=CENTER)
                    tree.heading("Cost_of_Vehicle",text="Cost_of_Vehicle",anchor=CENTER)
                    i=0
                    for ro in cur:
                        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
                        i=i+1
                    tree.pack()
                    r.mainloop()
                label_ch_ava=Label(windowava,text='ENTER THE SERIAL NUMBER OF THE VEHICLE WHOSE DATA IS TO BE CHANGED',font=('Garamond','19','bold'),bg='#9EA1D4')
                label_ch_ava.grid(row=0,column=0)
                entry_ch_ava=Entry(windowava,width=50,font=('Garamond','15','bold'));entry_ch_ava.grid(row=0,column=1,sticky=W)
                label_ch_veava=Label(windowava,text='ENTER THE NEW AVAILABILTY OF THE VEHICLE ',font=('Garamond','19','bold'),bg='#9EA1D4')
                label_ch_veava.grid(row=1,column=0,sticky=W)
                entry_ch_veava=Entry(windowava,width=50,font=('Garamond','15','bold'));entry_ch_veava.grid(row=1,column=1,sticky=W)
                label_ch_cost=Label(windowava,text='ENTER THE NEW COST OF THE VEHICLE ',font=('Garamond','19','bold'),bg='#9EA1D4')
                label_ch_cost.grid(row=2,column=0,sticky=W)
                entry_ch_cost=Entry(windowava,width=50,font=('Garamond','15','bold'));entry_ch_cost.grid(row=2,column=1)
                button_subch=Button(windowava,text='SUBMIT',font=('Garamond','15','bold'),command=submit,bg='#9EA1D4',padx=10,pady=10,width=28)
                button_subch.grid(row=6,column=0,sticky=W)
                button_show_cars=Button(windowava,text='CLICK HERE TO VIEW VEHICLES',command=showcars,font=('Garamond','15','bold'),bg='#9EA1D4',padx=10,pady=10,)
                button_show_cars.grid(row=5,column=0,sticky=W)
                button_exit=Button(windowava,text='EXIT',font=('Garamond','15','bold'),command=exitt,bg='#9EA1D4',padx=10,pady=10,width=28);button_exit.grid(row=7,column=0,sticky=W)
                windowava.mainloop()
            def addve():
                windowadve=Tk()
                windowadve.title('ADD A VEHICLE'); windowadve.geometry('1500x300');windowadve.config(bg='#4FA095')
                def exitt():
                    windowadve.destroy()
                def submit():
                    sno=entry_sno.get();nm=entry_nam_vehi.get();av=entry_availve.get();cost=entry_cost.get()
                    cur.execute('insert into car_det values ({},"{}",{},{})'.format(sno,nm,av,cost))
                    a.commit()
                    print("entered the values successfully")
                def showcars():
                    from tkinter import ttk
                    r=Tk();r.geometry('500x200');r.title('cars')
                    cur.execute('select * from car_det')
                    tree=ttk.Treeview(r)
                    tree["columns"]=('S_No','Name_of_Vehicle','Number_of_Vehicle','Cost_of_Vehicle')
                    tree['show']='headings'
                    s=ttk.Style(r)
                    s.theme_use("clam")
                    s.configure(".",font=("Helvetica",11))
                    s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))
                    tree.column("S_No",width=100,minwidth=50,anchor=CENTER)
                    tree.column("Name_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Number_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Cost_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.heading("S_No",text="S_No",anchor=CENTER)
                    tree.heading("Name_of_Vehicle",text="Name_of_Vehicle",anchor=CENTER)
                    tree.heading("Number_of_Vehicle",text="Number_of_Vehicle",anchor=CENTER)
                    tree.heading("Cost_of_Vehicle",text="Cost_of_Vehicle",anchor=CENTER)
                    i=0
                    for ro in cur:
                        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
                        i=i+1
                    tree.pack()
                    r.mainloop()
                button_show_cars=Button(windowadve,text='CLICK HERE TO VIEW VEHICLES',command=showcars,font=('Garamond','15','bold'),bg='#4FA095')
                button_show_cars.grid(row=4,column=0,sticky=W)
                label_sno=Label(windowadve,text='ENTER THE SERIAL NUMBER OF THE NEW VEHICLE ',font=('Garamond','21','bold'),bg='#4FA095')
                label_sno.grid(row=0,column=0,sticky=W)
                entry_sno=Entry(windowadve,font=('Garamond','15','bold'));entry_sno.grid(row=0,column=1)
                label_nam_vehi=Label(windowadve,text='ENTER THE NAME OF THE VEHICLE',font=('Garamond','19','bold'),bg='#4FA095')
                label_nam_vehi.grid(row=1,column=0,sticky=W)
                entry_nam_vehi=Entry(windowadve,font=('Garamond','15','bold'));entry_nam_vehi.grid(row=1,column=1)
                label_availve=Label(windowadve,text='ENTER THE AVAILABILITY OF THE VEHICLE',font=('Garamond','19','bold'),bg='#4FA095')
                label_availve.grid(row=2,column=0,sticky=W)
                entry_availve=Entry(windowadve,font=('Garamond','15','bold'));entry_availve.grid(row=2,column=1)
                label_cost=Label(windowadve,text='ENTER THE COST OF THE VEHICLE',font=('Garamond','19','bold'),bg='#4FA095')
                label_cost.grid(row=3,column=0,sticky=W)
                entry_cost=Entry(windowadve,font=('Garamond','15','bold'));entry_cost.grid(row=3,column=1)
                button_subch=Button(windowadve,text='SUBMIT',font=('Garamond','15','bold'),command=submit,bg='#4FA095',width=28)
                button_subch.grid(row=5,column=0,sticky=W)
                button_exit=Button(windowadve,text='EXIT',font=('Garamond','15','bold'),command=exitt,bg='#4FA095',width=28);button_exit.grid(row=6,column=0,sticky=W)
                windowadve.mainloop()
            def remove():
                windowremove=Tk()
                def exitt():
                    windowremove.destroy()
                def submit():
                    sno=entry_sn.get()
                    cur.execute('delete from car_det where S_No={}'.format(sno))
                    a.commit()
                    print("removed the value successfully")
                def showcars():
                    from tkinter import ttk
                    r=Tk();r.geometry('500x200');r.title('cars')
                    cur.execute('select * from car_det')
                    tree=ttk.Treeview(r)
                    tree["columns"]=('S_No','Name_of_Vehicle','Number_of_Vehicle','Cost_of_Vehicle')
                    tree['show']='headings'
                    s=ttk.Style(r)
                    s.theme_use("clam")
                    s.configure(".",font=("Helvetica",11))
                    s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))
                    tree.column("S_No",width=100,minwidth=50,anchor=CENTER)
                    tree.column("Name_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Number_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.column("Cost_of_Vehicle",width=150,minwidth=50,anchor=CENTER)
                    tree.heading("S_No",text="S_No",anchor=CENTER)
                    tree.heading("Name_of_Vehicle",text="Name_of_Vehicle",anchor=CENTER)
                    tree.heading("Number_of_Vehicle",text="Number_of_Vehicle",anchor=CENTER)
                    tree.heading("Cost_of_Vehicle",text="Cost_of_Vehicle",anchor=CENTER)
                    i=0
                    for ro in cur:
                        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
                        i=i+1
                    tree.pack()
                    r.mainloop()
                windowremove.title('remove a vehicle');windowremove.geometry('1500x170');windowremove.config(bg='#87A2FB')
                button_show_cars=Button(windowremove,text='CLICK HERE TO VIEW VEHICLES',command=showcars,font=('Garamond','15','bold'),bg='#87A2FB')
                button_show_cars.grid(row=2,column=0,sticky=W)
                label_sn=Label(windowremove,text='ENTER THE SERIAL NUMBER OF VEHICLE YOU WANT TO REMOVE',font=('Garamond','19','bold'),bg='#87A2FB')
                label_sn.grid(row=0,column=0)
                entry_sn=Entry(windowremove,font=('Garamond','15','bold'));entry_sn.grid(row=0,column=1)
                button_subch=Button(windowremove,text='SUBMIT',font=('Garamond','15','bold'),command=submit,bg='#87A2FB',width=28)
                button_subch.grid(row=3,column=0,sticky=W)
                button_exit=Button(windowremove,text='EXIT',font=('Garamond','15','bold'),command=exitt,bg='#87A2FB',width=28);button_exit.grid(row=4,column=0,sticky=W)
                windowremove.mainloop()
            def removecust():
                windowrecust=Tk()
                def exitt():
                    windowrecust.destroy()
                def submit():
                    incid=entry_custid.get()
                    cur.execute("delete from cust_det where Customer_id={}".format(incid))
                    a.commit()
                def showcust():
                    from tkinter import ttk
                    r=Tk();r.geometry('1500x200');r.title('CUSTOMER DETAILS')
                    cur.execute('select * from cust_det')
                    tree=ttk.Treeview(r)
                    tree["columns"]=('Customer_id','NAME','start_date','end_date','status','start','end','tot_dist','tot_num_day','phone_number','car_taken','number_of_vehicles_taken','number_of_people','cost','memebership')
                    tree['show']='headings'
                    s=ttk.Style(r)
                    s.theme_use("clam")
                    s.configure(".",font=("Helvetica",11))
                    s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,'bold'))
                    tree.column("Customer_id",width=100,minwidth=50,anchor=CENTER)
                    tree.column("NAME",width=150,minwidth=50,anchor=CENTER)
                    tree.column("start_date",width=100,minwidth=50,anchor=CENTER)
                    tree.column("end_date",width=100,minwidth=50,anchor=CENTER)
                    tree.column("status",width=100,minwidth=50,anchor=CENTER)
                    tree.column("start",width=100,minwidth=50,anchor=CENTER)
                    tree.column("end",width=100,minwidth=50,anchor=CENTER)
                    tree.column("tot_dist",width=100,minwidth=50,anchor=CENTER)
                    tree.column("tot_num_day",width=100,minwidth=50,anchor=CENTER)
                    tree.column("phone_number",width=150,minwidth=50,anchor=CENTER)
                    tree.column("car_taken",width=100,minwidth=50,anchor=CENTER)
                    tree.column("number_of_vehicles_taken",width=150,minwidth=100,anchor=CENTER)
                    tree.column("number_of_people",width=150,minwidth=50,anchor=CENTER)
                    tree.column("cost",width=100,minwidth=50,anchor=CENTER)
                    tree.column("memebership",width=100,minwidth=50,anchor=CENTER)
                    tree.heading("Customer_id",text="Customer_id",anchor=CENTER)
                    tree.heading("NAME",text="NAME",anchor=CENTER)
                    tree.heading("start_date",text="start_date",anchor=CENTER)
                    tree.heading("end_date",text="end_date",anchor=CENTER)
                    tree.heading("status",text="status",anchor=CENTER)
                    tree.heading("start",text="start",anchor=CENTER)
                    tree.heading("end",text="end",anchor=CENTER)
                    tree.heading("tot_dist",text="tot_dist",anchor=CENTER)
                    tree.heading("tot_num_day",text="tot_num_day",anchor=CENTER)
                    tree.heading("phone_number",text="phone_number",anchor=CENTER)
                    tree.heading("car_taken",text="car_taken",anchor=CENTER)
                    tree.heading("number_of_vehicles_taken",text="number_of_vehicles_taken",anchor=CENTER)
                    tree.heading("number_of_people",text="number_of_people",anchor=CENTER)
                    tree.heading("cost",text="cost",anchor=CENTER)
                    tree.heading("memebership",text="memebership",anchor=CENTER)
                    i=0
                    for ro in cur:
                        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]))
                        i=i+1
                    hsb=ttk.Scrollbar(r,orient='horizontal')
                    hsb.configure(command=tree.xview)
                    tree.configure(xscrollcommand=hsb.set)
                    hsb.pack(fill=X,side=BOTTOM)
                    tree.pack()
                    r.mainloop()
                windowrecust.title('REMOVE CUSTOMER');windowrecust.geometry('1500x180');windowrecust.config(bg='#6CC4A1')
                button_showcus=Button(windowrecust,text='CLICK HERE TO VIEW CUSTOMER DETAILS',font=('Garamond','15','bold'),command=showcust,bg='#6CC4A1')
                button_showcus.grid(row=2,column=0,sticky=W)
                label_custid=Label(windowrecust,text='ENTER THE CUSTOMER_ID OF OF THE CUSTOMER YOU WOULD LIKE TO REMOVE',font=('Garamond','19','bold'),bg='#6CC4A1')
                label_custid.grid(row=0,column=0)
                entry_custid=Entry(windowrecust,font=('Garamond','15','bold'))
                entry_custid.grid(row=0,column=1)
                button_subch=Button(windowrecust,text='SUBMIT',font=('Garamond','15','bold'),command=submit,bg='#6CC4A1',width=37)
                button_subch.grid(row=3,column=0,sticky=W)
                button_exit=Button(windowrecust,text='EXIT',font=('Garamond','15','bold'),command=exitt,bg='#6CC4A1',width=37);button_exit.grid(row=4,column=0,sticky=W)
                windowrecust.mainloop()
            def changepass():
                windowchpass=Tk();windowchpass.title("CHANGE PASSWORD")
                def exitt():
                    windowchpass.destroy()
                def submit():
                    newpass=entry_new_passag.get()
                    cur.execute('update admin set password="{}" where name="{}"'.format(newpass,'admin'))
                    a.commit()
                    print("password changed successfully")
                windowchpass.title('CHANGE PASSWORD');windowchpass.geometry('1500x200');windowchpass.config(bg='#00C897')
                label_new_pass=Label(windowchpass,text='ENTER THE NEW PASSWORD',font=('Garamond','19','bold'),bg='#00C897')
                label_new_pass.grid(row=0,column=0,sticky=W)
                entry_new_pass=Entry(windowchpass,font=('Garamond','19','bold'));entry_new_pass.grid(row=0,column=1)
                label_new_passag=Label(windowchpass,text='ENTER THE NEW PASSWORD AGAIN',font=('Garamond','19','bold'),bg='#00C897')
                label_new_passag.grid(row=1,column=0,sticky=W)
                entry_new_passag=Entry(windowchpass,font=('Garamond','19','bold'));entry_new_passag.grid(row=1,column=1)
                button_sub=Button(windowchpass,text='SUBMIT',font=('Garamond','15','bold'),command=submit,bg='#00C897',width=15);button_sub.grid(row=2,column=0,sticky=W)
                button_exit=Button(windowchpass,text='EXIT',font=('Garamond','15','bold'),command=exitt,bg='#00C897',width=15);button_exit.grid(row=3,column=0,sticky=W)
                windowchpass.mainloop()
            window2.title('ADMIN PAGE'); window2.geometry('1500x600');window2.config(bg='#ADE792')
            label=Label(window2,text='WELCOME ADMIN',font=('Garamond','30','bold'),bg='#ADE792')
            label.pack()
            label_ask=Label(window2,text='HOW WOULD YOU LIKE TO PROCEED ',font=('Garamond','30','bold'),bg='#ADE792')
            label_ask.pack()
            label_star=Label(window2,text='*********************************',font=('Garamond','30','bold'),bg='#ADE792')
            label_star.pack()
            button_change=Button(window2,text='CHANGE AVAILABILITY AND COST OF THE VEHICLE ',font=('Garamond','21','bold'),command=changeava,width=50,bg='#ADE792')
            button_change.pack()
            button_add=Button(window2,text='ADD A VEHICLE ',font=('Garamond','21','bold'),command=addve,width=50,bg='#ADE792')
            button_add.pack()
            button_remove=Button(window2,text='REMOVE A VEHICLE ',font=('Garamond','21','bold'),command=remove,width=50,bg='#ADE792')
            button_remove.pack()
            button_removecust=Button(window2,text='REMOVE CUSTOMER ',font=('Garamond','21','bold'),command=removecust,width=50,bg='#ADE792')
            button_removecust.pack()
            button_changepass=Button(window2,text='CHANGE PASSWORD ',font=('Garamond','21','bold'),command=changepass,width=50,bg='#ADE792')
            button_changepass.pack()
            button_exitpg=Button(window2,text='EXIT ',font=('Garamond','21','bold'),command=exitpg,width=50,bg='#ADE792')
            button_exitpg.pack()
        else:
            window1.destroy()
    window1.geometry('1500x200');window1.title('ADMIN LOGIN PAGE');window1.config(bg='#82AAE3')
    label=Label(window1,text='WELCOME TO THE ADMIN PAGE',font=('Garamond','50','bold'),bg='#82AAE3')
    label.pack()
    label_pass=Label(window1,text='PLEASE ENTER THE PASSWORD',font=('Garamond','20','bold'),bg='#82AAE3')
    label_pass.pack()
    pass_entry=Entry(window1,font=('Garamond','20','bold'),show='*')
    pass_entry.pack()
    button_submit=Button(window1,text='submit',font=('Garamond','20','bold'),command=grant,bg='#82AAE3',background='#82AAE3')
    button_submit.pack()
    window1.mainloop()
labelwel=Label(window,text=' WELCOME TO TOURS AND TRAVELS ',font=('Garamond','50','bold'),bg='#6497b1')
labelwel.grid(row=0,column=0)
lablespace=Label(window,text='                                  ',fg='#6497b1',bg='#6497b1')
lablespace.grid(row=1,column=1)
bookve=Button(window, text="BOOK A VEHICLE", font=('Consolas', '30','bold'), fg='light blue', bg='black',command=msg,width=25)
bookve.grid(sticky=W)
button_return=Button(window,text="RETURN VEHICLE", font=('Consolas', '30','bold'), fg='light blue', bg='black',command=retur,width=25)
button_return.grid(sticky=W)
button_admin=Button(window,text='ADMIN',font=('Garamond','30','bold'),command=adminpg, fg='light blue', bg='black',width=23)
button_admin.grid(sticky=W)
button_exit=Button(window,text='EXIT',font=('Garamond','30','bold'),command=exitn, fg='light blue', bg='black',width=23)
button_exit.grid(sticky=W)
window.mainloop()
