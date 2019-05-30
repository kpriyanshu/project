import pymysql
conn=pymysql.connect("localhost","root","password","ATM")
c=conn.cursor()

def acc():

        i=0
        n = input("NAME: \n")

        p = input("Create secured key/password: \n")




        a = input("Set account number\n")
        m = input("Enter amount to be deposite\n")
        qry = "Insert into account(name,password,account_no,amount)values('%s','%s','%s','%s')" % (n, p, a, m)

        r = c.execute(qry)
        if r > 0:
            print("Account created succesfully")
            print("*******THANKYOU*******")

        else:
            print("ERROR! please enter all columns carefully")

        conn.commit()

