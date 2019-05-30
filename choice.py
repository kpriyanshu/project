import update_account
import login_account
import account_creation
import transfer
import passbook
print("---------------------WELCOME TO ECO BANK--------------------\n")
print("    If you are \n Old Coustmer(enter 1.)  \n New Coustmer(enter 2.)\n")
x=int(input("Enter your choice\n"))

if(x==1):
    print("Enter 1. Update your details ")
    print("Enter 2. Deposite money to your account")
    print("Enter 3. transer money to other")
    print("Enter 4. To print passbook")
    print("Enter 5. logout")
    y=int(input("enter your choice"))

    if(y==1):
        update_account.update()
    if (y == 2):
        login_account.login()

    if(y==3):
        transfer.trans()

    if(y==4):
        passbook.passbook()

    if(y==5):
        pass



if(x==2):
    print("CREATE ACCOUNT")
    account_creation.acc()