
# Chapter 1 — Python Fundamentals

> **From writing your first Python program to understanding how Python can solve real business problems.**

---

## 1. Chapter Introduction

Imagine joining the data engineering team at **NovaMart**, a growing e-commerce company.

NovaMart sells products through its online platform. Every day, customers place orders, payments are processed, products are shipped, and inventory is updated.

Behind every one of these activities, data is being generated.

The business team wants to answer questions such as:

- How many orders were placed today?
- What is the total revenue?
- Which products generated the most sales?
- Which orders are invalid?
- How many customers are waiting for delivery?
- How much inventory is available?

Initially, the operations team handles many of these tasks manually.

An employee downloads an order file, opens it in a spreadsheet, calculates totals, and prepares a report.

This approach may work when the number of orders is small.

But as NovaMart grows, the amount of data increases.

The engineering team now needs a way to automate these tasks.

That is where Python enters the story.

---

## 2. NovaMart's First Automation Problem

### 2.1 The daily order file

Every morning, NovaMart's operations team receives a file containing the previous day's orders.

A simplified example looks like this:

| Order ID | Product | Quantity | Unit Price |
|---|---|---:|---:|
| 1001 | Laptop | 2 | 45000 |
| 1002 | Mouse | 3 | 800 |
| 1003 | Keyboard | 1 | 2500 |

The business team wants to calculate the total amount for each order.

For example:

**Order 1001**

```text
Quantity × Unit Price

2 × 45000 = 90000
```

**Order 1002**

```text
3 × 800 = 2400
```

**Order 1003**

```text
1 × 2500 = 2500
```

The total revenue from these three orders is:

```text
90000 + 2400 + 2500 = 94900
```

The calculation itself is simple.

But imagine the file contains:

- 100 orders.
- 10,000 orders.
- 1 million orders.

Manually calculating these values becomes increasingly difficult.

NovaMart needs a program that can:

1. Read order data.
2. Perform calculations.
3. Apply business rules.
4. Produce reliable results.
5. Repeat the process every day.

The engineering team decides to use Python.

---

## 3. What Is Python?

Python is a high-level, general-purpose programming language.

It is designed to allow developers to express solutions using readable and relatively concise code.

Python can be used for:

- Automation.
- Web development.
- Data analysis.
- Machine learning.
- Data engineering.
- Scripting.
- Application development.
- Testing.
- System administration.

For our journey, we are primarily interested in Python as a **data engineering programming language**.

### 3.1 Python in data engineering

Data engineering involves collecting, moving, transforming, validating, and preparing data for use.

Python helps engineers perform these activities.

For example:

```text
NovaMart Order Data
        |
        v
Python Program
        |
        v
Read Data
        |
        v
Validate Data
        |
        v
Transform Data
        |
        v
Write Processed Data
```

This is a simplified view of a data-processing workflow.

Later in the book, we will build more advanced versions of this architecture using databases, Apache Spark, cloud storage, and orchestration tools.

### 3.2 Why Python is useful

Python provides several capabilities that are valuable to data engineers.

#### Readable syntax

Python code is designed to be relatively easy to read.

For example:

```python
order_amount = quantity * unit_price
```

This expresses the business calculation directly.

#### Large ecosystem

Python has libraries for working with:

- CSV files.
- JSON.
- Databases.
- APIs.
- Cloud services.
- Data processing.
- Testing.
- Distributed computing.

We will introduce these libraries when NovaMart needs them.

#### Automation

Python allows us to turn repetitive manual tasks into repeatable programs.

#### Integration

Python can communicate with other systems, including databases, APIs, and data-processing frameworks.

#### Flexibility

Python can be used for small scripts as well as larger software projects.

However, Python is not automatically the best tool for every data engineering task.

For example, SQL is often more appropriate for querying relational databases, while distributed frameworks such as Apache Spark are useful for processing large datasets across multiple machines.

A data engineer needs to understand how these tools work together.

---

## 4. Python's Role in Our Data Engineering Journey

Throughout this book, Python will appear in many different parts of NovaMart's architecture.

### Stage 1 — Local data processing

We begin with Python scripts that process local files.

```text
CSV File
   |
   v
Python Script
   |
   v
Processed CSV File
```

### Stage 2 — Database integration

Later, Python will interact with relational databases.

```text
Python Program
      |
      v
SQL Database
      |
      v
Query and Transform Data
```

### Stage 3 — ETL pipelines

Python will help us build extract, transform, and load workflows.

```text
Source Data
     |
     v
Extract
     |
     v
Transform
     |
     v
Load
```

### Stage 4 — Distributed processing

When NovaMart's data becomes large, we will introduce tools such as Apache Spark.

Python can be used through PySpark to write distributed data-processing logic.

### Stage 5 — Production systems

Eventually, Python code will become part of systems involving:

- Data validation.
- Logging.
- Testing.
- Orchestration.
- Cloud services.
- Monitoring.
- Deployment.

The foundations we learn in this chapter will support those later topics.

---

## 5. Installing and Running Python

Before writing programs, we need to understand how Python code is executed.

### 5.1 The Python interpreter

A Python interpreter is a program that executes Python code.

When we write:

```python
print("Hello")
```

The interpreter executes the instruction and produces output.

In simple terms:

```text
Python Code
     |
     v
Python Interpreter
     |
     v
Program Output
```

The exact execution process involves several implementation details, which we will explore when discussing Python internals.

For now, remember:

> The interpreter is responsible for executing Python instructions.

### 5.2 Running Python from the terminal

Open the VS Code terminal.

Check whether Python is installed:

```powershell
python --version
```

Example output:

```text
Python 3.x.x
```

The exact version depends on your installation.

You can also try:

```powershell
py --version
```

On Windows, the Python launcher may be available through `py`.

### 5.3 Running the Python interactive interpreter

Run:

```powershell
python
```

You may see something similar to:

```text
>>>
```

The `>>>` symbol is called the Python prompt.

Now enter:

```python
print("Hello, NovaMart")
```

Expected output:

```text
Hello, NovaMart
```

You have just executed your first Python instruction.

To exit the interpreter on Windows, use:

```text
exit()
```

Or press:

```text
Ctrl + Z
Enter
```

### 5.4 Interactive interpreter vs Python script

There are two common ways to run Python code.

#### Interactive interpreter

You type instructions one at a time.

Example:

```python
>>> 2 + 3
5
```

This is useful for:

- Experimentation.
- Learning.
- Quick calculations.
- Testing small expressions.

#### Python script

You save code in a `.py` file and execute the file.

Example:

```text
hello.py
```

Contents:

```python
print("Hello, NovaMart")
```

Run it from the terminal:

```powershell
python hello.py
```

Expected output:

```text
Hello, NovaMart
```

For our book, we will use Python scripts for reusable implementations and notebooks for interactive experimentation.

---

## 6. Your First Python Program

Let's write our first program for NovaMart.

### 6.1 Create the Python file

Create or open:

```text
E:\Books-By-Chirag\Data Engineering - The Complete Journey\code\01-python-foundations\01-python-fundamentals\01_hello_novamart.py
```

Add the following code:

```python
print("Welcome to NovaMart Data Engineering")
print("We are starting our Python journey")
```

### 6.2 Run the program

From the project root, execute:

```powershell
python code\01-python-foundations\01-python-fundamentals\01_hello_novamart.py
```

Expected output:

```text
Welcome to NovaMart Data Engineering
We are starting our Python journey
```

### 6.3 Understanding the code

Let's examine the first line:

```python
print("Welcome to NovaMart Data Engineering")
```

There are two important parts:

**`print`**

`print` is a built-in Python function used to display information.

**`"Welcome to NovaMart Data Engineering"`**

This is a string literal.

A string is a sequence of characters used to represent text.

We will study strings in detail later in this chapter.

The parentheses are used to pass an argument to the function.

For now, remember:

```python
print(value)
```

means:

> Display the value.

### 6.4 Printing multiple values

Python can print more than one value.

```python
print("NovaMart", "Data Engineering")
```

Output:

```text
NovaMart Data Engineering
```

Another example:

```python
print(10)
print(20)
print(10 + 20)
```

Output:

```text
10
20
30
```

Notice that Python can also evaluate an expression before displaying the result.

### 6.5 Printing text and numbers

```python
print("Total Orders:", 100)
print("Total Revenue:", 94900)
```

Output:

```text
Total Orders: 100
Total Revenue: 94900
```

This is useful when displaying business metrics.

Later, we will learn better ways to format output using f-strings.

---

## 7. A Small NovaMart Calculation

Let's perform our first business calculation.

### 7.1 The problem

NovaMart received the following order:

```text
Product: Laptop
Quantity: 2
Unit Price: 45000
```

Calculate the total order amount.

### 7.2 Python implementation

```python
quantity = 2
unit_price = 45000

total_amount = quantity * unit_price

print("Total Order Amount:", total_amount)
```

Expected output:

```text
Total Order Amount: 90000
```

### 7.3 What happened?

The program performed three steps:

1. Stored the quantity.
2. Stored the unit price.
3. Multiplied the values.

The result was stored in `total_amount`.

This is our first example of using Python to automate a business calculation.

In the next sections, we will understand exactly how variables, values, and data types work.

---

## 8. Chapter Learning Checkpoint

Before moving forward, make sure you understand:

- What Python is.
- What a Python interpreter does.
- How to run Python from the terminal.
- The difference between the interactive interpreter and a script.
- How to create and execute a `.py` file.
- What the `print()` function does.
- How Python can perform basic calculations.

### Practice

Write a Python program that prints:

```text
Welcome to NovaMart
Company: NovaMart
Department: Data Engineering
First Order Amount: 90000
```

Then modify the program to calculate the order amount using:

```python
quantity = 2
unit_price = 45000
```

Do not hardcode the final amount.

Let Python calculate it.

---

## Next Section

We have written our first Python program and performed our first NovaMart business calculation.

But how does Python store values such as order IDs, customer names, quantities, and prices?

To answer that, we need to understand **variables and data types**.

**Next: Section 2 — Understanding Python Syntax.**


2. Understanding Python Syntax

Before writing larger Python programs, we need to understand how Python code is structured.

Every programming language has a set of rules that determine how instructions must be written. These rules are called syntax.

For example, in English:

The customer placed an order.

This sentence follows the rules of English grammar.

In Python:

print("The customer placed an order.")

This follows Python’s syntax rules.

If we break those rules, Python may not understand our instructions and will raise an error.

2.1 What Is Syntax?

Syntax is the set of rules that defines how Python code must be written.

Consider this valid Python statement:

print("Welcome to NovaMart")

Python understands that:

print is a built-in function.

"Welcome to NovaMart" is a string.

Parentheses contain the value passed to the function.

Now consider this invalid statement:

