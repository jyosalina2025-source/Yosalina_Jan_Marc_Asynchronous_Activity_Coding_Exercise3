Phase 1 Conceptual Check & Code Diagnosis

1. Conceptual Distinction

A. In your own words, differentiate Encapsulation from Abstraction. Give a real-world analogy other
than a car or a television.
- For me, encapsulation is about keeping the data and controlling how the data can be accessed or changed. Abstraction is about covering complicated and complex processes and showing only the important things to user.
A real-world example is smartphone. Our smartphone uses encapsulation to protect its user data or informations. Abstraction by allowing users to use apps without knowing how it work from inside.

2. Code Diagnosis
Syntax flaws:
- Wrong/Missing self attribute in innit
def __init__(wallet, owner, balance): ---> def __init__(self, owner, balance):

- Wrong instance naming
wallet.Owner = owner ---> self.owner = owner

- Missing @property and @balance.setter


Phase 4 Reflection

1. What error occurred when trying to access atm.__pin directly? Why does Python behave this
way?
- An AttributeError occurred because __pin is a private attribute, which helps prevent them from being accessed directly outside the class.

2. How did using @property allow you to change internal data structures or add validation without
altering the public API for the caller?
- Using @property allowed me to access the balance using account.balance and keeping the actual _balance variable protected/private. It also add validation, like preventing a negative balance.

3. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?
- The ATM class demonstrated abstraction by hiding the complicated BankAccount operations from the user, insted of 
showing complicated logic.