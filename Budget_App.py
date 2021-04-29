class Category:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # method
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        if amount > self.amount:
            return False
        else:
             return True
       

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} from {} category".format(amount, self.category)

    def transfer(self, amount, category):
        if not self.check_balance(amount):
            return "Insufficient funds, transfer not possible"
        else:
            self.amount -= amount
            category.deposit(amount)
            return "You have succesffully transfered: $ {} to {} category".format(amount, category.category)
        

    
clothing_category = Category("Clothing", 200)
food_category = Category("Food", 200)
car_category = Category( "Car Expenses", 250)
grooming_category = Category("Hair Salon Visits", 100)
education_category = Category("Tuition", 1200)


#print(food_category.budget_balance())
#print(food_category.check_balance(300))
print(food_category.transfer(20, car_category))

