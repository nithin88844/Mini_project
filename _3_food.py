class Food:
    def __init__(self,Food_id,Food_name,Food_quandity,Food_price,Food_discount,Food_stock):
        self.Food_id = Food_id
        self.Food_name = Food_name
        self.Food_quandity = Food_quandity
        self.Food_price = Food_price
        self.Food_discount = Food_discount
        self.Food_stock = Food_stock

    def __str__(self):
        return f"Food id : {self.Food_id} \nFood name : {self.Food_name} \nFood quandity : {self.Food_quandity} \nFood price : {self.Food_price} \nFood discount : {self.Food_discount} \nFood stock : {self.Food_stock}"

    def getfoodid(self):
        return self.Food_id
    def setfoodid(self,new_foodid):
        self.Food_id = new_foodid
    
    def getfoodname(self):
        return self.Food_name
    def setfoodname(self,new_foodname):
        self.Food_name = new_foodname

    def getfoodquandity(self):
        return self.Food_quandity
    def setfoodquandity(self,new_foodquandity):
        self.Food_quandity = new_foodquandity

    def getfoodprice(self):
        return self.Food_price
    def setfoodprice(self,new_foodprice):
        self.Food_price = new_foodprice

    def getfooddiscount(self):
        return self.Food_discount
    def setfooddiscount(self,new_discount):
        self.Food_discount = new_discount

    def getfoodstock(self):
        return self.Food_stock
    def setfoodstock(self,new_foodstock):
        self.Food_stock = new_foodstock


class register:
    def __init__(self,Name,Phone,email,address,password):
        self.Name = Name
        self.Phone = Phone
        self.email = email
        self.address = address
        self.password = password

    def __str__(self):
            return f"Name : {self.Name} \nPhone : {self.Phone} \nEmail : {self.email} \nAddress : {self.address} \nPassword : {self.password}"
    
    def getname(self):
        return self.Name
    def setname(self,new_name):
        self.Name = new_name

    def getphone(self):
        return self.Phone
    def setphone(self,new_phone):
        self.Phone = new_phone

    def getemail(self):
        return self.email
    def setemail(self,new_email):
        self.email = new_email

    def getaddress(self):
        return self.address
    def setaddress(self,new_address):
        self.address = new_address

    def getpassword(self):
        return self.password
    def setpassword(self,new_password):
        self.password = new_password