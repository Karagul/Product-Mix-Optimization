#!/usr/bin/env python
# coding: utf-8

# # Case Study: PC Tech Company
# 
# 
# ### Problem statement
#  
# The PC Tech company assembles and then tests two models of computers, Basic and XP.
# For the coming month, the company wants to decide how many of each model to
# assembly and then test. No computers are in inventory from the previous month, and
# because these models are going to be changed after this month, the company doesn’t want
# to hold any inventory after this month. It believes the most it can sell this month are 600
# Basics and 1200 XPs. Each Basic sells for \\$300 and each XP sells for \\$450. The cost of
# component parts for a Basic is \\$150; for an XP it is \\$225. Labor is required for assembly
# and testing. There are at most 10,000 assembly hours and 3000 testing hours available. Each
# labor hour for assembling costs \\$11 and each labor hour for testing costs \\$15. Each Basic
# requires five hours for assembling and one hour for testing, and each XP requires six hours
# for assembling and two hours for testing. PC Tech wants to know how many of each model
# it should produce (assemble and test) to maximize its net profit, but it cannot use more labor
# hours than are available, and it does not want to produce more than it can sell.

# ### Creating a mathematical model using linear algebra

# #### Parameters
#  
# $S_{i}$ = Maximum number of model type i computers to sell this month, where i $\in$ { Basic, XP } <br>
# $P_{i}$ = Sell price of model type i computers, where i $\in$ { Basic, XP } <br>
# $C_{i}$ = Cost price of component parts for model type i computers, where i $\in$ { Basic, XP } <br>
# $A_{i}$ = Assembly labor cost per hour of model type i computers, where i $\in$ { Basic, XP } <br>
# $T_{i}$ = Testing labor cost per hour of model type i computers, where i $\in$ { Basic, XP } <br>
# $A$ = Maximum assembly labor hours <br>
# $T$ = Maximum testing labor hours <br>
# $H_{A,i}$ = Assembly hours required for building each model type i computer, where i $\in$ { Basic, XP } <br>
# $H_{T,i}$ = Testing hours required for building each model type i computer, where i $\in$ { Basic, XP } <br>

# #### Decision Variables
#  
# $x_{i}$ = How many model type i computers to produce this month, where i $\in$ { Basic, XP }

# #### Objective Function
#  
# The objective is to maximize total profit.<br>
# 
# #### *<center>Total Profit = Sell Price - Assembly Cost - Testing Cost - Component Buying Cost </center>* <br>
# 
# $$Total Profit = \sum_{i \in { Basic, XP }} x_{i} * P_{i}   -   \sum_{i \in { Basic, XP }} x_{i} * H_{A,i} * A_{i}  - \sum_{i \in { Basic, XP }} x_{i} * H_{T,i} * T_{i}   - \sum_{i \in { Basic, XP }} x_{i} * C_{i} $$

# #### Constraints
# 
# Number of model type i computers to produce cannot be a negative number. <br>
# <center>$x_{i} \geq 0$, where i $\in$ { Basic, XP }</center><br><br>
# Total number of assembly hours cannot be greater than the maximum available assembly labor hours. <br>
# <center>$\sum_{i \in { Basic, XP }} x_{i} * H_{A,i} \leq A$</center>  <br><br>
# Total number of testing hours cannot be greater than the maximum available testing labor hours. <br>
# <center>$\sum_{i \in { Basic, XP }} x_{i} * H_{T,i} \leq T$</center>  <br><br>
# Number of model type i computers to produce cannot be greater than the maximum number of model type i computers to sell this month. <br>
# <center>$x_{i} \leq S_{i}$, where i $\in$ { Basic, XP }</center><br><br>

# ### Implementing mathematical model in Python

# #### Parameters

# In[1]:


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


# #### Importing PuLP modeler functions

# In[2]:


from pulp import *


# #### Creating main problem variable for adding problem data and maximizing objective function

# In[3]:


problem=LpProblem("Product Mix for PC Tech",LpMaximize)


# #### Creating decision variables and adding them to the main problem variable

# In[4]:


x_b=LpVariable("Amount of Basic",0,None,LpInteger)
x_x=LpVariable("Amount of XP",0,None,LpInteger)


# #### Defining objective function to maximize profit and adding it to the main problem variable

# In[5]:


p1= x_b*p_b + x_x*p_x #Sell Price
n1= x_b*H_A_b*A_b + x_x*H_A_x*A_x #Assembly Cost
n2= x_b*H_T_b*T_b + x_x*H_T_x*T_x #Testing Cost
n3= x_b*c_b + x_x*c_x #Component Cost
problem += p1-n1-n2-n3 #Profit = Sell Price - Assembly Cost - Testing Cost - Component Cost


# #### Constraints

# In[6]:


problem += x_b*H_A_b + x_x*H_A_x <= A,"Max Assembly Hours"
problem += x_b*H_T_b + x_x*H_T_x <= T,"Max Testing Hours"
problem += x_b<=s_b,"Production less than or equal to demand for Basic"
problem += x_x<=s_x,"Production less than or equal to  demand for XP"


# #### Solving the optimization problem

# In[7]:


problem.solve();


# #### Printing the results

# In[8]:


print("Maximized Profit: ",value(problem.objective))
print("Optimum number of Basic to produce: ",problem.variables()[0].varValue)
print("Optimum number of XP to produce: ",problem.variables()[1].varValue)


# #### Conclusion
# PC Tech Company should produce 560 of computer type Basic and 1200 of computer type XP to achieve maximum profit of \\$199,600.
