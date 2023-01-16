#CONNECTION
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ansh130204",database="Travels")
import datetime
import sys


#CONNECTION SUCCESS
if mydb.is_connected():
    print("Succesfull Connection")


#CURSOR
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Travels")


#USER TABLE
cursor. execute("CREATE TABLE IF NOT EXISTS Customers(Name VARCHAR(12) NOT NULL , Age INT(3) , EMAIL_ID VARCHAR(13) , Address VARCHAR(12) , ID int(12), Passwd INT(12),PRIMARY KEY(ID,Passwd))")
'''p1="INSERT INTO Customers(Name,Age,EMAIL_ID,Address,ID,Passwd) VALUES(%s,%s,%s,%s,%s,%s)"
s1=("Aditya","18","aditya22","Delhi-92","1005","1009")
cursor.execute(p1,s1)
mydb.commit()
'''


#TRIPS Table
cursor.execute("CREATE TABLE IF NOT EXISTS Trips(C_ID INT(12) NOT NULL,PastLoc VARCHAR(12)NULL ,Date DATE NULL,UpcomTrips VARCHAR(12) NULL,Date_1 DATE NULL)" )
'''g1="INSERT INTO Trips(C_ID,PastLoc,Date,UpcomTrips,Date_1) VALUES(%s,%s,%s,%s,%s)"
T1=("1005","NYC",datetime.datetime(2002,12,31),"PARIS",datetime.datetime(2003,3,20))
cursor.execute(g1,T1)
mydb.commit()
'''


#ADMIN TABLE
cursor. execute("CREATE TABLE IF NOT EXISTS Admin(Name VARCHAR(12) NOT NULL , Age INT(3) , EMAIL_ID VARCHAR(21) , Address VARCHAR(21) , ID int(12), Passwd INT(12),PRIMARY KEY(ID,Passwd))")
'''t2="INSERT INTO Admin(Name,Age,EMAIL_ID,Address,ID,Passwd) VALUES(%s,%s,%s,%s,%s,%s)"
sql9=("Lucky","23","lucky22","Delhi-92","1009","1005")
cursor.execute(t2,sql9)
mydb.commit()
'''

#USER DATA BY ADMIN
def userdataA_():
    x=int(input("Enter UserId Of The User"))
    cursor.execute("SELECT * FROM Customers")
    record=cursor.fetchall()
    for  i in record:
        if(i[4]==x):
            print("*******")
            print("The Details  Of The User Is As Follows","\n","Name :",i[0],"\n","AGE",i[1],"\n","EMAIL ID:",i[2],"\n","ADDRESS:",i[3],"\n","USER ID",i[4],"PASSWORD",i[5])
            print("********")
        else:
            print("TRY AGAIN PLEASE")
            userdataA_()
    print("\n")
    print("**************")
    print("PRESS 1 TO CONTNUE")
    print("PRESS 2 TO GO BACK TO ADMIN LOGIN")
    print("PRESS ANY KEY TO GO BACK TO MAIN MENU")
    print("**************")
 
    r=int(input("ENTER YOUR CHOICE"))
    print("\n")
 
    if r==1:
        print("\n")
        userdataA_()
    if r==2:
        print("\n")
        admin_login()
    else:
        print("\n")
        main()
    print("\n")
        
 
