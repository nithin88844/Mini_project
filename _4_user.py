from _2_admin_operations import admin_operations
from _1_admin import Main_admin
class user:
    def run(self,choice):
        if choice == 1:
            print("***Admin***")
            oper_obj.admin()


        elif choice == 2:
            print("***user***")
            oper_obj.user()
    

user_obj = user()
oper_obj = admin_operations()
admin_obj = Main_admin()
while True:
    user_obj.run(choice=int(input("1.Admin \n2.User \nselect an option : ")))