print("Welcome to NovaMart"

The closing parenthesis is missing.

Python will raise a SyntaxError because the instruction is incomplete.

Example
customer_name = "Chirag"
print(customer_name)

Output:

Chirag

The code follows Python syntax because:

The variable name is valid.

The assignment operator = is used correctly.

The string is enclosed in quotation marks.

The print() function is written correctly.

2.2 Python Uses Indentation

One of the most important features of Python is indentation.

Indentation means adding spaces at the beginning of a line.

Many programming languages use curly braces {} to define blocks of code. Python generally uses indentation instead.

For example:

order_value = 1500

if order_value > 1000:
    print("Eligible for premium delivery")

Output:

Eligible for premium delivery

The indented line belongs to the if block.

if condition:
    indented statement

The colon : indicates that a code block is starting.

The indentation tells Python which statements belong to that block.

Incorrect indentation
order_value = 1500

if order_value > 1000:
print("Eligible for premium delivery")

This produces an error similar to:

IndentationError: expected an indented block
Correct indentation
order_value = 1500

if order_value > 1000:
    print("Eligible for premium delivery")
Recommended indentation

The standard convention is to use four spaces for each indentation level.

if order_value > 1000:
    print("Premium order")

    if order_value > 5000:
        print("High-value premium order")

The second if statement is nested inside the first if statement.

Visual representation
if order_value > 1000:
    print("Premium order")

    if order_value > 5000:
        print("High-value premium order")

The indentation levels are:

Level 0: if order_value > 1000:
Level 1:     print("Premium order")
Level 1:     if order_value > 5000:
Level 2:         print("High-value premium order")
Important rule

Do not mix tabs and spaces within the same code block.

Use four spaces consistently.

Most modern code editors, including VS Code, can automatically insert spaces when you press the Tab key.

2.3 Code Blocks

A code block is a group of statements that belong together.

Python uses indentation to define code blocks in:

if statements

for loops

while loops

functions

classes

exception handling

context managers

Example: Conditional block
order_status = "shipped"

if order_status == "shipped":
    print("Send shipping notification")
    print("Update customer dashboard")

print("Process completed")

Output:

Send shipping notification
Update customer dashboard
Process completed

The first two print() statements belong to the if block.

The last statement is outside the block because it is not indented.

Example: Function block
def calculate_total(price, quantity):
    total = price * quantity
    return total

The statements inside the function are indented.

def calculate_total(price, quantity):
    total = price * quantity
    return total

The function ends when the indentation returns to the previous level.

2.4 Comments in Python

A comment is text written inside the code to explain what the code does.

Python ignores comments during execution.

Comments are useful for:

Explaining business logic

Documenting assumptions

Making code easier to understand

Temporarily disabling a line

Helping teammates maintain the code

Single-line comments

A single-line comment begins with #.

# Store the customer's order value
order_value = 2500

print(order_value)

Python ignores this line:

# Store the customer's order value
Inline comments

A comment can also appear after a statement.

order_value = 2500  # Order value in Indian rupees
Multiple comments
# Step 1: Read the order value
order_value = 2500

# Step 2: Calculate the delivery charge
delivery_charge = 50

# Step 3: Calculate the final amount
final_amount = order_value + delivery_charge

print(final_amount)

Output:

2550
Good comments

Good comments explain why something is done.

# Apply free delivery for orders above the premium threshold
if order_value >= 2000:
    delivery_charge = 0
Weak comments

Weak comments only repeat what the code already says.

# Add 50 to order value
final_amount = order_value + 50

The code already explains the operation.

Best practice

Use comments to explain:

Business rules

Important assumptions

Non-obvious decisions

Temporary workarounds

Data quality considerations

Avoid writing comments for every simple line.

2.5 Docstrings

A docstring is a string used to document a function, class, or module.

Docstrings are usually written using triple quotes.

def calculate_total(price, quantity):
    """
    Calculate the total value of an order.
    """
    return price * quantity

The text inside the triple quotes describes the purpose of the function.

Function docstring example
def calculate_delivery_charge(order_value):
    """
    Return the delivery charge based on the order value.

    Orders above or equal to 2000 receive free delivery.
    """
    if order_value >= 2000:
        return 0

    return 50

Docstrings are useful because tools such as Python help systems and documentation generators can read them.

You can inspect a function’s documentation using:

help(calculate_delivery_charge)
Comments vs docstrings

Feature

	

Comments

	

Docstrings




Begins with

	

#

	

Quotes, usually """




Main purpose

	

Explain code

	

Document modules, functions, and classes




Used by help()

	

No

	

Yes




Executed as Python expression

	

No

	

Yes, when placed appropriately

2.6 Statements and Expressions

To understand Python code clearly, we must distinguish between statements and expressions.

Statement

A statement is an instruction that performs an action.

Examples:

order_value = 1500
print("Processing order")
if order_value > 1000:
    print("Premium order")
Expression

An expression is a piece of code that produces a value.

Examples:

10 + 20
price * quantity
order_value > 1000
Example
price = 500
quantity = 3

total = price * quantity

Here:

price = 500 is an assignment statement.

quantity = 3 is an assignment statement.

price * quantity is an expression.

total = price * quantity is an assignment statement containing an expression.

Expression evaluation

Python evaluates:

price * quantity

If:

price = 500
quantity = 3

Then:

price * quantity

produces:

1500

This value is assigned to total.

2.7 Assignment Statements

Assignment is used to store a value in a variable.

customer_name = "Chirag"
order_value = 2500

The assignment operator is:

=

It does not mean mathematical equality.

It means:

Evaluate the expression on the right and store the result in the name on the left.

Example
order_value = 1000
order_value = order_value + 500

print(order_value)

Output:

1500

The second statement means:

Read the current value of order_value.

Add 500.

Store the result back in order_value.

Assignment shortcut

Python supports augmented assignment operators.

order_value = 1000
order_value += 500

print(order_value)

Output:

1500

These two statements are equivalent:

order_value = order_value + 500
order_value += 500

Other augmented assignment operators include:

order_value -= 100
order_value *= 2
order_value /= 5
NovaMart example
total_orders = 100

total_orders += 25

print(total_orders)

Output:

125

This can represent the addition of newly received orders to a running count.

2.8 Python Is Case-Sensitive

Python treats uppercase and lowercase letters as different.

For example:

customer_name = "Chirag"
Customer_name = "Rahul"
CUSTOMER_NAME = "Amit"

print(customer_name)
print(Customer_name)
print(CUSTOMER_NAME)

Output:

Chirag
Rahul
Amit

These are three different variable names.

customer_name
Customer_name
CUSTOMER_NAME
Common mistake
order_value = 2500

print(Order_value)

This raises:

NameError

because Order_value and order_value are different names.

Best practice

Use lowercase variable names with underscores:

order_value = 2500
customer_name = "Chirag"
delivery_charge = 50
2.9 Naming Conventions

Python allows names for:

Variables

Functions

Classes

Modules

Constants

Good naming improves readability and maintainability.

Rules for valid names

A Python name:

Can contain letters.

Can contain digits.

Can contain underscores.

Cannot begin with a digit.

Cannot contain spaces.

Cannot be a Python keyword.

Is case-sensitive.

Valid names
customer_name = "Chirag"
order_1 = 100
delivery_charge = 50
Invalid names
1st_order = 100

A name cannot begin with a digit.

customer name = "Chirag"

Spaces are not allowed in variable names.

class = "Premium"

class is a Python keyword.

Naming styles
snake_case

Commonly used for variables and functions.

customer_name = "Chirag"
calculate_order_total()
PascalCase

Commonly used for classes.

class OrderProcessor:
    pass


UPPER_CASE

UPPER_CASE is commonly used for constants.

Constants are values that are intended to remain unchanged during program execution.

MAX_RETRY_COUNT = 3
DEFAULT_DELIVERY_CHARGE = 50
NovaMart example
FREE_DELIVERY_THRESHOLD = 2000
STANDARD_DELIVERY_CHARGE = 50

order_value = 1500

if order_value >= FREE_DELIVERY_THRESHOLD:
    delivery_charge = 0
else:
    delivery_charge = STANDARD_DELIVERY_CHARGE

print(delivery_charge)

Output:

50

Using uppercase names makes important configuration values easy to identify.

Python does not strictly prevent constants from being changed. Uppercase naming is a convention that communicates developer intent.

2.10 Python Keywords

Keywords are reserved words that have special meaning in Python.

Examples include:

if
else
elif
for
while
def
return
class
try
except
finally
import
from
as
True
False
None
and
or
not
in
is

You cannot use these words as variable names.

Invalid example
class = "Premium"

This produces a syntax error because class is a Python keyword.

Valid example
order_class = "Premium"
View Python keywords

You can use Python’s built-in keyword module:

import keyword

print(keyword.kwlist)

This displays the keywords supported by your installed Python version.

2.11 Line Continuation

Python usually treats the end of a line as the end of a statement.

customer_name = "Chirag"
order_value = 2500

However, long expressions can be split across multiple lines.

Using parentheses
final_amount = (
    order_value
    + delivery_charge
    + tax_amount
)

This is easier to read than writing everything on one line.

Example
order_value = 2500
delivery_charge = 50
tax_amount = 100

final_amount = (
    order_value
    + delivery_charge
    + tax_amount
)

print(final_amount)

Output:

2650
Explicit line continuation

Python also supports the backslash character \.

final_amount = order_value + \
               delivery_charge + \
               tax_amount

Although this works, using parentheses is generally clearer and safer.

Recommended:

final_amount = (
    order_value
    + delivery_charge
    + tax_amount
)
2.12 Multiple Statements on One Line

Python allows multiple simple statements on one line using a semicolon.

order_value = 1000; delivery_charge = 50

However, this reduces readability.

Prefer:

order_value = 1000
delivery_charge = 50
Best practice

Write one logical statement per line unless there is a strong reason not to.

Readable code is especially important in data engineering because pipelines are often maintained and debugged by multiple people.

2.13 Blank Lines and Readability

Blank lines usually do not affect Python execution, but they improve readability.

Less readable
order_value = 2500
delivery_charge = 50
tax_amount = 100
final_amount = order_value + delivery_charge + tax_amount
print(final_amount)
More readable
order_value = 2500
delivery_charge = 50
tax_amount = 100

final_amount = (
    order_value
    + delivery_charge
    + tax_amount
)

print(final_amount)

The second version separates:

Input values

Calculation

Output

This makes the code easier to understand.

2.14 Common Syntax Errors

Syntax errors happen when Python cannot understand the structure of the code.

Missing quotation mark

Incorrect:

customer_name = "Chirag

Possible error:

SyntaxError: unterminated string literal

Correct:

customer_name = "Chirag"
Missing closing parenthesis

Incorrect:

print("Welcome to NovaMart"

Correct:

print("Welcome to NovaMart")
Missing colon

Incorrect:

if order_value > 1000
    print("Premium order")

Correct:

if order_value > 1000:
    print("Premium order")
Incorrect indentation

Incorrect:

if order_value > 1000:
print("Premium order")

Correct:

if order_value > 1000:
    print("Premium order")
Invalid variable name

Incorrect:

order value = 2500

Correct:

order_value = 2500
Using a keyword as a variable

Incorrect:

class = "Premium"

Correct:

order_class = "Premium"
Incorrect comparison operator

Incorrect:

if order_value = 1000:
    print("Order value is 1000")

Correct:

if order_value == 1000:
    print("Order value is 1000")

Remember:

= assigns a value.

== compares two values.

2.15 Syntax Errors vs Runtime Errors

Not every error is a syntax error.

Syntax error

Python cannot parse the code.

print("Hello"

Python stops before executing the program.

Runtime error

The code is syntactically valid, but an error occurs while it runs.

order_value = 1000
delivery_charge = "50"

final_amount = order_value + delivery_charge

This raises a TypeError because Python cannot add an integer and a string.

Logical error

The code runs successfully but produces the wrong result.

order_value = 1000
delivery_charge = 50

final_amount = order_value - delivery_charge

print(final_amount)

Output:

950

The code is valid Python, but the business logic is incorrect if the delivery charge should be added.

Comparison

Error type

	

Meaning

	

Example




Syntax error

	

Code structure is invalid

	

Missing )




Runtime error

	

Error occurs during execution

	

Adding string and integer




Logical error

	

Code runs but result is wrong

	

Subtracting delivery charge

2.16 NovaMart Syntax Practice

Create the following file:

code\01-python-foundations\01-python-fundamentals\02_python_syntax.py

Add this code:

"""
Practice Python syntax using a simple NovaMart example.
"""

# Customer and order information
customer_name = "Chirag"
order_value = 2500
delivery_charge = 0

# Apply the free-delivery rule
if order_value >= 2000:
    delivery_charge = 0
else:
    delivery_charge = 50

# Calculate the final amount
final_amount = order_value + delivery_charge

# Display the result
print("Customer:", customer_name)
print("Order value:", order_value)
print("Delivery charge:", delivery_charge)
print("Final amount:", final_amount)

Run the file from the project root:

python code\01-python-foundations\01-python-fundamentals\02_python_syntax.py

Expected output:

Customer: Chirag
Order value: 2500
Delivery charge: 0
Final amount: 2500
What this example demonstrates

The program uses:

A module docstring

Comments

Variables

Assignment

An if-else block

Indentation

Comparison operators

Arithmetic expressions

Output using print()

2.17 Syntax Checklist

Before moving forward, verify that you understand:

What Python syntax means
Why indentation is important
How code blocks are created
How to write comments
The purpose of docstrings
The difference between statements and expressions
How assignment works
Why Python is case-sensitive
Python naming conventions
Python keywords
How to split long expressions
Common syntax errors
The difference between syntax, runtime, and logical errors
2.18 Practice Exercises
Exercise 1: Customer Information

Create variables for:

customer_name
customer_city
customer_age

Print them in a readable format.

Expected output format:

Customer: Chirag
City: Bengaluru
Age: 25

Use your own values if required.

Exercise 2: Order Calculation

Create variables:

product_price = 1200
quantity = 3

Calculate and print the total order value.

Expected output:

Total order value: 3600
Exercise 3: Delivery Rule

Write a program that:

Gives free delivery when the order value is at least 2000.

Charges 50 otherwise.

Example:

order_value = 1800

Expected output:

Delivery charge: 50
Exercise 4: Identify the Error

Find and correct the error:

customer_name = "Chirag

print(customer_name)
Exercise 5: Indentation

Correct this code:

order_value = 3000

if order_value >= 2000:
print("Free delivery")
Exercise 6: Naming Convention

Rewrite these variable names using Python’s recommended naming style:

CustomerName
order-value
1st_order
DeliveryCharge
Exercise 7: Comments and Docstrings

Create a Python file containing:

A module docstring

Two comments

Three variables

One calculation

One output statement

Use a NovaMart order example.

2.19 Interview Questions
Beginner Questions

What is syntax in Python?

Why is indentation important in Python?

How many spaces are commonly used for indentation?

What is the purpose of a colon : in Python?

What is a comment?

How do you write a single-line comment?

What is a docstring?

Is Python case-sensitive?

What is the difference between = and ==?

What are Python keywords?

Intermediate Questions

What is the difference between a statement and an expression?

How does Python define code blocks?

What happens when indentation is incorrect?

What is the difference between a syntax error and a runtime error?

What is a logical error?

Why should meaningful variable names be used?

What is the recommended naming convention for Python variables?

How can a long Python expression be split across multiple lines?

Why is using semicolons generally discouraged in Python?

What is the difference between comments and docstrings?

Data Engineering Questions

Why is readable Python important in data pipelines?

How can poor naming make a data pipeline difficult to maintain?

Why should business rules be documented in pipeline code?

How can indentation errors affect scheduled ETL jobs?

Why are comments useful when implementing data quality rules?

How can syntax errors be detected before deploying a pipeline?

Why should complex calculations be split across multiple lines?

What is the difference between a syntax error and a data quality issue?

Why should pipeline code use consistent naming conventions?

How can clear code structure help during production debugging?

2.20 Section Summary

In this section, we learned how Python code is structured.

The main concepts were:

Syntax defines the rules for writing Python code.

Indentation is used to define code blocks.

A colon introduces blocks such as if, loops, functions, and classes.

Comments explain code and are ignored during execution.

Docstrings document modules, functions, and classes.

Statements perform actions, while expressions produce values.

Assignment stores values in variables.

Python is case-sensitive.

Meaningful names improve readability.

Keywords cannot be used as variable names.

Parentheses can be used to split long expressions.

Syntax errors prevent Python from parsing code.

Runtime errors occur during execution.

Logical errors produce incorrect results even when code runs.

Connection to the Next Section

Now that we understand how Python code is written, we can explore the values that Python works with.

In the next section, we will learn about:

Variables

Integers

Floats

Strings

Booleans

Data types

Type checking

Type conversion

How Python stores and references values

These concepts will help us process real NovaMart data such as:

Order ID
Customer Name
Product Price
Quantity
Order Status
Delivery Completed



3. Variables and Data Types

In the previous section, we learned how Python code is structured.

Now we will learn about the values that Python works with.

A data engineering pipeline processes many types of information, such as:

Customer names

Order IDs

Product prices

Order quantities

Payment amounts

Delivery status

Missing values

Dates and timestamps

Python stores and processes these values using variables and data types.

3.1 What Is a Variable?

A variable is a name that refers to a value stored in a Python program.

For example:

customer_name = "Chirag"
order_value = 2500

Here:

customer_name is a variable.

"Chirag" is the value.

order_value is a variable.

2500 is the value.

We can use the variable names later in the program.

customer_name = "Chirag"
order_value = 2500

print(customer_name)
print(order_value)

Output:

Chirag
2500
NovaMart example

Imagine NovaMart receives the following order:

Field

	

Value




Customer name

	

Chirag




Product price

	

1200




Quantity

	

2




Delivery charge

	

50

We can represent this information using variables:

customer_name = "Chirag"
product_price = 1200
quantity = 2
delivery_charge = 50

Then calculate the total:

total_amount = product_price * quantity + delivery_charge

print(total_amount)

Output:

2450

The variables make the program easier to understand than using unexplained values directly.

3.2 Variables Are References to Objects

A useful mental model is:

A variable is a label attached to an object.

Consider:

order_value = 2500

Conceptually:

order_value ───────► 2500

The name order_value refers to the integer object 2500.

When we assign another value:

order_value = 3000

The variable now refers to a different value:

order_value ───────► 3000

The original value is no longer referenced by order_value.

Important point

Python variables do not permanently have one data type.

The value referred to by the variable has a type.

This is why Python is called a dynamically typed language.

3.3 Creating and Assigning Variables

A variable is created when a value is assigned to a name.

customer_name = "Chirag"
order_count = 10
is_delivered = True

Python automatically determines the type of each value.

customer_name = "Chirag"   # str
order_count = 10           # int
is_delivered = True        # bool
Assignment process

For this statement:

order_value = 2500

Python:

Evaluates the value 2500.

Creates or identifies the integer object.

Binds the name order_value to that object.

Reassigning a variable
order_value = 2500
print(order_value)

order_value = 3000
print(order_value)

Output:

2500
3000

The same variable name can refer to a new value.

3.4 Dynamic Typing

Python uses dynamic typing.

This means a variable can refer to values of different types during the execution of a program.

value = 100
print(value)

value = "One hundred"
print(value)

Output:

100
One hundred

The variable value first refers to an integer and later refers to a string.

Example
data = 2500
print(type(data))

data = 2500.75
print(type(data))

data = "2500"
print(type(data))

Output:

<class 'int'>
<class 'float'>
<class 'str'>
Important caution

Dynamic typing is flexible, but it requires care.

This code is valid:

order_value = 2500
order_value = "2500"

However, this can cause problems:

order_value = "2500"
delivery_charge = 50

final_amount = order_value + delivery_charge

Python raises a TypeError because a string and an integer cannot be added directly.

3.5 Python’s Common Built-in Data Types

A data type defines the kind of value stored in a variable.

Common Python data types include:

Data type

	

Python name

	

Example




Integer

	

int

	

100




Floating-point number

	

float

	

99.50




String

	

str

	

"NovaMart"




Boolean

	

bool

	

True




None value

	

NoneType

	

None




List

	

list

	

[100, 200, 300]




Tuple

	

tuple

	

(100, 200, 300)




Set

	

set

	

{100, 200, 300}




Dictionary

	

dict

	

{"id": 101}

In this section, we will focus mainly on the basic scalar types:

int

float

str

bool

NoneType

Collections such as lists, tuples, sets, and dictionaries will be covered in detail later.

3.6 Integer Data Type: int

An integer is a whole number without a decimal component.

Examples:

order_id = 101
quantity = 3
customer_age = 25
total_orders = 1500

Python uses the int type for these values.

quantity = 3

print(quantity)
print(type(quantity))

Output:

3
<class 'int'>
Negative integers
temperature_difference = -5
Zero
failed_orders = 0
Large integers

Python integers can represent very large whole numbers.

large_order_id = 987654321987654321
print(large_order_id)

Python integers do not have the same small fixed range as integers in some other programming languages.

NovaMart example
order_id = 1001
quantity = 4
product_price = 750

total_product_value = product_price * quantity

print("Order ID:", order_id)
print("Total product value:", total_product_value)

Output:

Order ID: 1001
Total product value: 3000
3.7 Floating-Point Data Type: float

A floating-point number represents a number with a decimal component.

Examples:

product_price = 999.99
discount_percentage = 10.5
average_order_value = 2450.75

Check the type:

product_price = 999.99

print(product_price)
print(type(product_price))

Output:

999.99
<class 'float'>
Arithmetic with floats
price = 999.99
quantity = 2

total = price * quantity

print(total)

Output:

1999.98
Important note about precision

Floating-point numbers are stored using binary representation.

Because of this, some decimal values cannot be represented exactly.

Example:

result = 0.1 + 0.2

print(result)

Output may be:

0.30000000000000004

This is normal floating-point behavior.

Money and financial calculations

For financial calculations where exact decimal precision is important, consider using Python’s Decimal type instead of relying only on float.

Example:

from decimal import Decimal

price = Decimal("0.10")
tax = Decimal("0.20")

total = price + tax

print(total)

Output:

0.30

For this beginner section, use float to understand decimal values. Later, we will discuss Decimal and financial data processing in more detail.

3.8 String Data Type: str

A string is a sequence of characters used to represent text.

Examples:

customer_name = "Chirag"
city = "Bengaluru"
order_status = "Shipped"

Strings can be written using:

Single quotes

Double quotes

Triple quotes

Single quotes
customer_name = 'Chirag'
Double quotes
customer_name = "Chirag"

Both are valid.

Triple quotes

Triple quotes are commonly used for multi-line strings and docstrings.

message = """
Welcome to NovaMart.
Your order has been received.
"""
Checking the type
order_status = "Shipped"

print(type(order_status))

Output:

<class 'str'>
Strings can contain numbers
order_id = "1001"

Although the value looks numeric, it is a string because it is enclosed in quotation marks.

print(type(order_id))

Output:

<class 'str'>

This distinction is important when reading data from CSV files, APIs, or databases.

3.9 Boolean Data Type: bool

A Boolean represents one of two logical values:

True
False

Booleans are commonly used for:

Conditions

Flags

Status indicators

Data quality checks

Feature engineering

Pipeline decisions

Example
is_delivered = True
is_cancelled = False

print(is_delivered)
print(is_cancelled)

Output:

True
False
Checking the type
is_delivered = True

print(type(is_delivered))

Output:

<class 'bool'>
NovaMart example
order_value = 2500
is_premium_order = order_value >= 2000

print(is_premium_order)

Output:

True

The expression:

order_value >= 2000

produces a Boolean value.

Boolean values are case-sensitive

Correct:

is_active = True

Incorrect:

is_active = true

Python uses:

True
False

with an uppercase first letter.

3.10 The None Value

Python uses None to represent the absence of a value.

delivery_date = None

This may mean:

The delivery date is not available.

The order has not been delivered.

The value has not been assigned yet.

The source system did not provide a value.

Check the type:

delivery_date = None

print(type(delivery_date))

Output:

<class 'NoneType'>

3.11 Checking Data Types with type()

Python provides the built-in type() function to inspect the type of a value.

customer_name = "Chirag"
order_count = 10
average_order_value = 2500.75
is_delivered = True
delivery_date = None

print(type(customer_name))
print(type(order_count))
print(type(average_order_value))
print(type(is_delivered))
print(type(delivery_date))

Output:

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
Practical inspection
order_id = "1001"

print("Value:", order_id)
print("Type:", type(order_id))

Output:

Value: 1001
Type: <class 'str'>

This is useful when debugging data ingestion issues.

For example, an order ID may arrive from a CSV file as a string even if it looks like a number.

3.12 Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions include:

Function

	

Converts to




int()

	

Integer




float()

	

Float




str()

	

String




bool()

	

Boolean

Convert string to integer
quantity = "3"

quantity = int(quantity)

print(quantity)
print(type(quantity))

Output:

3
<class 'int'>
Convert string to float
price = "999.50"

price = float(price)

print(price)
print(type(price))

Output:

999.5
<class 'float'>
Convert integer to string
order_id = 1001

order_id_text = str(order_id)

print(order_id_text)
print(type(order_id_text))

Output:

1001
<class 'str'>
Convert integer to float
quantity = 3

quantity_as_float = float(quantity)

print(quantity_as_float)

Output:

3.0
Convert values to Boolean
print(bool(1))
print(bool(0))
print(bool("NovaMart"))
print(bool(""))

Output:

True
False
True
False
3.13 Important Type Conversion Rules

Not every value can be converted successfully.

Valid conversion
quantity = int("5")
Invalid conversion
quantity = int("five")

This raises:

ValueError
Invalid float conversion
price = float("not available")

This also raises:

ValueError
Converting a float to an integer
price = 99.99

print(int(price))

Output:

99

The decimal portion is removed. It is not rounded to the nearest integer.

Example
print(int(10.9))
print(int(10.1))
print(int(-10.9))

Output:

10
10
-10
Important data engineering caution

When converting raw data, values may contain:

Empty strings

Spaces

Invalid text

Null values

Currency symbols

Commas

For example:

price = "₹1,299"

This cannot be directly converted using:

float(price)

Data cleaning is required before conversion.

3.14 Multiple Assignment

Python allows assigning multiple variables in one statement.

customer_name, city = "Chirag", "Bengaluru"

This is equivalent to:

customer_name = "Chirag"
city = "Bengaluru"
Example
product_price, quantity, delivery_charge = 1200, 2, 50

print(product_price)
print(quantity)
print(delivery_charge)

Output:

1200
2
50
Assign the same value to multiple variables
pending_orders = completed_orders = 0

print(pending_orders)
print(completed_orders)

Output:

0
0
Swapping variables

Python supports simple variable swapping.

first_value = 10
second_value = 20

first_value, second_value = second_value, first_value

print(first_value)
print(second_value)

Output:

20
10

This is useful when rearranging values without creating a temporary variable.

3.15 Variable Naming Best Practices

Use names that clearly communicate the meaning of the value.

Good names
customer_name = "Chirag"
order_value = 2500
delivery_charge = 50
number_of_orders = 150
Poor names
x = "Chirag"
a = 2500
n = 50
d = 150

Short names may be acceptable for small mathematical calculations, but business and pipeline code should generally use descriptive names.

Avoid ambiguous names

Instead of:

data = 2500

Prefer:

average_order_value = 2500

Instead of:

status = True

Prefer:

is_delivery_completed = True
Avoid shadowing built-in functions

Do not use names such as:

list = [1, 2, 3]
str = "NovaMart"
type = "order"

These names override access to Python’s built-in functions or types within the current scope.

Prefer:

order_list = [1, 2, 3]
order_text = "NovaMart"
order_type = "online"
3.16 Practical Project: NovaMart Order Record

Create the following file:

code\01-python-foundations\01-python-fundamentals\03_variables_and_data_types.py

Add this code:

"""
Practice variables and data types using a NovaMart order.
"""

# Order information
order_id = 1001
customer_name = "Chirag"
product_name = "Wireless Mouse"
product_price = 799.50
quantity = 2

# Order status
is_delivered = False
delivery_date = None

# Calculate order value
total_order_value = product_price * quantity

# Display order details
print("Order ID:", order_id)
print("Customer:", customer_name)
print("Product:", product_name)
print("Product price:", product_price)
print("Quantity:", quantity)
print("Total order value:", total_order_value)
print("Delivered:", is_delivered)
print("Delivery date:", delivery_date)

# Display data types
print("\nData types:")
print("Order ID:", type(order_id))
print("Customer name:", type(customer_name))
print("Product price:", type(product_price))
print("Quantity:", type(quantity))
print("Delivered:", type(is_delivered))
print("Delivery date:", type(delivery_date))

Run the file from the project root:

python code\01-python-foundations\01-python-fundamentals\03_variables_and_data_types.py

Expected output:

Order ID: 1001
Customer: Chirag
Product: Wireless Mouse
Product price: 799.5
Quantity: 2
Total order value: 1599.0
Delivered: False
Delivery date: None

Data types:
Order ID: <class 'int'>
Customer name: <class 'str'>
Product price: <class 'float'>
Quantity: <class 'int'>
Delivered: <class 'bool'>
Delivery date: <class 'NoneType'>
3.17 Practical Project: Handling Raw Order Data

Data engineering systems often receive data as strings.

For example:

raw_product_price = "799.50"
raw_quantity = "2"

Before performing calculations, convert the values.

raw_product_price = "799.50"
raw_quantity = "2"

product_price = float(raw_product_price)
quantity = int(raw_quantity)

total_order_value = product_price * quantity

print("Total order value:", total_order_value)

Output:

Total order value: 1599.0
Why conversion matters

This code does not work as intended:

raw_product_price = "799.50"
raw_quantity = "2"

total_order_value = raw_product_price * raw_quantity

Python cannot multiply two strings in the way required for order calculations.

Correct conversion is required before applying business logic.

3.18 Common Mistakes
Mistake 1: Treating numeric text as a number
quantity = "3"
price = 500

total = quantity * price

This raises a TypeError.

Correct:

quantity = int("3")
price = 500

total = quantity * price
Mistake 2: Forgetting quotation marks

Incorrect:

customer_name = Chirag

Python interprets Chirag as a variable name.

Correct:

customer_name = "Chirag"
Mistake 3: Using lowercase Boolean values

Incorrect:

is_delivered = true

Correct:

is_delivered = True
Mistake 4: Comparing None incorrectly

Prefer:

if delivery_date is None:
    print("Date unavailable")

Instead of:

if delivery_date == None:
    print("Date unavailable")
Mistake 5: Assuming int() rounds numbers
price = 99.99

print(int(price))

Output:

99

int() removes the decimal part. It does not perform normal rounding.

Mistake 6: Overwriting a Useful Variable

A variable can be reassigned at any time. However, overwriting a useful value may make the code difficult to understand or cause incorrect results.

Example
order_total = 2499.00

# Later, the same variable is reused for a different purpose
order_total = "Pending"

Now order_total no longer contains the numeric order amount.

print(order_total)

Output:

Pending
Better Approach

Use separate variables for separate meanings:

order_total = 2499.00
payment_status = "Pending"

print(order_total)
print(payment_status)

Output:

2499.0
Pending
NovaMart Example

Avoid this:

customer_data = 1500
customer_data = "Chirag"

Prefer:

customer_id = 1500
customer_name = "Chirag"

Rule: A variable should have one clear meaning throughout its useful lifetime.

Mistake 7: Confusing = with ==

The single equals sign = is used for assignment.

The double equals sign == is used for comparison.

Assignment
order_status = "Delivered"

This stores "Delivered" in the variable.

Comparison
order_status == "Delivered"

This checks whether the value is equal to "Delivered".

Output:

True
Example
order_status = "Delivered"

if order_status == "Delivered":
    print("Order completed")

Output:

Order completed
Common Mistake
if order_status = "Delivered":
    print("Order completed")

This causes a SyntaxError because assignment cannot be used in this position.

Mistake 8: Assuming All Input Values Are Numbers

Values received from users or external systems often arrive as strings.

quantity = input("Enter quantity: ")

print(type(quantity))

If the user enters 5, the output is still:

<class 'str'>
Incorrect Calculation
quantity = input("Enter quantity: ")
price = 500

total = quantity * price

This does not perform numeric multiplication because quantity is a string.

Correct Approach

Convert the input before performing calculations:

quantity = int(input("Enter quantity: "))
price = 500

total = quantity * price

print("Total:", total)

If the user enters 5, the output is:

Total: 2500

Rule: Always verify and convert data types before calculations.

Mistake 9: Using bool() Carelessly

Many beginners assume that bool() converts strings such as "False" into the Boolean value False.

That is not correct.

print(bool("True"))
print(bool("False"))

Output:

True
True

Both strings are non-empty, so both are considered truthy.

Correct Boolean Conversion

If a value comes from text, handle it explicitly:

status = "False"

is_active = status.strip().lower() == "true"

print(is_active)

Output:

False
Empty Values
print(bool(""))
print(bool(0))
print(bool(None))

Output:

False
False
False

Data engineering caution: Boolean fields from CSV files, APIs, or databases may contain values such as:

"True"
"False"
"Y"
"N"
"1"
"0"
"yes"
"no"

These values should be normalized using clear rules instead of blindly calling bool().

Mistake 10: Ignoring Floating-Point Precision

Floating-point numbers may not always represent decimal values exactly.

price = 0.1
tax = 0.2

print(price + tax)

Output may look like:

0.30000000000000004

This happens because of the way floating-point numbers are represented internally.

Better Approach for Currency

For simple learning examples, rounding may be sufficient:

total = round(price + tax, 2)

print(total)

Output:

0.3

For financial systems, use the Decimal type:

from decimal import Decimal

price = Decimal("0.10")
tax = Decimal("0.20")

total = price + tax

print(total)

Output:

0.30

Production rule: Do not depend on raw floating-point arithmetic for sensitive financial calculations.

3.18 Testing the Variables and Data Types Implementation

Create the following file:

code\01-python-foundations\01-python-fundamentals\03_variables_and_data_types.py

Add this code:

"""
Practice file for Python variables and data types.

NovaMart example:
Working with customer, product, order, and payment data.
"""


# 1. Basic variables
customer_name = "Chirag"
customer_age = 25
is_registered = True
account_balance = 1250.75

print("Customer Name:", customer_name)
print("Customer Age:", customer_age)
print("Registered:", is_registered)
print("Account Balance:", account_balance)


# 2. Checking data types
print("\nData Types:")
print(type(customer_name))
print(type(customer_age))
print(type(is_registered))
print(type(account_balance))


# 3. Order data
product_name = "Wireless Mouse"
quantity = 2
unit_price = 799.50

order_total = quantity * unit_price

print("\nOrder Details:")
print("Product:", product_name)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("Order Total:", order_total)


# 4. Type conversion
quantity_text = "3"
price_text = "450.50"

quantity_number = int(quantity_text)
price_number = float(price_text)

converted_total = quantity_number * price_number

print("\nConverted Order:")
print("Quantity:", quantity_number)
print("Price:", price_number)
print("Total:", converted_total)


# 5. None value
delivery_date = None

print("\nDelivery Date:", delivery_date)
print("Delivery Date Type:", type(delivery_date))


# 6. Multiple assignment
product_id, category, stock_available = 101, "Electronics", True

print("\nProduct Information:")
print("Product ID:", product_id)
print("Category:", category)
print("Stock Available:", stock_available)


# 7. Boolean conversion
payment_status = "Paid"
is_paid = payment_status == "Paid"

print("\nPayment Status:")
print("Payment Status:", payment_status)
print("Is Paid:", is_paid)


# 8. Currency calculation using Decimal
from decimal import Decimal

item_price = Decimal("199.99")
shipping_charge = Decimal("40.00")

final_amount = item_price + shipping_charge

print("\nFinal Amount:")
print(final_amount)
Run the File

From the project root:

python code\01-python-foundations\01-python-fundamentals\03_variables_and_data_types.py

Check that:

Customer details are printed.

Data types are displayed.

Order total is calculated.

String values are converted into numbers.

None is displayed correctly.

Multiple assignment works.

Boolean comparison works.

Decimal calculates the final amount.

3.19 Failure Scenarios and Production Considerations

In real data engineering systems, data may be incomplete, incorrectly formatted, or inconsistent.

Failure Scenario

	

Example

	

Possible Solution




Missing customer name

	

None

	

Apply validation or default handling




Invalid quantity

	

"two"

	

Validate before converting to int




Empty price

	

""

	

Handle missing values




Incorrect Boolean value

	

"False" converted with bool()

	

Normalize explicitly




Currency precision issue

	

0.1 + 0.2

	

Use Decimal where required




Variable overwritten

	

order_total = "Pending"

	

Use meaningful variable names




Wrong data type

	

"500" + 100

	

Convert data before calculation




Unexpected null value

	

Missing delivery date

	

Handle None safely

Example: Basic Validation
quantity_text = "5"

if quantity_text.isdigit():
    quantity = int(quantity_text)
    print("Valid quantity:", quantity)
else:
    print("Invalid quantity")

Output:

Valid quantity: 5
Example: Handling Missing Values
delivery_date = None

if delivery_date is None:
    print("Delivery date is not available")
else:
    print("Delivery date:", delivery_date)

Output:

Delivery date is not available
Important Production Principle

Do not assume that incoming data is clean.

Data engineers must check:

Data type

Missing values

Allowed values

Numeric ranges

Formatting

Business rules

3.20 Exercises
Exercise 1: Customer Profile

Create variables for:

Customer ID

Customer name

Customer age

Customer email

Whether the customer is active

Print each value and its data type.

Exercise 2: Product Calculation

Create variables for:

Product name

Quantity

Unit price

Discount

Calculate the final amount.

Example:

Quantity = 3
Unit Price = 500
Discount = 50

Expected result:

Final Amount = 1450
Exercise 3: Type Conversion

Start with the following values:

quantity = "4"
price = "299.99"

Convert them into suitable numeric types and calculate the total price.

Exercise 4: Missing Delivery Date

Create a variable:

delivery_date = None

Print:

Delivery date is not available

when the value is None.

Exercise 5: Boolean Normalization

Convert these text values into Boolean values:

"True"
"False"
"true"
"false"

The result should be correct regardless of capitalization.

Exercise 6: Data Quality Check

Create variables for:

quantity = -2
price = 500

Write a validation check that identifies the quantity as invalid because it is negative.

3.21 Interview Questions
Beginner Questions

What is a variable in Python?

How do you check the data type of a variable?

What is the difference between int, float, and str?

What is the use of None?

Is Python statically typed or dynamically typed?

What is the difference between = and ==?

How do you convert a string into an integer?

What happens when you convert 3.8 into an integer?

What is multiple assignment?

What are valid Python variable names?

Data Engineering Questions

Why is data type validation important in data pipelines?

Why can bool("False") return True?

Why should currency calculations sometimes use Decimal?

How would you handle missing values represented by None?

How would you convert a column containing numeric strings into numbers?

What problems can occur when a variable is overwritten?

How would you validate that an order quantity is positive?

What is the difference between missing data and an empty string?

Why should raw input data not be trusted?

How can incorrect data types affect downstream transformations?

3.22 Section Summary

In this section, you learned:

How variables store values.

How Python uses dynamic typing.

Common Python data types.

How to inspect types using type().

How to convert between data types.

How to use None for missing values.

How to assign multiple variables.

How to avoid naming mistakes.

How to handle Boolean values.

Why floating-point precision matters.

How to use Decimal for currency calculations.

How variables and data types appear in data engineering workflows.

Why validation is necessary before processing incoming data.

Python variables and data types are the foundation for working with:

CSV records

JSON documents

Database rows

API responses

DataFrames

ETL pipelines

Data validation systems

In the next section, you will learn how Python performs calculations and makes decisions using operators and expressions.

3.23 Completion Checklist

Before moving to the next section, confirm that you have:

Completed all explanations in Section 3.
Created 03_variables_and_data_types.py.
Run the file successfully.
Practiced type conversion.
Practiced handling None.
Practiced Boolean conversion.
Practiced currency calculations.
Completed the exercises.
Reviewed the interview questions.
Updated the book documentation if required.
Committed and pushed the changes to GitHub.


# 4. Operators and Expressions

## 4.1 What Are Operators?

Operators are symbols or keywords used to perform operations on values and variables.

In data engineering, operators are used to:

- Calculate order totals.
- Compare values.
- Validate records.
- Combine conditions.
- Update counters.
- Check whether values exist in collections.

Example:

```python
quantity = 3
unit_price = 500

order_total = quantity * unit_price

print(order_total)

Output:

1500

Here:

quantity and unit_price are operands.

* is the multiplication operator.

quantity * unit_price is an expression.

order_total = ... stores the result.

Python provides several types of operators:

Arithmetic operators

Comparison operators

Logical operators

Assignment operators

Membership operators

Identity operators

Bitwise operators

We will focus first on the operators most commonly used in data engineering.

4.2 Arithmetic Operators

Arithmetic operators perform mathematical calculations.

Operator

	

Meaning

	

Example

	

Result




+

	

Addition

	

10 + 3

	

13




-

	

Subtraction

	

10 - 3

	

7




*

	

Multiplication

	

10 * 3

	

30




/

	

Division

	

10 / 3

	

3.333...




//

	

Floor division

	

10 // 3

	

3




%

	

Modulus/remainder

	

10 % 3

	

1




**

	

Exponentiation

	

10 ** 3

	

1000

Addition
subtotal = 1000
shipping_charge = 100

total = subtotal + shipping_charge

print(total)

Output:

1100
Subtraction
order_amount = 1500
discount = 200

final_amount = order_amount - discount

print(final_amount)

Output:

1300
Multiplication
quantity = 4
unit_price = 250

total = quantity * unit_price

print(total)

Output:

1000
Division
total_sales = 1000
number_of_orders = 4

average_order_value = total_sales / number_of_orders

print(average_order_value)

Output:

250.0

The / operator always returns a floating-point result.

Floor Division
items = 10
boxes = 3

items_per_box = items // boxes

print(items_per_box)

Output:

3

Floor division returns the quotient rounded down to the nearest whole number.

Modulus
items = 10
box_capacity = 3

remaining_items = items % box_capacity

print(remaining_items)

Output:

1

The modulus operator is useful for identifying:

Remaining items.

Odd and even numbers.

Batch boundaries.

Partitioning logic.

Exponentiation
base = 2
power = 3

result = base ** power

print(result)

Output:

8
4.3 Comparison Operators

Comparison operators compare two values and return a Boolean result:

True
False

Operator

	

Meaning




==

	

Equal to




!=

	

Not equal to




>

	

Greater than




<

	

Less than




>=

	

Greater than or equal to




<=

	

Less than or equal to

Examples
order_amount = 2500

print(order_amount == 2500)
print(order_amount != 1000)
print(order_amount > 2000)
print(order_amount < 3000)
print(order_amount >= 2500)
print(order_amount <= 2500)

Output:

True
True
True
True
True
True
NovaMart Validation Example
quantity = 5

is_valid_quantity = quantity > 0

print(is_valid_quantity)

Output:

True

A quantity of zero or a negative quantity may be invalid for a normal order.

4.4 Logical Operators

Logical operators combine or reverse conditions.

Operator

	

Meaning




and

	

Both conditions must be true




or

	

At least one condition must be true




not

	

Reverses a Boolean result

and
order_amount = 2500
is_customer_active = True

can_process_order = order_amount > 0 and is_customer_active

print(can_process_order)

Output:

True

Both conditions must be true.

or
payment_status = "Pending"
order_status = "Processing"

needs_attention = payment_status == "Pending" or order_status == "Cancelled"

print(needs_attention)

Output:

True

At least one condition is true.

not
is_delivered = False

print(not is_delivered)

Output:

True

not reverses the Boolean value.

4.5 Assignment Operators

Assignment operators assign or update values.

Operator

	

Example

	

Equivalent To




=

	

x = 10

	

Assign 10




+=

	

x += 5

	

x = x + 5




-=

	

x -= 5

	

x = x - 5




*=

	

x *= 5

	

x = x * 5




/=

	

x /= 5

	

x = x / 5




//=

	

x //= 5

	

x = x // 5




%=

	

x %= 5

	

x = x % 5




**=

	

x **= 5

	

x = x ** 5

Example
total_sales = 1000

total_sales += 500
print(total_sales)

total_sales -= 200
print(total_sales)

Output:

1500
1300
NovaMart Counter Example
processed_orders = 0

processed_orders += 1
processed_orders += 1
processed_orders += 1

print(processed_orders)

Output:

3

This pattern is common when processing records in a loop.

4.6 Membership Operators

Membership operators check whether a value exists inside a collection.

Operator

	

Meaning




in

	

Value exists




not in

	

Value does not exist

Example with a List
available_categories = ["Electronics", "Books", "Clothing"]

print("Books" in available_categories)
print("Furniture" in available_categories)

Output:

True
False
Example with a String
order_status = "Order Delivered"

print("Delivered" in order_status)
print("Cancelled" not in order_status)

Output:

True
True

Membership checks are useful when validating:

Allowed categories.

Accepted statuses.

Required columns.

Supported file extensions.

4.7 Identity Operators

Identity operators check whether two variables refer to the same object.

Operator

	

Meaning




is

	

Same object




is not

	

Different objects

Identity is different from equality.

Equality
first_value = [1, 2, 3]
second_value = [1, 2, 3]

print(first_value == second_value)

Output:

True

The contents are equal.

Identity
print(first_value is second_value)

Output:

False

They are separate list objects.

Correct Use with None
delivery_date = None

if delivery_date is None:
    print("Delivery date is missing")

Use:

is None

instead of:

== None

when checking for None.

4.8 Operator Precedence

Operator precedence determines the order in which Python evaluates an expression.

result = 10 + 5 * 2

print(result)

Output:

20

Multiplication happens before addition.

Using Parentheses
result = (10 + 5) * 2

print(result)

Output:

30

Parentheses make the intended order explicit.

Common Precedence Order

A simplified order is:

Parentheses: ()

Exponentiation: **

Multiplication, division, floor division, modulus: * / // %

Addition and subtraction: + -

Comparisons: == != > < >= <=

not

and

or

Best Practice

Use parentheses when an expression may be difficult to read.

is_valid_order = (quantity > 0) and (unit_price > 0)

Readable expressions are easier to debug and maintain.

4.9 Expressions vs Statements

An expression produces a value.

quantity * unit_price

A statement performs an action.

order_total = quantity * unit_price

Other examples of statements include:

if order_total > 1000:
    print("High-value order")

Expressions can appear inside statements:

if quantity * unit_price > 1000:
    print("High-value order")

Understanding this difference helps when reading Python code and debugging errors.

4.10 NovaMart Order Calculation

NovaMart wants to calculate the final payable amount.

The calculation includes:

Product quantity

Unit price

Subtotal

Discount

Shipping charge

Final amount

quantity = 3
unit_price = 799.50
discount = 100
shipping_charge = 50

subtotal = quantity * unit_price
final_amount = subtotal - discount + shipping_charge

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)

Output:

Subtotal: 2398.5
Discount: 100
Shipping Charge: 50
Final Amount: 2348.5
Adding a Discount Percentage
subtotal = 3000
discount_percentage = 10

discount_amount = subtotal * discount_percentage / 100
final_amount = subtotal - discount_amount

print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)

Output:

Discount Amount: 300.0
Final Amount: 2700.0
Checking a Free-Shipping Rule
subtotal = 2500

if subtotal >= 2000:
    shipping_charge = 0
else:
    shipping_charge = 100

final_amount = subtotal + shipping_charge

print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)

Output:

Shipping Charge: 0
Final Amount: 2500
4.11 Practical Implementation

Create this file:

code\01-python-foundations\01-python-fundamentals\04_operators_and_expressions.py

Add the following code:

"""
Practice file for Python operators and expressions.

NovaMart example:
Calculating order amounts and validating order information.
"""


# 1. Arithmetic operators
quantity = 3
unit_price = 799.50

subtotal = quantity * unit_price

print("Subtotal:", subtotal)
print("Addition:", subtotal + 100)
print("Subtraction:", subtotal - 100)
print("Multiplication:", quantity * unit_price)
print("Division:", subtotal / quantity)
print("Floor Division:", 10 // 3)
print("Remainder:", 10 % 3)
print("Power:", 2 ** 3)


# 2. Comparison operators
print("\nComparison Operators:")
print(subtotal == 2398.50)
print(subtotal != 1000)
print(subtotal > 2000)
print(subtotal < 3000)
print(subtotal >= 2398.50)
print(subtotal <= 2398.50)


# 3. Logical operators
is_customer_active = True
is_payment_confirmed = True

can_process_order = (
    quantity > 0
    and unit_price > 0
    and is_customer_active
    and is_payment_confirmed
)

print("\nCan Process Order:", can_process_order)


# 4. Assignment operators
processed_orders = 0

processed_orders += 1
processed_orders += 1
processed_orders += 1

print("Processed Orders:", processed_orders)


# 5. Membership operators
allowed_statuses = ["Pending", "Processing", "Delivered"]

current_status = "Processing"

print("\nStatus Allowed:", current_status in allowed_statuses)
print("Status Not Cancelled:", current_status not in ["Cancelled"])


# 6. Identity operator
delivery_date = None

print("Delivery Date Missing:", delivery_date is None)


# 7. Discount calculation
discount_percentage = 10
discount_amount = subtotal * discount_percentage / 100

amount_after_discount = subtotal - discount_amount

print("\nDiscount Amount:", discount_amount)
print("Amount After Discount:", amount_after_discount)


# 8. Shipping calculation
if amount_after_discount >= 2000:
    shipping_charge = 0
else:
    shipping_charge = 100

final_amount = amount_after_discount + shipping_charge

print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)


# 9. Order validation
is_valid_order = (
    quantity > 0
    and unit_price > 0
    and final_amount >= 0
)

print("Is Valid Order:", is_valid_order)
4.12 Running the Implementation

From the project root, run:

python code\01-python-foundations\01-python-fundamentals\04_operators_and_expressions.py

Verify that:

Arithmetic operations produce expected values.

Comparison operators return Boolean results.

Logical conditions work correctly.

Assignment operators update values.

Membership operators check allowed statuses.

is None correctly identifies missing values.

Discount and shipping calculations work.

Order validation returns True.

Mistake 1: Using / When Integer Division Is Required

The / operator performs normal division and returns a floating-point number.

items = 10
boxes = 3

print(items / boxes)

Output:

3.3333333333333335

However, sometimes we only need the number of complete groups.

For example, NovaMart has 10 items and wants to place 3 items in each box. The number of complete boxes is 3.

Use the floor division operator //:

items = 10
boxes = 3

complete_boxes = items // boxes

print(complete_boxes)

Output:

3
Difference Between / and //

Operator

	

Purpose

	

Example

	

Result




/

	

Normal division

	

10 / 3

	

3.333...




//

	

Floor division

	

10 // 3

	

3

NovaMart Batch Processing Example

Suppose NovaMart receives 105 records and processes 20 records per batch.

total_records = 105
batch_size = 20

complete_batches = total_records // batch_size
remaining_records = total_records % batch_size

print("Complete Batches:", complete_batches)
print("Remaining Records:", remaining_records)

Output:

Complete Batches: 5
Remaining Records: 5

Here:

// calculates the number of complete batches.

% calculates the remaining records.

Important Note

Floor division rounds down, not simply toward zero.

print(7 // 2)
print(-7 // 2)

Output:

3
-4

For positive values, // often behaves like integer division. For negative values, it rounds toward negative infinity.

Rule: Use / when you need an exact division result. Use // when you need the number of complete groups or batches.

Mistake 2: Forgetting Operator Precedence

Python follows a specific order when evaluating expressions.

result = 10 + 5 * 2

print(result)

Output:

20

Multiplication happens before addition.

If addition should happen first, use parentheses:

result = (10 + 5) * 2

print(result)

Output:

30
Best Practice

Use parentheses when the intended calculation is not immediately clear.

is_valid_order = (quantity > 0) and (unit_price > 0)

Parentheses improve readability and reduce calculation mistakes.

Mistake 3: Using is Instead of ==

The == operator compares values.

The is operator checks whether two variables refer to the same object.

Incorrect Example
status = "Delivered"

if status is "Delivered":
    print("Order delivered")

This should not be used for normal value comparison.

Correct Example
status = "Delivered"

if status == "Delivered":
    print("Order delivered")

Output:

Order delivered
Correct Use of is

Use is when checking for None:

delivery_date = None

if delivery_date is None:
    print("Delivery date is missing")

Output:

Delivery date is missing

Rule:

Use == to compare values.

Use is to compare object identity.

Use is None to check for None.

Mistake 4: Dividing by Zero

Division by zero causes a ZeroDivisionError.

total_sales = 1000
number_of_orders = 0

average_order_value = total_sales / number_of_orders

This produces an error:

ZeroDivisionError
Safer Approach
total_sales = 1000
number_of_orders = 0

if number_of_orders > 0:
    average_order_value = total_sales / number_of_orders
else:
    average_order_value = 0

print("Average Order Value:", average_order_value)

Output:

Average Order Value: 0
Production Consideration

In a data pipeline, the denominator may be zero because:

No records were received.

A filter removed all records.

A file was empty.

A database query returned no rows.

Always validate the denominator before division.

Mistake 5: Allowing Negative Order Values

A negative quantity may produce an incorrect order total.

quantity = -2
unit_price = 500

total = quantity * unit_price

print(total)

Output:

-1000

The calculation is mathematically valid but does not represent a normal customer order.

Correct Approach
quantity = -2
unit_price = 500

if quantity <= 0:
    print("Invalid quantity")
else:
    total = quantity * unit_price
    print("Order Total:", total)

Output:

Invalid quantity
Additional Validation
quantity = 3
unit_price = 500

if quantity <= 0:
    print("Quantity must be greater than zero")
elif unit_price <= 0:
    print("Unit price must be greater than zero")
else:
    total = quantity * unit_price
    print("Order Total:", total)

Rule: Mathematical operations do not automatically enforce business rules. Add validation explicitly.

Mistake 6: Mixing Strings and Numbers

Python does not allow direct addition between a string and an integer.

quantity = "5"
price = 100

total = quantity + price

This causes:

TypeError
Correct Approach

Convert the string into a number:

quantity = "5"
price = 100

total = int(quantity) * price

print(total)

Output:

500
Important Difference

String addition performs concatenation:

print("10" + "20")

Output:

1020

Numeric addition performs arithmetic:

print(10 + 20)

Output:

30

Always verify the data type before performing calculations.

Mistake 7: Using Floating-Point Values for Sensitive Currency Calculations

Floating-point numbers may produce unexpected decimal results.

price = 0.1
tax = 0.2

print(price + tax)

Output may be:

0.30000000000000004
Simple Solution: round()
total = round(price + tax, 2)

print(total)

Output:

0.3
Better Solution: Decimal
from decimal import Decimal

price = Decimal("0.10")
tax = Decimal("0.20")

total = price + tax

print(total)

Output:

0.30

For financial systems, use Decimal when exact decimal arithmetic is required.

Mistake 8: Writing Very Complex Conditions

Complex conditions can become difficult to read and debug.

Difficult to Read
if quantity > 0 and unit_price > 0 and is_customer_active and is_payment_confirmed and order_status != "Cancelled":
    print("Order can be processed")
Better Approach

Break the condition into meaningful variables:

has_valid_quantity = quantity > 0
has_valid_price = unit_price > 0
customer_is_active = is_customer_active
payment_is_confirmed = is_payment_confirmed
order_is_not_cancelled = order_status != "Cancelled"

can_process_order = (
    has_valid_quantity
    and has_valid_price
    and customer_is_active
    and payment_is_confirmed
    and order_is_not_cancelled
)

if can_process_order:
    print("Order can be processed")

This is easier to understand, test, and maintain.

4.14 Practical NovaMart Order Calculator

NovaMart wants to calculate the final payable amount for an order.

The calculation includes:

Product quantity

Unit price

Subtotal

Discount percentage

Discount amount

Shipping charge

Final amount

Order validation

Example
quantity = 3
unit_price = 799.50
discount_percentage = 10

subtotal = quantity * unit_price
discount_amount = subtotal * discount_percentage / 100
amount_after_discount = subtotal - discount_amount

if amount_after_discount >= 2000:
    shipping_charge = 0
else:
    shipping_charge = 100

final_amount = amount_after_discount + shipping_charge

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Amount After Discount:", amount_after_discount)
print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)

Output:

Subtotal: 2398.5
Discount Amount: 239.85
Amount After Discount: 2158.65
Shipping Charge: 0
Final Amount: 2158.65
Adding Validation
quantity = 3
unit_price = 799.50
discount_percentage = 10

if quantity <= 0:
    print("Invalid quantity")
elif unit_price <= 0:
    print("Invalid unit price")
elif discount_percentage < 0 or discount_percentage > 100:
    print("Invalid discount percentage")
else:
    subtotal = quantity * unit_price
    discount_amount = subtotal * discount_percentage / 100
    amount_after_discount = subtotal - discount_amount

    if amount_after_discount >= 2000:
        shipping_charge = 0
    else:
        shipping_charge = 100

    final_amount = amount_after_discount + shipping_charge

    print("Final Amount:", final_amount)
4.15 Practical Implementation

Create this file:

code\01-python-foundations\01-python-fundamentals\04_operators_and_expressions.py

Add:

"""
Practice file for Python operators and expressions.

NovaMart example:
Calculating order amounts and validating order information.
"""


# 1. Arithmetic operators
quantity = 3
unit_price = 799.50

subtotal = quantity * unit_price

print("Subtotal:", subtotal)
print("Addition:", subtotal + 100)
print("Subtraction:", subtotal - 100)
print("Multiplication:", quantity * unit_price)
print("Division:", subtotal / quantity)
print("Floor Division:", 10 // 3)
print("Remainder:", 10 % 3)
print("Power:", 2 ** 3)


# 2. Comparison operators
print("\nComparison Operators:")
print(subtotal == 2398.50)
print(subtotal != 1000)
print(subtotal > 2000)
print(subtotal < 3000)
print(subtotal >= 2398.50)
print(subtotal <= 2398.50)


# 3. Logical operators
is_customer_active = True
is_payment_confirmed = True

can_process_order = (
    quantity > 0
    and unit_price > 0
    and is_customer_active
    and is_payment_confirmed
)

print("\nCan Process Order:", can_process_order)


# 4. Assignment operators
processed_orders = 0

processed_orders += 1
processed_orders += 1
processed_orders += 1

print("Processed Orders:", processed_orders)


# 5. Membership operators
allowed_statuses = ["Pending", "Processing", "Delivered"]
current_status = "Processing"

print("\nStatus Allowed:", current_status in allowed_statuses)
print("Status Not Cancelled:", current_status not in ["Cancelled"])


# 6. Identity operator
delivery_date = None

print("Delivery Date Missing:", delivery_date is None)


# 7. Discount calculation
discount_percentage = 10

discount_amount = subtotal * discount_percentage / 100
amount_after_discount = subtotal - discount_amount

print("\nDiscount Amount:", discount_amount)
print("Amount After Discount:", amount_after_discount)


# 8. Shipping calculation
if amount_after_discount >= 2000:
    shipping_charge = 0
else:
    shipping_charge = 100

final_amount = amount_after_discount + shipping_charge

print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)


# 9. Order validation
is_valid_order = (
    quantity > 0
    and unit_price > 0
    and final_amount >= 0
)

print("Is Valid Order:", is_valid_order)
4.16 Running the Implementation

From the project root, run:

python code\01-python-foundations\01-python-fundamentals\04_operators_and_expressions.py

Check that:

Arithmetic calculations work.

Comparison operators return True or False.

Logical conditions work.

Assignment operators update values.

Membership operators check statuses.

is None works correctly.

Discount and shipping calculations work.

Order validation returns True.

4.17 Testing and Production Considerations

Operators are commonly used in data engineering for:

Data quality checks.

Record validation.

Batch calculations.

Filtering records.

Conditional transformations.

Monitoring thresholds.

Calculating metrics.

Example:

quantity = 3
unit_price = 799.50

is_valid = quantity > 0 and unit_price > 0

if is_valid:
    total = quantity * unit_price
    print("Valid order total:", total)
else:
    print("Invalid order data")

Important checks include:

Avoid division by zero.

Validate numeric ranges.

Handle missing values.

Use parentheses for complex expressions.

Use Decimal for sensitive currency calculations.

Keep conditions readable.

Test boundary values such as 0, negative numbers, and empty values.

4.18 Exercises
Exercise 1: Basic Calculator

Create two numbers and calculate:

Addition

Subtraction

Multiplication

Division

Floor division

Remainder

Power

Exercise 2: Order Validation

Create:

quantity = 4
unit_price = 250

Check whether both values are greater than zero.

Exercise 3: Discount Calculation

Given:

subtotal = 5000
discount_percentage = 15

Calculate:

Discount amount

Final amount

Exercise 4: Shipping Rule

If the order amount is greater than or equal to 2000, shipping should be free. Otherwise, shipping should be 100.

Exercise 5: Status Validation

Check whether this status is allowed:

status = "Delivered"
allowed_statuses = ["Pending", "Processing", "Delivered"]
Exercise 6: Batch Processing

Given:

total_records = 105
batch_size = 20

Calculate:

Number of complete batches.

Number of remaining records.

Exercise 7: Average Order Value

Given:

total_sales = 15000
number_of_orders = 25

Calculate the average order value and safely handle the case where the number of orders is zero.

4.19 Interview Questions

What are operators in Python?

What is the difference between / and //?

What does the modulus operator return?

What is the use of **?

What is the difference between = and ==?

What is the difference between == and is?

What are logical operators?

How does operator precedence work?

What is short-circuit evaluation?

How can you prevent division-by-zero errors?

How are membership operators used in data validation?

Why should complex expressions use parentheses?

How would you validate a positive order quantity?

How would you calculate complete batches and remaining records?

Why should financial calculations be handled carefully with floating-point values?

4.20 Section Summary

In this section, you learned:

What operators and expressions are.

How arithmetic operators perform calculations.

How comparison operators return Boolean results.

How logical operators combine conditions.

How assignment operators update variables.

How membership operators validate values.

How identity operators work with objects and None.

How operator precedence affects calculations.

The difference between expressions and statements.

How to calculate NovaMart order totals.

How to validate order data.

How operators are used in data engineering pipelines.

In the next section, you will learn about Python’s built-in data structures:

Lists

Tuples

Sets

Dictionaries

These structures are essential for handling collections of records and structured data.

4.21 Completion Checklist

Before moving to Section 5, confirm that you have:

Added the remaining Common Mistakes.
Added the NovaMart order calculator.
Created 04_operators_and_expressions.py.
Run the implementation successfully.
Practiced arithmetic operators.
Practiced comparison and logical operators.
Practiced membership and identity operators.
Practiced operator precedence.
Completed the exercises.
Reviewed the interview questions.
Updated documentation if required.
Committed and pushed the changes.


5. Strings and Text Processing

Strings are one of the most commonly used data types in Python.

In data engineering, strings are used to represent:

Customer names

Product names

Email addresses

Order statuses

File paths

CSV values

JSON fields

API responses

Database text columns

For example, NovaMart may receive customer data like this:

" chirag.kaura@example.com "

Before using this value, we may need to:

Remove extra spaces.

Convert the text to lowercase.

Validate the email format.

Extract the username.

Store the cleaned value.

Python provides many built-in features for working with strings.

5.1 What Is a String?

A string is a sequence of characters enclosed within quotes.

customer_name = "Chirag"
product_name = 'Wireless Mouse'
order_status = "Delivered"

You can use either single quotes or double quotes.

first_name = "Chirag"
last_name = 'Kaura'

Both values are strings:

print(type(first_name))
print(type(last_name))

Output:

<class 'str'>
<class 'str'>

A string can contain:

Letters

Numbers

Spaces

Symbols

Special characters

customer_id = "CUST1001"
email = "chirag@example.com"
address = "Mumbai, India"

Although "1001" contains numbers, it is still a string because it is enclosed in quotes.

5.2 Creating Strings
Single Quotes
product_name = 'Laptop'
Double Quotes
product_name = "Laptop"
Triple Quotes

Triple quotes are used for multiline strings.

description = """
This product is a wireless mouse.
It has five buttons.
It is suitable for office use.
"""

print(description)

Triple quotes are also commonly used for:

Documentation strings.

Long text.

Multiline messages.

SQL queries.

JSON examples.

5.3 Strings Containing Quotes

If a string contains an apostrophe, use double quotes around it:

message = "Customer's order is confirmed"

If a string contains double quotes, use single quotes:

message = 'The customer said "Thank you"'

You can also use an escape character.

message = 'Customer\'s order is confirmed'

print(message)

Output:

Customer's order is confirmed
Common Escape Characters

Escape Sequence

	

Meaning




\n

	

New line




\t

	

Tab




\\

	

Backslash




\'

	

Single quote




\"

	

Double quote

Example:

print("NovaMart\nOrder Confirmed")

Output:

NovaMart
Order Confirmed

Example:

print("Product:\tWireless Mouse")
print("Quantity:\t2")

Output:

Product:    Wireless Mouse
Quantity:   2
5.4 String Indexing

A string is a sequence of characters. Each character has a position called an index.

Python uses zero-based indexing.

product_name = "Laptop"

Character

	

L

	

a

	

p

	

t

	

o

	

p




Index

	

0

	

1

	

2

	

3

	

4

	

5

Accessing Characters
product_name = "Laptop"

print(product_name[0])
print(product_name[1])
print(product_name[5])

Output:

L
a
p
Negative Indexing

Negative indexes start from the end.

Character

	

L

	

a

	

p

	

t

	

o

	

p




Negative Index

	

-6

	

-5

	

-4

	

-3

	

-2

	

-1

product_name = "Laptop"

print(product_name[-1])
print(product_name[-2])

Output:

p
o
Index Error

Trying to access an index that does not exist causes an error.

product_name = "Laptop"

print(product_name[10])

This causes:

IndexError

Before accessing an index, remember that valid indexes range from:

0

to:

len(product_name) - 1
5.5 Finding the Length of a String

Use the len() function to count the number of characters.

product_name = "Laptop"

print(len(product_name))

Output:

6

Spaces are also counted.

customer_name = "Chirag Kaura"

print(len(customer_name))

Output:

12
NovaMart Example
order_id = "ORD2026001"

print("Order ID:", order_id)
print("Order ID Length:", len(order_id))

String length checks are useful for:

Validating IDs.

Checking phone numbers.

Checking postal codes.

Validating text fields.

Detecting empty strings.

5.6 String Slicing

Slicing extracts part of a string.

The syntax is:

string[start:stop]

The start index is included, but the stop index is excluded.

product_name = "Laptop"

print(product_name[0:3])

Output:

Lap

Indexes 0, 1, and 2 are included. Index 3 is excluded.

More Examples
product_name = "Laptop"

print(product_name[:3])
print(product_name[3:])
print(product_name[:])

Output:

Lap
top
Laptop
Using a Step

The syntax can also include a step:

string[start:stop:step]

Example:

product_name = "Laptop"

print(product_name[::2])

Output:

Lpo
Reversing a String
product_name = "Laptop"

print(product_name[::-1])

Output:

potpaL
NovaMart Example
order_id = "ORD2026001"

prefix = order_id[:3]
year = order_id[3:7]

print("Prefix:", prefix)
print("Year:", year)

Output:

Prefix: ORD
Year: 2026
5.7 Strings Are Immutable

Strings are immutable, meaning their individual characters cannot be changed directly.

This is not allowed:

product_name = "Laptop"

product_name[0] = "T"

It causes:

TypeError
Correct Approach

Create a new string:

product_name = "Laptop"

updated_product_name = "T" + product_name[1:]

print(updated_product_name)

Output:

Taptop

Another example:

customer_name = "chirag"

customer_name = customer_name.capitalize()

print(customer_name)

Output:

Chirag

String methods return a new string instead of modifying the original string.

5.8 Common String Methods

Python provides many useful string methods.

lower()

Converts text to lowercase.

status = "DELIVERED"

print(status.lower())

Output:

delivered
upper()

Converts text to uppercase.

status = "delivered"

print(status.upper())

Output:

DELIVERED
capitalize()

Capitalizes the first character.

customer_name = "chirag"

print(customer_name.capitalize())

Output:

Chirag
title()

Capitalizes the first character of each word.

customer_name = "chirag kaura"

print(customer_name.title())

Output:

Chirag Kaura
strip()

Removes leading and trailing spaces.

customer_name = "  Chirag Kaura  "

print(customer_name.strip())

Output:

Chirag Kaura
lstrip()

Removes spaces from the left side.

value = "   NovaMart"

print(value.lstrip())
rstrip()

Removes spaces from the right side.

value = "NovaMart   "

print(value.rstrip())
replace()

Replaces one piece of text with another.

status = "Order pending"

updated_status = status.replace("pending", "confirmed")

print(updated_status)

Output:

Order confirmed
find()

Returns the index of the first occurrence of a substring.

email = "chirag@example.com"

print(email.find("@"))

Output:

6

If the substring is not found, find() returns -1.

print(email.find("#"))

Output:

-1
index()

The index() method also returns the position of a substring.

email = "chirag@example.com"

print(email.index("@"))

Output:

6

However, unlike find(), index() raises a ValueError if the substring is not found.

print(email.index("#"))

This causes:

ValueError
Difference Between find() and index()

Method

	

If value is found

	

If value is missing




find()

	

Returns index

	

Returns -1




index()

	

Returns index

	

Raises ValueError

Practical rule: Use find() when the value may not exist and you want to handle the result safely.

5.9 Counting and Checking Text
count()

Counts how many times a substring appears.

order_status = "Pending, Processing, Pending"

print(order_status.count("Pending"))

Output:

2
startswith()

Checks whether a string starts with a specific value.

order_id = "ORD2026001"

print(order_id.startswith("ORD"))

Output:

True
endswith()

Checks whether a string ends with a specific value.

file_name = "orders.csv"

print(file_name.endswith(".csv"))

Output:

True

These methods are useful for checking:

File extensions.

Order ID prefixes.

Product code formats.

API paths.

Customer identifiers.

5.10 Checking String Content
isdigit()

Checks whether all characters are digits.

quantity = "25"

print(quantity.isdigit())

Output:

True

A decimal value returns False:

price = "299.99"

print(price.isdigit())

Output:

False

The decimal point is not a digit.

isalpha()

Checks whether all characters are alphabetic.

customer_name = "Chirag"

print(customer_name.isalpha())

Output:

True

A string containing spaces returns False:

customer_name = "Chirag Kaura"

print(customer_name.isalpha())

Output:

False
isalnum()

Checks whether all characters are letters or numbers.

customer_id = "CUST1001"

print(customer_id.isalnum())

Output:

True

A hyphen causes False:

product_code = "NM-LAP-1001"

print(product_code.isalnum())

Output:

False
isspace()

Checks whether the string contains only whitespace.

value = "   "

print(value.isspace())

Output:

True
in Operator

Checks whether a substring exists inside another string.

email = "chirag@example.com"

print("@" in email)
print(".com" in email)

Output:

True
True
5.11 Splitting and Joining Strings
split()

The split() method divides a string into a list.

categories = "Electronics,Books,Clothing"

category_list = categories.split(",")

print(category_list)

Output:

['Electronics', 'Books', 'Clothing']
Splitting by Spaces
customer_name = "Chirag Kaura"

name_parts = customer_name.split(" ")

print(name_parts)

Output:

['Chirag', 'Kaura']
join()

The join() method combines string values into one string.

categories = ["Electronics", "Books", "Clothing"]

category_text = ", ".join(categories)

print(category_text)

Output:

Electronics, Books, Clothing
Important Difference
text = "A,B,C"

print(text.split(","))

Output:

['A', 'B', 'C']
values = ["A", "B", "C"]

print(",".join(values))

Output:

A,B,C

split() converts a string into a list.

join() converts a list of strings into one string.

5.12 Cleaning and Normalizing Text

Data received from external systems is often inconsistent.

Example:

raw_status = "  delivered "

The value contains:

Leading spaces.

Trailing spaces.

Lowercase text.

Cleaning the Value
raw_status = "  delivered "

clean_status = raw_status.strip().lower()

print(clean_status)

Output:

delivered
Standardizing the Status
raw_status = "  delivered "

clean_status = raw_status.strip().lower()

if clean_status == "delivered":
    final_status = "Delivered"
else:
    final_status = "Unknown"

print(final_status)

Output:

Delivered
Normalizing Customer Names
raw_name = "  chirag kaura  "

clean_name = raw_name.strip().title()

print(clean_name)

Output:

Chirag Kaura
Normalizing Email Addresses
raw_email = "  CHIRAG@EXAMPLE.COM "

clean_email = raw_email.strip().lower()

print(clean_email)

Output:

chirag@example.com
Normalizing Product Codes
raw_product_code = " nm-lap-1001 "

product_code = raw_product_code.strip().upper()

print(product_code)

Output:

NM-LAP-1001
Important Production Principle

Do not apply the same transformation to every text field.

For example:

Names may use .title().

Emails may use .lower().

Product codes may use .upper().

Status values may be mapped to standard values.

Product descriptions should usually preserve their original wording.

5.13 NovaMart Text Processing Example

NovaMart receives the following raw order information:

raw_customer_name = "  chirag kaura "
raw_email = " CHIRAG@EXAMPLE.COM "
raw_status = " delivered "
raw_product_code = " nm-lap-1001 "

Clean the values:

customer_name = raw_customer_name.strip().title()
email = raw_email.strip().lower()
status = raw_status.strip().title()
product_code = raw_product_code.strip().upper()

print("Customer Name:", customer_name)
print("Email:", email)
print("Status:", status)
print("Product Code:", product_code)

Output:

Customer Name: Chirag Kaura
Email: chirag@example.com
Status: Delivered
Product Code: NM-LAP-1001
Validating an Order ID
order_id = "ORD2026001"

is_valid_order_id = (
    order_id.startswith("ORD")
    and len(order_id) == 10
)

print("Valid Order ID:", is_valid_order_id)

Output:

Valid Order ID: True
Extracting Order Information
order_id = "ORD2026001"

order_prefix = order_id[:3]
order_year = order_id[3:7]
order_number = order_id[7:]

print("Prefix:", order_prefix)
print("Year:", order_year)
print("Order Number:", order_number)

Output:

Prefix: ORD
Year: 2026
Order Number: 001
5.14 Practical Implementation

Create this file:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\code\01-python-foundations\01-python-fundamentals\05_strings_and_text_processing.py

Add:

"""
Practice file for strings and text processing.

NovaMart example:
Cleaning and validating customer, product, and order text.
"""


# 1. Basic strings
customer_name = "Chirag"
product_name = "Wireless Mouse"
order_status = "Delivered"

print("Customer Name:", customer_name)
print("Product Name:", product_name)
print("Order Status:", order_status)


# 2. String indexing
print("\nString Indexing:")
print(product_name[0])
print(product_name[-1])


# 3. String length
print("\nString Length:")
print(len(product_name))


# 4. String slicing
order_id = "ORD2026001"

print("\nString Slicing:")
print("Prefix:", order_id[:3])
print("Year:", order_id[3:7])
print("Order Number:", order_id[7:])


# 5. String methods
raw_status = "  delivered "

print("\nString Methods:")
print("Lower:", raw_status.lower())
print("Upper:", raw_status.upper())
print("Stripped:", raw_status.strip())
print("Title:", raw_status.strip().title())


# 6. Searching and checking text
email = "chirag@example.com"

print("\nSearching and Checking:")
print("Position of @:", email.find("@"))
print("Contains @:", "@" in email)
print("Starts with chirag:", email.startswith("chirag"))
print("Ends with .com:", email.endswith(".com"))


# 7. Text normalization
raw_customer_name = "  chirag kaura "
raw_email = " CHIRAG@EXAMPLE.COM "
raw_product_code = " nm-lap-1001 "

clean_customer_name = raw_customer_name.strip().title()
clean_email = raw_email.strip().lower()
clean_product_code = raw_product_code.strip().upper()

print("\nCleaned Data:")
print("Customer Name:", clean_customer_name)
print("Email:", clean_email)
print("Product Code:", clean_product_code)


# 8. String validation
print("\nString Validation:")
print("Order ID Starts Correctly:", order_id.startswith("ORD"))
print("Email Contains @:", "@" in clean_email)
print(
    "Product Code Is Valid:",
    clean_product_code.replace("-", "").isalnum()
)


# 9. Splitting and joining
raw_categories = "electronics, books, clothing"

categories = raw_categories.split(",")

cleaned_categories = []

for category in categories:
    cleaned_categories.append(category.strip().title())

print("\nCategories:")
print(cleaned_categories)

category_text = ", ".join(cleaned_categories)

print("Joined Categories:", category_text)


# 10. f-string formatting
quantity = 3
unit_price = 799.50
total_amount = quantity * unit_price

print("\nOrder Summary:")
print(f"Customer: {clean_customer_name}")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ₹{unit_price:.2f}")
print(f"Total Amount: ₹{total_amount:.2f}")


# 11. Order ID validation
is_valid_order_id = (
    order_id.startswith("ORD")
    and len(order_id) == 10
)

print("\nOrder ID Validation:")
print("Is Valid Order ID:", is_valid_order_id)
5.15 Running the Implementation

From the project root, run:

python code\01-python-foundations\01-python-fundamentals\05_strings_and_text_processing.py
Verify that:

String values are printed.

Positive indexing works.

Negative indexing works.

String length is displayed.

String slicing extracts the correct order details.

lower(), upper(), strip(), and title() work.

find() returns the correct position.

startswith() and endswith() return Boolean values.

Customer names, emails, and product codes are normalized.

Categories are split into a list.

Categories are joined into a string.

The order summary is displayed using f-strings.

The total amount is formatted to two decimal places.

Order ID validation returns True.

Expected Output

The exact output may vary depending on your code, but it should look similar to:

Customer Name: Chirag
Product Name: Wireless Mouse
Order Status: Delivered

String Indexing:
W
e

String Length:
14

String Slicing:
Prefix: ORD
Year: 2026
Order Number: 001

String Methods:
Lower:   delivered
Upper:   DELIVERED
Stripped: delivered
Title: Delivered

Searching and Checking:
Position of @: 6
Contains @: True
Starts with chirag: True
Ends with .com: True

Cleaned Data:
Customer Name: Chirag Kaura
Email: chirag@example.com
Product Code: NM-LAP-1001

String Validation:
Order ID Starts Correctly: True
Email Contains @: True
Product Code Is Valid: True

Categories:
['Electronics', 'Books', 'Clothing']
Joined Categories: Electronics, Books, Clothing

Order Summary:
Customer: Chirag Kaura
Product: Wireless Mouse
Quantity: 3
Unit Price: ₹799.50
Total Amount: ₹2398.50

Order ID Validation:
Is Valid Order ID: True

The output does not need to match spacing exactly. The important point is that the operations execute successfully and produce the expected values.

5.16 Common Mistakes
Mistake 1: Forgetting That Indexing Starts at Zero
product_name = "Laptop"

print(product_name[1])

Output:

a

The first character is at index 0.

Mistake 2: Accessing an Invalid Index
product_name = "Laptop"

print(product_name[10])

This causes:

IndexError

Use len() to understand the valid index range.

Mistake 3: Trying to Modify a String Directly
product_name = "Laptop"

product_name[0] = "T"

This causes:

TypeError

Strings are immutable. Create a new string instead.

Mistake 4: Forgetting to Store the Result of a String Method
customer_name = "chirag"

customer_name.upper()

print(customer_name)

Output:

chirag

The original string remains unchanged.

Correct:

customer_name = customer_name.upper()

print(customer_name)

Output:

CHIRAG
Mistake 5: Confusing split() and join()

split() converts a string into a list:

text = "A,B,C"

print(text.split(","))

Output:

['A', 'B', 'C']

join() combines strings into one string:

values = ["A", "B", "C"]

print(",".join(values))

Output:

A,B,C
Mistake 6: Using index() Without Handling Missing Values
email = "chirag@example.com"

position = email.index("#")

This raises:

ValueError

Use find() when the substring may not exist:

position = email.find("#")

if position == -1:
    print("Character not found")
Mistake 7: Assuming isdigit() Handles Decimal Values
price = "299.99"

print(price.isdigit())

Output:

False

The decimal point is not a digit.

For numeric conversion, use appropriate validation:

price = "299.99"

try:
    price_number = float(price)
    print(price_number)
except ValueError:
    print("Invalid price")
Mistake 8: Calling join() on Non-String Values

This causes an error:

quantities = [1, 2, 3]

print(",".join(quantities))

join() expects strings, not integers.

Correct:

quantities = [1, 2, 3]

quantity_text = ",".join(map(str, quantities))

print(quantity_text)

Output:

1,2,3
5.17 Testing and Production Considerations

Strings are important in data engineering because external data often arrives as text.

Common sources include:

CSV files.

JSON files.

APIs.

Database columns.

Log files.

User input.

Configuration files.

Before processing string values, check:

Leading and trailing spaces.

Uppercase and lowercase differences.

Empty strings.

Missing values.

Unexpected characters.

Invalid formats.

Duplicate separators.

Encoding issues.

Inconsistent status values.

Incorrect identifiers.

Empty String Check
customer_name = "   "

if customer_name.strip() == "":
    print("Customer name is missing")
else:
    print("Customer name is valid")

Output:

Customer name is missing
Basic Email Check
email = "chirag@example.com"

if "@" in email and "." in email:
    print("Email format appears valid")
else:
    print("Invalid email format")

This is only a basic check. Production systems may require stronger validation.

Status Mapping

Instead of relying on exact incoming values, normalize them first:

status_mapping = {
    "pending": "Pending",
    "processing": "Processing",
    "delivered": "Delivered",
    "cancelled": "Cancelled",
}

raw_status = " DELIVERED "

normalized_status = raw_status.strip().lower()
final_status = status_mapping.get(normalized_status, "Unknown")

print(final_status)

Output:

Delivered
Handling Unknown Statuses
raw_status = "returned"

normalized_status = raw_status.strip().lower()
final_status = status_mapping.get(normalized_status, "Unknown")

print(final_status)

Output:

Unknown

In a production pipeline, unknown values should generally be:

Logged.

Counted.

Sent to a validation report.

Reviewed by the data-quality team.

Handled according to business rules.

5.18 Exercises
Exercise 1: String Information

Create a string containing a product name and print:

First character.

Last character.

Length.

Reversed string.

Exercise 2: Customer Name Cleaning

Given:

customer_name = "   cHIRAG kAURA   "

Convert it into:

Chirag Kaura
Exercise 3: Email Normalization

Given:

email = "  CHIRAG@EXAMPLE.COM "

Remove spaces and convert the email into lowercase.

Exercise 4: Order ID Extraction

Given:

order_id = "ORD2026001"

Extract:

Prefix.

Year.

Order number.

Exercise 5: Category Cleaning

Given:

categories = " electronics, books , clothing "

Convert it into:

["Electronics", "Books", "Clothing"]
Exercise 6: Product Code Validation

Given:

product_code = "NM-LAP-1001"

Check whether the product code:

Starts with "NM".

Contains only letters, numbers, and hyphens.

Is uppercase.

Exercise 7: Order Summary

Create an f-string showing:

Customer name.

Product name.

Quantity.

Unit price.

Total amount.

Exercise 8: Status Normalization

Convert each of the following into a standard status:

" delivered "
"DELIVERED"
"Delivered"
" delivered"

Expected result:

Delivered
Exercise 9: Safe Substring Search

Given:

email = "chirag@example.com"

Use find() to check whether the email contains:

#

Print a meaningful message when the character is not found.

Exercise 10: Convert Numbers Before Joining

Given:

order_ids = [1001, 1002, 1003]

Convert the values into one comma-separated string:

1001,1002,1003
5.19 Interview Questions

What is a string in Python?

What is zero-based indexing?

What is negative indexing?

How do you find the length of a string?

What is string slicing?

Are Python strings mutable or immutable?

What is the difference between find() and index()?

What does find() return when a substring is not found?

What is the use of strip()?

What is the difference between split() and join()?

What is the difference between replace() and strip()?

How do you check whether a string starts with a specific value?

How do you check whether a string contains only digits?

Why does "299.99".isdigit() return False?

What are f-strings?

How do you format a number to two decimal places?

How would you normalize email addresses?

How would you clean inconsistent order statuses?

How would you validate an order ID using string methods?

Why is string cleaning important in data engineering pipelines?

5.20 Section Summary

In this section, you learned:

What strings are.

How to create strings.

How to use single, double, and triple quotes.

How to use escape characters.

How string indexing works.

How negative indexing works.

How to find string length.

How to slice strings.

Why strings are immutable.

How to use common string methods.

How to search within strings using find().

The difference between find() and index().

How to split and join strings.

How to format text using f-strings.

How to clean and normalize external text data.

How to validate order IDs and product codes.

How string processing is used in data engineering.

Strings are essential when working with:

CSV columns.

JSON fields.

API responses.

Customer records.

Product data.

Database values.

Log messages.

File names and paths.

The next section is:

6. Input and Output

You will learn:

How print() works.

How to take input using input().

How to convert input values.

How to validate user input.

How to build a NovaMart order input program.

5.21 Completion Checklist

Before moving to Section 6, confirm that you have:

Added the remaining Section 5 content.
Created 05_strings_and_text_processing.py.
Run the file successfully.
Practiced string indexing.
Practiced slicing.
Practiced find() and index().
Practiced string methods.
Practiced splitting and joining.
Practiced f-strings.
Practiced text normalization.
Completed the exercises.
Reviewed the interview questions.
Updated documentation if required.
Committed and pushed the changes.