#UPGRADATION OF USER DATA BY ADMIN
def UpdateUData_():
    print("**********")
    print("PRESS 1 TO CHANGE NAME")
    print("PRESS 2 TO CHANGE AGE")
    print("PRESS 3 TO CHANGE EMAIL ID")
    print("PRESS 4 TO CHANGE ADDRESS")
    print("**********")
    print("\n")
    r=int(input("enter your choice: "))
    z=int(input("ENTER THE ID OF THE CUSTOMER TO BE CHANGED"))
    cursor.execute("SELECT * FROM CUSTOMERS")
    res=cursor.fetchall()
    for i in res:
        if(i[4]==z):
            
            #update name
            if(r==1):
                print("\n")
                z=input("ENTER NEW NAME: ")
                cursor.execute("UPDATE Customers SET Name='z' WHERE ID='z' ")
                mydb.commit()
                print("THE NAME OF  USER HAS BEEN CHANGED TO",z)
 
        #update age
        elif(r==2):
            print("\n")
            z1=int(input("ENTER NEW AGE: "))
            cursor.execute("UPDATE Customers SET Age='z1' WHERE ID='z' ")
            mydb.commit()
            print("THE AGE OF  USER HAS BEEN CHANGED TO")
 
        #update email id
        elif(r==3):
            print("\n")
            z2=input("ENTER NEW EMAIL ID: ")
            cursor.execute("UPDATE Customers SET EMAIL_ID='z2' WHERE ID='z' ")
            mydb.commit()
            print("THE EMAIL ID OF USER HAS BEEN CHANGED TO",z2)
 
        #update address
        elif(r==4):
            print("\n")
            z3=input("ENTER NEW ADDRESS: ")
            cursor.execute("UPDATE Customers SET Address='z3' WHERE ID='z' ")
            mydb.commit()
            print("THE ADDRESS OF USER HAS BEEN CHANGED TO",z2)
            print("\n")
            
        print("***********")
        print("PRESS 1 TO CONTNUE")
        print("PRESS 2 TO GO BACK TO ADMIN LOGIN")
        print("*************")
        print("\n")
        r=int(input("ENTER YOUR CHOICE"))
        if r==1:
            print("\n")
            UpdateUData_()
        if r==2:
            print("\n")
            admin_login()
        else:
            print("\n")
            main()
            print("\n")
 
 
 
#DELETION OF USER DATA BY ADMIN
def UDataDel_():
    print("\n")
    x=int(input("Enter The UserID Of User "))
    sql3="DELETE FROM Customer WHERE ID='x'"
    cursor.execute(sql3)
    mydb.commit()
    print("\n")
    print("************")
    print("PRESS 1 TO CONTNUE")
    print("PRESS 2 TO GO BACK TO ADMIN LOGIN")
    print("*************")
    r=int(input("ENTER YOUR CHOICE"))
    print("\n")
 
    if r==1:
        print("\n")
        UDataDel_()
    if r==2:
        print("\n")
        admin_login()
    else:
        print("\n")
        main()
    print("\n")
 
#ADMIN SIGNUP
def SignupA_():
        print("******************")
        a=input("ENTER YOUR NAME")
        o=int(input("ENTER YOUR AGE"))
        b=input("ENTER YOUR EMAIL")
        c=input("ENTER YOUR ADDRESS")
        d=int(input("ENTER THE ID GIVEN TO YOU VIA ADMINISTRATION"))
        e=int(input("ENTER THE PASSWD GIVEN TO YOU VIA ADMINISTRATION"))
        print("******************")
 
        t1="INSERT INTO Admin(Name,Age,EMAIL_ID,Address,ID,Passwd) VALUES(%s,%s,%s,%s,%s,%s)"
        s=(a,o,b,c,d,e)
        cursor.execute(t1,s)
        mydb.commit()
        print("YOU ARE SUCCESSFULLY REGISTERED TO OUR AGENCY")
        print("\n")
        print("************")
        print("PRESS 1 TO GO  TO ADMIN LOGIN")
        print("PRESS ANY KEY TO GO BACK TO MAIN MENU")
        print("************")
        r=int(input("ENTER YOUR CHOICE"))
        print("\n")
 
        if r==1:
            print("\n")
            admin_login()
        else:
            print("\n")
            main()
        print("\n")
 
 
#ADMIN LOGIN    
def admin_login():
    global w
    global w1
    print("***********")
    w=int(input("ENTER ADMIN ID: "))
    w1=int(input("ENTER ADMIN PASSWORD: "))
    print("**********")
 
    
    cursor.execute("SELECT * FROM Admin")
    res=cursor.fetchall()
    op=1
    for i in res:
        if(i[4]==w and i[5]==w1):
            op=0
            break
        else:
            op=1
 
    if op==0:
        print("\n")
        print("WELCOME ADMIN:",i[0])
        print("*********")
        print("PRESS 1 TO SEE USER DATA")
        print("PRESS 2 TO UPDATE USER DATA")
        print("PRESS 3 TO DELETE USER DATA")
        print("PRESS 4 TO SEE YOUR DATA")
        print("PRESS 5 TO MAIN MENU")
        print("**********")
        c=int(input("Enter Your  Choice"))
        print("\n")
 
        if c==1:
            print("\n")
            userdataA_()
            
        if c==2:
            print("\n")
            UpdateUData_()
            
        if c==3:
            print("\n")
            UDataDel_()
        if c==4:
            print("\n")
            admin_DATA_()
        if c==5:
            print("\n")
            main()
    else: 
        print("\n")
        print("**************")
        print("TO TRY AGAIN PRESS 1")
        print("TO GO BACK TO HOME PAGE PRESS ANY KEY")
        print("**************")
        n=int(input("ENTER YOUR CHOICE PLEASE"))
        if n==1:
            print("\n")
            admin_login()
        else:
            print("\n")
            main()
            print("\n")
       
 
