import pymysql
con=pymysql.connect("localhost","root","password","ATM")
c=con.cursor()

def passbook():
    x=int(input("enter your account number carefully\n"))
    qry="select *from account where account_no='%s'"%(x)
    r=c.execute(qry)

    for data in c.fetchall():
       print(data[0]+" \tpassword:-"+data[1]+"\t account_n0:-"+data[2]+"\t balance:- "+data[3])

    con.commit()
    con.close()

