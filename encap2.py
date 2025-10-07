coins = 100
coins =100 + 500
print("i have;",coins,"coins")

class Pigybank:
    def __init__(self,coins):
        self._coins=coins #protected
        #getter this enables us to add in more coins into our bank
        self.put_in(coins)
    def put_in(self,amount):
        if amount <=0:
        #this show that incase the amount put is less than or equal to 0, the programm raises a value error.
            raise ValueError("Add real money")
        self._coins +=amount
    def take_out(self,amount):
        if amount> self.coins:
        #this shows that the amount to be takenout is greater than the amount present
            raise ValueError("Be real")
        if amount >self.coins:
            raise ValueError("Money is coming") 
        self.coin -= amount
    def how_much(self):
        return self._coins           

#Amount present
Assy =Pigybank(500000)

#print("Assy's Box has",Assy.coins) 

print("Assy's box has:",Assy.how_much())


