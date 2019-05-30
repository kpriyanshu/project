import pymysql
con=pymysql.connect("localhost","root","password","ATM")
c=con.cursor()

def trans():
    x=int(input("Enter your account number"))
    s=int(input("Enter the amount you want to transfer"))

    qry = "select *from account where account_no='%s'" % (x)
    r = c.execute(qry)

    for data in c.fetchall():
        dat = data[3]
        dataa = int(dat)
        bb=dataa-s
        cc=500

        if bb>cc:

            n = dataa - s
            h = int(input("enter the account number of reciver"))
            dep = "update account set amount='%s' where account_no='%s'" % (n, x)
            p = c.execute(dep)

            mm = "select *from account where account_no='%s'" % (h)
            r = c.execute(mm)

            for data in c.fetchall():
                ll = data[3]
                v = int(ll)
                nn = v + s

                dep = "update account set amount='%s' where account_no='%s'" % (nn, h)
                pp = c.execute(dep)

                if pp > 0:
                    print("deposited sucessfully")
                else:
                    print("server problem")


        else:
            print("you have no sufficent money to transfer!!")
            s=0






    con.commit()
    con.close()