#ADMIN DATA
def admin_DATA_():
    cursor.execute("SELECT * FROM Admin")
    record=cursor.fetchall()
    for  i in record:
        if(i[4]==w):
            print("*******")
            print("The Details  OfF YOU Is As Follows","\n","Name :",i[0],"\n","AGE",i[1],"\n","EMAIL ID:",i[2],"\n","ADDRESS:",i[3],"\n","USER ID",i[4],"PASSWORD",i[5])
            print("********")
        else:
            print("\n")
            print("****************")
            print("SORRY;;;WRONG PASSWORD")
            print(" TO TRY AGAIN PRESS 1")
            print("PRESS ANY OTHER KEY TO GO BACK TO ADMIN PORTAL")
            print("****************")
            e=int(input("ENTER YOUR OPTIONS"))
            if y==1:
                print("\n")
                userdataA_()
            else:
                print("\n")
                admin_login()
                    
 
    print("\n")
    print("****************")
    print("PRESS 1 TO CONTNUE")
    print("PRESS 2 TO GO BACK TO ADMIN LOGIN")
    print("PRESS ANY KEY TO GO BACK TO MAIN MENU")
    print("****************")
    r=int(input("ENTER YOUR CHOICE"))
    print("\n")
 
    if r==1:
        admin_DATA_()
    if r==2:
        admin_login()
    else:
        main()
    print("\n")
 
 
 
 
 
 
 
 
#SIGNUP BY USER
def Signup_():
        print("  WELCOME;;; REGISTER YOURSELF QUICKLY AND LEAVE YOUR HOLIDAYS TO US")
        print("****************")
        a=input("ENTER YOUR NAME")
        o=int(input("ENTER YOUR AGE"))
        b=input("ENTER YOUR EMAIL")
        c=input("ENTER YOUR ADDRESS")
        d=int(input("ENTER THE ID SENT TO YOU ON YOUR PHONE"))
        e=int(input("ENTER THE PASSWD SENT TO YOUR PHONE"))
        print("****************")
        t1="INSERT INTO Customers(Name,Age,EMAIL_ID,Address,ID,Passwd) VALUES(%s,%s,%s,%s,%s,%s)"
        s=(a,o,b,c,d,e)
        cursor.execute(t1,s)
        mydb.commit()
        print("YOU ARE SUCCESSFULLY REGISTERED TO OUR AGENCY")
 
        print("***************")
        print("Do U WISH TO GO TO LOGIN PORTAL:IF YES PRESS 1","\n","TO GO TO HOME PAGEPRESS 2","\n")
        print("***************")
        x=int(input("Enter Your Choice"))
        if x==1:
            print("\n")
            user_()
        if x==2:
            print("\n")
            main()   
        else:
            print("\n")
            print("************")
            print("SORRY WRONG OPTION")
            print("YOU ARE REDIRECTED TO HOME PAGE")
            print("************")
            print("\n")
            main()
            print("\n")    
        
#USER DATA SEEN BY USER
def Udata_():
    cursor.execute("SELECT * FROM CUSTOMERS")
    res=cursor.fetchall()
    for i in res:
        if(i[4]==l and i[5]==p):
            print("WELCOME :")
    print("***********")
    print("YOUR DETAILS ARE AS FOLLOWS","\n","Name :",i[0],"\n","AGE",i[1],"\n","EMAIL_ID:",i[2],"\n","ADDRESS:",i[3],"\n")
    print("***********")
   
 
    print("************")
    print("PRESS 1 TO BACK TO HOME PAGE","\n","PRESS 2 TO GO BACK TO YOUR USER PORTAL","\n","PRESS 3 TO LEAVE SITE")
    print("************")
    K=int(input("PLEASE ENTER YOUR OPTIONS"))
    
    if(K==1):
        print("\n")
        main()
    if(K==2):
        print("\n")
        user_()
    if(K==3):
        print("\n")
        print("PORTAL DOWN ;;;PLEASE TRY AGAIN;;;SORRY FOR THE PROBLEM")
        
    print("\n")
                   
