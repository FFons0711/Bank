import re
import sys
import csv
import random
import tickets
import matplotlib.pyplot as plt


class Client:
    def __init__(self, name, last_name, bank_account, balance, credit_score):
        self.name = name
        self.last_name = last_name
        self.bank_account = bank_account
        self.balance = balance
        self.credit_score = credit_score

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise NameError("Insufficient balance")
        self._balance = balance

    def __str__(self):
        return f"Welcome to the 'CS50 Bank' Mr/Mrs {self.last_name}, your current balance is: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


def main():
    """
    This is the main function
    """
    print("Welcome to the 'CS50 Bank', please type your bank acount")
    while True:
        try:
            number = input("Bank acount: ")

            if validate_card(number):
                client = get_client(number)
                print(client)
            else:
                raise ValueError
        except ValueError:
            print("Your bank account must have 16 characters, only numbers")
        except NameError:
            print("You don't have a account, do you want to get one?")
            if yes_no_validation():
                add_user()
            else:
                print("Thanks for your visit!")
                break
        except EOFError:
            sys.exit("\nThank for choice us!")
        else:
            menu(client)
            pass


def menu(client):
    """
    This function deploy the menu of the application in an infinite loop
    to interact with the user
    :param client: costumer
    :type client: object
    :return: None
    """
    while True:
        print(
            """
                [1] - Add balance
                [2] - Whitdraw balance
                [3] - Transfer balance
                [4] - Investment
                [5] - Get ticket
                [6] - Exit

            Choose the option of your preference
            """
        )

        try:
            choice = input()
            ["1", "2", "3", "4", "5", "6"].index(choice)

        except:
            print("You have to choose a valid option")
            pass

        else:
            if choice == "1":
                if user_deposit(client):
                    pass
                else:
                    break

            elif choice == "2":
                if user_withdraw(client):
                    pass
                else:
                    break

            elif choice == "3":
                if transfer(client):
                    pass
                else:
                    break

            elif choice == "4":
                if investment(client):
                    pass
                else:
                    break

            elif choice == "5":
                try:
                    turn = tickets.decorator()
                except StopIteration:
                    print(
                        "We have given all the tickets for today, please come back tomorrow"
                    )
                    pass
                else:
                    print(f"You have {turn}")
                    print("Please wait, you will be attended soon")
                    print("Do you want to do something more?")
                    if yes_no_validation():
                        pass
                    else:
                        break
            else:
                break


def user_deposit(client):
    """
    This function is used to deposit money to the account and
    then update the database
    :param client: costumer
    :type client: object
    :return: value of yes_no_validation function
    :rtype: bool
    """
    while True:
        try:
            amount = float(input("Amount: "))
            client.deposit(amount)
        except ValueError:
            print("Please write a valid amount")
            pass
        else:
            update_database(client.bank_account, client.balance)
            print(f"Deposit successful!\nYour current balance is: ${client.balance}")
            print("Do you want to do something more?")
            if yes_no_validation():
                return True
            return False


def user_withdraw(client):
    """
    This function is used to withdraw money of the account and
    then update the database
    :param client: costumer
    :type client: object
    :return: value of yes_no_validation function
    :rtype: bool
    """
    while True:
        try:
            amount = float(input("Amount: "))
            client.withdraw(amount)
        except ValueError:
            print("Please write a valid amount")
            pass
        except NameError:
            print("Insufficient balance")
            pass
        else:
            update_database(client.bank_account, client.balance)
            print(f"Withdraw successful!\nYour current balance is: ${client.balance}")
            print("Do you want to do something more?")
            if yes_no_validation():
                return True
            return False


def transfer(client):
    """
    This function make a transfer between users
    :param client: costumer
    :type client: object
    :return: value of yes_no_validation function
    :rtype: bool
    """
    while True:
        try:
            receiver_account = input(
                "Please enter the account you are transferring to:  "
            )
            if validate_card(receiver_account):
                receiver = get_client(receiver_account)
            else:
                raise ValueError
        except ValueError:
            print("The account must have 16 characters, only numbers")
        except NameError:
            print("This account doesn't exits")
        else:
            while True:
                try:
                    amount = float(input("Amount: "))
                    client.withdraw(amount)
                    receiver.deposit(amount)
                except ValueError:
                    print("Please write a valid amount")
                    pass
                except NameError:
                    print("Insufficient balance")
                    pass
                else:
                    update_database(client.bank_account, client.balance)
                    update_database(receiver.bank_account, receiver.balance)
                    print(
                        f"Transfer successful!\nYour current balance is: ${client.balance}"
                    )
                    print("Do you want to do something more?")
                    if yes_no_validation():
                        return True
                    return False


