from _2_admin_operations import admin_operations
class Main_admin:
    def execute(self):
        choice=int(input("\n1.ADD ITEM \n2.EDIT ITEM \n3.VIEW ITEM \n4.REMOVE ITEM \nEnter your choice : "))
        if choice ==1:
            print()
            print("****ADD ITEM*****")
            print()
            oper_obj.add_item()
            print()
        elif choice ==2:
            print()
            print("****EDIT ITEM*****")
            print()
            oper_obj.edit_item()
            print()
        elif choice ==3:
            print()
            print("****VIEW ITEM*****")
            print()
            oper_obj.view_food()
            print()
        elif choice ==4:
            print()
            print("****REMOVE ITEM*****")
            oper_obj.remove_item()
        else:
            print()
            print("invalid entry \nplease try again")

if __name__ == "__main__":
    admin_obj = Main_admin()
    oper_obj = admin_operations()
    while True:
        admin_obj.execute()