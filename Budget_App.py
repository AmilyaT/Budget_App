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
            return "Insufficient funds available for this transaction. Your current balance is: {}".format(self.amount)
        elif amount < self.amount:
            return "Your request has been processed."
    
        

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} from {} category".format(amount, self.category)

    def transfer(self, amount, category):
        return self.withdraw(amount) + "" + category.deposit(amount)

    
clothing_category = Category("Clothing", 200)
food_category = Category("Food", 200)
car_category = Category( "Car Expenses", 250)
grooming_category = Category("Hair Salon Visits", 100)
education_category = Category("Tuition", 1200)


#print(food_category.budget_balance())
print(food_category.check_balance(300))