def ForgotPasswd_():
    print("PASSWORD CHANGE LINK HAS BEEN SEND TO YOUR REGISTERED EMAIL-ID")
    print("\n")
    print("PRESS 1 TO BACK TO HOME PAGE","\n","PRESS 2 TO GO BACK TO YOUR USER PORTAL","\n","PRESS 3 TO LEAVE SITE")
    K=int(input("PLEASE ENTER YOUR OPTIONS"))
    
    if(K==1):
        main()
 
    if(K==2):
        user_()
 
    if(K==3):
       print("PORTAL DOWN ;;;PLEASE TRY AGAIN;;;SORRY FOR THE PROBLEM")
       print("\n")
 
 
#CALENDER/PLACES WHERE THEY CUSTOMER HAS GONE AND WANTS TO GO
def calender_():
        print("**************")
        print("PRESS 1 TO CHECK YOUR UPCOMING/PAST TRIPS")
        print("PRESS 2 TO PLAN A TOUR")
        print("**************")
        q=int(input("PLEASE ENTER YOUR OPTION"))
        #NEW LINE CHARACTER
        print("\n")
 
 
        #DETAILS OF THE TRIP
        if(q==1):
            cursor.execute("SELECT * FROM Trips" )
            leg=0
            ref=cursor.fetchall()
            #WAY TO FIND THE SPECIFIC PERSON IN THE LIST OF CUSTOMERS
            for key in ref:
                if(key[0]==l):
                    leg=1
                    break
                else:
                    leg=0
            if(leg==1):
 
                #DETAILS OF THE TRIP
                print("YOUR TRIP DETAILS ARE AS FOLLOWS")
                print("*************")
                print("PAST LOCATION :",key[1],"\n","Date:",key[2])
                print("FUTURE LOCATION:",key[3],"\n","DATE:",key[4])
                print("*************")
 
        #PACKAGES/BOOKING OF THE TRIP  
        if(q==2):
            print("**************")
            print("PLEASE SELECT YOUR BEST PACKAGES AVAILABLE")
            print("PRESS 1 FOR 3 NIGHT AND 2 DAYS IN USA")
            print("PRESS 2 FOR 10 DAY TRIP TO EUROPE")
            print("PRESS 3 FOR 5 DAY TRIP TO CHINA")
            print("PRESS 4 FOR 3 DAY TRIP TO  GUJARAT")
            print("PRESS 5 FOR 6 DAY TRIP TO GOA")
            print("PRESS 6 FOR ANY OTHER PLACE")
            print("**************")
             
            d=int(input("ENTER YOUR CHOICE"))
            if(d in (1,2,3,4,5)):
                print("REQUESTED BROCHURE AND DETAILS ARE SEND TO YOUR REQUESTED EMAIL ID")
 
 
            if(d==6):
                print("*************")
                a=input("ENTER YOUR LOCATION")
                b=int(input("ENTER THE BUDGET OF YOUR TRIP"))
                c=input("ENTER THE DURARTION OF YOUR TRIP")
                print("*************")
                print("ALL NECESSARY INFORMATION INCLUDING BROCHURE AND DISCOUNT BOOKLET IS SEND TO OUR REGISTERED EMAIL ID")
            print("\n")
 
        print("**********")
        print("PRESS 1 TO BACK TO HOME PAGE","\n","PRESS 2 TO GO BACK TO YOUR USER PORTAL","\n","PRESS 3 TO LEAVE SITE")
        print("**********")
 
        K=int(input("PLEASE ENTER YOUR OPTIONS"))
    
        if(K==1):
            main()
 
        if(K==2):
            user_()
 
        if(K==3):
           print("*******************")
           print("PORTAL DOWN ;;;PLEASE TRY AGAIN;;;SORRY FOR THE PROBLEM")
           print("*******************")
           sys.exit()
           print("\n")
 
            
 
