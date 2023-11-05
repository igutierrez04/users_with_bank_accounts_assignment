# users_with_bank_accounts_assignment

Create a User class that has an association with the BankAccount class. You should not have to change anything in the BankAccount class.

For example, from the User class we should be able to deposit money into the user's account

But our User class does not have a self.account_balance attribute. What it does have is an instance of a BankAccount by the name of self.account That means that we'll be mirroring the methods created in the BankAccount class like make_deposite (and other methods referencing self.account_balance). But we'll be calling on the BankAccount class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.

Remember in our User methods, we can now access the BankAccount class through our self.account attribute.

    - Create a User class with an __init__ method
    - Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    - add a make_withdrawal method to the User class that class on it's bank account's instance methods.
    - add a display_user_balance method to the User class that displays user's account balance
    - SENPAI BONUS: add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the User's account into another user's account