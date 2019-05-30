import pymysql
conn=pymysql.connect("localhost","root","password","BANK")
c=conn.cursor()

def acc():


        n = input("NAME: \t\t")
        cd=0
        q = input("Create secured key/password: \n")
        while len(p)==4:
            p=q
        else:
            print("please enter valid number\n")
        b=300200

        #m = input("Enter amount to be deposite\n")
        m=0
        qry1="select *from account"
        r = c.execute(qry1)
        for data in c.fetchall():
            cd=cd+5
        a=b+cd

        qry = "Insert into account(name,password,no,money)values('%s','%s','%s','%s')" % (n, p, a, m)

        r1 = c.execute(qry)

        if r1 > 0:
            print("Account created succesfully")
            print("*******THANKYOU*******")

        else:
            print("ERROR! please enter all columns carefully")

        conn.commit()

acc()