#USER PORTAL
def user_():
        global l
        global p
        l=int(input("ENTER YOUR ID PLEASE"))
        p=int(input("ENTER YOUR PASSWORD"))
            
        cursor.execute("SELECT * FROM Customers")
        res=cursor.fetchall()
        flag=0
        for i in res:
            if(i[4]==l and i[5]==p):
               flag=1
               break
        if(flag==1):
 
            print("\n")
            print("WELCOME:",i[0])
            print("**********")
            print("PRESS 1 TO VIEW DATA")
            print("PRESS 2 TO CHECK YOUR CALENDER")
            print("Press 3 To Go Back To Login")
            print("Press 4 To Go To Home Page")
            print("**********")
            print("\n")
            c=int(input("PLEASE ENTER YOUR CHOICE"))
            print("\n")
 
            if c==1:
                Udata_()
                
            if c==2:
                calender_()
       
            if c==3:
                Udata_()
                
            if c==4:
                main()
 
            
        else:
           print("SORRY NO USER;;;;PLEASE TRY AGAIN")
           print("\n")
           user_()
           
#LOGIN PORTAL
def login_():
    print("WELCOME TO THE SIGN IN PORTAL"         )
    print("**********")
    print("PRESS 1 IF YOU ARE A USER")
    print("PRESS 2 IF YOU ARE AN ADMIN")
    print("PRESS 3 IF YOU WANT TO SIGN UP")
    print("PRESS 4 IF FORGET PASSWORD")
    print("***********")
    y=int(input("PLEASE ENTER YOUR CHOICE"))
    print("\n")
    #OPTION SELECTION
    if(y==1):
        print("                 WELCOME USER"            )
        
        user_()
        
    if y==2:
        
        admin_login() 
 
    if y==3:
        print("\n")
        print("**************")
        print("PRESS 1 IF YOU WANT TO REGISTER AS AN ADMIN")
        print("PRESS 2 IF YOU WANT TO REGISTER AS A USER")
        print("PRESS ANY OTHER KEY TO GO BACK ")
        print("**************")
        p=int(input("ENTER YOUR OPTIONS"))
        if p==1:
            print("\n")
            SignupA_()
        if p==2:
            print("\n")
            Signup_()
        else:
            print("\n")
            login_()
 
    if y==4:
        #FORGOT PASSWORD OPTION
        global j
        j=int(input("ENTER YOUR ID PLEASE "))
        cursor.execute("SELECT * FROM Customers")
        res=cursor.fetchall()
        for i in res:
            if(i[4]==j):
                break
            else:
                print("PLEASE TRY AGAIN")
                print("\n")
                login_()
 
                
        print("THE PASSWORD CHANGE LINK IS SEND TO YOUR REGISTERED EMAIL-ID:")
        a=int(input("ENTER THE NEW PASSWORD YOU CHANGED"))
        cursor.execute("UPDATE Customers SET Passwd='a' WHERE ID='j' ")
        mydb.commit()
        print("\n")
        print("TRY NOW ")
        login_()
        print("\n")
        
#COMPLAINT REGISTRATION
def admin1_():
    print("PLEASE WRITE DOWN COMPLAINT")
    a=input( "")
    print("YOUR COMPLAINT HAS BEEN RECORDED AND SENT TO THE ADMINISTRATION","\n"
          "SORRY FOR THE INCONVIENCE YOU WILL INFORMED WITHIN 2 HOURS")
 
 
#HOME PAGE
def main():
    print("                  WELCOME TO TRAVELETO:YOUR PERFECT TRAVEL PARTNER     ")
    print("\n")
    print("***************")
    print("PRESS 1 FOR LOGIN")
    print("PRESS 2 TO VIEW OUR BEST PACKAGES")
    print("PRESS 3 TO CONTACT TO OUR ADMINISTRATION  ")
    print("***************")
    print("\n")
    x=int(input("ENTER YOUR OPTIONS"))
    print("\n")
 
    if(x==1):
        login_()
    if x==2:
        print("**************")
        print("YOUR BEST PACKAGES AVAILABLE")
        print(" 3 NIGHT AND 2 DAYS IN USA")
        print(" 10 DAY TRIP TO EUROPE")
        print(" 5 DAY TRIP TO CHINA")
        print(" 3 DAY TRIP TO  GUJARAT")
        print(" 6 DAY TRIP TO GOA")
        print("**************")
        print("\n")
        print("LOGIN TO VIEW ARE BEST DEALS")
        print("PRESS 'Y' TO CONTINUE","\n","PRESS 'NO' TO GO BACK TO HOME PAGE")
        y=input("ENTER YOUR OPTION")
        if y=='Y':
              print("\n")
              login_()
              print("\n")
        else:
              print("\n")
              main()
              print("\n")
    if x==3:
        admin1_()
    else:
       main()
 
 
main()
