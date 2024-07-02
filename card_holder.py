class cardHolder():
    def __init__(self, cardNum,pin,firstname, lastname,balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def get_cardNum(self):
        return self.cardNum
    
    def get_pin(self):
        return self.pin
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_balance(self):
        return self.balance
    

    def set_cardnum(self,new_value):
        self.cardNum = new_value

    def set_pin(self,new_value):
        self.pin = new_value
    
    def set_firstname(self,new_value):
        self.firstname = new_value

    def set_lastname(self,new_value):
        self.lastname = new_value

    def set_balance(self,new_value):
        self.balance = new_value

    def print_out(self):
        print("Card Number: ", self.get_cardNum)
        print("Pin :", self.get_pin)
        print("FirstNAme :", self.get_firstname)
        print("Lastname : ", self.get_lastname)
        print("Balance :", self.get_balance)
    
    