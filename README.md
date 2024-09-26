# CS50 Bank

#### Video Demo:  <URL HERE>
#### Description:

<div style="text-align: justify;">
This project is a simulation of a banking system developed in Python. The application allows users to perform various banking operations such as account creation, balance enquiries, transfers, deposits,a ticket system for customer service and simulations of financial calculations such as compound interest. It is ideal for learning and experimenting with key programming concepts, data structures, and financial workflows in a simulated environment. It also corresponds to the evolution of my final project for the Harvard course "CS50 Introduction to programming with Python". Thanks Platzi 💚.
</div>

<div style="text-align: justify;">
The bank’s operation is found within the <em>main.py</em> file, whose main function develops an infinite loop where the client is welcomed, asking for their account number and going through a preliminary validation process (the account number must have 16 digits and begin with 12497602). If the above parameters are met, a client variable is created that generates an instance of the <em>Client</em> class, through a function that goes through the database found in the <em>data/database.csv</em> file and returns all the data of the client in question. The database was generated by GPT chat and contains information on name, surname, account number, balance and credit score. If no match is found, the program will give the user the option to create their account and immediately log in. It is assumed that the initial credit for a new client is 560. Once the client is created, the menu function is developed, giving the client the option to modify their balance by adding, removing or transferring balance, where each option is developed in separate functions where when any operation occurs, the existing database is updated. In addition, other functions related to the operation of the bank were developed, one of them is the option to obtain a ticket to be attended to at the installation, whose function was developed in the <em>tickets/tickets.py</em> module in the root of the project and was imported into the main file. For this function, a small range of numbers was generated for explanatory reasons of the process, but this range can be modified at your discretion (also modifying the range in the testing function). As a last feature, the application develops an investment system based on the analysis of compound interest, where, based on the credit information found in the database, the percentage of return on their investment is determined, in which the user will be able to define the conditions of their investment (initial investment, capitalization by years and return time). Each investment request will save a graph for the client in the <em>/imgs</em> folder comparing the performance of their investment with compound interest against a current investment. As mentioned, the application is developed in an infinite loop, so to exit it an <strong>EOFError</strong> must be generated which the application expects and exits the program using <strong>sys.exit</strong>.
</div>

<div style="text-align: justify;">
The application is tested in the <em>tests/test_bank</em> file, where the <em>unittest</em> module is used to check the methods of the <em>Client</em> class, as well as other applications. All tests are run with pytest.
</div>


## 🛠 Skills
Python 💚...

## Deployment
```bash
  pip install -r requirements.txt
  python main.py
```

## Running Tests
```bash
  pytest 
```

## Authors
- [@FFons0711](https://https://github.com/FFons0711)

