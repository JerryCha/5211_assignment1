# Question 1: The coin change problem (20 marks)

A vending machine contains certain quantities of coins and notes, and we want to determine if it can provide a given list of changes. (Since the operating system of the vending machine runs in a Jupyter notebook, the currency it uses is the euro (€) and not the dollar (\$), which is more complicated to handle in a Jupyter Notebook.)

For example, suppose that the vending machine contains five 1€ coins, one 5€ note, and three 10€ notes.  Can the machine provide the list of changes?
* [20€, 25€, 15€]. Clearly not, as the machine only has $5*1+1*5+3*10=40$€, but must give 60€ in change. The answer is then False.
* [15€, 15€]. Yes, with one 10€ note and one 5€ note for the first amount, and with one 10€ note and five 1€ coins for the second amount. The answer is then True.
* [8€, 15€]. It's less clear, but the answer is no. The only way to make 8€ is to use the 5€ note and three 1€ coins, and then there is no way to make 15€ with the remaining coins. The answer is then False.

In this problem, the possible denominations of coins or notes that the machine can contain are 1€, 5€, 10€, 20€, 100€. This will be provided in a list called *denominations*, always equal to [1, 5, 10, 20, 100] in this question.

There is also a number of each kind of denomination on hand, provided in a list called *multiplicities*, for instance [1, 3, 2, 3, 7], which means that there is one 1€ coin, three 5€ notes, two 10€ notes, three 20€ notes, and seven 100€ notes. The lists *denominations* and *multiplicities* will always have the same size.

A series of customers need to get their change back and we want to know if there is adequate denominations and multiplicities in the cash register to give them all change. The *change_amounts* list contains these change amounts in euro (€). For example [12,30,5] means that changes of 12€, 30€, and 5€ have been requested.

To formalise, the input of the program that you need to write is:
* A list of $k$ denominations, always equal to [1, 5, 10, 20, 100] in our case.
* A list of $k$ non-negative multiplicities (e.g. [1, 3, 2, 3, 7]).
* A list of $n$ values, where each value is a positive integer (e.g. [12,30,5])

The output is:
* True if the vending machine can provide the exact changes, False otherwise.

The runtime complexity of your algorithm should be in $O(k n)$.
