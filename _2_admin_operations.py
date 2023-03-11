from _3_food import *
class admin_operations:
    n=0
    food_list =[]
    user_list =[]

    def admin(self):
        choice=int(input("\n1.ADD ITEM \n2.EDIT ITEM \n3.VIEW ITEM \n4.REMOVE ITEM \nEnter your choice : "))
        if choice ==1:
            print()
            print("****ADD ITEM*****")
            print()
            food_id = f"FD00{self.n+1}"
            food_name = input("Enter your food name : ")
            food_quandity = input("Enter food quandity : ")
            food_price = float(input("Enter food price : "))
            food_discount = input("Enter your discount : ")
            food_stock = int(input("Enter food stock : "))
            food_obj = Food(Food_id=food_id,Food_name=food_name,Food_quandity=food_quandity,Food_price=food_price,Food_discount=food_discount,Food_stock=food_stock)
            self.food_list.append(food_obj)
            self.n+=1
            print("Food added successfully")
        elif choice ==2:
            print()
            print("****EDIT ITEM*****")
            print()
            chck_id = input("Enter your food id to edit : ")
            for food in self.food_list:
                if food.getfoodid() == chck_id:
                    new_foodname = input("Enter updated food name : ")
                    new_foodquandity = input("Enter updated food quandity : ")
                    new_foodprice = float(input("Enter updated food price : "))
                    new_fooddiscount = input("Enter updated food discount : ")
                    new_foodstock = input("Enter updated food stock : ")
                    food.setfoodname(new_foodname)
                    food.setfoodquandity(new_foodquandity)
                    food.setfoodprice(new_foodprice)
                    food.setfooddiscount(new_fooddiscount)
                    food.setfoodstock(new_foodstock)
                    return self.food_list
                else:
                    print("invalid intex")
                    print()
        elif choice ==3:
            print()
            print("****VIEW ITEM*****")
            print()
            for food in self.food_list:
                print(food,"\n")
                print()

        elif choice ==4:
            print()
            print("****REMOVE ITEM*****")
            chck_id = input("Enter your food id to edit : ")
            for food in self.food_list:
                if food.getfoodid() == chck_id:
                    self.food_list.remove(food)
                    print("\nFood removed sucessfully")
                    break
            
                else:
                    print("invalid entry\ntry again")
            
            
        



    # def add_item(self):
    #     food_id = f"FD00{self.n+1}"
    #     food_name = input("Enter your food name : ")
    #     food_quandity = input("Enter food quandity : ")
    #     food_price = float(input("Enter food price : "))
    #     food_discount = input("Enter your discount : ")
    #     food_stock = int(input("Enter food stock : "))
    #     food_obj = Food(Food_id=food_id,Food_name=food_name,Food_quandity=food_quandity,Food_price=food_price,Food_discount=food_discount,Food_stock=food_stock)
    #     self.food_list.append(food_obj)
    #     self.n+=1
    #     print("Food added successfully")

    # def view_food(self):
    #     for food in self.food_list:
    #         print(food,"\n")

    # def edit_item(self):
    #     chck_id = input("Enter your food id to edit : ")
    #     for food in self.food_list:
    #         if food.getfoodid() == chck_id:
    #             new_foodname = input("Enter updated food name : ")
    #             new_foodquandity = input("Enter updated food quandity : ")
    #             new_foodprice = float(input("Enter updated food price : "))
    #             new_fooddiscount = input("Enter updated food discount : ")
    #             new_foodstock = input("Enter updated food stock : ")
    #             food.setfoodname(new_foodname)
    #             food.setfoodquandity(new_foodquandity)
    #             food.setfoodprice(new_foodprice)
    #             food.setfooddiscount(new_fooddiscount)
    #             food.setfoodstock(new_foodstock)
    #             return self.food_list
    #     else:
    #         print("invalid intex")

    # def remove_item(self):
    #     chck_id = input("Enter your food id to edit : ")
    #     for food in self.food_list:
    #         if food.getfoodid() == chck_id:
    #             self.food_list.remove(food)
    #             print("\nFood removed sucessfully")
    #             break
            
    #     else:
    #         print("invalid entry\ntry again")
# ***************************************************************************************************
    def register(self):
        name = input("Enter your name : ")
        phone = input("Enter your phone number : ")
        email = input("Enter your email id : ")
        address = input("Enter your address : ")
        password = input("Enter your password : ")
        user_detls = register(Name=name,Phone=phone,email=email,address=address,password=password)
        self.user_list.append(user_detls)
        print("*****REGISTERED SUCCESSFULLY*****")

    def user(self):
        choice = int(input("\n1.Register \n2.Log in \nselect an option : "))
        if choice == 1:
            name = input("Enter your name : ")
            phone = input("Enter your phone number : ")
            email = input("Enter your email id : ")
            address = input("Enter your address : ")
            password = input("Enter your password : ")
            user_detls = register(Name=name,Phone=phone,email=email,address=address,password=password)
            self.user_list.append(user_detls)
            print("*****REGISTERED SUCCESSFULLY*****")

        elif choice == 2:
            email_ =input("Enter your registered email id : ")
            password_ = input("Enter your password : ")
            for id in self.user_list:
                if id.getemail() == email_ and id.getpassword() == password_:
                    choice = int(input("\n1.Place new order \n2.Order History \n3.Update Profile \nselect an option"))
                    if choice ==1:
                        for food in self.food_list:
                            print(food,"\n")

                else:
                    print("invalid credentials\ntry again") 


    
