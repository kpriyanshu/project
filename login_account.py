import pymysql
conn=pymysql.connect("localhost","root","password","ATM")
c=conn.cursor()

def login():
    print("Enter the below details to login your acount")
    n=input("Enter your name")
    p=input("enter your password")
    qry="select name password from account where name='%s' and password='%s'"%(n,p)
    r=c.execute(qry)
    if r>0:
        print("login succesfully")

        a=input("enter your account number")
        d=int(input("enter the amount to deposite money"))
        ab="select *from account where account_no='%s'"%(a)
        k=c.execute(ab)
        for data in c.fetchall():
            dat = data[3]
            dataa = int(dat)
            n=dataa+d


        dep="update account set amount='%s' where account_no='%s'"%(n,a)
        p = c.execute(dep)

        if p>0:
            print("deposited sucessfully")
        else:
            print("server problem")


    else:
        print("login feild! try again")


    conn.commit()
    conn.close()


