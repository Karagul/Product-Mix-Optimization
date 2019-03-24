
# Case Study: PC Tech Company

###       by Mohit Singh

### Problem statement
 
The PC Tech company assembles and then tests two models of computers, Basic and XP.
For the coming month, the company wants to decide how many of each model to
assembly and then test. No computers are in inventory from the previous month, and
because these models are going to be changed after this month, the company doesn’t want
to hold any inventory after this month. It believes the most it can sell this month are 600
Basics and 1200 XPs. Each Basic sells for $300 and each XP sells for $450. The cost of
component parts for a Basic is $150; for an XP it is $225. Labor is required for assembly
and testing. There are at most 10,000 assembly hours and 3000 testing hours available. Each
labor hour for assembling costs $11 and each labor hour for testing costs $15. Each Basic
requires five hours for assembling and one hour for testing, and each XP requires six hours
for assembling and two hours for testing. PC Tech wants to know how many of each model
it should produce (assemble and test) to maximize its net profit, but it cannot use more labor
hours than are available, and it does not want to produce more than it can sell. <sup>[1]</sup>

### Creating a mathematical model using linear algebra

#### Parameters
 
![](https://latex.codecogs.com/svg.latex?S_{i}) = Maximum number of model type i computers to sell this month, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?P_{i}) = Sell price of model type i computers, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?C_{i}) = Cost price of component parts for model type i computers, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?A_{i}) = Assembly labor cost per hour of model type i computers, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?T_{i}) = Testing labor cost per hour of model type i computers, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?A) = Maximum assembly labor hours <br>
![](https://latex.codecogs.com/svg.latex?T) = Maximum testing labor hours <br>
![](https://latex.codecogs.com/svg.latex?H_{A,i}) = Assembly hours required for building each model type i computer, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>
![](https://latex.codecogs.com/svg.latex?H_{T,i}) = Testing hours required for building each model type i computer, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br>

#### Decision Variables
 
![](https://latex.codecogs.com/svg.latex?x_{i}) = How many model type i computers to produce this month, where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP }

#### Objective Function
 
The objective is to maximize total profit.<br>

#### *<center>Total Profit = Sell Price - Assembly Cost - Testing Cost - Component Buying Cost </center>* <br>

![](https://latex.codecogs.com/svg.latex?Total&space;Profit&space;=&space;\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;P_{i}&space;-&space;\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;H_{A,i}&space;*&space;A_{i})
![](https://latex.codecogs.com/svg.latex?-&space;\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;H_{T,i}&space;*&space;T_{i}&space;-&space;\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;C_{i})

#### Constraints

Number of model type i computers to produce cannot be a negative number. <br>
![](https://latex.codecogs.com/svg.latex?x_{i}&space;\geq&space;0), where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP }<br><br>
Total number of assembly hours cannot be greater than the maximum available assembly labor hours. <br>
![](https://latex.codecogs.com/svg.latex?$\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;H_{A,i}&space;\leq&space;A$) <br><br>
Total number of testing hours cannot be greater than the maximum available testing labor hours. <br>
![](https://latex.codecogs.com/svg.latex?$\sum_{i&space;\in&space;{&space;Basic,&space;XP&space;}}&space;x_{i}&space;*&space;H_{T,i}&space;\leq&space;T$) <br><br>
Number of model type i computers to produce cannot be greater than the maximum number of model type i computers to sell this month. <br>
![](https://latex.codecogs.com/svg.latex?$x_{i}&space;\leq&space;S_{i}$), where i ![](https://latex.codecogs.com/svg.latex?\in) { Basic, XP } <br><br>

### Implementing mathematical model in Python

#### Parameters


```python
s_b=600 #Maximum number of model type Basic computers to sell this month
s_x=1200 #Maximum number of model type XP computers to sell this month
p_b=300 #Sell price of model type Basic computers
p_x=450 #Sell price of model type XP computers
c_b=150 #Cost price of component parts for model type Basic computers
c_x=225 #Cost price of component parts for model type XP computers
A_b=11 #Assembly labor cost per hour of model type Basic computers
A_x=11 #Assembly labor cost per hour of model type XP computers
T_b=15 #Testing labor cost per hour of model type Basic computers
T_x=15 #Testing labor cost per hour of model type XP computers
A=10000 #Maximum assembly labor hours 
T=3000 #Maximum testing labor hours 
H_A_b=5 #Assembly hours required for building each model type Basic computer
H_A_x=6 #Assembly hours required for building each model type XP computer
H_T_b=1 #Testing hours required for building each model type Basic computer
H_T_x=2 #Testing hours required for building each model type XP computer
```

#### Importing PuLP modeler functions


```python
from pulp import *
```

#### Creating main problem variable for adding problem data and maximizing objective function


```python
problem=LpProblem("Product Mix for PC Tech",LpMaximize)
```

#### Creating decision variables and adding them to the main problem variable


```python
x_b=LpVariable("Amount of Basic",0,None,LpInteger)
x_x=LpVariable("Amount of XP",0,None,LpInteger)
```

#### Defining objective function to maximize profit and adding it to the main problem variable


```python
p1= x_b*p_b + x_x*p_x #Sell Price
n1= x_b*H_A_b*A_b + x_x*H_A_x*A_x #Assembly Cost
n2= x_b*H_T_b*T_b + x_x*H_T_x*T_x #Testing Cost
n3= x_b*c_b + x_x*c_x #Component Cost
problem += p1-n1-n2-n3 #Profit = Sell Price - Assembly Cost - Testing Cost - Component Cost
```

#### Constraints


```python
problem += x_b*H_A_b + x_x*H_A_x <= A,"Max Assembly Hours"
problem += x_b*H_T_b + x_x*H_T_x <= T,"Max Testing Hours"
problem += x_b<=s_b,"Production less than or equal to demand for Basic"
problem += x_x<=s_x,"Production less than or equal to  demand for XP"
```

#### Solving the optimization problem


```python
problem.solve();
```

#### Printing the results


```python
print("Maximized Profit: ",value(problem.objective))
print("Optimum number of Basic to produce: ",problem.variables()[0].varValue)
print("Optimum number of XP to produce: ",problem.variables()[1].varValue)
```

    Maximized Profit:  199600.0
    Optimum number of Basic to produce:  560.0
    Optimum number of XP to produce:  1200.0
    

#### Conclusion
PC Tech Company should produce 560 of computer type Basic and 1200 of computer type XP to achieve maximum predicted profit of $199,600.


#### Citations
[1] Winston, Wayne L., and S., Christian Albright, *Practical Management Science*, Cengage, 2019.

