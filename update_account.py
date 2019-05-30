import pymysql
con=pymysql.connect("localhost","root","password","ATM")
c=con.cursor()

def update():
    print("ENTER BELOW DETAILS TO UPDATE YOUR ACCOUNT")
    a=input("Enter your account number")
    print("What you want to update on your account\n")

    print("enter 1 to update your name")
    print("enter 2 to update your password")
    x=int(input("enter your choice"))

    if x==1:
        nam=input("if you want to update your name then enter your new name carefully")
        com="update account set name='%s' where account_no='%s'"%(nam,a)
    if x==2:
        pas=input("if you want to update your password then enter your new password carefully")
        com="update account set password='%s' where account_no='%s'"%(pas,a)

    r=c.execute(com)
    if r>0:
        print("record updated")
    else:
        print("record not updated! try again")

    con.commit()
    con.close()