def yes_no_validation():
    """
    This function validate if the user's input is Y or N
    :return: True or False
    :rtype: bool
    """
    while True:
        print("Please type Y|N for Yes/No?")
        try:
            answer = input().upper()
            ["Y", "N"].index(answer)
        except:
            print("Write a valid option")
            pass
        else:
            if answer == "Y":
                return True
            return False


def validate_card(s: str) -> bool:
    if re.match(r"^\d{16}$", s):
        return True
    return False


def get_client(n):
    """
    This function get a client for the database
    :param n: customer bank account
    :type n: str
    :return: costumer
    :rtype: object
    """
    counter = 0

    with open("database.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["bank_account"] == n:
                counter += 1
                return Client(
                    row["name"],
                    row["last_name"],
                    row["bank_account"],
                    float(row["balance"]),
                    int(row["credit_score"]),
                )

        if counter == 0:
            raise NameError("User not found")


def update_database(n, balance):
    """
    This function update the database when any transaction is made
    :param n: This is the client's bank account that it'll be modificated
    :type n: str
    :param balance: This is the balance to update
    :type balance: float
    :return: None
    """
    list_updated = []

    with open("database.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            list_updated.append(row)

    for i in range(1, len(list_updated)):
        if list_updated[i]["bank_account"] == n:
            list_updated[i]["balance"] = balance

    with open("database.csv", "w") as csvfile:
        fieldnames = ["name", "last_name", "bank_account", "balance", "credit_score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in list_updated:
            writer.writerow(i)


def generate_number():
    """
    This function generate a new customer bank account, checking that isn't exists in the actual database
    :return bank account's number
    :rtype: str
    """
    while True:
        counter = 0
        new_number = "12497602" + str(random.randint(10**7, ((10**8) - 1)))

        with open("database.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["bank_account"] == new_number:
                    counter += 1
        if counter == 0:
            return new_number


def add_user():
    """
    This function add a user to the local database
    :return: None
    """
    print("We need some data for you")
    name = input("Name: ")
    last_name = input("Last name: ")
    bank_account = generate_number()
    l = [name, last_name, bank_account, 0, 560]
    with open("database.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(l)
    print("Your account is ready, you can sign up now")
    print(f"You bank account is {bank_account}")


def compound_interest(amount, r, n, t):
    """
    This function returns a compound interest of an investment and a list
    with the elements of the ordinate axis for the subsequent graph of this behavior.

    :param amount: initial amount
    :type amount: float
    :param r: annual interest rate
    :type r: float
    :param n: number of times interest is capitalized per year
    :type n: int
    :param t: number of years
    :type n: int
    :return: final amount after investment, list of ordinate axis for compound interest,
     list of ordinate axis for normal investment
    :rtype: float, list, list
    """
    b = [amount + (x * amount * r) for x in range(t)]
    a = []
    for i in range(1, t + 1):
        a.append(round(amount * (1 + (r / n)) ** (n * i), 2))

    return a[len(a) - 1], a, b


def get_graphic(client, x, y1, y2):
    """
    This function save a img with the behavior of the compund interest
    vs regular saving for the client
    :param client: client that request the services
    :type client: object
    :param x: time of investment (abscis axis)
    :type x: list
    :param y1: ordinate axis for compound interest
    :type y1: list
    :param y2: ordinate axis for normal investment
    :type y2: list
    """
    fig, ax = plt.subplots(layout="constrained")
    ax.set_title("Investment growth with compound interest")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Amount ($)")
    ax.plot(x, y1, label="Compound interest")
    ax.plot(x, y2, label="Normal invest")
    ax.grid(True)
    ax.legend()
    fig.savefig(f"imgs/{client.name}'s_graphic.jpg", format="jpg")


def investment(client):
    """
    This function deploy de investment option of the menu
    :param client: client that request the services
    :type client: object
    :return: value of yes_no_validation function
    :rtype: bool
    """
    if client.credit_score < 660:
        percentage = 10
    elif 660 < client.credit_score < 730:
        percentage = 16
    else:
        percentage = 22

    print(
        f"After an exhaustive search of your credit score we have determined that the percentage of return for your investment is {percentage}% "
    )

    while True:
        try:
            amount = float(input("Please type your initial amount: "))
            n = int(
                input(
                    "Please type the number of times interest is capitalized per year: "
                )
            )
            years = int(
                input(
                    "Please type the number of years that you will keep your investment: "
                )
            )
        except:
            print("Please type a correct answer")
            pass
        else:
            final_amount, y1, y2 = compound_interest(amount, percentage / 100, n, years)
            print(f"This is your final amount: ${final_amount}")
            get_graphic(client, range(1, years + 1), y1, y2)
            print("Do you want to do something more?")
            if yes_no_validation():
                return True
            return False


if __name__ == "__main__":
    main()
