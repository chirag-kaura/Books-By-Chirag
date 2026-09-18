
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

6. Input and Output

A program becomes useful when it can communicate with the outside world.

So far, we have written programs that work with values already defined inside the code:

name = "Chirag"
age = 25

However, real-world applications need to:

Display information to users.

Accept values from users.

Read configuration values.

Receive data from files, APIs, and databases.

Format results clearly.

Validate user-provided input.

Python provides simple built-in tools for basic input and output:

print() for displaying output.

input() for receiving user input.

Understanding these two functions is essential before building larger programs.

6.1 Using print()

The print() function displays information on the screen.

Basic Example
print("Hello, Python!")

Output:

Hello, Python!

We can also print numbers:

print(100)
print(25.5)

Output:

100
25.5

We can print the result of an expression:

print(10 + 20)

Output:

30

We can also print variables:

name = "Chirag"
age = 25

print(name)
print(age)

Output:

Chirag
25
General Syntax
print(value)
6.2 Printing Multiple Values

The print() function can display multiple values separated by commas.

name = "Chirag"
age = 25
city = "Pune"

print(name, age, city)

Output:

Chirag 25 Pune

By default, Python separates multiple values using a space.

print("Name:", name)
print("Age:", age)
print("City:", city)

Output:

Name: Chirag
Age: 25
City: Pune

This is useful when displaying labels and values together.

6.3 Understanding sep

The sep parameter controls the separator between multiple values.

By default:

print("Python", "SQL", "Spark")

Output:

Python SQL Spark

We can change the separator:

print("Python", "SQL", "Spark", sep=" | ")

Output:

Python | SQL | Spark

Another example:

print("2026", "09", "19", sep="-")

Output:

2026-09-19

The separator can be any string:

print("A", "B", "C", sep="---")

Output:

A---B---C
Practical Example
order_id = "ORD1001"
customer = "Rahul"
amount = 1499

print(order_id, customer, amount, sep=" | ")

Output:

ORD1001 | Rahul | 1499
6.4 Understanding end

By default, print() moves to a new line after displaying the output.

print("Hello")
print("World")

Output:

Hello
World

The end parameter controls what is printed at the end.

print("Hello", end=" ")
print("World")

Output:

Hello World

Another example:

print("Loading", end="...")
print("Done")

Output:

Loading...Done

We can also prevent the new line:

print("Python", end=" ")
print("Programming", end=" ")
print("Language")

Output:

Python Programming Language
Important Point

The default value of end is:

"\n"

The \n character represents a new line.

6.5 Printing Formatted Output

Readable output is important in real applications.

Consider this code:

name = "Chirag"
age = 25
salary = 50000

print(name, age, salary)

Output:

Chirag 25 50000

The output is difficult to understand.

A better approach is:

print("Name:", name)
print("Age:", age)
print("Salary:", salary)

Output:

Name: Chirag
Age: 25
Salary: 50000

We can also use f-strings.

name = "Chirag"
age = 25

print(f"My name is {name} and I am {age} years old.")

Output:

My name is Chirag and I am 25 years old.

F-strings are one of the most commonly used ways to format output in modern Python.

6.6 Formatting Numbers in Output

F-strings can format numbers.

price = 1499.5678

print(f"Price: {price:.2f}")

Output:

Price: 1499.57

Here:

:.2f

means:

f means floating-point number.

.2 means two digits after the decimal point.

Formatting with Commas
revenue = 1250000

print(f"Revenue: {revenue:,}")

Output:

Revenue: 1,250,000
Formatting Percentages
conversion_rate = 0.8567

print(f"Conversion Rate: {conversion_rate:.2%}")

Output:

Conversion Rate: 85.67%
Formatting Currency
amount = 2499.5

print(f"Total Amount: ₹{amount:,.2f}")

Output:

Total Amount: ₹2,499.50
6.7 Taking Input with input()

The input() function is used to receive data from the user.

name = input("Enter your name: ")

print(f"Hello, {name}!")

Example interaction:

Enter your name: Chirag
Hello, Chirag!

The text inside input() is called the prompt.

input("Enter your name: ")

The program waits until the user enters a value and presses Enter.

General Syntax
variable = input("Prompt message: ")
6.8 Important Rule: input() Returns a String

Regardless of what the user enters, input() returns a string.

age = input("Enter your age: ")

print(age)
print(type(age))

If the user enters:

25

Output:

25
<class 'str'>

Even though the input looks like a number, Python stores it as a string.

This creates a problem when performing mathematical operations.

age = input("Enter your age: ")

print(age + 1)

This causes an error:

TypeError: can only concatenate str (not "int") to str

To perform numerical calculations, we must convert the input into the correct data type.

6.9 Converting Input Values
Converting to Integer

Use int() when the user enters a whole number.

age = int(input("Enter your age: "))

print(age + 1)

Example:

Enter your age: 25
26
Converting to Float

Use float() when the user enters a decimal number.

price = float(input("Enter product price: "))

print(price * 2)

Example:

Enter product price: 149.50
299.0

Converting to Boolean

Python uses the bool() function to convert a value into either:

True

or:

False

Example:

print(bool(1))
print(bool(0))

Output:

True
False
Truthy and Falsy Values

Python considers some values as truthy and others as falsy.

Common falsy values include:

False
None
0
0.0
""
[]
{}
()

Examples:

print(bool(""))
print(bool("Python"))

print(bool(0))
print(bool(10))

print(bool([]))
print(bool([1, 2, 3]))

Output:

False
True
False
True
False
True

The general rule is:

Empty values and zero are usually falsy. Non-empty values and non-zero numbers are usually truthy.

Important Example: Converting User Input to Boolean

Consider this code:

answer = input("Do you want to continue? ")

print(bool(answer))

If the user enters:

False

The output will be:

True

Why?

Because the string "False" is not empty.

Python checks whether the string contains any characters. It does not automatically interpret the text "False" as the Boolean value False.

print(bool("False"))
print(bool("True"))
print(bool(""))

Output:

True
True
False

This is a common beginner mistake.

Correct Way to Convert Yes/No Input

If the user enters "yes" or "no", we can explicitly check the text.

answer = input("Do you want to continue? ").strip().lower()

if answer == "yes":
    continue_process = True
else:
    continue_process = False

print(continue_process)

Example:

Do you want to continue? yes
True

Another example:

Do you want to continue? no
False

The following methods are used here:

.strip()

Removes extra spaces.

.lower()

Converts the input to lowercase.

For example:

answer = " YES "

print(answer.strip().lower())

Output:

yes
Using a Boolean Expression Directly

We can simplify the previous example:

answer = input("Do you want to continue? ").strip().lower()

continue_process = answer == "yes"

print(continue_process)

The expression:

answer == "yes"

returns either True or False.

Example:

print("yes" == "yes")
print("no" == "yes")

Output:

True
False

This is cleaner than writing a complete if-else statement.

Accepting Multiple Boolean Inputs

Sometimes a program accepts values such as:

yes

y

true

1

We can support multiple valid inputs.

answer = input("Do you want email notifications? ").strip().lower()

enabled_values = {"yes", "y", "true", "1"}

email_notifications = answer in enabled_values

print(f"Email notifications enabled: {email_notifications}")

Example:

Do you want email notifications? y
Email notifications enabled: True

Example:

Do you want email notifications? no
Email notifications enabled: False

The expression:

answer in enabled_values

checks whether the input exists in the set.

Creating a Reusable Boolean Conversion Function

Later in this book, we will learn functions in detail. For now, consider this example:

def convert_to_boolean(value):
    value = value.strip().lower()

    if value in {"yes", "y", "true", "1"}:
        return True

    if value in {"no", "n", "false", "0"}:
        return False

    return None

Example usage:

print(convert_to_boolean("yes"))
print(convert_to_boolean("false"))
print(convert_to_boolean("unknown"))

Output:

True
False
None

Here:

True means the input represents an enabled or positive value.

False means the input represents a disabled or negative value.

None means the input could not be understood.

This approach is useful when processing configuration files, command-line arguments, and data received from external systems.

Practical Example: NovaMart Delivery Confirmation

NovaMart wants to ask customers whether they want delivery notifications.

notification_input = input(
    "Do you want delivery notifications? yes/no: "
).strip().lower()

if notification_input in {"yes", "y"}:
    notifications_enabled = True
elif notification_input in {"no", "n"}:
    notifications_enabled = False
else:
    notifications_enabled = None

if notifications_enabled is True:
    print("Delivery notifications enabled.")

elif notifications_enabled is False:
    print("Delivery notifications disabled.")

else:
    print("Invalid response. Please enter yes or no.")

Example:

Do you want delivery notifications? yes/no: yes
Delivery notifications enabled.

Invalid input:

Do you want delivery notifications? yes/no: maybe
Invalid response. Please enter yes or no.
Important Note

Use:

is True

and:

is False

when you specifically want to check for the Boolean objects True and False.

For general truth checking, use:

if value:

or:

if not value:

For example:

is_active = True

if is_active:
    print("Account is active.")

Quick Practice

Try predicting the output:

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))
print(bool([]))
print(bool([0]))
print(bool(None))

Expected output:

False
True
False
True
False
True
False

The most important result to remember is:

bool("False") == True

because "False" is a non-empty string.

6.10 Input Validation Basics

User input cannot always be trusted.

A user may enter:

Text instead of a number.

A negative quantity.

An empty value.

An invalid menu option.

Unexpected spaces.

A decimal number where an integer is required.

For example:

age = int(input("Enter your age: "))

If the user enters:

twenty-five

Python raises:

ValueError

A basic validation approach is to check the input before conversion.

age_text = input("Enter your age: ")

if age_text.isdigit():
    age = int(age_text)
    print(f"Your age is {age}")
else:
    print("Please enter a valid whole number.")
Using strip()

The strip() method removes extra spaces from the beginning and end of a string.

name = input("Enter your name: ").strip()

print(f"Hello, {name}")

If the user enters:

   Chirag

The stored value becomes:

Chirag
Checking for Empty Input
name = input("Enter your name: ").strip()

if name == "":
    print("Name cannot be empty.")
else:
    print(f"Welcome, {name}!")

A shorter version is:

if not name:
    print("Name cannot be empty.")
6.11 Practical Example: NovaMart Order Input

NovaMart needs a simple program that accepts order information from a user and displays a formatted order summary.

The program should collect:

Customer name.

Product name.

Quantity.

Unit price.

Basic Implementation
customer_name = input("Enter customer name: ").strip()
product_name = input("Enter product name: ").strip()
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total_amount = quantity * unit_price

print("\n----- NovaMart Order Summary -----")
print(f"Customer: {customer_name}")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ₹{unit_price:,.2f}")
print(f"Total Amount: ₹{total_amount:,.2f}")

Example interaction:

Enter customer name: Rahul
Enter product name: Keyboard
Enter quantity: 2
Enter unit price: 1499

----- NovaMart Order Summary -----
Customer: Rahul
Product: Keyboard
Quantity: 2
Unit Price: ₹1,499.00
Total Amount: ₹2,998.00
What This Program Demonstrates

This example combines:

input()

print()

strip()

int()

float()

Arithmetic operators.

F-strings.

Number formatting.

User-friendly output.

These concepts are frequently used in command-line tools and data-processing scripts.

6.12 Improving the NovaMart Program

The previous implementation assumes that the user enters valid values.

We can add basic validation.

customer_name = input("Enter customer name: ").strip()
product_name = input("Enter product name: ").strip()

if not customer_name:
    print("Customer name cannot be empty.")

elif not product_name:
    print("Product name cannot be empty.")

else:
    quantity_text = input("Enter quantity: ").strip()
    price_text = input("Enter unit price: ").strip()

    if not quantity_text.isdigit():
        print("Quantity must be a whole number.")

    else:
        quantity = int(quantity_text)

        if quantity <= 0:
            print("Quantity must be greater than zero.")

        else:
            try:
                unit_price = float(price_text)

                if unit_price <= 0:
                    print("Unit price must be greater than zero.")

                else:
                    total_amount = quantity * unit_price

                    print("\n----- NovaMart Order Summary -----")
                    print(f"Customer: {customer_name}")
                    print(f"Product: {product_name}")
                    print(f"Quantity: {quantity}")
                    print(f"Unit Price: ₹{unit_price:,.2f}")
                    print(f"Total Amount: ₹{total_amount:,.2f}")

            except ValueError:
                print("Unit price must be a valid number.")

This version is longer, but it handles common invalid inputs.

Later, we will learn better ways to organize validation using:

Functions.

Loops.

Exceptions.

Custom validation logic.

6.13 Practical Implementation

Create the following file:

code\01-python-foundations\01-python-fundamentals\06_input_and_output.py

Add the following code:

"""
Section 6: Input and Output

This program demonstrates:
- print()
- sep
- end
- input()
- Type conversion
- split()
- Basic validation
- Formatted output
"""


# --------------------------------------------------
# 1. Basic print()
# --------------------------------------------------

print("Hello, Python!")

print(100)
print(25.5)
print(10 + 20)


# --------------------------------------------------
# 2. Printing variables
# --------------------------------------------------

name = "Chirag"
age = 25

print(name)
print(age)

print("Name:", name)
print("Age:", age)


# --------------------------------------------------
# 3. sep parameter
# --------------------------------------------------

print("Python", "SQL", "Spark", sep=" | ")


# --------------------------------------------------
# 4. end parameter
# --------------------------------------------------

print("Hello", end=" ")
print("World")


# --------------------------------------------------
# 5. Formatted output
# --------------------------------------------------

salary = 50000

print(f"Employee: {name}, Salary: ₹{salary:,}")


# --------------------------------------------------
# 6. Number formatting
# --------------------------------------------------

price = 1499.5678

print(f"Price: ₹{price:,.2f}")


# --------------------------------------------------
# 7. Basic input
# --------------------------------------------------

user_name = input("Enter your name: ").strip()

if user_name:
    print(f"Hello, {user_name}!")
else:
    print("Name cannot be empty.")


# --------------------------------------------------
# 8. Numeric input
# --------------------------------------------------

age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    user_age = int(age_text)
    print(f"Next year, you will be {user_age + 1}.")
else:
    print("Age must be a whole number.")


# --------------------------------------------------
# 9. Multiple inputs
# --------------------------------------------------

try:
    first_number, second_number = map(
        int,
        input("Enter two numbers separated by space: ").split()
    )

    print(f"Sum: {first_number + second_number}")

except ValueError:
    print("Please enter exactly two whole numbers.")


# --------------------------------------------------
# 10. Boolean input
# --------------------------------------------------

notification_input = input(
    "Do you want email notifications? yes/no: "
).strip().lower()

enabled_values = {"yes", "y", "true", "1"}

email_notifications = notification_input in enabled_values

print(f"Email notifications enabled: {email_notifications}")


# --------------------------------------------------
# 11. NovaMart order summary
# --------------------------------------------------

customer_name = input("Enter customer name: ").strip()
product_name = input("Enter product name: ").strip()
quantity_text = input("Enter quantity: ").strip()
unit_price_text = input("Enter unit price: ").strip()

if not customer_name or not product_name:
    print("Customer name and product name are required.")

elif not quantity_text.isdigit():
    print("Quantity must be a whole number.")

else:
    quantity = int(quantity_text)

    try:
        unit_price = float(unit_price_text)

        if quantity <= 0:
            print("Quantity must be greater than zero.")

        elif unit_price <= 0:
            print("Unit price must be greater than zero.")

        else:
            total_amount = quantity * unit_price

            print("\n----- NovaMart Order Summary -----")
            print(f"Customer: {customer_name}")
            print(f"Product: {product_name}")
            print(f"Quantity: {quantity}")
            print(f"Unit Price: ₹{unit_price:,.2f}")
            print(f"Total Amount: ₹{total_amount:,.2f}")

    except ValueError:
        print("Unit price must be a valid number.")
6.14 Running the Implementation

Open the terminal from the project root:

E:\Books-By-Chirag\Data Engineering - The Complete Journey

Run:

python code\01-python-foundations\01-python-fundamentals\06_input_and_output.py

The program will ask for different values.

Example:

Enter your name: Chirag
Enter your age: 25
Enter two numbers separated by space: 10 20
Do you want email notifications? yes/no: yes
Enter customer name: Rahul
Enter product name: Keyboard
Enter quantity: 2
Enter unit price: 1499

Expected order output:

----- NovaMart Order Summary -----
Customer: Rahul
Product: Keyboard
Quantity: 2
Unit Price: ₹1,499.00
Total Amount: ₹2,998.00
6.15 Common Mistakes
Mistake 1: Treating input() as a number

Incorrect:

age = input("Enter age: ")

print(age + 1)

Correct:

age = int(input("Enter age: "))

print(age + 1)
Mistake 2: Forgetting to convert decimal input

Incorrect:

price = int(input("Enter price: "))

This fails for:

1499.50

Correct:

price = float(input("Enter price: "))
Mistake 3: Using bool() directly on user input

Incorrect:

answer = bool(input("Continue? "))

The string "False" is non-empty and therefore truthy.

Better:

answer = input("Continue? ").strip().lower()

if answer == "yes":
    print("Continuing...")
else:
    print("Stopping...")
Mistake 4: Not handling invalid numeric input

Risky:

quantity = int(input("Enter quantity: "))

If the user enters text, the program crashes.

Safer:

try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Invalid quantity.")
Mistake 5: Forgetting strip()

Without strip():

name = input("Enter name: ")

The user may accidentally enter extra spaces.

Better:

name = input("Enter name: ").strip()
Mistake 6: Incorrect f-string formatting

Incorrect:

price = 1499.5

print(f"₹{price.2f}")

Correct:

print(f"₹{price:.2f}")
Mistake 7: Expecting split() to convert values
a, b = input().split()

Both values are strings.

For integers:

a, b = map(int, input().split())
6.16 Testing and Production Considerations

Input and output code should be tested with different types of values.

Test Case 1: Valid Input
Customer: Rahul
Product: Keyboard
Quantity: 2
Unit Price: 1499

Expected:

Total Amount: ₹2,998.00
Test Case 2: Empty Customer Name
Customer:

Expected:

Customer name and product name are required.
Test Case 3: Invalid Quantity
Quantity: two

Expected:

Quantity must be a whole number.
Test Case 4: Negative Quantity
Quantity: -2

Expected behavior:

Quantity must be a whole number.

Note: .isdigit() does not accept negative numbers. Later, we will implement more flexible validation.

Test Case 5: Decimal Unit Price
Unit Price: 1499.75

Expected:

Unit Price: ₹1,499.75
Production Considerations

In production applications:

Do not assume user input is valid.

Validate all external input.

Use clear error messages.

Avoid exposing technical tracebacks to end users.

Keep input validation separate from business logic.

Use logging for unexpected failures.

Use functions to avoid repeating validation code.

Use appropriate data types for financial calculations.

Consider Decimal instead of float for financial amounts.

For example:

from decimal import Decimal

price = Decimal("1499.50")
quantity = 2

total = price * quantity

print(total)

Output:

2999.00
6.17 Exercises
Exercise 1: Personal Introduction

Write a program that accepts:

Name.

Age.

City.

Display:

My name is Chirag.
I am 25 years old.
I live in Pune.
Exercise 2: Simple Calculator

Accept two numbers and display:

Addition.

Subtraction.

Multiplication.

Division.

Example:

Enter first number: 20
Enter second number: 5

Addition: 25
Subtraction: 15
Multiplication: 100
Division: 4.0
Exercise 3: Temperature Converter

Accept temperature in Celsius and convert it to Fahrenheit.

Formula:

F=(C×
5
9
	​

)+32
Exercise 4: Employee Salary Summary

Accept:

Employee name.

Monthly salary.

Number of working months.

Calculate annual salary.

Example:

Employee: Chirag
Monthly Salary: ₹50,000
Annual Salary: ₹600,000
Exercise 5: Shopping Bill

Accept:

Product name.

Quantity.

Price.

Display the total bill using two decimal places.

Exercise 6: Data Engineering Tools

Accept three tool names from the user:

Python
SQL
Spark

Display them in this format:

Python | SQL | Spark
Exercise 7: Input Validation

Accept an age and check whether it is:

Empty.

Invalid.

Less than zero.

A valid age.

6.18 Interview Questions
Question 1

What is the difference between print() and input()?

Answer:

print() displays output.

input() receives user input and returns it as a string.

Question 2

What data type does input() return?

Answer:

input() always returns a string.

Question 3

How do you accept an integer from the user?

age = int(input("Enter age: "))
Question 4

What is the purpose of sep in print()?

Answer:

sep defines the separator between multiple values.

print("A", "B", "C", sep="-")

Output:

A-B-C
Question 5

What is the purpose of end in print()?

Answer:

end defines what is printed after the output.

print("Hello", end=" ")
print("World")

Output:

Hello World
Question 6

What does split() do?

Answer:

It divides a string into a list of smaller strings.

"Python SQL Spark".split()

Result:

['Python', 'SQL', 'Spark']
Question 7

How do you accept two integers in one line?

a, b = map(int, input().split())
Question 8

Why is bool("False") equal to True?

Answer:

Because "False" is a non-empty string, and all non-empty strings are truthy in Python.

Question 9

How do you format a number to two decimal places?

price = 1499.5678

print(f"{price:.2f}")

Output:

1499.57
Question 10

How can invalid numeric input be handled?

Answer:

Use try-except.

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number.")
6.19 Summary

In this section, we learned how Python programs communicate with users.

Important concepts included:

Using print() to display output.

Printing multiple values.

Using sep to control separators.

Using end to control line endings.

Formatting output with f-strings.

Formatting currency, percentages, and decimals.

Using input() to receive user input.

Understanding that input() returns a string.

Converting input using int() and float().

Converting values to Boolean values.

Understanding truthy and falsy values.

Taking multiple inputs using split().

Validating empty and invalid input.

Building a NovaMart order summary.

Handling input errors using try-except.

Input and output are foundational skills for command-line applications, automation scripts, ETL tools, and data engineering workflows.

6.20 Completion Checklist

Before moving to the next section, confirm that you can:

Use print() to display values.
Print variables and expressions.
Print multiple values.
Use sep to control separators.
Use end to control line endings.
Format strings using f-strings.
Format decimal numbers.
Format currency values.
Format percentages.
Use input() to accept user input.
Understand that input() returns a string.
Convert strings to integers.
Convert strings to floats.
Convert values to Boolean values.
Understand truthy and falsy values.
Use strip() to remove extra spaces.
Use split() to divide input into multiple values.
Use map() to convert multiple inputs.
Check for empty input.
Validate numeric input.
Handle invalid input using try-except.
Build a simple order summary program.
Format output in a user-friendly way.
Run the implementation file successfully.
6.21 Final Section Practice

Complete the following mini-project without directly copying the previous NovaMart implementation.

Mini-Project: NovaMart Customer Order

Create a program that accepts:

Customer name.

Product name.

Quantity.

Unit price.

Whether the customer wants delivery notifications.

The program should:

Remove unnecessary spaces from text input.

Convert quantity into an integer.

Convert unit price into a float.

Convert the notification response into a Boolean value.

Calculate the total amount.

Display a formatted order summary.

Expected Output
----- NovaMart Customer Order -----

Customer: Chirag
Product: Wireless Mouse
Quantity: 2
Unit Price: ₹799.00
Total Amount: ₹1,598.00
Delivery Notifications: True
Additional Requirements

Your program should also:

Reject an empty customer name.

Reject an empty product name.

Reject a quantity less than or equal to zero.

Reject a unit price less than or equal to zero.

Display a message for invalid notification input.

Avoid crashing when the user enters invalid numeric values.

6.22 Section Review

Input and output are the connection between a Python program and the outside world.

The main flow is:

Receive Input
     ↓
Clean Input
     ↓
Convert Data Type
     ↓
Validate Input
     ↓
Process Data
     ↓
Format Output
     ↓
Display Result

For example, in a shopping application:

Customer enters quantity
     ↓
Convert quantity to integer
     ↓
Check quantity is greater than zero
     ↓
Calculate total price
     ↓
Display formatted bill

This pattern is used in many real-world applications, including:

Command-line tools.

Data ingestion scripts.

ETL pipelines.

Configuration utilities.

Automation scripts.

Data validation programs.

Interactive applications.

6.23 Important Concepts to Remember
print()

Used to display output.

print("Hello Python")
input()

Used to receive user input.

name = input("Enter name: ")
int()

Converts a value into an integer.

age = int("25")
float()

Converts a value into a floating-point number.

price = float("1499.50")
bool()

Converts a value into True or False.

print(bool(1))
print(bool(0))
strip()

Removes leading and trailing spaces.

name = input().strip()
split()

Divides a string into multiple parts.

values = "10 20 30".split()
map()

Applies a conversion function to multiple values.

numbers = map(int, input().split())
try-except

Handles errors without immediately crashing the program.

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number.")
6.24 Key Takeaways

print() is used to display information.

input() always returns a string.

Numeric input must be converted before performing calculations.

int() is used for whole numbers.

float() is used for decimal numbers.

bool() converts values based on truthiness.

A non-empty string such as "False" is truthy.

strip() helps clean text input.

split() helps process multiple values.

map() is useful for converting multiple inputs.

Input validation prevents incorrect data from entering a program.

try-except helps handle conversion errors.

F-strings make output easier to read.

Currency and decimal values should be formatted carefully.

Production applications should separate input validation from business logic.

6.25 Section Completion

Section 6 — Input and Output is now complete.

You have learned how to:

Display information.

Accept user input.

Convert input values.

Work with Boolean input.

Validate values.

Handle invalid input.

Format output.

Build a basic customer order program.

The next section will introduce None and Basic Missing Values. This topic was briefly introduced earlier, but we will now explore it in more detail and understand why missing values matter in data engineering.

Save Your Work

Run the implementation file:

python code\01-python-foundations\01-python-fundamentals\06_input_and_output.py

Check that the program executes successfully.


Section 7 — None and Basic Missing Values

Add the following content to:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\book\01-python-foundations\01-python-fundamentals.md

Place it after Section 6 — Input and Output.

# 7. `None` and Basic Missing Values

In real-world data engineering, values are not always available.

A customer may not provide an email address.  
A transaction may not have a discount.  
A delivery record may not contain a completed delivery date.  
A database column may contain a missing value.

Python represents the absence of a value using a special object called `None`.

Understanding `None` is important because data engineers frequently work with incomplete, missing, or unavailable data.

---

## 7.1 Understanding `None`

`None` is a special Python value that represents the absence of a value.

It is not the same as:

- `0`
- `False`
- An empty string `""`
- An empty list `[]`
- An empty dictionary `{}`

Example:

```python
customer_email = None

print(customer_email)
print(type(customer_email))

Output:

None
<class 'NoneType'>

The type of None is NoneType.

There is only one None object in a normal Python program.

Example
delivery_date = None

print(delivery_date)

Output:

None

This means that the delivery date is currently unavailable.

It does not mean that the delivery date is:

"None"

0

False

An empty string

It means that no value has been assigned.

7.2 None Is Not Zero or an Empty Value

It is important to understand the difference between None and other values.

value_none = None
value_zero = 0
value_false = False
value_empty_string = ""
value_empty_list = []

print(value_none)
print(value_zero)
print(value_false)
print(value_empty_string)
print(value_empty_list)

Output:

None
0
False

[]

Each value has a different meaning.

Value

	

Meaning




None

	

Value is absent or unavailable




0

	

Numeric value is zero




False

	

Boolean condition is false




""

	

String contains no characters




[]

	

List contains no elements




{}

	

Dictionary contains no key-value pairs

Example: Customer Information
customer_name = "Aarav"
customer_email = None
customer_age = 0
customer_is_active = False

print(customer_name)
print(customer_email)
print(customer_age)
print(customer_is_active)

Here:

The customer has a name.

The email address is missing.

The customer's age is recorded as 0.

The customer is marked as inactive.

These values should not be treated as interchangeable.

7.3 Checking for None Using is

The recommended way to check whether a value is None is by using is.

customer_email = None

if customer_email is None:
    print("Email address is missing")

Output:

Email address is missing

To check whether a value is not None, use:

customer_email = "aarav@example.com"

if customer_email is not None:
    print("Email address is available")

Output:

Email address is available
Why Use is?

Use:

value is None

Instead of:

value == None

The is operator checks whether two references point to the same object.

The == operator checks whether two values are equal.

For checking None, Python convention recommends:

is None

and:

is not None
Example
value = None

print(value is None)
print(value is not None)

Output:

True
False
7.4 Comparing None with Other Values

Let's compare None with different values.

print(None == 0)
print(None == "")
print(None == False)
print(None == [])
print(None is None)

Output:

False
False
False
False
True

This demonstrates that None is different from all these values.

Important Rule

Use:

if value is None:

Do not use:

if value == None:

Although the second form may work in many cases, the first form is the standard and recommended Python style.

7.5 None and Boolean Conditions

None behaves as a falsy value in a Boolean condition.

Example:

value = None

if value:
    print("Value is available")
else:
    print("Value is missing or falsy")

Output:

Value is missing or falsy

However, a Boolean check alone cannot tell us whether the value is specifically None.

Consider:

value = 0

if value:
    print("Value is available")
else:
    print("Value is missing or falsy")

Output:

Value is missing or falsy

The value is 0, not None.

Therefore, these two checks have different meanings.

Check for Missing Value
if value is None:
    print("Value is missing")
Check for Any Falsy Value
if not value:
    print("Value is missing or falsy")

The second check also matches:

0

False

""

[]

{}

None

Example
values = [None, 0, False, "", [], "Python", 10]

for value in values:
    if value is None:
        print("Specifically None:", value)

Output:

Specifically None: None

Only the None value matches the condition.

7.6 Functions That Return None

A Python function returns None when it does not explicitly return another value.

Example:

def greet_customer():
    print("Welcome to NovaMart")


result = greet_customer()

print(result)

Output:

Welcome to NovaMart
None

The function prints a message but does not use the return statement.

Therefore, the function automatically returns None.

Function with an Explicit Return
def calculate_total():
    return 500


result = calculate_total()

print(result)

Output:

500
Function Without a Return Value
def display_total():
    print("Total amount: 500")


result = display_total()

print(result)

Output:

Total amount: 500
None
Important Difference

print() displays a value.

return sends a value back to the caller.

Example:

def add_numbers(a, b):
    print(a + b)


result = add_numbers(10, 20)

print("Result:", result)

Output:

30
Result: None

The function displayed 30, but it did not return 30.

Correct version:

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Result:", result)

Output:

Result: 30

This distinction becomes very important when building reusable data processing functions.

7.7 None in Data Engineering

Data engineering pipelines frequently process incomplete data.

For example, a customer dataset may contain:

customer = {
    "customer_id": 101,
    "name": "Aarav",
    "email": None,
    "phone": "9876543210",
    "city": None
}

Here:

customer_id is available.

name is available.

email is missing.

phone is available.

city is missing.

We can check missing values individually.

if customer["email"] is None:
    print("Email is missing")

if customer["city"] is None:
    print("City is missing")

Output:

Email is missing
City is missing
Why Missing Values Matter

Missing values can affect:

Data quality

Data validation

Data transformation

Database loading

Analytics

Machine learning

Reporting

Business decisions

For example, a missing email address may be acceptable for some reports but unacceptable for an email marketing pipeline.

A missing transaction amount may be a serious data quality problem.

A missing delivery date may be normal for an order that has not yet been delivered.

The meaning of a missing value depends on the business context.

7.8 Handling Missing Values with Default Values

Sometimes we want to replace a missing value with a default value.

Example:

customer_email = None

if customer_email is None:
    customer_email = "Not Provided"

print(customer_email)

Output:

Not Provided

A shorter version is:

customer_email = None

display_email = customer_email if customer_email is not None else "Not Provided"

print(display_email)

Output:

Not Provided
Using or

Python also allows:

customer_email = None

display_email = customer_email or "Not Provided"

print(display_email)

Output:

Not Provided

However, be careful.

The or operator replaces every falsy value, not only None.

Example:

customer_age = 0

display_age = customer_age or "Not Provided"

print(display_age)

Output:

Not Provided

This may be incorrect because 0 is a real value.

If we only want to replace None, use an explicit check:

customer_age = 0

if customer_age is None:
    display_age = "Not Provided"
else:
    display_age = customer_age

print(display_age)

Output:

0
Recommended Approach

Use an explicit None check when 0, False, or an empty string may be valid values.

7.9 Practical Example: NovaMart Customer Data

Suppose NovaMart receives customer records from an external system.

Some records contain missing email addresses or city names.

customer_records = [
    {
        "customer_id": 101,
        "name": "Aarav",
        "email": "aarav@example.com",
        "city": "Mumbai"
    },
    {
        "customer_id": 102,
        "name": "Diya",
        "email": None,
        "city": "Pune"
    },
    {
        "customer_id": 103,
        "name": "Kabir",
        "email": "kabir@example.com",
        "city": None
    }
]

We can identify records with missing values.

for customer in customer_records:
    if customer["email"] is None:
        print("Missing email:", customer["customer_id"])

    if customer["city"] is None:
        print("Missing city:", customer["customer_id"])

Output:

Missing email: 102
Missing city: 103
Creating a Clean Display Record
for customer in customer_records:
    email = customer["email"]
    city = customer["city"]

    if email is None:
        email = "Not Provided"

    if city is None:
        city = "Not Provided"

    print(
        f"Customer: {customer['name']}, "
        f"Email: {email}, "
        f"City: {city}"
    )

Output:

Customer: Aarav, Email: aarav@example.com, City: Mumbai
Customer: Diya, Email: Not Provided, City: Pune
Customer: Kabir, Email: kabir@example.com, City: Not Provided

This is a basic example of data cleaning.

7.10 Practical Implementation

Create the following Python file:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\code\01-python-foundations\01-python-fundamentals\07_none_and_missing_values.py

Add the following code:

"""
Section 7: None and Basic Missing Values

This script demonstrates:
1. Understanding None
2. Checking for None
3. Difference between None and falsy values
4. Functions returning None
5. Handling missing customer data
"""

print("SECTION 7: NONE AND BASIC MISSING VALUES")
print("-" * 50)


# --------------------------------------------------
# 1. Understanding None
# --------------------------------------------------

customer_email = None

print("\n1. Understanding None")
print("Customer email:", customer_email)
print("Data type:", type(customer_email))
print("Is None:", customer_email is None)


# --------------------------------------------------
# 2. None Compared with Other Values
# --------------------------------------------------

print("\n2. Comparing None with Other Values")

print("None == 0:", None == 0)
print('None == "":', None == "")
print("None == False:", None == False)
print("None == []:", None == [])
print("None is None:", None is None)


# --------------------------------------------------
# 3. Checking for Missing Values
# --------------------------------------------------

print("\n3. Checking for Missing Values")

phone_number = None

if phone_number is None:
    print("Phone number is missing")
else:
    print("Phone number is available")


# --------------------------------------------------
# 4. None and Falsy Values
# --------------------------------------------------

print("\n4. None and Falsy Values")

values = [None, 0, False, "", [], "Python", 10]

for value in values:
    if value is None:
        print(f"{value!r} is specifically None")
    elif not value:
        print(f"{value!r} is falsy but not None")
    else:
        print(f"{value!r} is truthy")


# --------------------------------------------------
# 5. Function Returning None
# --------------------------------------------------

print("\n5. Function Returning None")


def display_welcome_message():
    print("Welcome to NovaMart")


result = display_welcome_message()

print("Returned value:", result)


# --------------------------------------------------
# 6. Function Returning a Value
# --------------------------------------------------

print("\n6. Function Returning a Value")


def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(250, 3)

print("Calculated total:", total)


# --------------------------------------------------
# 7. NovaMart Customer Records
# --------------------------------------------------

print("\n7. NovaMart Customer Records")

customer_records = [
    {
        "customer_id": 101,
        "name": "Aarav",
        "email": "aarav@example.com",
        "city": "Mumbai"
    },
    {
        "customer_id": 102,
        "name": "Diya",
        "email": None,
        "city": "Pune"
    },
    {
        "customer_id": 103,
        "name": "Kabir",
        "email": "kabir@example.com",
        "city": None
    }
]

for customer in customer_records:
    print(f"\nCustomer ID: {customer['customer_id']}")
    print(f"Name: {customer['name']}")

    if customer["email"] is None:
        print("Email: Not Provided")
    else:
        print(f"Email: {customer['email']}")

    if customer["city"] is None:
        print("City: Not Provided")
    else:
        print(f"City: {customer['city']}")


# --------------------------------------------------
# 8. Counting Missing Values
# --------------------------------------------------

print("\n8. Counting Missing Values")

missing_email_count = 0
missing_city_count = 0

for customer in customer_records:
    if customer["email"] is None:
        missing_email_count += 1

    if customer["city"] is None:
        missing_city_count += 1

print("Missing email count:", missing_email_count)
print("Missing city count:", missing_city_count)


# --------------------------------------------------
# 9. Final Summary
# --------------------------------------------------

print("\n" + "-" * 50)
print("Section 7 completed successfully.")
print("Key concept: None represents an absent or unavailable value.")
7.11 Running the Implementation

Open PowerShell in the project root:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

Run the script:

python code\01-python-foundations\01-python-fundamentals\07_none_and_missing_values.py

You should see output demonstrating:

The type of None

Comparisons with other values

Missing value checks

Functions returning None

Customer records with missing data

Missing email and city counts

## 7.12 Common Mistakes

### Mistake 1: Comparing with the String `"None"`

Incorrect:

```python
email = None

if email == "None":
    print("Email is missing")

This condition is false because None and "None" are different values.

Correct:

if email is None:
    print("Email is missing")
Mistake 2: Using 0 to Represent Missing Data

Incorrect:

customer_age = 0

This may incorrectly suggest that the customer is zero years old.

Better:

customer_age = None

Use None when the age is unavailable.

However, if the business system explicitly uses 0 to represent missing data, that rule should be documented and handled during data cleaning.

Mistake 3: Using False to Represent Missing Data

Incorrect:

customer_is_verified = False

This means the customer is not verified.

It does not necessarily mean that verification information is missing.

A better representation would be:

customer_is_verified = None

This allows us to distinguish between:

Value

	

Meaning




True

	

Customer is verified




False

	

Customer is not verified




None

	

Verification status is unknown

This distinction is important in business and analytics systems.

Mistake 4: Confusing print() with return

Incorrect:

def calculate_total(price, quantity):
    print(price * quantity)

This function displays the result but returns None.

Example:

result = calculate_total(100, 3)

print(result)

Output:

300
None

Correct:

def calculate_total(price, quantity):
    return price * quantity

Now:

result = calculate_total(100, 3)

print(result)

Output:

300
Mistake 5: Using == None Instead of is None

Although the following may work:

if value == None:
    print("Missing")

The recommended Python style is:

if value is None:
    print("Missing")

Use:

if value is not None:
    print("Value is available")

when checking that a value exists.

Mistake 6: Replacing Valid Falsy Values

Consider:

discount = 0

display_discount = discount or "Not Available"

print(display_discount)

Output:

Not Available

This may be incorrect because a discount of 0 can be a valid value.

Use an explicit check instead:

discount = 0

if discount is None:
    display_discount = "Not Available"
else:
    display_discount = discount

print(display_discount)

Output:

0

The explicit check replaces only None.

Mistake 7: Accessing a Missing Dictionary Key

Consider:

customer = {
    "name": "Aarav"
}

print(customer["email"])

This raises:

KeyError

Use .get() when a key may not exist:

email = customer.get("email")

print(email)

Output:

None

You can also provide a default value:

email = customer.get("email", "Not Provided")

print(email)

Output:

Not Provided
Mistake 8: Assuming All Missing Values Are the Same

These values may look similar but have different meanings:

email_1 = None
email_2 = ""
email_3 = "N/A"
email_4 = "unknown"

They may represent:

None: Value is absent

"": Empty string received

"N/A": Not applicable or unavailable

"unknown": Source system does not know the value

Before cleaning these values, understand the source system and business rules.

Mistake 9: Performing Operations on None

Incorrect:

price = None

total = price * 2

print(total)

This raises a TypeError because Python cannot multiply None by an integer.

Correct:

price = None

if price is None:
    print("Price is missing")
else:
    total = price * 2
    print(total)

Another option is to assign a default value:

price = None

if price is None:
    price = 0

total = price * 2

print(total)

However, replacing a missing price with 0 is only correct if the business rule allows it.

Mistake 10: Forgetting That Missing Data Requires a Business Rule

Consider a missing delivery date:

delivery_date = None

Possible meanings include:

The order has not been delivered.

The delivery date was not recorded.

The source system failed.

The order was cancelled.

The data has not arrived yet.

The correct handling depends on the business meaning.

Do not automatically replace every missing value with:

"Not Provided"

or:

0

without understanding the data.

7.13 Testing and Production Considerations

When handling missing values in production data pipelines, consider the following practices.

1. Identify Required Fields

Some fields may be mandatory.

For example:

required_fields = [
    "customer_id",
    "name"
]

A record without a customer ID may not be usable.

customer = {
    "customer_id": None,
    "name": "Aarav"
}

for field in required_fields:
    if customer.get(field) is None:
        print(f"Required field is missing: {field}")

Output:

Required field is missing: customer_id
2. Identify Optional Fields

Some fields may be optional.

For example:

Email address

Secondary phone number

Apartment number

Customer nickname

A missing optional field may not require the record to be rejected.

Example:

customer = {
    "customer_id": 101,
    "name": "Aarav",
    "email": None
}

The record may still be valid if the email field is optional.

3. Count Missing Values

Counting missing values helps monitor data quality.

records = [
    {"email": "a@example.com"},
    {"email": None},
    {"email": "b@example.com"},
    {"email": None}
]

missing_email_count = 0

for record in records:
    if record.get("email") is None:
        missing_email_count += 1

print("Missing email count:", missing_email_count)

Output:

Missing email count: 2
4. Separate Validation from Transformation

Validation checks whether the data is acceptable.

Transformation changes the data into the required format.

Example:

email = None

# Validation
if email is None:
    print("Email is missing")

# Transformation
if email is None:
    cleaned_email = "Not Provided"
else:
    cleaned_email = email

print(cleaned_email)

In larger pipelines, these activities are often separated into different stages.

5. Avoid Silent Data Loss

Do not remove records containing missing values without recording the reason.

Incorrect:

cleaned_records = [
    record for record in records
    if record.get("email") is not None
]

This removes every record without an email address.

That may be correct for an email marketing pipeline, but incorrect for a customer sales report.

A safer approach is to count or log rejected records:

valid_records = []
rejected_records = []

for record in records:
    if record.get("email") is None:
        rejected_records.append(record)
    else:
        valid_records.append(record)

print("Valid records:", len(valid_records))
print("Rejected records:", len(rejected_records))

This makes the transformation more transparent.

6. Document Missing-Value Rules

A production pipeline should document rules such as:

customer_id:
    Required. Reject record if missing.

email:
    Optional. Replace missing value with "Not Provided".

age:
    Required for age-based analysis.
    Do not replace missing age with zero.

delivery_date:
    Missing value may indicate that delivery is incomplete.

These rules should be agreed upon with the business or data owner.

7. Test Different Missing-Value Cases

A good test should include:

A valid value

None

An empty string

0

False

A missing dictionary key

An invalid value

Example:

test_values = [
    "Aarav",
    None,
    "",
    0,
    False
]

for value in test_values:
    print(repr(value), value is None)

This helps confirm that the code handles each case correctly.

7.14 Exercises
Exercise 1: Basic None Check

Create a variable called delivery_date with the value None.

Print:

The value

Its type

Whether it is None

Exercise 2: Customer Email

Create a variable:

customer_email = None

If the email is missing, print:

Customer email is not available

Otherwise, print the email address.

Exercise 3: Function Return Value

Create a function called show_message() that prints:

Data pipeline started

Store the function result in a variable and print the result.

Observe why the result is None.

Exercise 4: Missing City Count

Use the following records:

customers = [
    {"name": "Aarav", "city": "Mumbai"},
    {"name": "Diya", "city": None},
    {"name": "Kabir", "city": "Pune"},
    {"name": "Meera", "city": None}
]

Count how many customers have a missing city.

Expected output:

Missing city count: 2
Exercise 5: Safe Dictionary Access

Create a dictionary containing only:

{
    "customer_id": 101,
    "name": "Aarav"
}

Use .get() to safely access:

email

phone

city

Print "Not Provided" when a value is missing.

Exercise 6: Preserve Zero

Create:

discount = 0

Write logic that displays 0 instead of "Not Available".

Then test the same logic with:

discount = None
Exercise 7: Required Fields

Create the following record:

customer = {
    "customer_id": None,
    "name": "Diya",
    "email": None
}

Write a program that:

Checks whether customer_id is missing.

Prints an error message if it is missing.

Checks whether the email is missing.

Prints a warning if the email is missing.

Expected output:

Error: Customer ID is missing
Warning: Email is missing
Exercise 8: Count Missing Values by Field

Use:

customers = [
    {"name": "Aarav", "email": None, "city": "Mumbai"},
    {"name": "Diya", "email": "diya@example.com", "city": None},
    {"name": "Kabir", "email": None, "city": None}
]

Count:

Missing emails

Missing cities

Expected output:

Missing emails: 2
Missing cities: 2
7.15 Interview Questions
Question 1: What is None in Python?

None is a special Python object that represents the absence of a value. Its type is NoneType.

Question 2: What is the difference between None, 0, and ""?

None represents an absent value.

0 is a numeric value.

"" is an empty string.

They have different meanings and should not be treated as identical.

Question 3: How do you check whether a value is None?

Use:

if value is None:
Question 4: Why is is None preferred over == None?

is checks object identity and is the standard Python approach for checking the singleton None object.

Question 5: What does a function return if it has no return statement?

It returns None.

Question 6: What is the difference between print() and return?

print() displays information on the screen.

return sends a value back to the caller.

Question 7: What happens when a missing dictionary key is accessed using square brackets?

A KeyError is raised.

Example:

customer["email"]

Use .get() when the key may not exist.

Question 8: Why should data engineers care about None?

Because real-world datasets frequently contain missing values. Data engineers must detect, validate, transform, replace, or preserve these values based on business requirements.

Question 9: Is an empty string the same as None?

No.

"" is None

is false.

An empty string is a string containing zero characters, while None represents the absence of a value.

Question 10: What is the difference between a missing dictionary key and a key with a None value?

Example with a None value:

{"email": None}

The key exists, but its value is missing.

Example with a missing key:

{}

The key does not exist at all.

Question 11: What is the difference between if value is None and if not value?
if value is None:

checks specifically for None.

if not value:

checks for any falsy value, including:

None

0

False

""

[]

{}

Use the condition that matches the business requirement.

Question 12: What happens if you perform arithmetic on None?

Python generally raises a TypeError.

Example:

price = None
total = price * 2

This fails because None is not a numeric value.

Question 13: Should every missing value be replaced with zero?

No.

Replacing a missing value with zero may change the meaning of the data.

For example:

Missing age is not the same as age zero.

Missing sales is not always the same as zero sales.

Missing discount may not mean no discount.

The replacement rule must be based on business context.

Question 14: Why should missing-value rules be documented?

Because different fields have different meanings and requirements.

Documentation helps ensure that data engineers, analysts, and business users handle missing values consistently.

7.16 Summary

In this section, we learned:

None represents the absence of a value.

The type of None is NoneType.

None is different from 0, False, "", and empty collections.

Use is None to check for None.

Use is not None to check that a value is available.

Functions without a return statement return None.

print() displays a value but does not return it.

Missing values are common in data engineering pipelines.

.get() provides safer access to dictionary values.

Missing keys and keys containing None are different situations.

External systems may represent missing values using NULL, null, empty fields, or other formats.

Missing values must be handled according to the business context.

if not value checks all falsy values, not only None.

Missing values should be validated, transformed, counted, and documented.

Production pipelines should avoid silent data loss.

Required and optional fields should have separate handling rules.

7.17 Completion Checklist

Before moving to the next section, confirm that you can:

Explain what None means.
Identify the type of None.
Differentiate None from 0 and "".
Use is None.
Use is not None.
Explain why functions may return None.
Differentiate print() from return.
Detect missing values in dictionaries.
Use .get() safely.
Count missing values in a collection.
Distinguish missing keys from keys containing None.
Explain the difference between None and falsy values.
Handle required and optional fields.
Avoid replacing valid values accidentally.
Document missing-value handling rules.
Run the Section 7 Python script successfully.


## 7.18 Section Review

In this review, you will build a small customer data-quality checker.

The purpose of the checker is to identify missing values and separate valid customer records from records that are missing required information.

### Business Requirements

NovaMart requires the following rules:

1. `customer_id` is required.
2. `name` is required.
3. `email` is optional.
4. `city` is optional.
5. Missing emails should be counted.
6. Missing cities should be counted.
7. Records missing required fields should be marked as invalid.
8. Valid records should be separated from invalid records.
9. The program should print a data-quality summary.

---

### Sample Data

Use the following customer records:

```python
customers = [
    {
        "customer_id": 101,
        "name": "Aarav",
        "email": "aarav@example.com",
        "city": "Mumbai"
    },
    {
        "customer_id": None,
        "name": "Diya",
        "email": None,
        "city": "Pune"
    },
    {
        "customer_id": 103,
        "name": "Kabir",
        "email": "kabir@example.com",
        "city": None
    },
    {
        "customer_id": 104,
        "name": None,
        "email": None,
        "city": None
    }
]
Step 1: Create Counters

Create counters for:

Total records

Missing emails

Missing cities

Missing customer IDs

Missing names

total_records = len(customers)

missing_emails = 0
missing_cities = 0
missing_customer_ids = 0
missing_names = 0
Step 2: Create Valid and Invalid Lists

Create two empty lists:

valid_records = []
invalid_records = []

The valid records will contain customers with all required fields.

The invalid records will contain customers missing at least one required field.

Step 3: Process Each Customer

Loop through each customer:

for customer in customers:
    is_valid = True

    if customer.get("customer_id") is None:
        missing_customer_ids += 1
        is_valid = False

    if customer.get("name") is None:
        missing_names += 1
        is_valid = False

    if customer.get("email") is None:
        missing_emails += 1

    if customer.get("city") is None:
        missing_cities += 1

    if is_valid:
        valid_records.append(customer)
    else:
        invalid_records.append(customer)

Notice the difference between required and optional fields:

Missing customer_id makes the record invalid.

Missing name makes the record invalid.

Missing email does not make the record invalid.

Missing city does not make the record invalid.

Step 4: Print the Summary
print("Total records:", total_records)
print("Valid records:", len(valid_records))
print("Invalid records:", len(invalid_records))
print("Missing emails:", missing_emails)
print("Missing cities:", missing_cities)
print("Missing customer IDs:", missing_customer_ids)
print("Missing names:", missing_names)

Expected output:

Total records: 4
Valid records: 2
Invalid records: 2
Missing emails: 2
Missing cities: 2
Missing customer IDs: 1
Missing names: 1
Complete Section Review Solution
customers = [
    {
        "customer_id": 101,
        "name": "Aarav",
        "email": "aarav@example.com",
        "city": "Mumbai"
    },
    {
        "customer_id": None,
        "name": "Diya",
        "email": None,
        "city": "Pune"
    },
    {
        "customer_id": 103,
        "name": "Kabir",
        "email": "kabir@example.com",
        "city": None
    },
    {
        "customer_id": 104,
        "name": None,
        "email": None,
        "city": None
    }
]


total_records = len(customers)

missing_emails = 0
missing_cities = 0
missing_customer_ids = 0
missing_names = 0

valid_records = []
invalid_records = []


for customer in customers:
    is_valid = True

    if customer.get("customer_id") is None:
        missing_customer_ids += 1
        is_valid = False

    if customer.get("name") is None:
        missing_names += 1
        is_valid = False

    if customer.get("email") is None:
        missing_emails += 1

    if customer.get("city") is None:
        missing_cities += 1

    if is_valid:
        valid_records.append(customer)
    else:
        invalid_records.append(customer)


print("Total records:", total_records)
print("Valid records:", len(valid_records))
print("Invalid records:", len(invalid_records))
print("Missing emails:", missing_emails)
print("Missing cities:", missing_cities)
print("Missing customer IDs:", missing_customer_ids)
print("Missing names:", missing_names)


print("\nValid records:")
for record in valid_records:
    print(record)


print("\nInvalid records:")
for record in invalid_records:
    print(record)

Expected output:

Total records: 4
Valid records: 2
Invalid records: 2
Missing emails: 2
Missing cities: 2
Missing customer IDs: 1
Missing names: 1

Valid records:
{'customer_id': 101, 'name': 'Aarav', 'email': 'aarav@example.com', 'city': 'Mumbai'}
{'customer_id': 103, 'name': 'Kabir', 'email': 'kabir@example.com', 'city': None}

Invalid records:
{'customer_id': None, 'name': 'Diya', 'email': None, 'city': 'Pune'}
{'customer_id': 104, 'name': None, 'email': None, 'city': None}
What This Review Demonstrates

This exercise combines several important concepts:

Lists

Dictionaries

Loops

Conditional statements

None

.get()

Counters

Data validation

Separating valid and invalid records

Basic data-quality reporting

This is a simple example of a task that may appear inside a real data ingestion or data validation pipeline.

7.19 Key Takeaways

Remember these important rules:

value is None

Use this when checking specifically for None.

value is not None

Use this when checking that a value is available.

not value

Use this only when you want to check for any falsy value.

dictionary.get("key")

Use this when a dictionary key may not exist.

return value

Use return when a function needs to send a result back to the caller.

Missing values should not automatically be replaced with zero, an empty string, or "Not Provided".

The correct handling depends on:

The meaning of the field

Whether the field is required

The source system

The business requirement

The downstream use of the data

A missing email may be acceptable.

A missing customer ID may make a record unusable.

A missing delivery date may indicate that an order has not yet been delivered.

Therefore, missing-value handling is both a technical and business decision.

7.20 Section Completion

Section 7 is complete when you have:

Read and understood the explanation.
Reviewed the examples.
Created the Python implementation file.
Executed the script successfully.
Completed the exercises.
Attempted the section review.
Compared your solution with the reference solution.
Committed the changes to Git.

Run the implementation:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

python code\01-python-foundations\01-python-fundamentals\07_none_and_missing_values.py


Section 8 — Conditional Statements

We will continue in the same Markdown file:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\book\01-python-foundations\01-python-fundamentals.md

Add the following content after Section 7.

# 8. Conditional Statements

Programs often need to make decisions.

For example:

- If a customer is above 18, allow registration.
- If an order amount is greater than ₹1,000, apply a discount.
- If a required field is missing, reject the record.
- If a delivery is completed, calculate delivery time.
- If a transaction is suspicious, send it for review.

Python uses **conditional statements** to make these decisions.

The main conditional keywords in Python are:

- `if`
- `elif`
- `else`

---

## 8.1 Understanding Conditions

A condition is an expression that evaluates to either:

```python
True

or:

False

Example:

age = 25

print(age > 18)

Output:

True

Another example:

age = 15

print(age > 18)

Output:

False

Python uses the result of a condition to decide which block of code should execute.

8.2 The if Statement

The if statement executes a block of code only when its condition is true.

Syntax
if condition:
    # code to execute

Example:

age = 25

if age >= 18:
    print("Customer is eligible")

Output:

Customer is eligible

The condition is:

age >= 18

Since 25 >= 18 is true, Python executes the print() statement.

Example with a False Condition
age = 15

if age >= 18:
    print("Customer is eligible")

Output:

Nothing is printed because the condition is false.

8.3 Indentation in Conditional Statements

Python uses indentation to define code blocks.

Correct:

age = 25

if age >= 18:
    print("Customer is eligible")
    print("Registration can continue")

Both statements belong to the if block.

Incorrect:

age = 25

if age >= 18:
print("Customer is eligible")

This causes an IndentationError.

Python commonly uses four spaces for indentation.

Important Rule

The colon : starts the conditional block.

The indented lines belong to that block.

if condition:
    statement_1
    statement_2
8.4 Using Comparison Operators

Conditional statements commonly use comparison operators.

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

Example:

order_amount = 1500

if order_amount > 1000:
    print("Discount is applicable")

Output:

Discount is applicable
More Examples
temperature = 35

if temperature > 30:
    print("High temperature")
stock_quantity = 0

if stock_quantity == 0:
    print("Product is out of stock")
payment_status = "failed"

if payment_status != "success":
    print("Payment requires attention")
8.5 The else Statement

The else block executes when the if condition is false.

Syntax
if condition:
    # runs when condition is true
else:
    # runs when condition is false

Example:

age = 16

if age >= 18:
    print("Customer is eligible")
else:
    print("Customer is not eligible")

Output:

Customer is not eligible
Example: Order Amount
order_amount = 750

if order_amount >= 1000:
    print("Free delivery")
else:
    print("Delivery charges apply")

Output:

Delivery charges apply

The else block does not have a condition of its own.

It runs when the preceding if condition is false.

8.6 The elif Statement

The elif keyword means else if.

It allows us to check multiple conditions.

Syntax
if condition_1:
    # code
elif condition_2:
    # code
else:
    # code

Example:

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

Output:

Grade B

Python checks conditions from top to bottom.

Once a condition is true, its block executes and the remaining conditions are skipped.

8.7 Multiple elif Conditions

Example:

marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

Output:

Grade: B
Order Matters

Consider:

marks = 95

if marks >= 40:
    print("Pass")
elif marks >= 90:
    print("Grade A")

Output:

Pass

The second condition is never checked because the first condition is already true.

Correct ordering:

marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

Output:

Grade A

More specific conditions should generally be checked before broader conditions.

8.8 Using Logical Operators

Conditions can be combined using logical operators.

Operator

	

Meaning




and

	

Both conditions must be true




or

	

At least one condition must be true




not

	

Reverses the Boolean result

Using and
age = 25
has_license = True

if age >= 18 and has_license:
    print("Customer can rent a vehicle")

Output:

Customer can rent a vehicle

Both conditions must be true.

Using or
payment_method = "UPI"

if payment_method == "UPI" or payment_method == "Card":
    print("Digital payment selected")

Output:

Digital payment selected

At least one condition must be true.

Using not
is_blocked = False

if not is_blocked:
    print("Customer can continue")

Output:

Customer can continue
8.9 Combining Comparison and Logical Operators

Example:

age = 28
annual_income = 600000

if age >= 21 and annual_income >= 500000:
    print("Customer meets the eligibility criteria")
else:
    print("Customer does not meet the eligibility criteria")

Output:

Customer meets the eligibility criteria

Another example:

city = "Mumbai"
is_member = True

if city == "Mumbai" and is_member:
    print("Premium delivery benefits available")
8.10 Conditional Statements with None

Conditional statements are useful for checking missing values.

customer_email = None

if customer_email is None:
    print("Email address is missing")
else:
    print("Email address is available")

Output:

Email address is missing

This connects directly with the previous section.

Example: Required Customer ID
customer_id = None

if customer_id is None:
    print("Invalid record: customer ID is missing")
else:
    print("Customer record is valid")

Output:

Invalid record: customer ID is missing
8.11 Nested Conditional Statements

A conditional statement inside another conditional statement is called a nested conditional.

Example:

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Customer can rent a vehicle")
    else:
        print("Driving license is required")
else:
    print("Customer must be at least 18 years old")

Output:

Customer can rent a vehicle

Nested conditions are useful, but too many nested levels can make code difficult to understand.

Sometimes logical operators provide a simpler solution:

age = 25
has_license = True

if age >= 18 and has_license:
    print("Customer can rent a vehicle")
else:
    print("Customer is not eligible")
8.12 Membership Conditions

The in operator checks whether a value exists inside a collection.

Example:

payment_method = "UPI"

if payment_method in ["UPI", "Card", "Net Banking"]:
    print("Supported payment method")
else:
    print("Unsupported payment method")

Output:

Supported payment method
Using not in
status = "cancelled"

if status not in ["completed", "processing"]:
    print("Order requires attention")

Output:

Order requires attention
8.13 Identity Conditions

The is operator checks object identity.

It is commonly used with None.

value = None

if value is None:
    print("Value is missing")

Use:

is None

instead of:

== None

For normal value comparisons, use ==.

status = "completed"

if status == "completed":
    print("Order completed")
8.14 Practical Example: NovaMart Order Validation

NovaMart wants to validate an order before processing it.

Business rules:

The order ID must be available.

The order amount must be greater than zero.

The payment status must be "success".

If all conditions are satisfied, the order can be processed.

Otherwise, the order should be rejected.

order_id = 1001
order_amount = 1500
payment_status = "success"

if order_id is None:
    print("Order rejected: order ID is missing")
elif order_amount <= 0:
    print("Order rejected: invalid order amount")
elif payment_status != "success":
    print("Order rejected: payment unsuccessful")
else:
    print("Order approved for processing")

Output:

Order approved for processing
Invalid Example
order_id = 1002
order_amount = 0
payment_status = "success"

if order_id is None:
    print("Order rejected: order ID is missing")
elif order_amount <= 0:
    print("Order rejected: invalid order amount")
elif payment_status != "success":
    print("Order rejected: payment unsuccessful")
else:
    print("Order approved for processing")

Output:

Order rejected: invalid order amount

8.15 Practical Example: Delivery Status

In an e-commerce system, an order can have different delivery statuses:

pending

processing

shipped

out_for_delivery

delivered

cancelled

We can use conditional statements to display an appropriate message.

delivery_status = "shipped"

if delivery_status == "pending":
    print("Your order is waiting for processing.")

elif delivery_status == "processing":
    print("Your order is being prepared.")

elif delivery_status == "shipped":
    print("Your order has been shipped.")

elif delivery_status == "out_for_delivery":
    print("Your order is out for delivery.")

elif delivery_status == "delivered":
    print("Your order has been delivered.")

elif delivery_status == "cancelled":
    print("Your order has been cancelled.")

else:
    print("Unknown delivery status.")

Output:

Your order has been shipped.
Why Use elif?

Only one matching branch is executed.

Once Python finds:

delivery_status == "shipped"

it executes that block and skips the remaining conditions.

8.16 Practical Example: Customer Segmentation

Businesses often divide customers into segments based on their spending.

For example:

Annual Spending

	

Customer Segment




₹50,000 or more

	

Premium




₹20,000–₹49,999

	

Regular




₹1–₹19,999

	

Occasional




₹0

	

Inactive

annual_spending = 35000

if annual_spending >= 50000:
    segment = "Premium"

elif annual_spending >= 20000:
    segment = "Regular"

elif annual_spending > 0:
    segment = "Occasional"

else:
    segment = "Inactive"

print(f"Customer segment: {segment}")

Output:

Customer segment: Regular
Important: Condition Order

The conditions are checked from top to bottom.

If we write:

if annual_spending > 0:
    segment = "Occasional"

elif annual_spending >= 50000:
    segment = "Premium"

then a customer spending ₹60,000 would incorrectly be classified as Occasional.

The more specific or higher threshold conditions should usually come first.

8.17 Practical Example: Data Quality Validation

Data engineering systems frequently validate incoming records before processing them.

Suppose we receive a customer record:

customer = {
    "customer_id": 101,
    "name": "Amit",
    "age": 25,
    "email": "amit@example.com"
}

We can validate the record using conditions.

if customer["customer_id"] is None:
    print("Invalid record: customer ID is missing.")

elif customer["name"] == "":
    print("Invalid record: customer name is missing.")

elif customer["age"] < 18:
    print("Invalid record: customer must be at least 18 years old.")

elif "@" not in customer["email"]:
    print("Invalid record: email address is invalid.")

else:
    print("Customer record is valid.")

Output:

Customer record is valid.
Why This Matters in Data Engineering

Conditional statements are used in:

Data validation

Data cleaning

Pipeline control

Error handling

File processing

API response handling

Business rule implementation

Data transformation

For example:

if record_is_valid:
    process_record()
else:
    send_record_to_error_table()

This pattern is common in real-world data pipelines.

8.18 Practical Example: NovaMart Order Validation

Let us create a small order validation system for NovaMart.

An order should be approved only when:

The order ID is available.

The customer ID is available.

The order amount is greater than zero.

The payment status is successful.

order = {
    "order_id": "ORD1001",
    "customer_id": "CUS501",
    "order_amount": 2500,
    "payment_status": "success"
}

if order["order_id"] is None:
    print("Order rejected: order ID is missing.")

elif order["customer_id"] is None:
    print("Order rejected: customer ID is missing.")

elif order["order_amount"] <= 0:
    print("Order rejected: invalid order amount.")

elif order["payment_status"] != "success":
    print("Order rejected: payment unsuccessful.")

else:
    print("Order approved.")

Output:

Order approved.
Adding a Discount Rule

We can add another condition inside the approved order block.

order_amount = 2500

if order_amount >= 2000:
    print("Customer is eligible for a discount.")
else:
    print("Customer is not eligible for a discount.")

Output:

Customer is eligible for a discount.
Complete Example
order = {
    "order_id": "ORD1001",
    "customer_id": "CUS501",
    "order_amount": 2500,
    "payment_status": "success",
    "delivery_status": "processing"
}

if order["order_id"] is None:
    print("Order rejected: order ID is missing.")

elif order["customer_id"] is None:
    print("Order rejected: customer ID is missing.")

elif order["order_amount"] <= 0:
    print("Order rejected: invalid order amount.")

elif order["payment_status"] != "success":
    print("Order rejected: payment unsuccessful.")

else:
    print("Order approved.")

    if order["order_amount"] >= 2000:
        print("Customer is eligible for a discount.")

    if order["delivery_status"] == "processing":
        print("Your order is being prepared.")

    elif order["delivery_status"] == "shipped":
        print("Your order has been shipped.")

    elif order["delivery_status"] == "delivered":
        print("Your order has been delivered.")

    else:
        print("Delivery status is currently unavailable.")

Output:

Order approved.
Customer is eligible for a discount.
Your order is being prepared.

This example combines:

Dictionary access

if

elif

else

Nested conditions

Comparison operators

Business rules

8.19 Practical Example: Handling Missing Values

In data engineering, missing values are common.

Consider this customer record:

customer_name = None
customer_age = 28

We can check whether the name is missing.

if customer_name is None:
    print("Customer name is missing.")
else:
    print(f"Customer name: {customer_name}")

Output:

Customer name is missing.
Using a Default Value
customer_name = None

if customer_name is None:
    customer_name = "Unknown Customer"

print(customer_name)

Output:

Unknown Customer
Important Difference

Do not use:

if customer_name == None:

Prefer:

if customer_name is None:

The is operator checks object identity and is the recommended way to check for None.

8.20 Practical Example: Checking File Type

Suppose a data pipeline accepts only CSV and JSON files.

file_extension = ".csv"

if file_extension == ".csv":
    print("Process the file using CSV logic.")

elif file_extension == ".json":
    print("Process the file using JSON logic.")

else:
    print("Unsupported file format.")

Output:

Process the file using CSV logic.

This type of condition is useful when:

Reading multiple file formats

Selecting different parsing logic

Processing files from cloud storage

Validating uploaded files

8.21 Common Mistakes
Mistake 1: Using = Instead of ==

Incorrect:

age = 18

if age = 18:
    print("Eligible")

Correct:

age = 18

if age == 18:
    print("Eligible")

= assigns a value.

== compares two values.

Mistake 2: Forgetting the Colon

Incorrect:

if age >= 18
    print("Eligible")

Correct:

if age >= 18:
    print("Eligible")

Every conditional statement must end with a colon.

Mistake 3: Incorrect Indentation

Incorrect:

if age >= 18:
print("Eligible")

Correct:

if age >= 18:
    print("Eligible")

Python uses indentation to identify the code block.

Mistake 4: Incorrect Condition Order

Incorrect:

marks = 95

if marks >= 40:
    print("Pass")

elif marks >= 90:
    print("Excellent")

Output:

Pass

The second condition is never reached.

Correct:

marks = 95

if marks >= 90:
    print("Excellent")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")

Output:

Excellent
Mistake 5: Comparing Different Data Types
age = "25"

if age > 18:
    print("Adult")

This raises a TypeError because a string cannot be compared directly with an integer.

Correct:

age = "25"

if int(age) > 18:
    print("Adult")

Output:

Adult
Mistake 6: Using is for Normal Value Comparison

Avoid:

age = 25

if age is 25:
    print("Age is 25")

Use:

age = 25

if age == 25:
    print("Age is 25")

Use is mainly for identity checks such as:

if value is None:
    print("Value is missing")
Mistake 7: Overcomplicated Conditions

Instead of writing:

if age >= 18 and age <= 60 and has_license == True:
    print("Eligible")

Prefer:

if 18 <= age <= 60 and has_license:
    print("Eligible")

The second version is easier to read.

8.22 Exercises
Exercise 1: Positive, Negative, or Zero

Write a program that checks whether a number is:

Positive

Negative

Zero

Example:

number = -5

Expected output:

Negative
Exercise 2: Even or Odd

Write a program that checks whether a number is even or odd.

Hint:

number % 2

Example:

number = 12

Expected output:

Even
Exercise 3: Age Category

Create a program that classifies a person into:

Child: below 13

Teenager: 13–19

Adult: 20–59

Senior: 60 or above

Exercise 4: Grade Calculator

Create a program using the following rules:

Marks

	

Grade




90 or above

	

A




75–89

	

B




60–74

	

C




40–59

	

D




Below 40

	

F

Exercise 5: Login Validation

Create a program that checks:

Username is correct.

Password is correct.

Example:

username = "admin"
password = "python123"

Expected output:

Login successful
Exercise 6: Order Amount Validation

Write a program that checks:

If order amount is less than or equal to zero, reject the order.

If order amount is greater than zero, approve the order.

Exercise 7: Delivery Status

Create a program that displays a message based on:

delivery_status = "delivered"

Expected output:

Your order has been delivered.
Exercise 8: Data Quality Check

Create a customer record and validate:

Customer ID is not missing.

Customer name is not empty.

Age is greater than zero.

Email contains @.

8.23 Interview Questions
Question 1: What is a conditional statement?

A conditional statement executes different blocks of code based on whether a condition is true or false.

Question 2: What is the difference between if, elif, and else?

if checks the first condition.

elif checks additional conditions.

else executes when no previous condition is true.

Question 3: Can we use multiple elif blocks?

Yes.

if condition_1:
    pass

elif condition_2:
    pass

elif condition_3:
    pass

else:
    pass
Question 4: Can we use multiple independent if statements?

Yes.

age = 25

if age >= 18:
    print("Adult")

if age >= 21:
    print("Can legally purchase certain products")

Both conditions are checked independently.

Question 5: What is the difference between multiple if statements and if-elif-else?

Multiple if statements check every condition.

An if-elif-else chain stops after the first matching condition.

Question 6: What is a nested conditional statement?

A conditional statement written inside another conditional statement is called a nested conditional statement.

if is_logged_in:
    if has_permission:
        print("Access granted")
Question 7: What is the difference between == and is?

== compares values.

is compares object identity.

Example:

value is None
Question 8: What are truthy and falsy values?

Falsy values include:

False
None
0
0.0
""
[]
{}
()

Most other values are truthy.

Question 9: What happens if no condition is true and there is no else block?

Nothing is executed for that conditional statement.

age = 15

if age >= 18:
    print("Adult")

There is no output.

Question 10: Why is condition order important?

Python checks conditions from top to bottom. Once a condition is true in an if-elif-else chain, the remaining conditions are skipped.

8.24 Section Summary

In this section, we learned:

What conditional statements are.

How to use if.

How to use else.

How to use elif.

How indentation works.

How comparison operators are used.

How logical operators combine conditions.

How to write nested conditions.

How to check membership using in.

How to check identity using is.

How to handle None.

How to validate business rules.

How conditional logic is used in data engineering.

Conditional statements help Python programs make decisions based on data and business requirements.

8.25 Key Takeaways

Python uses indentation to define code blocks.

Conditions must produce a truthy or falsy result.

Use == for value comparison.

Use is None to check for missing values.

Use elif for multiple possible conditions.

Use else as a fallback block.

The order of conditions matters.

and, or, and not combine conditions.

Nested conditions can represent complex business rules.

Conditional statements are widely used in data validation and data pipelines.

8.26 Section Checklist

Before moving to the next section, make sure you can:

Write a basic if statement.
Use else.
Use multiple elif conditions.
Compare numbers and strings.
Use and, or, and not.
Check whether a value is None.
Use nested conditions.
Validate a dictionary record.
Check file extensions.
Implement an order validation system.
Explain the difference between == and is.
Explain the difference between multiple if statements and if-elif-else.
8.27 Practice Implementation

Create the following file:

code/
└── 01-python-foundations/
    └── 01-python-fundamentals/
        └── 08_conditional_statements.py

Add this implementation:

# 08_conditional_statements.py


# Example 1: Basic condition
age = 22

if age >= 18:
    print("You are an adult.")


# Example 2: if-else
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Example 3: if-elif-else
marks = 85

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"

print(f"Grade: {grade}")


# Example 4: Logical operators
has_account = True
has_verified_email = True

if has_account and has_verified_email:
    print("User is eligible to continue.")
else:
    print("User verification is incomplete.")


# Example 5: None check
customer_name = None

if customer_name is None:
    print("Customer name is missing.")
else:
    print(f"Customer name: {customer_name}")


# Example 6: Delivery status
delivery_status = "shipped"

if delivery_status == "pending":
    print("Order is waiting for processing.")

elif delivery_status == "processing":
    print("Order is being prepared.")

elif delivery_status == "shipped":
    print("Order has been shipped.")

elif delivery_status == "delivered":
    print("Order has been delivered.")

else:
    print("Unknown delivery status.")


# Example 7: NovaMart order validation
order = {
    "order_id": "ORD1001",
    "customer_id": "CUS501",
    "order_amount": 2500,
    "payment_status": "success"
}

if order["order_id"] is None:
    print("Order rejected: order ID is missing.")

elif order["customer_id"] is None:
    print("Order rejected: customer ID is missing.")

elif order["order_amount"] <= 0:
    print("Order rejected: invalid order amount.")

elif order["payment_status"] != "success":
    print("Order rejected: payment unsuccessful.")

else:
    print("Order approved.")
8.28 Running the Code

Open PowerShell from the project root:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

Run the Python file:

python code\01-python-foundations\01-python-fundamentals\08_conditional_statements.py

Expected output will be similar to:

You are an adult.
The number is odd.
Grade: B
User is eligible to continue.
Customer name is missing.
Order has been shipped.
Order approved.

8.29 Updating the Documentation

After completing the section, update the learning documentation.

The main book file is:

book\01-python-foundations\01-python-fundamentals.md

The corresponding Python implementation file is:

code\01-python-foundations\01-python-fundamentals\08_conditional_statements.py

Add the following project-learning record at the end of your documentation notes.

Section 8 completed: Conditional Statements

Topics covered:
- if statements
- if-else statements
- if-elif-else statements
- Comparison operators
- Logical operators
- Nested conditions
- None checks
- Truthy and falsy values
- Membership operators
- Identity operators
- Data validation
- Business rule implementation
- Delivery status logic
- Customer segmentation
- File type validation
- NovaMart order validation
Documentation Example

You can maintain a simple learning record like this:

### Section 8: Conditional Statements

Status: Completed

Python conditional statements allow a program to execute different
blocks of code based on conditions.

Topics completed:

- `if`
- `elif`
- `else`
- Comparison operators
- Logical operators
- Nested conditions
- Truthy and falsy values
- `None` checks
- Membership checks
- Identity checks
- Data validation
- Business rule implementation

Practical examples completed:

1. Age validation
2. Even and odd number checking
3. Grade calculation
4. Customer segmentation
5. Delivery status handling
6. File extension validation
7. Customer data quality validation
8. NovaMart order validation

Implementation file:

`code/01-python-foundations/01-python-fundamentals/08_conditional_statements.py`
8.30 Final Section Review

Before moving forward, review the following concepts.

Basic Conditional Statement
age = 25

if age >= 18:
    print("Adult")
Conditional Statement with else
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
Multiple Conditions
marks = 82

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

else:
    grade = "Needs improvement"

print(grade)
Logical Conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("Eligible to drive")
else:
    print("Not eligible to drive")
Missing Value Check
email = None

if email is None:
    print("Email is missing")
else:
    print("Email is available")
Data Validation
record = {
    "customer_id": 101,
    "age": 25,
    "email": "customer@example.com"
}

if record["customer_id"] is None:
    print("Customer ID is missing.")

elif record["age"] <= 0:
    print("Invalid age.")

elif "@" not in record["email"]:
    print("Invalid email.")

else:
    print("Record is valid.")
8.31 Important Concepts to Remember
1. Conditions Are Evaluated from Top to Bottom
score = 95

if score >= 90:
    print("Excellent")

elif score >= 75:
    print("Good")

Output:

Excellent

The second condition is not checked after the first condition succeeds.

2. elif Is Optional

This is valid:

if temperature > 30:
    print("Hot")

This is also valid:

if temperature > 30:
    print("Hot")
else:
    print("Not hot")

And this is valid:

if temperature > 35:
    print("Very hot")
elif temperature > 30:
    print("Hot")
else:
    print("Comfortable")
3. Multiple if Statements Are Independent
age = 25

if age >= 18:
    print("Adult")

if age >= 21:
    print("Above 21")

if age >= 25:
    print("Age is 25 or above")

Output:

Adult
Above 21
Age is 25 or above

Every condition is evaluated separately.

4. if-elif-else Selects One Branch
age = 25

if age >= 18:
    print("Adult")

elif age >= 21:
    print("Above 21")

else:
    print("Minor")

Output:

Adult

Only the first matching branch is executed.

5. Use is None for Missing Values

Recommended:

if value is None:
    print("Missing value")

Avoid:

if value == None:
    print("Missing value")

Use == for comparing normal values:

if status == "success":
    print("Payment successful")
8.32 Final Practice Challenge

Create a complete customer order validation program.

Requirements

The program should validate:

Customer ID is available.

Order ID is available.

Order amount is greater than zero.

Payment status is successful.

Delivery status is displayed.

Customers spending at least ₹2,000 receive a discount message.

Reference Solution
order = {
    "customer_id": "CUS1001",
    "order_id": "ORD5001",
    "order_amount": 2500,
    "payment_status": "success",
    "delivery_status": "processing"
}


if order["customer_id"] is None:
    print("Order rejected: customer ID is missing.")

elif order["order_id"] is None:
    print("Order rejected: order ID is missing.")

elif order["order_amount"] <= 0:
    print("Order rejected: invalid order amount.")

elif order["payment_status"] != "success":
    print("Order rejected: payment unsuccessful.")

else:
    print("Order approved.")

    if order["order_amount"] >= 2000:
        print("Customer is eligible for a discount.")
    else:
        print("Customer is not eligible for a discount.")

    if order["delivery_status"] == "processing":
        print("Your order is being prepared.")

    elif order["delivery_status"] == "shipped":
        print("Your order has been shipped.")

    elif order["delivery_status"] == "delivered":
        print("Your order has been delivered.")

    else:
        print("Delivery status is currently unavailable.")

Expected output:

Order approved.
Customer is eligible for a discount.
Your order is being prepared.
8.33 Section Completion Checklist

Confirm that you can now:

Explain what a condition is.
Write an if statement.
Use else.
Use multiple elif blocks.
Compare numbers.
Compare strings.
Use and.
Use or.
Use not.
Use nested conditions.
Check for None.
Understand truthy and falsy values.
Use in for membership checks.
Use is for identity checks.
Validate customer records.
Validate orders.
Implement business rules.
Explain why condition order matters.
Run the implementation file successfully.
8.34 Running the Final Implementation

From the project root, run:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

Execute the Python file:

python code\01-python-foundations\01-python-fundamentals\08_conditional_statements.py

9. Loops and Iteration

Loops are used to execute a block of code repeatedly.

In real-world programming, we often need to perform the same operation on multiple values.

For example:

Print every customer name.

Process every order.

Read every row from a dataset.

Validate every record.

Calculate the total sales.

Process files inside a folder.

Iterate through API responses.

Instead of writing the same code repeatedly, we use loops.

9.1 Why Do We Need Loops?

Without a loop:

print("Processing order 1")
print("Processing order 2")
print("Processing order 3")
print("Processing order 4")
print("Processing order 5")

This approach becomes inefficient when there are thousands or millions of records.

With a loop:

for order_id in range(1, 6):
    print(f"Processing order {order_id}")

Output:

Processing order 1
Processing order 2
Processing order 3
Processing order 4
Processing order 5

The loop reduces repeated code and makes the program easier to maintain.

9.2 Types of Loops in Python

Python mainly provides two types of loops:

for loop

while loop

for Loop

A for loop is used when we want to iterate over a sequence or collection.

Examples:

List

Tuple

String

Dictionary

Set

Range of numbers

for item in collection:
    # Code to execute
    pass
while Loop

A while loop is used when code should continue running as long as a condition remains true.

while condition:
    # Code to execute
    pass
9.3 The for Loop

The basic syntax of a for loop is:

for variable in iterable:
    statement

Here:

for is the loop keyword.

variable stores the current item.

in connects the variable to the iterable.

iterable is the collection being processed.

The indented block executes for every item.

Example:

customers = ["Amit", "Priya", "Rahul"]

for customer in customers:
    print(customer)

Output:

Amit
Priya
Rahul
How It Works

The loop executes as follows:

customer receives "Amit".

The print statement runs.

customer receives "Priya".

The print statement runs.

customer receives "Rahul".

The print statement runs.

The loop ends.

9.4 Iterating Over a List

A list contains multiple values.

products = ["Laptop", "Mouse", "Keyboard"]

for product in products:
    print(product)

Output:

Laptop
Mouse
Keyboard
Practical Example
orders = [101, 102, 103, 104]

for order_id in orders:
    print(f"Processing order: {order_id}")

Output:

Processing order: 101
Processing order: 102
Processing order: 103
Processing order: 104
9.5 Iterating Over a String

A string is also iterable.

name = "Python"

for character in name:
    print(character)

Output:

P
y
t
h
o
n

Each loop iteration processes one character.

Practical Example
word = "Data"

for character in word:
    print(f"Character: {character}")

Output:

Character: D
Character: a
Character: t
Character: a
9.6 Iterating Over a Tuple
coordinates = (10, 20, 30)

for coordinate in coordinates:
    print(coordinate)

Output:

10
20
30

Tuples can be iterated over in the same way as lists.

9.7 Iterating Over a Set
unique_regions = {"North", "South", "East", "West"}

for region in unique_regions:
    print(region)

The output order may vary because sets are unordered collections.

Example output:

South
West
North
East

Do not depend on a particular order when iterating over a set.

9.8 Iterating Over a Dictionary

Dictionaries contain key-value pairs.

customer = {
    "customer_id": 101,
    "name": "Amit",
    "city": "Mumbai"
}
Iterating Over Keys
for key in customer:
    print(key)

Output:

customer_id
name
city

The following is equivalent:

for key in customer.keys():
    print(key)
Iterating Over Values
for value in customer.values():
    print(value)

Output:

101
Amit
Mumbai
Iterating Over Key-Value Pairs

Use .items():

for key, value in customer.items():
    print(f"{key}: {value}")

Output:

customer_id: 101
name: Amit
city: Mumbai

This is very useful when processing JSON-like records.

9.9 The range() Function

The range() function generates a sequence of numbers.

Basic Example
for number in range(5):
    print(number)

Output:

0
1
2
3
4

Important:

range(5) starts at 0 and stops before 5.

range(start, stop)
for number in range(2, 6):
    print(number)

Output:

2
3
4
5

The stop value is excluded.

range(start, stop, step)
for number in range(2, 11, 2):
    print(number)

Output:

2
4
6
8
10

Here:

Start = 2

Stop = 11

Step = 2

Counting Backward
for number in range(5, 0, -1):
    print(number)

Output:

5
4
3
2
1
9.10 Practical Example: Processing Customer IDs
for customer_id in range(1001, 1006):
    print(f"Processing customer: {customer_id}")

Output:

Processing customer: 1001
Processing customer: 1002
Processing customer: 1003
Processing customer: 1004
Processing customer: 1005

This pattern can be used for:

Generating test records.

Processing batches.

Creating sample IDs.

Running repeated operations.

9.11 Practical Example: Calculating Total Sales

Suppose we have sales values:

sales = [1200, 2500, 1800, 3200]

We can calculate the total using a loop.

sales = [1200, 2500, 1800, 3200]

total_sales = 0

for sale in sales:
    total_sales += sale

print(f"Total sales: {total_sales}")

Output:

Total sales: 8700
Explanation

Initially:

total_sales = 0

During each iteration:

total_sales += sale

The values are added one by one:

Sale

	

Running Total




1200

	

1200




2500

	

3700




1800

	

5500




3200

	

8700

9.12 Practical Example: Counting Valid Records
records = [
    {"id": 1, "is_valid": True},
    {"id": 2, "is_valid": False},
    {"id": 3, "is_valid": True},
    {"id": 4, "is_valid": True}
]

valid_count = 0

for record in records:
    if record["is_valid"]:
        valid_count += 1

print(f"Valid records: {valid_count}")

Output:

Valid records: 3

This combines:

A for loop.

A conditional statement.

A counter variable.

9.13 Practical Example: Filtering Failed Orders
orders = [
    {"order_id": 101, "status": "success"},
    {"order_id": 102, "status": "failed"},
    {"order_id": 103, "status": "success"},
    {"order_id": 104, "status": "failed"}
]

for order in orders:
    if order["status"] == "failed":
        print(f"Failed order: {order['order_id']}")

Output:

Failed order: 102
Failed order: 104

This is a common pattern in data processing pipelines.

9.14 The while Loop

A while loop repeatedly executes a block of code as long as its condition is true.

Syntax:

while condition:
    statement

Example:

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

Output:

1
2
3
4
5
How It Works

counter starts at 1.

Python checks whether counter <= 5.

The value is printed.

counter increases by 1.

The condition is checked again.

The loop stops when the condition becomes false.

9.15 Practical Example: Processing Batches

Imagine a system processing records in batches.

batch_number = 1
total_batches = 4

while batch_number <= total_batches:
    print(f"Processing batch {batch_number}")
    batch_number += 1

Output:

Processing batch 1
Processing batch 2
Processing batch 3
Processing batch 4

A while loop can be useful when the number of iterations depends on a changing condition.

9.16 Avoiding Infinite Loops

An infinite loop never stops.

Example:

counter = 1

while counter <= 5:
    print(counter)

This loop is infinite because counter never changes.

Correct version:

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

Always ensure that the loop condition can eventually become false.

9.17 Comparing for and while

Feature

	

for Loop

	

while Loop




Main use

	

Iterate over a sequence

	

Repeat while condition is true




Common input

	

List, tuple, string, range

	

Boolean condition




Number of iterations

	

Often known or collection-based

	

Often condition-based




Risk of infinite loop

	

Low

	

Higher




Common use

	

Processing records

	

Waiting or repeated condition checks

Example: for
for number in range(5):
    print(number)
Example: while
number = 0

while number < 5:
    print(number)
    number += 1

Both produce the same output.

9.18 The break Statement

The break statement immediately terminates a loop.

for number in range(1, 11):
    if number == 6:
        break

    print(number)

Output:

1
2
3
4
5

When number becomes 6, the loop stops.

Practical Example: Finding an Order
orders = [101, 102, 103, 104, 105]
target_order = 103

for order_id in orders:
    print(f"Checking order {order_id}")

    if order_id == target_order:
        print("Order found.")
        break

Output:

Checking order 101
Checking order 102
Checking order 103
Order found.

break is useful when the required item has been found and further processing is unnecessary.

9.19 The continue Statement

The continue statement skips the current iteration and moves to the next iteration.

for number in range(1, 6):
    if number == 3:
        continue

    print(number)

Output:

1
2
4
5

When number is 3, the print statement is skipped.

Practical Example: Skipping Invalid Records
records = [
    {"id": 1, "is_valid": True},
    {"id": 2, "is_valid": False},
    {"id": 3, "is_valid": True}
]

for record in records:
    if not record["is_valid"]:
        continue

    print(f"Processing record {record['id']}")

Output:

Processing record 1
Processing record 3

9.20 The pass Statement

The pass statement is a placeholder. It tells Python:

“Do nothing for now, but keep this block syntactically valid.”

Unlike break and continue, pass does not change the flow of a loop.

Example
for number in range(5):
    pass

The loop executes five times, but nothing happens inside the loop.

Example: Placeholder for Future Logic
sales = [1200, 2500, 1800, 3200]

for sale in sales:
    if sale > 3000:
        pass
    else:
        print(f"Sale amount: {sale}")

Output:

Sale amount: 1200
Sale amount: 2500
Sale amount: 1800

When the sale is greater than 3000, Python executes pass, which means no action is performed.

pass vs continue

These statements behave differently.

Using pass
for number in range(5):
    if number == 2:
        pass

    print(number)

Output:

0
1
2
3
4

The loop continues normally after pass.

Using continue
for number in range(5):
    if number == 2:
        continue

    print(number)

Output:

0
1
3
4

The continue statement skips the remaining code in the current iteration.

Comparison

Statement

	

Purpose




pass

	

Do nothing




continue

	

Skip the current iteration




break

	

Exit the loop completely

9.21 Nested Loops

A nested loop is a loop inside another loop.

The outer loop runs once, and for each outer-loop iteration, the inner loop runs completely.

Basic Example
for outer_number in range(3):
    for inner_number in range(2):
        print(outer_number, inner_number)

Output:

0 0
0 1
1 0
1 1
2 0
2 1

The inner loop runs two times for every outer-loop iteration.

Execution Flow

For:

for outer_number in range(3):
    for inner_number in range(2):
        print(outer_number, inner_number)

The execution is:

Outer = 0
    Inner = 0
    Inner = 1

Outer = 1
    Inner = 0
    Inner = 1

Outer = 2
    Inner = 0
    Inner = 1
Example: Multiplication Table
number = 5

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Example: Tables from 1 to 3
for number in range(1, 4):
    print(f"\nMultiplication table of {number}")

    for multiplier in range(1, 6):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")

Output:

Multiplication table of 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

Multiplication table of 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

Multiplication table of 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
Example: Printing a Pattern
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")

    print()

Output:

* 
* * 
* * * 
* * * * 
* * * * * 
Explanation

The outer loop controls the number of rows.

The inner loop controls the number of stars in each row.

end=" " keeps the output on the same line.

The final print() moves to the next line.

9.22 Loop else Clause

Python allows an else block with both for and while loops.

The else block executes when the loop finishes normally.

It does not execute if the loop is terminated using break.

Example with for
for number in range(5):
    print(number)
else:
    print("Loop completed successfully")

Output:

0
1
2
3
4
Loop completed successfully
Example with break
for number in range(5):
    print(number)

    if number == 2:
        break
else:
    print("Loop completed successfully")

Output:

0
1
2

The else block does not execute because the loop was stopped by break.

Practical Example: Searching for a Product
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
search_product = "Keyboard"

for product in products:
    if product == search_product:
        print("Product found")
        break
else:
    print("Product not found")

Output:

Product found
Example: Product Not Found
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
search_product = "Printer"

for product in products:
    if product == search_product:
        print("Product found")
        break
else:
    print("Product not found")

Output:

Product not found

This pattern is useful when searching for an item.

9.23 Practical Example: Processing Sales Records

Consider a list of sales records:

sales = [1200, 2500, 1800, 3200, 4500]

We want to calculate:

Total sales

Number of transactions

Average sale

Highest sale

Lowest sale

Solution
sales = [1200, 2500, 1800, 3200, 4500]

total_sales = 0
highest_sale = sales[0]
lowest_sale = sales[0]

for sale in sales:
    total_sales += sale

    if sale > highest_sale:
        highest_sale = sale

    if sale < lowest_sale:
        lowest_sale = sale

number_of_transactions = len(sales)
average_sale = total_sales / number_of_transactions

print(f"Total sales: {total_sales}")
print(f"Number of transactions: {number_of_transactions}")
print(f"Average sale: {average_sale}")
print(f"Highest sale: {highest_sale}")
print(f"Lowest sale: {lowest_sale}")

Output:

Total sales: 13200
Number of transactions: 5
Average sale: 2640.0
Highest sale: 4500
Lowest sale: 1200
Explanation
total_sales += sale

is equivalent to:

total_sales = total_sales + sale

The variable total_sales acts as an accumulator.

An accumulator stores a running total while the loop executes.

9.24 Practical Example: Counting Positive and Negative Numbers
numbers = [10, -5, 20, -8, 0, 15, -2]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")

Output:

Positive numbers: 3
Negative numbers: 3
Zeros: 1

This is a common pattern in data preprocessing and exploratory data analysis.

9.25 Practical Example: Validating User Input

A while loop can repeatedly ask for input until the user enters a valid value.

while True:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible")
        break

    print("You must be at least 18 years old")

Example execution:

Enter your age: 15
You must be at least 18 years old
Enter your age: 16
You must be at least 18 years old
Enter your age: 21
You are eligible

The loop continues until the user enters an age greater than or equal to 18.

Safer Version with Exception Handling
while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative")
            continue

        print(f"Your age is {age}")
        break

    except ValueError:
        print("Please enter a valid number")

This example combines:

while

if

continue

break

try

except

9.26 Practical Example: Processing a List of Files

Suppose a data engineering pipeline needs to process several files.

file_names = [
    "sales_january.csv",
    "sales_february.csv",
    "sales_march.csv",
    "sales_april.txt",
    "sales_may.csv"
]

for file_name in file_names:
    if not file_name.endswith(".csv"):
        print(f"Skipping unsupported file: {file_name}")
        continue

    print(f"Processing file: {file_name}")

Output:

Processing file: sales_january.csv
Processing file: sales_february.csv
Processing file: sales_march.csv
Skipping unsupported file: sales_april.txt
Processing file: sales_may.csv

This pattern is useful when:

Reading multiple CSV files

Processing log files

Validating file extensions

Building ETL pipelines

Filtering unsupported inputs

9.27 Practical Example: Batch Processing

In data engineering, records are often processed in batches instead of processing everything at once.

records = list(range(1, 21))
batch_size = 5

for start_index in range(0, len(records), batch_size):
    batch = records[start_index:start_index + batch_size]

    print(f"Processing batch: {batch}")

Output:

Processing batch: [1, 2, 3, 4, 5]
Processing batch: [6, 7, 8, 9, 10]
Processing batch: [11, 12, 13, 14, 15]
Processing batch: [16, 17, 18, 19, 20]
Explanation
range(0, len(records), batch_size)

generates:

0, 5, 10, 15

Each value is used as the starting index of a batch.

records[start_index:start_index + batch_size]

extracts the current batch.

Why Batch Processing Is Useful

Batch processing can help:

Reduce memory usage

Control processing size

Improve pipeline organization

Handle large datasets

Retry failed batches independently

9.28 Practical Example: Processing NovaMart Transactions

Assume NovaMart has transaction records:

transactions = [
    {"customer": "Amit", "amount": 1200, "status": "completed"},
    {"customer": "Riya", "amount": 2500, "status": "completed"},
    {"customer": "Karan", "amount": 1800, "status": "failed"},
    {"customer": "Neha", "amount": 3200, "status": "completed"},
]

We want to calculate the total amount of completed transactions.

transactions = [
    {"customer": "Amit", "amount": 1200, "status": "completed"},
    {"customer": "Riya", "amount": 2500, "status": "completed"},
    {"customer": "Karan", "amount": 1800, "status": "failed"},
    {"customer": "Neha", "amount": 3200, "status": "completed"},
]

completed_total = 0
completed_count = 0

for transaction in transactions:
    if transaction["status"] != "completed":
        continue

    completed_total += transaction["amount"]
    completed_count += 1

print(f"Completed transactions: {completed_count}")
print(f"Completed transaction value: {completed_total}")

Output:

Completed transactions: 3
Completed transaction value: 6900
Finding the First Failed Transaction
for transaction in transactions:
    if transaction["status"] == "failed":
        print("First failed transaction found:")
        print(transaction)
        break

Output:

First failed transaction found:
{'customer': 'Karan', 'amount': 1800, 'status': 'failed'}
9.29 Common Loop Mistakes
Mistake 1: Forgetting to Update a while Loop Variable

Incorrect:

number = 1

while number <= 5:
    print(number)

This creates an infinite loop because number never changes.

Correct:

number = 1

while number <= 5:
    print(number)
    number += 1
Mistake 2: Using the Wrong Range
for number in range(1, 5):
    print(number)

Output:

1
2
3
4

The value 5 is not included.

To include 5, write:

for number in range(1, 6):
    print(number)
Mistake 3: Accidentally Using break
for number in range(10):
    if number == 5:
        break

    print(number)

Output:

0
1
2
3
4

The loop ends completely when number becomes 5.

If you only want to skip 5, use continue:

for number in range(10):
    if number == 5:
        continue

    print(number)
Mistake 4: Modifying a List While Iterating

Avoid directly removing elements from a list while iterating over it.

Problematic example:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)

This may skip elements because the list changes during iteration.

A safer approach is to create a new list:

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)

Output:

[1, 3, 5]
Mistake 5: Incorrect Indentation

Incorrect:

for number in range(5):
print(number)

Correct:

for number in range(5):
    print(number)

Python uses indentation to define code blocks.

Mistake 6: Creating an Unnecessary Nested Loop

Incorrect approach:

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    for another_number in numbers:
        print(number, another_number)

This prints every possible pair and performs 25 iterations.

Use nested loops only when the problem actually requires combinations, comparisons, or multi-dimensional processing.

9.30 Loop Performance and Complexity

Loops are essential for processing data, but the number of iterations affects program performance.

When working with large datasets, understanding loop complexity helps us write efficient programs.

9.30.1 Single Loop

Consider:

for number in range(n):
    print(number)

If n is 10, the loop runs 10 times.

If n is 1,000, the loop runs 1,000 times.

The number of operations grows approximately in proportion to the input size.

Time Complexity
O(n)

This is called linear time complexity.

Example
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

The loop runs once for each item in the list.

If the list contains:

5 items → approximately 5 iterations

100 items → approximately 100 iterations

1,000 items → approximately 1,000 iterations

9.30.2 Nested Loops

A nested loop is a loop inside another loop.

n = 5

for first in range(n):
    for second in range(n):
        print(first, second)

The outer loop runs 5 times.

For every outer-loop iteration, the inner loop also runs 5 times.

Total iterations:

5 × 5 = 25
Time Complexity
O(n²)

This is called quadratic time complexity.

Example with n = 100

A single loop performs approximately:

100 iterations

A nested loop performs approximately:

100 × 100 = 10,000 iterations

As the dataset grows, the difference becomes significant.

9.30.3 Three Nested Loops

Consider:

n = 10

for first in range(n):
    for second in range(n):
        for third in range(n):
            print(first, second, third)

Total iterations:

10 × 10 × 10 = 1,000
Time Complexity
O(n³)

This is called cubic time complexity.

Nested loops are not always bad, but they should be used carefully when processing large datasets.

9.30.4 Comparing Loop Complexities

Code Structure

	

Complexity

	

Example for n = 100




No loop

	

O(1)

	

1 operation




One loop

	

O(n)

	

100 operations




Two nested loops

	

O(n²)

	

10,000 operations




Three nested loops

	

O(n³)

	

1,000,000 operations

These are simplified estimates. Actual execution time also depends on the operation performed inside the loop.

9.30.5 Avoiding Unnecessary Nested Loops

Suppose we want to check whether a number exists in a list.

Less Efficient Approach
numbers = [10, 20, 30, 40, 50]
search_numbers = [20, 40, 60]

for search_number in search_numbers:
    for number in numbers:
        if search_number == number:
            print(f"{search_number} found")

This compares every search value with every item in the list.

More Efficient Approach Using a Set
numbers = [10, 20, 30, 40, 50]
search_numbers = [20, 40, 60]

number_set = set(numbers)

for search_number in search_numbers:
    if search_number in number_set:
        print(f"{search_number} found")

Output:

20 found
40 found

A set provides efficient membership checking for most normal use cases.

9.30.6 Use Built-in Functions When Appropriate

Python's built-in functions are often implemented efficiently and can make code shorter and clearer.

Instead of:

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print(total)

We can use:

numbers = [10, 20, 30, 40, 50]

print(sum(numbers))

Instead of:

numbers = [10, 20, 30, 40, 50]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

We can use:

print(max(numbers))

Built-in functions improve readability and often reduce the amount of code we need to maintain.

9.31 Common Loop Mistakes
9.31.1 Forgetting to Update a while Loop Variable

Incorrect:

number = 1

while number <= 5:
    print(number)

The condition always remains true because number never changes.

This creates an infinite loop.

Correct:

number = 1

while number <= 5:
    print(number)
    number += 1

Output:

1
2
3
4
5
9.31.2 Using the Wrong range() Stop Value

Consider:

for number in range(1, 5):
    print(number)

Output:

1
2
3
4

The stop value 5 is excluded.

To include 5, use:

for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5

Remember:

range(start, stop)

includes start but excludes stop.

9.31.3 Accidentally Using break
for number in range(10):
    if number == 5:
        break

    print(number)

Output:

0
1
2
3
4

The loop stops completely when number becomes 5.

If we only want to skip 5, use continue:

for number in range(10):
    if number == 5:
        continue

    print(number)

Output:

0
1
2
3
4
6
7
8
9
9.31.4 Modifying a List While Iterating

Avoid removing items directly from a list while iterating over it.

Problematic example:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)

Changing the list during iteration can cause elements to be skipped.

A safer approach is to create a new list:

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)

Output:

[1, 3, 5]

Another option is to iterate over a copy:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
9.31.5 Incorrect Indentation

Incorrect:

for number in range(5):
print(number)

Correct:

for number in range(5):
    print(number)

Python uses indentation to identify the body of a loop.

9.31.6 Creating an Unnecessary Nested Loop

Consider:

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    for another_number in numbers:
        print(number, another_number)

This performs:

5 × 5 = 25 iterations

Use nested loops only when the problem requires combinations, comparisons, or multi-dimensional processing.

9.31.7 Forgetting That Strings Are Iterable

Strings can be iterated character by character.

name = "Python"

for character in name:
    print(character)

Output:

P
y
t
h
o
n

If the intention is to process the entire string as one value, do not accidentally loop over it.

9.32 Practical Example: Processing Sales Records

Consider the following sales data:

sales = [1200, 2500, 1800, 3200, 4500]

We want to calculate:

Total sales

Number of transactions

Average sale

Highest sale

Lowest sale

Solution
sales = [1200, 2500, 1800, 3200, 4500]

total_sales = 0
highest_sale = sales[0]
lowest_sale = sales[0]

for sale in sales:
    total_sales += sale

    if sale > highest_sale:
        highest_sale = sale

    if sale < lowest_sale:
        lowest_sale = sale

number_of_transactions = len(sales)
average_sale = total_sales / number_of_transactions

print(f"Total sales: {total_sales}")
print(f"Number of transactions: {number_of_transactions}")
print(f"Average sale: {average_sale}")
print(f"Highest sale: {highest_sale}")
print(f"Lowest sale: {lowest_sale}")

Output:

Total sales: 13200
Number of transactions: 5
Average sale: 2640.0
Highest sale: 4500
Lowest sale: 1200
Explanation

The variable total_sales is an accumulator.

total_sales += sale

is equivalent to:

total_sales = total_sales + sale

The accumulator stores the running total during the loop.

9.33 Practical Example: Counting Positive and Negative Numbers
numbers = [10, -5, 20, -8, 0, 15, -2]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")

Output:

Positive numbers: 3
Negative numbers: 3
Zeros: 1

This pattern is useful in:

Data cleaning

Data profiling

Exploratory data analysis

Validation checks

Numerical analysis

9.34 Practical Example: Validating User Input

A while loop can repeatedly ask for input until the user enters a valid value.

while True:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible")
        break

    print("You must be at least 18 years old")

Example execution:

Enter your age: 15
You must be at least 18 years old
Enter your age: 16
You must be at least 18 years old
Enter your age: 21
You are eligible
Safer Version

The previous example assumes that the user enters a number. If the user enters text, int() raises a ValueError.

A safer version is:

while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative")
            continue

        if age >= 18:
            print("You are eligible")
        else:
            print("You are not eligible")

        break

    except ValueError:
        print("Please enter a valid number")

This example combines:

while

if

continue

break

try

except

9.35 Practical Example: Processing a List of Files

Suppose a data engineering pipeline needs to process several files.

file_names = [
    "sales_january.csv",
    "sales_february.csv",
    "sales_march.csv",
    "sales_april.txt",
    "sales_may.csv",
]

for file_name in file_names:
    if not file_name.endswith(".csv"):
        print(f"Skipping unsupported file: {file_name}")
        continue

    print(f"Processing file: {file_name}")

Output:

Processing file: sales_january.csv
Processing file: sales_february.csv
Processing file: sales_march.csv
Skipping unsupported file: sales_april.txt
Processing file: sales_may.csv

This pattern is useful when:

Reading multiple CSV files

Processing log files

Validating file extensions

Building ETL pipelines

Filtering unsupported inputs

9.36 Practical Example: Batch Processing

In data engineering, records are often processed in batches instead of processing everything at once.

records = list(range(1, 21))
batch_size = 5

for start_index in range(0, len(records), batch_size):
    batch = records[start_index:start_index + batch_size]

    print(f"Processing batch: {batch}")

Output:

Processing batch: [1, 2, 3, 4, 5]
Processing batch: [6, 7, 8, 9, 10]
Processing batch: [11, 12, 13, 14, 15]
Processing batch: [16, 17, 18, 19, 20]
Explanation
range(0, len(records), batch_size)

generates:

0, 5, 10, 15

Each value becomes the starting index of a batch.

records[start_index:start_index + batch_size]

extracts the current batch.

Why Batch Processing Is Useful

Batch processing can help:

Reduce memory usage

Control processing size

Improve pipeline organization

Handle large datasets

Retry failed batches independently

9.37 Practical Example: NovaMart Transaction Processing

Assume NovaMart has the following transaction records:

transactions = [
    {"customer": "Amit", "amount": 1200, "status": "completed"},
    {"customer": "Riya", "amount": 2500, "status": "completed"},
    {"customer": "Karan", "amount": 1800, "status": "failed"},
    {"customer": "Neha", "amount": 3200, "status": "completed"},
]

We want to calculate the total value of completed transactions.

transactions = [
    {"customer": "Amit", "amount": 1200, "status": "completed"},
    {"customer": "Riya", "amount": 2500, "status": "completed"},
    {"customer": "Karan", "amount": 1800, "status": "failed"},
    {"customer": "Neha", "amount": 3200, "status": "completed"},
]

completed_total = 0
completed_count = 0

for transaction in transactions:
    if transaction["status"] != "completed":
        continue

    completed_total += transaction["amount"]
    completed_count += 1

print(f"Completed transactions: {completed_count}")
print(f"Completed transaction value: {completed_total}")

Output:

Completed transactions: 3
Completed transaction value: 6900
Finding the First Failed Transaction
for transaction in transactions:
    if transaction["status"] == "failed":
        print("First failed transaction found:")
        print(transaction)
        break

Output:

First failed transaction found:
{'customer': 'Karan', 'amount': 1800, 'status': 'failed'}

9.38 Practice Exercises

The following exercises are designed to strengthen your understanding of loops and iteration.

Try solving each problem yourself before checking the solution.

Exercise 1: Print Numbers from 1 to 20

Write a for loop that prints numbers from 1 to 20.

Expected Output
1
2
3
...
20
Solution
for number in range(1, 21):
    print(number)
Exercise 2: Print Even Numbers

Print all even numbers between 1 and 50.

Solution
for number in range(1, 51):
    if number % 2 == 0:
        print(number)
Alternative Solution
for number in range(2, 51, 2):
    print(number)

The second solution is more direct because the loop increases by 2.

Exercise 3: Print Odd Numbers

Print all odd numbers between 1 and 50.

Solution
for number in range(1, 51):
    if number % 2 != 0:
        print(number)
Alternative Solution
for number in range(1, 51, 2):
    print(number)
Exercise 4: Calculate the Sum of Numbers

Calculate the sum of numbers from 1 to 100.

Expected Output
5050
Solution
total = 0

for number in range(1, 101):
    total += number

print(total)
Exercise 5: Calculate the Factorial of a Number

The factorial of a number is the product of all positive integers from 1 to that number.

For example:

5! = 5 × 4 × 3 × 2 × 1 = 120
Solution
number = 5
factorial = 1

for value in range(1, number + 1):
    factorial *= value

print(f"Factorial of {number}: {factorial}")

Output:

Factorial of 5: 120
Exercise 6: Multiplication Table

Ask the user for a number and print its multiplication table from 1 to 10.

Solution
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
Exercise 7: Count Vowels

Count the number of vowels in a string.

text = "Data Engineering"
Solution
text = "Data Engineering"
vowels = "aeiouAEIOU"

vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")

Output:

Number of vowels: 7
Exercise 8: Reverse a String Using a Loop

Reverse the following string without using slicing:

text = "Python"
Solution
text = "Python"
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print(reversed_text)

Output:

nohtyP
Exercise 9: Find the Largest Number

Find the largest number without using the built-in max() function.

numbers = [45, 12, 89, 34, 67, 23]
Solution
numbers = [45, 12, 89, 34, 67, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number: {largest}")

Output:

Largest number: 89
Exercise 10: Find the Smallest Number

Find the smallest number without using the built-in min() function.

Solution
numbers = [45, 12, 89, 34, 67, 23]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"Smallest number: {smallest}")

Output:

Smallest number: 12
Exercise 11: Count Positive, Negative, and Zero Values

Given:

numbers = [10, -5, 0, 20, -8, 15, 0]

Count:

Positive numbers

Negative numbers

Zeros

Solution
numbers = [10, -5, 0, 20, -8, 15, 0]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")
Exercise 12: Filter Invalid Transactions

Given:

transactions = [1200, -500, 2500, -100, 3000]

Create a new list containing only positive transaction amounts.

Expected Output
[1200, 2500, 3000]
Solution
transactions = [1200, -500, 2500, -100, 3000]

valid_transactions = []

for transaction in transactions:
    if transaction > 0:
        valid_transactions.append(transaction)

print(valid_transactions)
Exercise 13: Calculate Average Sales

Given:

sales = [1200, 2500, 1800, 3200, 4500]

Calculate the average sale amount.

Solution
sales = [1200, 2500, 1800, 3200, 4500]

total_sales = 0

for sale in sales:
    total_sales += sale

average_sales = total_sales / len(sales)

print(f"Average sales: {average_sales}")

Output:

Average sales: 2640.0
Exercise 14: Password Validation

Keep asking the user for a password until they enter:

python123
Solution
correct_password = "python123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password. Try again.")
Exercise 15: Print a Pattern

Print the following pattern:

*
* *
* * *
* * * *
* * * * *
Solution
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")

    print()
Exercise 16: Print a Number Pattern

Print:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Solution
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")

    print()
Exercise 17: Search for a Product

Search for a product in a list.

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

Use the loop else clause to display a message when the product is not found.

Solution
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
search_product = "Printer"

for product in products:
    if product == search_product:
        print("Product found")
        break
else:
    print("Product not found")

Output:

Product not found
Exercise 18: Process Records in Batches

Split the following records into batches of three:

records = list(range(1, 11))
Expected Output
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10]
Solution
records = list(range(1, 11))
batch_size = 3

for start_index in range(0, len(records), batch_size):
    batch = records[start_index:start_index + batch_size]
    print(batch)
Exercise 19: Find the First Failed Transaction

Given:

transactions = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "completed"},
    {"id": 3, "status": "failed"},
    {"id": 4, "status": "completed"},
]

Find and display the first failed transaction.

Solution
transactions = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "completed"},
    {"id": 3, "status": "failed"},
    {"id": 4, "status": "completed"},
]

for transaction in transactions:
    if transaction["status"] == "failed":
        print("Failed transaction found:")
        print(transaction)
        break
Exercise 20: Remove Duplicate Values

Given:

numbers = [10, 20, 10, 30, 20, 40, 30]

Create a new list containing unique values.

Solution
numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

Output:

[10, 20, 30, 40]
9.39 Interview Questions
1. What is a loop?

A loop is a programming structure used to execute a block of code repeatedly.

Python mainly supports:

for loops

while loops

2. What is the difference between a for loop and a while loop?

A for loop is commonly used to iterate over an iterable such as a list, string, tuple, set, dictionary, or range.

A while loop executes as long as its condition remains true.

for number in range(5):
    print(number)
number = 0

while number < 5:
    print(number)
    number += 1
3. What does range() return?

range() returns a range object representing a sequence of numbers.

numbers = range(1, 5)

print(list(numbers))

Output:

[1, 2, 3, 4]
4. Is the stop value included in range()?

No.

range(1, 5)

generates:

1, 2, 3, 4

The stop value 5 is excluded.

5. What is an infinite loop?

An infinite loop is a loop that never stops because its condition never becomes false.

Example:

number = 1

while number <= 5:
    print(number)

The variable number never changes, so the condition remains true.

6. How can an infinite loop be stopped?

An infinite loop can be stopped by:

Updating the loop condition

Using break

Interrupting program execution

Example:

while True:
    command = input("Enter quit to stop: ")

    if command == "quit":
        break
7. What is the difference between break and continue?

Statement

	

Behavior




break

	

Exits the loop completely




continue

	

Skips the current iteration




pass

	

Does nothing

8. What is the purpose of pass?

pass is a placeholder statement.

It is used when Python requires a statement but no action is currently needed.

for number in range(5):
    pass
9. Can a loop have an else block?

Yes.

The loop else block executes when the loop completes normally.

It does not execute if the loop is stopped using break.

10. What is a nested loop?

A nested loop is a loop inside another loop.

Example:

for row in range(3):
    for column in range(3):
        print(row, column)

Nested loops are commonly used for:

Matrix processing

Pattern printing

Pair comparisons

Multi-dimensional data

11. What is an accumulator?

An accumulator is a variable that stores a running result.

total = 0

for number in range(1, 6):
    total += number

print(total)

Output:

15
12. What is the time complexity of a single loop?

A loop that processes n items generally has:

O(n)

This is called linear time complexity.

13. What is the time complexity of two nested loops?

Two nested loops that each run n times generally have:

O(n²)

This is called quadratic time complexity.

14. Why should nested loops be used carefully?

Nested loops are loops placed inside another loop.

Example:

for i in range(3):
    for j in range(3):
        print(i, j)

Output:

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2

The inner loop runs completely for every iteration of the outer loop.

Why can nested loops be expensive?

If the outer loop runs n times and the inner loop also runs n times, the total number of operations becomes:

n×n=n
2

This is called O(n²) time complexity.

For example:

for customer in customers:
    for transaction in transactions:
        process(customer, transaction)

If there are:

1,000 customers

10,000 transactions

The loop may perform:

1,000×10,000=10,000,000

iterations.

Better approach

Instead of repeatedly searching through a list, use a dictionary or set for faster lookup.

Inefficient approach
for customer in customers:
    for transaction in transactions:
        if customer["id"] == transaction["customer_id"]:
            print(transaction)
More efficient approach
transactions_by_customer = {}

for transaction in transactions:
    customer_id = transaction["customer_id"]

    if customer_id not in transactions_by_customer:
        transactions_by_customer[customer_id] = []

    transactions_by_customer[customer_id].append(transaction)

for customer in customers:
    customer_id = customer["id"]

    for transaction in transactions_by_customer.get(customer_id, []):
        print(transaction)
Interview answer

Nested loops should be used carefully because they can increase time complexity, often from O(n) to O(n²). They may be acceptable for small datasets, but for large datasets we should consider dictionaries, sets, sorting, joins, or vectorized operations to improve performance.

15. What is the difference between break and continue?
break

break immediately terminates the loop.

for number in range(1, 6):
    if number == 4:
        break

    print(number)

Output:

1
2
3
continue

continue skips the current iteration and moves to the next iteration.

for number in range(1, 6):
    if number == 4:
        continue

    print(number)

Output:

1
2
3
5

Statement

	

Behavior




break

	

Stops the entire loop




continue

	

Skips only the current iteration




pass

	

Does nothing; placeholder statement

16. What is the purpose of the pass statement?

pass is a placeholder. It allows Python code to remain syntactically valid when no action is required yet.

for number in range(5):
    if number == 3:
        pass
    else:
        print(number)

Output:

0
1
2
4

Another example:

def future_function():
    pass

The function is valid but does not perform any action.

Important point

pass does not skip an iteration. It simply does nothing.

17. Can a loop have an else block?

Yes. Python allows else with both for and while loops.

The else block runs when the loop finishes normally, without encountering break.

for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully")

Output:

1
2
3
4
5
Loop completed successfully

If break is used, the else block does not execute.

for number in range(1, 6):
    if number == 3:
        break

    print(number)
else:
    print("Loop completed successfully")

Output:

1
2
Practical example: Searching for a record
transactions = [101, 102, 103, 104]
search_id = 103

for transaction_id in transactions:
    if transaction_id == search_id:
        print("Transaction found")
        break
else:
    print("Transaction not found")

Output:

Transaction found
18. What is the difference between range(5) and range(1, 5)?
range(5)

Generates:

0, 1, 2, 3, 4
range(1, 5)

Generates:

1, 2, 3, 4

The stop value is excluded.

Examples
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 10, 2)))
print(list(range(10, 0, -2)))

Output:

[0, 1, 2, 3, 4]
[1, 2, 3, 4]
[1, 3, 5, 7, 9]
[10, 8, 6, 4, 2]

The structure is:

range(start, stop, step)
19. How can you iterate over a dictionary?
Iterating over keys
sales = {
    "North": 120000,
    "South": 95000,
    "West": 110000
}

for region in sales:
    print(region)
Iterating over values
for amount in sales.values():
    print(amount)
Iterating over keys and values
for region, amount in sales.items():
    print(region, amount)

Output:

North 120000
South 95000
West 110000
20. How do you process data in batches using a loop?

Batch processing means dividing a large dataset into smaller groups.

records = list(range(1, 11))
batch_size = 3

for start in range(0, len(records), batch_size):
    batch = records[start:start + batch_size]

    print("Processing batch:", batch)

Output:

Processing batch: [1, 2, 3]
Processing batch: [4, 5, 6]
Processing batch: [7, 8, 9]
Processing batch: [10]

Batch processing is useful when:

Data is too large to process at once.

API requests have limits.

Database inserts should be performed in groups.

Memory usage needs to be controlled.

ETL pipelines process records incrementally.

9.40 Section Project: Transaction Processing Program
Project Objective

Build a small transaction-processing program that demonstrates:

for loops

while loops

range()

break

continue

pass

Nested loops

Dictionary iteration

Data validation

Batch processing

Summary calculations

The program will process sample transactions from a fictional company called NovaMart.

Project Requirements

The program should:

Display a welcome message.

Process a list of transactions.

Skip invalid transactions.

Calculate total sales.

Count successful and failed transactions.

Display sales by region.

Search for a particular transaction.

Process transactions in batches.

Demonstrate a nested loop.

Display a final summary.

9.41 Implementation File

Create or update this file:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\code\01-python-foundations\01-python-fundamentals\09_loops_and_iteration.py

Add the following code:

"""
Section 9: Loops and Iteration

Project:
Transaction Processing Program

This file demonstrates:
- for loops
- while loops
- range()
- break
- continue
- pass
- nested loops
- dictionary iteration
- batch processing
"""


print("=" * 60)
print("NOVAMART TRANSACTION PROCESSING SYSTEM")
print("=" * 60)


# ---------------------------------------------------------
# 1. Sample transaction data
# ---------------------------------------------------------

transactions = [
    {
        "transaction_id": 101,
        "customer": "Amit",
        "region": "North",
        "amount": 1200,
        "status": "success"
    },
    {
        "transaction_id": 102,
        "customer": "Priya",
        "region": "South",
        "amount": 2500,
        "status": "success"
    },
    {
        "transaction_id": 103,
        "customer": "Rahul",
        "region": "West",
        "amount": 0,
        "status": "failed"
    },
    {
        "transaction_id": 104,
        "customer": "Neha",
        "region": "North",
        "amount": 1800,
        "status": "success"
    },
    {
        "transaction_id": 105,
        "customer": "Karan",
        "region": "East",
        "amount": -500,
        "status": "failed"
    },
    {
        "transaction_id": 106,
        "customer": "Sneha",
        "region": "South",
        "amount": 3200,
        "status": "success"
    }
]


# ---------------------------------------------------------
# 2. Process transactions using a for loop
# ---------------------------------------------------------

print("\nPROCESSING TRANSACTIONS")

total_sales = 0
successful_transactions = 0
failed_transactions = 0

for transaction in transactions:

    transaction_id = transaction["transaction_id"]
    amount = transaction["amount"]
    status = transaction["status"]

    # Skip invalid transaction amounts
    if amount <= 0:
        failed_transactions += 1
        print(
            f"Transaction {transaction_id} skipped: "
            f"invalid amount {amount}"
        )
        continue

    # Skip failed transactions
    if status != "success":
        failed_transactions += 1
        print(
            f"Transaction {transaction_id} skipped: "
            f"status is {status}"
        )
        continue

    total_sales += amount
    successful_transactions += 1

    print(
        f"Transaction {transaction_id} processed successfully: "
        f"₹{amount}"
    )


# ---------------------------------------------------------
# 3. Calculate average transaction value
# ---------------------------------------------------------

if successful_transactions > 0:
    average_transaction_value = (
        total_sales / successful_transactions
    )
else:
    average_transaction_value = 0

print("\nSALES SUMMARY")
print("-" * 40)
print(f"Total sales: ₹{total_sales}")
print(f"Successful transactions: {successful_transactions}")
print(f"Failed transactions: {failed_transactions}")
print(
    f"Average transaction value: "
    f"₹{average_transaction_value:.2f}"
)


# ---------------------------------------------------------
# 4. Calculate sales by region
# ---------------------------------------------------------

sales_by_region = {}

for transaction in transactions:

    if transaction["status"] != "success":
        continue

    if transaction["amount"] <= 0:
        continue

    region = transaction["region"]
    amount = transaction["amount"]

    if region not in sales_by_region:
        sales_by_region[region] = 0

    sales_by_region[region] += amount


print("\nSALES BY REGION")
print("-" * 40)

for region, amount in sales_by_region.items():
    print(f"{region}: ₹{amount}")


# ---------------------------------------------------------
# 5. Search for a transaction using break
# ---------------------------------------------------------

search_transaction_id = 104
transaction_found = False

print("\nTRANSACTION SEARCH")

for transaction in transactions:

    if transaction["transaction_id"] == search_transaction_id:
        print("Transaction found:")
        print(transaction)

        transaction_found = True
        break

if not transaction_found:
    print("Transaction not found")


# ---------------------------------------------------------
# 6. Demonstrate loop else
# ---------------------------------------------------------

print("\nSEARCH USING LOOP ELSE")

search_transaction_id = 999

for transaction in transactions:

    if transaction["transaction_id"] == search_transaction_id:
        print("Transaction found")
        break
else:
    print("Transaction not found")


# ---------------------------------------------------------
# 7. Demonstrate while loop
# ---------------------------------------------------------

print("\nWHILE LOOP DEMONSTRATION")

attempt = 1
maximum_attempts = 3

while attempt <= maximum_attempts:
    print(f"Processing attempt {attempt}")
    attempt += 1


# ---------------------------------------------------------
# 8. Demonstrate pass
# ---------------------------------------------------------

print("\nPASS STATEMENT DEMONSTRATION")

for transaction in transactions:

    if transaction["status"] == "pending":
        pass
    else:
        print(
            f"Transaction {transaction['transaction_id']} "
            f"does not require pending review"
        )


# ---------------------------------------------------------
# 9. Batch processing
# ---------------------------------------------------------

print("\nBATCH PROCESSING")

batch_size = 2

for start in range(0, len(transactions), batch_size):

    batch = transactions[start:start + batch_size]

    print(
        f"Processing batch starting at index {start}: "
        f"{len(batch)} transactions"
    )

    for transaction in batch:
        print(
            f"  Processing transaction "
            f"{transaction['transaction_id']}"
        )


# ---------------------------------------------------------
# 10. Nested loop demonstration
# ---------------------------------------------------------

print("\nNESTED LOOP DEMONSTRATION")

regions = ["North", "South"]
transaction_statuses = ["success", "failed"]

for region in regions:

    for status in transaction_statuses:

        print(
            f"Region: {region}, "
            f"Status: {status}"
        )


# ---------------------------------------------------------
# 11. Final report
# ---------------------------------------------------------

print("\nFINAL REPORT")
print("=" * 60)
print(f"Total transactions received: {len(transactions)}")
print(f"Successful transactions: {successful_transactions}")
print(f"Failed transactions: {failed_transactions}")
print(f"Total valid sales: ₹{total_sales}")
print("=" * 60)
9.42 Running the Implementation

Open PowerShell and run:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

Execute the file:

python .\code\01-python-foundations\01-python-fundamentals\09_loops_and_iteration.py

You should see output similar to:

============================================================
NOVAMART TRANSACTION PROCESSING SYSTEM
============================================================

PROCESSING TRANSACTIONS
Transaction 101 processed successfully: ₹1200
Transaction 102 processed successfully: ₹2500
Transaction 103 skipped: invalid amount 0
Transaction 104 processed successfully: ₹1800
Transaction 105 skipped: invalid amount -500
Transaction 106 processed successfully: ₹3200

SALES SUMMARY
----------------------------------------
Total sales: ₹8700
Successful transactions: 4
Failed transactions: 2
Average transaction value: ₹2175.00

The exact formatting may vary slightly depending on your terminal.

9.43 Important Concepts Demonstrated
for loop

Used to process each transaction:

for transaction in transactions:
    print(transaction)
continue

Used to skip invalid records:

if amount <= 0:
    continue
break

Used to stop searching after finding a transaction:

if transaction["transaction_id"] == search_transaction_id:
    break
while loop

Used to repeat processing while a condition remains true:

while attempt <= maximum_attempts:
    attempt += 1
range()

Used for batch start positions:

for start in range(0, len(transactions), batch_size):
    ...
Nested loop

Used to combine regions and transaction statuses:

for region in regions:
    for status in transaction_statuses:
        print(region, status)
Dictionary iteration

Used to display regional sales:

for region, amount in sales_by_region.items():
    print(region, amount)
9.44 Documentation Update

For the book project, update:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\book\01-python-foundations\01-python-fundamentals.md

9.45 Section 9 Completion Checklist
Understood for loops.
Understood while loops.
Used range().
Iterated over strings.
Iterated over lists.
Iterated over dictionaries.
Used break.
Used continue.
Used pass.
Understood loop else.
Practiced nested loops.
Understood nested-loop performance.
Practiced batch processing.
Completed loop-related interview questions.
Built the transaction-processing project.
Created the implementation file.
Ran the implementation successfully.
Updated the book documentation.
Committed and pushed the changes to GitHub.

Section 10 — Python Collections

Python collections are used to store, organize, access, and process multiple values.

In data engineering and data science, collections are essential because real-world data usually contains multiple records, transactions, customers, products, and measurements.

For example:

customer_name = "Amit"
customer_age = 28
customer_city = "Delhi"

This stores information about only one customer.

If we have many customers, storing every value in a separate variable becomes difficult:

customer_1 = "Amit"
customer_2 = "Priya"
customer_3 = "Rahul"
customer_4 = "Neha"

Instead, we can use a collection:

customers = ["Amit", "Priya", "Rahul", "Neha"]

Now all customer names are stored in one structure.

10.1 Learning Objectives

By the end of this section, you will understand:

What Python collections are.

The difference between lists, tuples, sets, and dictionaries.

Mutable and immutable collections.

Ordered and unordered collections.

Indexing and slicing.

Collection methods.

Nested collections.

List comprehensions.

Dictionary comprehensions.

Collection unpacking.

Shallow and deep copying.

Collection performance.

Practical data-processing use cases.

10.2 What Are Python Collections?

A collection is a data structure that stores multiple values in a single variable.

Python provides four main built-in collection types:

Collection

	

Description

	

Example




List

	

Ordered and changeable collection

	

[10, 20, 30]




Tuple

	

Ordered and unchangeable collection

	

(10, 20, 30)




Set

	

Unordered collection of unique values

	

{10, 20, 30}




Dictionary

	

Collection of key-value pairs

	

{"name": "Amit"}

Example
numbers_list = [10, 20, 30]
numbers_tuple = (10, 20, 30)
numbers_set = {10, 20, 30}

student = {
    "name": "Amit",
    "age": 22
}
10.3 Why Are Collections Important?

Collections are used in almost every programming and data-processing task.

Common use cases

Storing customer records.

Storing transaction amounts.

Removing duplicate values.

Grouping data by category.

Counting values.

Reading JSON data.

Processing API responses.

Preparing data for Pandas.

Creating lookup tables.

Managing configuration values.

Example:

transactions = [1200, 2500, 1800, 3200]

total_sales = sum(transactions)

print(total_sales)

Output:

8700

Without a collection, we would need separate variables:

transaction_1 = 1200
transaction_2 = 2500
transaction_3 = 1800
transaction_4 = 3200

total_sales = (
    transaction_1
    + transaction_2
    + transaction_3
    + transaction_4
)

Collections make the code shorter, cleaner, and easier to maintain.

10.4 List

A list is an ordered and mutable collection.

Lists can contain:

Integers

Floats

Strings

Booleans

Other lists

Dictionaries

Mixed data types

10.4.1 Creating a List
numbers = [10, 20, 30, 40, 50]

print(numbers)

Output:

[10, 20, 30, 40, 50]

A list can contain strings:

cities = ["Delhi", "Mumbai", "Pune", "Bengaluru"]

print(cities)

A list can contain mixed data types:

mixed_data = [
    101,
    "Amit",
    85.5,
    True
]

print(mixed_data)

An empty list can be created using:

empty_list = []

print(empty_list)

Or:

empty_list = list()

print(empty_list)
10.4.2 Accessing List Elements

List elements are accessed using indexes.

Python indexing starts from 0.

cities = ["Delhi", "Mumbai", "Pune", "Bengaluru"]

Element

	

Index




Delhi

	

0




Mumbai

	

1




Pune

	

2




Bengaluru

	

3

cities = ["Delhi", "Mumbai", "Pune", "Bengaluru"]

print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

Output:

Delhi
Mumbai
Pune
Bengaluru
Negative indexing

Negative indexes access elements from the end.

Element

	

Negative index




Bengaluru

	

-1




Pune

	

-2




Mumbai

	

-3




Delhi

	

-4

print(cities[-1])
print(cities[-2])

Output:

Bengaluru
Pune
10.4.3 Updating List Elements

Lists are mutable, meaning their elements can be changed.

cities = ["Delhi", "Mumbai", "Pune"]

cities[1] = "Jaipur"

print(cities)

Output:

['Delhi', 'Jaipur', 'Pune']

This is not possible with tuples because tuples are immutable.

10.4.4 Adding Elements to a List
append()

Adds one element to the end of the list.

cities = ["Delhi", "Mumbai"]

cities.append("Pune")

print(cities)

Output:

['Delhi', 'Mumbai', 'Pune']
insert()

Adds an element at a specific index.

cities = ["Delhi", "Mumbai", "Pune"]

cities.insert(1, "Jaipur")

print(cities)

Output:

['Delhi', 'Jaipur', 'Mumbai', 'Pune']
extend()

Adds multiple elements to the list.

cities = ["Delhi", "Mumbai"]

cities.extend(["Pune", "Jaipur"])

print(cities)

Output:

['Delhi', 'Mumbai', 'Pune', 'Jaipur']
Difference between append() and extend()
cities = ["Delhi", "Mumbai"]

cities.append(["Pune", "Jaipur"])

print(cities)

Output:

['Delhi', 'Mumbai', ['Pune', 'Jaipur']]

The entire list is added as one element.

Using extend():

cities = ["Delhi", "Mumbai"]

cities.extend(["Pune", "Jaipur"])

print(cities)

Output:

['Delhi', 'Mumbai', 'Pune', 'Jaipur']

Method

	

Behavior




append()

	

Adds one object as one element




extend()

	

Adds elements from another iterable




insert()

	

Adds an element at a specific position

10.4.5 Removing Elements from a List
remove()

Removes the first matching value.

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)

Output:

[10, 30, 20, 40]
pop()

Removes and returns an element by index.

numbers = [10, 20, 30, 40]

removed_value = numbers.pop(1)

print(removed_value)
print(numbers)

Output:

20
[10, 30, 40]

If no index is provided, pop() removes the last element.

numbers = [10, 20, 30]

last_value = numbers.pop()

print(last_value)
print(numbers)

Output:

30
[10, 20]
del

Deletes an element or a slice.

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

Output:

[10, 30, 40]
clear()

Removes all elements.

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

Output:

[]
10.4.6 List Slicing

Slicing extracts a part of a list.

The syntax is:

list[start:stop:step]

The stop index is excluded.

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])

Output:

[20, 30, 40]
Examples
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])

Output:

[10, 20, 30]
[40, 50, 60]
[10, 30, 50]
[60, 50, 40, 30, 20, 10]
10.4.7 Useful List Methods

Method

	

Purpose




append()

	

Adds one element




extend()

	

Adds multiple elements




insert()

	

Adds an element at an index




remove()

	

Removes the first matching value




pop()

	

Removes and returns an element




clear()

	

Removes all elements




index()

	

Returns the index of a value




count()

	

Counts occurrences




sort()

	

Sorts the list




reverse()

	

Reverses the list




copy()

	

Creates a shallow copy

Example
numbers = [40, 10, 30, 20, 10]

print(numbers.count(10))
print(numbers.index(30))

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers)

Output:

2
2
[10, 10, 20, 30, 40]
[40, 30, 20, 10, 10]
10.4.8 Sorting Lists
Ascending order
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

Output:

[10, 20, 30, 40, 50]
Descending order
numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)

Output:

[50, 40, 30, 20, 10]
Using sorted()

The sorted() function returns a new sorted list.

numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)

Output:

[10, 20, 30, 40, 50]
[50, 10, 40, 20, 30]
Difference between sort() and sorted()

sort()

	

sorted()




Modifies the original list

	

Returns a new sorted list




Works on lists

	

Works on many iterables




Returns None

	

Returns a sorted list

10.4.9 Iterating Over a List
sales = [1200, 2500, 1800, 3200]

for amount in sales:
    print(amount)

Output:

1200
2500
1800
3200

Calculating total sales:

sales = [1200, 2500, 1800, 3200]

total_sales = 0

for amount in sales:
    total_sales += amount

print(total_sales)

Output:

8700

Python also provides the built-in sum() function:

total_sales = sum(sales)

print(total_sales)
10.4.10 Checking Membership

Use in to check whether a value exists in a list.

cities = ["Delhi", "Mumbai", "Pune"]

print("Mumbai" in cities)
print("Chennai" in cities)

Output:

True
False

Use not in to check whether a value does not exist.

print("Chennai" not in cities)

Output:

True
10.4.11 Nested Lists

A list can contain other lists.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])
print(matrix[1][2])

Output:

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3]
6

Nested lists are useful for:

Matrices.

Tabular data.

Rows and columns.

Grouped records.

Batch processing.

10.4.12 List of Dictionaries

A list of dictionaries stores multiple records where each record is represented by a dictionary.

This is one of the most common data structures used when working with:

JSON data.

REST APIs.

MongoDB documents.

Customer records.

Transaction data.

Data engineering pipelines.

customers = [
    {
        "id": 101,
        "name": "Amit",
        "city": "Delhi"
    },
    {
        "id": 102,
        "name": "Priya",
        "city": "Mumbai"
    },
    {
        "id": 103,
        "name": "Rahul",
        "city": "Pune"
    }
]
Accessing a complete record
print(customers[0])

Output:

{'id': 101, 'name': 'Amit', 'city': 'Delhi'}
Accessing a specific field
print(customers[0]["name"])

Output:

Amit
Iterating over records
for customer in customers:
    print(customer["name"])

Output:

Amit
Priya
Rahul
Filtering records
for customer in customers:
    if customer["city"] == "Delhi":
        print(customer)

Output:

{'id': 101, 'name': 'Amit', 'city': 'Delhi'}
Updating a record
customers[0]["city"] = "Jaipur"

print(customers[0])
Adding a new field
customers[0]["status"] = "active"

print(customers[0])
Adding a new record
customers.append(
    {
        "id": 104,
        "name": "Neha",
        "city": "Bengaluru"
    }
)
Finding a customer
search_id = 102

for customer in customers:
    if customer["id"] == search_id:
        print("Customer found:", customer)
        break
Converting records into a lookup dictionary

Searching a list repeatedly can be inefficient. We can create a dictionary using the customer ID as the key.

customers_by_id = {}

for customer in customers:
    customers_by_id[customer["id"]] = customer

print(customers_by_id[102])

Output:

{'id': 102, 'name': 'Priya', 'city': 'Mumbai'}

This is useful when we need frequent lookups by ID.

10.5 Tuple

A tuple is an ordered and immutable collection.

A tuple is similar to a list, but its elements cannot be changed after creation.

10.5.1 Creating a Tuple
numbers = (10, 20, 30, 40)

print(numbers)

Output:

(10, 20, 30, 40)

A tuple can contain mixed data types:

employee = (101, "Amit", "Data Engineer", 75000)

print(employee)

An empty tuple:

empty_tuple = ()
Single-element tuple

A comma is required:

single_value = (10,)

print(type(single_value))

Without the comma:

not_a_tuple = (10,)

print(type(not_a_tuple))

The comma is what makes it a tuple.

10.5.2 Accessing Tuple Elements

Tuples use indexing like lists.

coordinates = (28.6139, 77.2090)

print(coordinates[0])
print(coordinates[1])

Output:

28.6139
77.209

Negative indexing also works:

print(coordinates[-1])
10.5.3 Tuple Immutability

The following code causes an error:

numbers = (10, 20, 30)

numbers[0] = 100

Error:

TypeError: 'tuple' object does not support item assignment

A tuple cannot be modified after creation.

10.5.4 Tuple Unpacking

Tuple unpacking assigns tuple values to separate variables.

employee = (101, "Amit", "Data Engineer")

employee_id, name, role = employee

print(employee_id)
print(name)
print(role)

Output:

101
Amit
Data Engineer
Extended unpacking
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

Output:

10
[20, 30, 40]
50
10.5.5 Tuple Methods

Tuples provide two main methods:

Method

	

Purpose




count()

	

Counts occurrences




index()

	

Returns the index of a value

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
print(numbers.index(30))

Output:

3
3
10.5.6 When Should Tuples Be Used?

Use tuples when:

The values should not change.

You are storing fixed configuration.

You are representing coordinates.

You are returning multiple values from a function.

You want to communicate that the data is fixed.

Example:

DATABASE_CONFIG = (
    "localhost",
    27017,
    "vehicle_insurance"
)

A tuple communicates that these configuration values are not expected to change.

10.6 Set

A set is an unordered collection of unique values.

Sets are useful for:

Removing duplicates.

Membership testing.

Comparing groups of values.

Finding common elements.

Finding missing elements.

10.6.1 Creating a Set
numbers = {10, 20, 30, 40}

print(numbers)

Sets do not maintain duplicates:

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

Output:

{10, 20, 30}

The order of set output should not be relied upon.

Empty set

An empty set must be created using set():

empty_set = set()

This creates an empty dictionary:

empty_dictionary = {}
10.6.2 Adding and Removing Set Elements
add()
cities = {"Delhi", "Mumbai"}

cities.add("Pune")

print(cities)
update()
cities.update(["Jaipur", "Bengaluru"])

print(cities)
remove()
cities.remove("Mumbai")

If the value does not exist, remove() raises a KeyError.

discard()
cities.discard("Chennai")

discard() does not raise an error if the value is missing.

pop()
cities.pop()

Because sets are unordered, pop() removes an arbitrary element.

clear()
cities.clear()
10.6.3 Set Operations

Suppose we have two sets:

python_students = {"Amit", "Priya", "Rahul"}
sql_students = {"Priya", "Rahul", "Neha"}
Union

Combines all unique values.

all_students = python_students.union(sql_students)

print(all_students)

Output:

{'Amit', 'Priya', 'Rahul', 'Neha'}

Using the operator:

all_students = python_students | sql_students
Intersection

Returns values common to both sets.

common_students = python_students.intersection(sql_students)

print(common_students)

Output:

{'Priya', 'Rahul'}

Using the operator:

common_students = python_students & sql_students
Difference

Returns values present in the first set but not in the second.

only_python = python_students.difference(sql_students)

print(only_python)

Output:

{'Amit'}

Using the operator:

only_python = python_students - sql_students
Symmetric difference

Returns values that exist in either set, but not in both.

different_students = python_students.symmetric_difference(
    sql_students
)

print(different_students)

Using the operator:

different_students = python_students ^ sql_students
10.6.4 Removing Duplicates from a List
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)

This removes duplicates, but the original order may not be preserved.

Order-preserving approach
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)

Output:

[10, 20, 30, 40]
10.6.5 Set Membership Testing

Set membership is generally faster than list membership for large collections.

customer_ids = {101, 102, 103, 104}

print(102 in customer_ids)
print(999 in customer_ids)

Output:

True
False

This is useful for validating whether an ID exists.

10.7 Dictionary

A dictionary stores data in key-value pairs.

Example:

customer = {
    "id": 101,
    "name": "Amit",
    "city": "Delhi"
}

Here:

Key	Value
id	101
name	"Amit"
city	"Delhi"

Dictionaries are especially important in data engineering because JSON documents, API responses, configuration files, and many database records naturally map to Python dictionaries.

10.7.1 Creating a Dictionary
student = {
    "name": "Amit",
    "age": 22,
    "course": "Data Science"
}

print(student)

Output:

{'name': 'Amit', 'age': 22, 'course': 'Data Science'}

An empty dictionary can be created using:

student = {}

or:

student = dict()
10.7.2 Accessing Dictionary Values

Use the key to access its corresponding value.

student = {
    "name": "Amit",
    "age": 22,
    "course": "Data Science"
}

print(student["name"])
print(student["age"])

Output:

Amit
22

If the key does not exist:

print(student["city"])

Python raises:

KeyError
10.7.3 Using get()

The get() method provides a safer way to access dictionary values.

student = {
    "name": "Amit",
    "age": 22
}

print(student.get("name"))
print(student.get("city"))

Output:

Amit
None

We can also provide a default value:

print(student.get("city", "Unknown"))

Output:

Unknown
[] vs get()
Approach	Missing key
dictionary["key"]	Raises KeyError
dictionary.get("key")	Returns None
dictionary.get("key", default)	Returns specified default

This distinction is particularly useful when processing real-world data where fields may be missing.

10.7.4 Adding and Updating Dictionary Values

Dictionaries are mutable.

customer = {
    "id": 101,
    "name": "Amit"
}

customer["city"] = "Delhi"

print(customer)

Output:

{'id': 101, 'name': 'Amit', 'city': 'Delhi'}

If the key already exists, its value is updated:

customer["city"] = "Mumbai"

print(customer)

Output:

{'id': 101, 'name': 'Amit', 'city': 'Mumbai'}
10.7.5 Updating Multiple Values

The update() method can add or modify multiple key-value pairs.

customer = {
    "id": 101,
    "name": "Amit"
}

customer.update({
    "city": "Delhi",
    "age": 28
})

print(customer)

Output:

{'id': 101, 'name': 'Amit', 'city': 'Delhi', 'age': 28}
10.7.6 Removing Dictionary Elements
pop()

Removes a specified key and returns its value.

customer = {
    "id": 101,
    "name": "Amit",
    "city": "Delhi"
}

removed_city = customer.pop("city")

print(removed_city)
print(customer)

Output:

Delhi
{'id': 101, 'name': 'Amit'}
popitem()

Removes and returns the last inserted key-value pair.

customer = {
    "id": 101,
    "name": "Amit",
    "city": "Delhi"
}

item = customer.popitem()

print(item)
print(customer)
del
customer = {
    "id": 101,
    "name": "Amit",
    "city": "Delhi"
}

del customer["city"]

print(customer)
clear()

Removes all key-value pairs.

customer.clear()

print(customer)

Output:

{}
10.7.7 Dictionary Methods

Some important dictionary methods are:

Method	Purpose
keys()	Returns dictionary keys
values()	Returns dictionary values
items()	Returns key-value pairs
get()	Safely retrieves a value
update()	Adds or updates values
pop()	Removes a specified key
popitem()	Removes the last inserted pair
clear()	Removes all items
copy()	Creates a shallow copy
setdefault()	Gets a value and optionally creates a key
10.7.8 Getting Dictionary Keys
customer = {
    "id": 101,
    "name": "Amit",
    "city": "Delhi"
}

print(customer.keys())

We can convert the result into a list:

print(list(customer.keys()))

Output:

['id', 'name', 'city']
10.7.9 Getting Dictionary Values
print(customer.values())

Or:

print(list(customer.values()))

Output:

[101, 'Amit', 'Delhi']
10.7.10 Getting Keys and Values Together

The items() method returns key-value pairs.

print(customer.items())

More commonly, we iterate through the pairs:

for key, value in customer.items():
    print(key, value)

Output:

id 101
name Amit
city Delhi

This is one of the most common dictionary patterns in Python.

10.7.11 Checking Whether a Key Exists

Use in:

customer = {
    "id": 101,
    "name": "Amit"
}

print("name" in customer)
print("city" in customer)

Output:

True
False

Important: in checks keys, not values.

print("Amit" in customer)

Output:

False

To check values:

print("Amit" in customer.values())

Output:

True
10.8 Nested Dictionaries

A dictionary can contain another dictionary.

company = {
    "employee": {
        "id": 101,
        "name": "Amit",
        "role": "Data Engineer"
    }
}

Access nested values:

print(company["employee"]["name"])

Output:

Amit

A more realistic example:

sales = {
    "North": {
        "revenue": 120000,
        "orders": 150
    },
    "South": {
        "revenue": 95000,
        "orders": 120
    }
}

Access:

print(sales["North"]["revenue"])

Output:

120000
10.9 Dictionary of Lists

Dictionaries can also contain lists.

department_employees = {
    "Data Engineering": [
        "Amit",
        "Priya",
        "Rahul"
    ],
    "Data Science": [
        "Neha",
        "Karan"
    ]
}

Access:

print(department_employees["Data Engineering"])

Output:

['Amit', 'Priya', 'Rahul']

Iterate through the employees:

for employee in department_employees["Data Engineering"]:
    print(employee)
10.10 List of Dictionaries vs Dictionary of Lists

These two structures are both useful, but they represent data differently.

List of dictionaries
customers = [
    {"id": 101, "name": "Amit"},
    {"id": 102, "name": "Priya"},
    {"id": 103, "name": "Rahul"}
]

This is useful when each dictionary represents one complete record.

It resembles rows in a table:

id	name
101	Amit
102	Priya
103	Rahul
Dictionary of lists
customers = {
    "id": [101, 102, 103],
    "name": ["Amit", "Priya", "Rahul"]
}

This groups values by field.

The first structure is often more natural when processing records from APIs or JSON.

10.11 Dictionary Comprehension

Dictionary comprehensions provide a concise way to create dictionaries.

Traditional approach
squares = {}

for number in range(1, 6):
    squares[number] = number ** 2

print(squares)

Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Dictionary comprehension
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)

Same output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

The general syntax is:

{key_expression: value_expression for item in iterable}
10.12 Conditional Dictionary Comprehension

We can include conditions.

numbers = range(1, 11)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)

Output:

{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

This is useful when filtering and transforming data simultaneously.

10.13 List Comprehension

A list comprehension creates a list using a compact syntax.

Traditional approach:

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

List comprehension:

squares = [
    number ** 2
    for number in numbers
]

print(squares)

Output:

[1, 4, 9, 16, 25]
10.13.1 Conditional List Comprehension
numbers = range(1, 11)

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)

Output:

[2, 4, 6, 8, 10]
10.13.2 Practical Data Example

Suppose we have transaction amounts:

transactions = [500, 1200, 300, 2500, 800]

We want transactions greater than ₹1,000:

large_transactions = [
    amount
    for amount in transactions
    if amount > 1000
]

print(large_transactions)

Output:

[1200, 2500]
10.14 Set Comprehension

Set comprehensions work similarly to list comprehensions.

numbers = [1, 2, 2, 3, 3, 4]

squares = {
    number ** 2
    for number in numbers
}

print(squares)

Output:

{1, 4, 9, 16}

Duplicate results are automatically removed because the result is a set.

10.15 Collection Unpacking

Python allows values from collections to be assigned to variables.

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

Output:

10
20
30
Using *
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

Output:

10
[20, 30, 40]
50

This is useful when the number of middle elements is variable.

10.16 Shallow Copy vs Deep Copy

Copying collections is an important concept because nested collections can behave unexpectedly.

10.16.1 Assignment Does Not Create a Copy
numbers = [10, 20, 30]

new_numbers = numbers

new_numbers.append(40)

print(numbers)
print(new_numbers)

Output:

[10, 20, 30, 40]
[10, 20, 30, 40]

Both variables refer to the same list.

10.16.2 Shallow Copy

A shallow copy creates a new outer collection.

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)

Output:

[10, 20, 30]
[10, 20, 30, 40]

For a simple list, this behaves as expected.

However, nested objects are still shared.

data = [
    [1, 2],
    [3, 4]
]

new_data = data.copy()

new_data[0].append(100)

print(data)
print(new_data)

Output:

[[1, 2, 100], [3, 4]]
[[1, 2, 100], [3, 4]]

The inner list is shared.

10.16.3 Deep Copy

A deep copy recursively copies nested objects.

import copy

data = [
    [1, 2],
    [3, 4]
]

new_data = copy.deepcopy(data)

new_data[0].append(100)

print(data)
print(new_data)

Output:

[[1, 2], [3, 4]]
[[1, 2, 100], [3, 4]]
Comparison
Operation	Outer collection	Nested objects
Assignment	Same	Same
Shallow copy	New	Shared
Deep copy	New	New
10.17 Mutable vs Immutable Collections

Mutability determines whether an object can be changed after creation.

Mutable

These can be modified:

List
Set
Dictionary

Example:

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
Immutable

These cannot be modified after creation:

Tuple
String

Example:

numbers = (10, 20, 30)

# numbers[0] = 100

This raises a TypeError if uncommented.

Summary
Type	Mutable
List	Yes
Tuple	No
Set	Yes
Dictionary	Yes
String	No
10.18 Collection Comparison
Feature	List	Tuple	Set	Dictionary
Ordered	Yes	Yes	No*	Yes**
Mutable	Yes	No	Yes	Yes
Duplicates	Yes	Yes	No	Keys: No
Indexing	Yes	Yes	No	By key
Key-value pairs	No	No	No	Yes
Main use	Sequence	Fixed sequence	Unique values	Mappings

* Sets are unordered collections and should not be relied upon for positional order.

** Dictionaries preserve insertion order in modern Python versions.

10.19 Choosing the Right Collection

The choice depends on the problem.

Use a list when:

You need an ordered collection that can change.

transactions = [1200, 1500, 2200]
Use a tuple when:

The values represent a fixed collection.

coordinates = (28.6139, 77.2090)
Use a set when:

You need unique values or fast membership testing.

customer_ids = {101, 102, 103}
Use a dictionary when:

You need key-value relationships.

customer = {
    "id": 101,
    "name": "Amit"
}
10.20 Collection Performance

Performance becomes important when processing large datasets.

Typical average-case behavior:

Operation	List	Set	Dictionary
Membership search	O(n)	O(1)	O(1)
Index access	O(1)	Not supported	O(1) by key
Append/add	O(1)*	O(1)*	O(1)*
Delete by value/key	O(n)	O(1)*	O(1)*

* Average/amortized behavior; exact performance depends on the operation and implementation.

Example

For a list:

customer_ids = [101, 102, 103, 104, 105]

if 105 in customer_ids:
    print("Customer found")

Python may need to check multiple elements.

With a set:

customer_ids = {101, 102, 103, 104, 105}

if 105 in customer_ids:
    print("Customer found")

Set membership is generally much faster for large collections.

10.21 Practical Data Engineering Example

Consider transaction records:

transactions = [
    {
        "transaction_id": 101,
        "customer_id": 501,
        "amount": 1200
    },
    {
        "transaction_id": 102,
        "customer_id": 502,
        "amount": 2500
    },
    {
        "transaction_id": 103,
        "customer_id": 501,
        "amount": 1800
    }
]
Calculate total sales
total_sales = sum(
    transaction["amount"]
    for transaction in transactions
)

print(total_sales)

Output:

5500
Get unique customers
customer_ids = {
    transaction["customer_id"]
    for transaction in transactions
}

print(customer_ids)

Output:

{501, 502}
Create a customer-to-transactions mapping
transactions_by_customer = {}

for transaction in transactions:

    customer_id = transaction["customer_id"]

    if customer_id not in transactions_by_customer:
        transactions_by_customer[customer_id] = []

    transactions_by_customer[customer_id].append(transaction)

Result:

{
    501: [
        {
            "transaction_id": 101,
            "customer_id": 501,
            "amount": 1200
        },
        {
            "transaction_id": 103,
            "customer_id": 501,
            "amount": 1800
        }
    ],
    502: [
        {
            "transaction_id": 102,
            "customer_id": 502,
            "amount": 2500
        }
    ]
}

This demonstrates how Python collections can be combined to solve realistic data-processing problems.

10.22 JSON-Like Data

Python dictionaries and lists closely resemble JSON structures.

Example JSON-like Python object:

customer = {
    "customer_id": 101,
    "name": "Amit",
    "orders": [
        {
            "order_id": 1001,
            "amount": 1200
        },
        {
            "order_id": 1002,
            "amount": 2500
        }
    ]
}

Accessing nested data:

print(customer["name"])

for order in customer["orders"]:
    print(order["order_id"], order["amount"])

Output:

Amit
1001 1200
1002 2500

This structure is extremely common when working with REST APIs and document databases.

10.23 Practice Exercises

Try solving these before looking at the solutions.

Exercise 1 — Create a List

Create a list containing five programming languages and print it.

Exercise 2 — List Indexing

Given:

languages = ["Python", "SQL", "Java", "Scala", "R"]

Print:

First element
Last element
Third element
Exercise 3 — List Modification

Add "Spark" to the list.

Then remove "Java".

Exercise 4 — List Filtering

Given:

numbers = [10, 15, 20, 25, 30, 35, 40]

Create a list containing only even numbers.

Exercise 5 — Tuple

Create a tuple containing:

101, "Amit", "Data Engineer"

Unpack it into three variables.

Exercise 6 — Remove Duplicates

Given:

numbers = [10, 20, 20, 30, 40, 40, 50]

Create a collection containing only unique values.

Exercise 7 — Set Intersection

Find the common elements between:

python_users = {"Amit", "Priya", "Rahul"}
sql_users = {"Priya", "Rahul", "Neha"}
Exercise 8 — Dictionary

Create a dictionary representing an employee with:

ID
Name
Department
Salary
Exercise 9 — Dictionary Filtering

Given:

sales = {
    "North": 120000,
    "South": 95000,
    "East": 85000,
    "West": 110000
}

Create a new dictionary containing regions with sales greater than 100000.

Exercise 10 — List of Dictionaries

Given:

employees = [
    {"name": "Amit", "salary": 70000},
    {"name": "Priya", "salary": 85000},
    {"name": "Rahul", "salary": 65000}
]

Print employees whose salary is greater than 70000.

Exercise 11 — Dictionary Comprehension

Create a dictionary mapping numbers from 1 to 5 to their squares.

Exercise 12 — Transaction Data

Given:

transactions = [
    {"id": 101, "amount": 1200},
    {"id": 102, "amount": 800},
    {"id": 103, "amount": 2500}
]

Calculate total transaction value.

Exercise 13 — Unique Customer IDs

Given a list of transactions, extract unique customer IDs using a set.

Exercise 14 — Frequency Counter

Given:

products = [
    "Laptop",
    "Phone",
    "Laptop",
    "Tablet",
    "Phone",
    "Laptop"
]

Create a dictionary containing the frequency of each product.

Exercise 15 — Nested Dictionary

Create a dictionary representing two departments and their employees.

Exercise 16 — Shallow Copy

Create a list, make a copy using .copy(), modify the copied list, and verify that the original list remains unchanged.

Exercise 17 — List Comprehension

Create a list of squares for numbers from 1 to 10.

Exercise 18 — Conditional Comprehension

Create a list containing only numbers greater than 50:

numbers = [20, 55, 70, 30, 90, 45]
Exercise 19 — Data Filtering

Given a list of transaction dictionaries, create a new list containing only transactions with amount greater than 1000.

Exercise 20 — Combined Collections

Build a program that:

Stores transactions in a list of dictionaries.
Extracts unique customer IDs into a set.
Calculates total sales.
Creates a dictionary mapping customer IDs to their total sales.
10.24 Practice Exercise Solutions
Solution 1
languages = ["Python", "SQL", "Java", "Scala", "R"]

print(languages)
Solution 2
languages = ["Python", "SQL", "Java", "Scala", "R"]

print(languages[0])
print(languages[-1])
print(languages[2])
Solution 3
languages = ["Python", "SQL", "Java", "Scala", "R"]

languages.append("Spark")
languages.remove("Java")

print(languages)
Solution 4
numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
Solution 5
employee = (101, "Amit", "Data Engineer")

employee_id, name, role = employee

print(employee_id)
print(name)
print(role)
Solution 6
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print(unique_numbers)
Solution 7
python_users = {"Amit", "Priya", "Rahul"}
sql_users = {"Priya", "Rahul", "Neha"}

common_users = python_users & sql_users

print(common_users)
Solution 8
employee = {
    "id": 101,
    "name": "Amit",
    "department": "Data Engineering",
    "salary": 75000
}

print(employee)
Solution 9
sales = {
    "North": 120000,
    "South": 95000,
    "East": 85000,
    "West": 110000
}

high_sales_regions = {
    region: amount
    for region, amount in sales.items()
    if amount > 100000
}

print(high_sales_regions)

Output:

{'North': 120000, 'West': 110000}
Solution 10
employees = [
    {"name": "Amit", "salary": 70000},
    {"name": "Priya", "salary": 85000},
    {"name": "Rahul", "salary": 65000}
]

for employee in employees:
    if employee["salary"] > 70000:
        print(employee["name"])

Output:

Priya
Solution 11
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
Solution 12
transactions = [
    {"id": 101, "amount": 1200},
    {"id": 102, "amount": 800},
    {"id": 103, "amount": 2500}
]

total = sum(
    transaction["amount"]
    for transaction in transactions
)

print(total)

Output:

4500
Solution 13
transactions = [
    {"customer_id": 501, "amount": 1200},
    {"customer_id": 502, "amount": 800},
    {"customer_id": 501, "amount": 2500}
]

customer_ids = {
    transaction["customer_id"]
    for transaction in transactions
}

print(customer_ids)
Solution 14
products = [
    "Laptop",
    "Phone",
    "Laptop",
    "Tablet",
    "Phone",
    "Laptop"
]

frequency = {}

for product in products:
    frequency[product] = frequency.get(product, 0) + 1

print(frequency)

Output:

{'Laptop': 3, 'Phone': 2, 'Tablet': 1}

This is an important pattern in data processing:

dictionary[key] = dictionary.get(key, 0) + 1

It is frequently used for counting occurrences.

Solution 15
departments = {
    "Data Engineering": [
        "Amit",
        "Priya"
    ],
    "Data Science": [
        "Rahul",
        "Neha"
    ]
}

print(departments)
Solution 16
numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)

Output:

[10, 20, 30]
[10, 20, 30, 40]
Solution 17
squares = [
    number ** 2
    for number in range(1, 11)
]

print(squares)
Solution 18
numbers = [20, 55, 70, 30, 90, 45]

large_numbers = [
    number
    for number in numbers
    if number > 50
]

print(large_numbers)

Output:

[55, 70, 90]
Solution 19
transactions = [
    {"id": 101, "amount": 1200},
    {"id": 102, "amount": 800},
    {"id": 103, "amount": 2500}
]

large_transactions = [
    transaction
    for transaction in transactions
    if transaction["amount"] > 1000
]

print(large_transactions)
Solution 20
transactions = [
    {
        "id": 101,
        "customer_id": 501,
        "amount": 1200
    },
    {
        "id": 102,
        "customer_id": 502,
        "amount": 800
    },
    {
        "id": 103,
        "customer_id": 501,
        "amount": 2500
    },
    {
        "id": 104,
        "customer_id": 503,
        "amount": 1500
    }
]

# Unique customer IDs
customer_ids = {
    transaction["customer_id"]
    for transaction in transactions
}

# Total sales
total_sales = sum(
    transaction["amount"]
    for transaction in transactions
)

# Sales by customer
sales_by_customer = {}

for transaction in transactions:

    customer_id = transaction["customer_id"]
    amount = transaction["amount"]

    sales_by_customer[customer_id] = (
        sales_by_customer.get(customer_id, 0)
        + amount
    )

print("Customer IDs:", customer_ids)
print("Total sales:", total_sales)
print("Sales by customer:", sales_by_customer)

Output:

Customer IDs: {501, 502, 503}
Total sales: 6000
Sales by customer: {501: 3700, 502: 800, 503: 1500}

This exercise combines list + dictionary + set + iteration + aggregation and represents a pattern frequently encountered in data-processing workflows.

10.25 Interview Questions
1. What are the four main Python collection types?

List, tuple, set, and dictionary.

2. What is the difference between a list and a tuple?

A list is mutable, while a tuple is immutable.

my_list = [10, 20]
my_tuple = (10, 20)
3. Why would you use a set?

When you need unique values or efficient membership testing.

customer_ids = {101, 102, 103}
4. Can a set contain duplicate values?

No.

numbers = {10, 10, 20, 20}

print(numbers)

The duplicates are removed.

5. Can dictionary keys be duplicated?

No. Assigning the same key again replaces its previous value.

data = {
    "name": "Amit",
    "name": "Rahul"
}

print(data)

Result:

{'name': 'Rahul'}
6. Can dictionary values be duplicated?

Yes.

data = {
    "employee_1": "Data Engineer",
    "employee_2": "Data Engineer"
}
7. What is dictionary comprehension?

A concise way to create dictionaries.

squares = {
    x: x ** 2
    for x in range(1, 6)
}
8. What is list comprehension?

A concise way to create lists.

squares = [
    x ** 2
    for x in range(1, 6)
]
9. What is the difference between append() and extend()?

append() adds one object as a single element, while extend() adds elements from another iterable.

10. What is the difference between remove() and pop()?

remove() removes a value, while pop() removes an element by position and returns it.

11. What is the difference between sort() and sorted()?

sort() modifies the original list. sorted() creates and returns a new sorted list.

12. What is tuple unpacking?

Assigning tuple elements to multiple variables.

employee = (101, "Amit", "Engineer")

employee_id, name, role = employee
13. What is mutability?

Mutability describes whether an object can be modified after it has been created.

Lists are mutable:

numbers = [1, 2, 3]
numbers[0] = 100

Tuples are immutable:

numbers = (1, 2, 3)
14. Why are sets generally faster for membership testing than lists?

Sets use hash-based lookup, which generally provides average O(1) membership testing, while list membership generally requires a sequential search and is O(n).

15. Why are dictionaries important in data engineering?

Dictionaries naturally represent key-value data and are commonly used for:

JSON.
API responses.
Configuration.
Lookup tables.
Aggregation.
Data transformation.
Database documents.
16. What is a list of dictionaries?

A collection where each list element is a dictionary representing a record.

employees = [
    {"id": 101, "name": "Amit"},
    {"id": 102, "name": "Priya"}
]

This structure is extremely common when processing JSON and API data.

17. What is the difference between shallow copy and deep copy?

A shallow copy creates a new outer collection but may share nested objects. A deep copy recursively creates copies of nested objects.

18. What happens when you use {}?

It creates an empty dictionary.

For an empty set, use:

set()
10.26 Section Project — Customer and Transaction Data Management System

Now we will combine everything learned in this section into a practical project.

Project Objective

Build a small customer and transaction management system using:

Lists
Tuples
Sets
Dictionaries
Nested collections
List comprehensions
Dictionary comprehensions
Data validation
Aggregation
Searching
Duplicate detection

The program will work with fictional NovaMart customer and transaction data.

Project Requirements

The program should:

Store customer records.
Store transaction records.
Store fixed configuration using a tuple.
Identify unique customers using a set.
Calculate total sales.
Calculate sales by customer.
Identify high-value transactions.
Detect duplicate transaction IDs.
Create a customer lookup dictionary.
Display a final report.
10.27 Project Implementation

Create:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\code\01-python-foundations\01-python-fundamentals\10_python_collections.py

Add:

"""
Section 10: Python Collections

Project:
Customer and Transaction Data Management System

Demonstrates:
- Lists
- Tuples
- Sets
- Dictionaries
- Nested collections
- List comprehensions
- Dictionary comprehensions
- Data aggregation
- Duplicate detection
"""

print("=" * 60)
print("NOVAMART CUSTOMER AND TRANSACTION SYSTEM")
print("=" * 60)


# ---------------------------------------------------------
# 1. Fixed company configuration using a tuple
# ---------------------------------------------------------

COMPANY_CONFIG = (
    "NovaMart",
    "India",
    "INR"
)

company_name, country, currency = COMPANY_CONFIG

print("\nCOMPANY INFORMATION")
print("-" * 40)
print(f"Company: {company_name}")
print(f"Country: {country}")
print(f"Currency: {currency}")


# ---------------------------------------------------------
# 2. Customer records
# ---------------------------------------------------------

customers = [
    {
        "customer_id": 501,
        "name": "Amit",
        "city": "Delhi"
    },
    {
        "customer_id": 502,
        "name": "Priya",
        "city": "Mumbai"
    },
    {
        "customer_id": 503,
        "name": "Rahul",
        "city": "Pune"
    },
    {
        "customer_id": 504,
        "name": "Neha",
        "city": "Bengaluru"
    }
]


# ---------------------------------------------------------
# 3. Transaction records
# ---------------------------------------------------------

transactions = [
    {
        "transaction_id": 1001,
        "customer_id": 501,
        "amount": 1200,
        "status": "success"
    },
    {
        "transaction_id": 1002,
        "customer_id": 502,
        "amount": 2500,
        "status": "success"
    },
    {
        "transaction_id": 1003,
        "customer_id": 501,
        "amount": 1800,
        "status": "success"
    },
    {
        "transaction_id": 1004,
        "customer_id": 503,
        "amount": 800,
        "status": "failed"
    },
    {
        "transaction_id": 1005,
        "customer_id": 504,
        "amount": 3200,
        "status": "success"
    },
    {
        "transaction_id": 1006,
        "customer_id": 502,
        "amount": 1500,
        "status": "success"
    }
]


# ---------------------------------------------------------
# 4. Create customer lookup dictionary
# ---------------------------------------------------------

customers_by_id = {
    customer["customer_id"]: customer
    for customer in customers
}

print("\nCUSTOMER LOOKUP")
print("-" * 40)

for customer_id, customer in customers_by_id.items():
    print(
        customer_id,
        customer["name"],
        customer["city"]
    )


# ---------------------------------------------------------
# 5. Extract unique customer IDs
# ---------------------------------------------------------

unique_customer_ids = {
    transaction["customer_id"]
    for transaction in transactions
}

print("\nUNIQUE CUSTOMERS")
print("-" * 40)
print(unique_customer_ids)


# ---------------------------------------------------------
# 6. Filter successful transactions
# ---------------------------------------------------------

successful_transactions = [
    transaction
    for transaction in transactions
    if transaction["status"] == "success"
]

print("\nSUCCESSFUL TRANSACTIONS")
print("-" * 40)
print(len(successful_transactions))


# ---------------------------------------------------------
# 7. Calculate total sales
# ---------------------------------------------------------

total_sales = sum(
    transaction["amount"]
    for transaction in successful_transactions
)

print("\nTOTAL SALES")
print("-" * 40)
print(f"₹{total_sales}")


# ---------------------------------------------------------
# 8. Calculate sales by customer
# ---------------------------------------------------------

sales_by_customer = {}

for transaction in successful_transactions:

    customer_id = transaction["customer_id"]
    amount = transaction["amount"]

    sales_by_customer[customer_id] = (
        sales_by_customer.get(customer_id, 0)
        + amount
    )

print("\nSALES BY CUSTOMER")
print("-" * 40)

for customer_id, amount in sales_by_customer.items():

    customer = customers_by_id.get(customer_id)

    if customer:
        print(
            f"{customer['name']}: ₹{amount}"
        )


# ---------------------------------------------------------
# 9. Identify high-value transactions
# ---------------------------------------------------------

high_value_transactions = [
    transaction
    for transaction in successful_transactions
    if transaction["amount"] > 2000
]

print("\nHIGH-VALUE TRANSACTIONS")
print("-" * 40)

for transaction in high_value_transactions:
    print(
        transaction["transaction_id"],
        transaction["amount"]
    )


# ---------------------------------------------------------
# 10. Detect duplicate transaction IDs
# ---------------------------------------------------------

transaction_ids = [
    transaction["transaction_id"]
    for transaction in transactions
]

unique_transaction_ids = set(transaction_ids)

duplicate_count = (
    len(transaction_ids)
    - len(unique_transaction_ids)
)

print("\nDUPLICATE TRANSACTION CHECK")
print("-" * 40)

if duplicate_count == 0:
    print("No duplicate transaction IDs found")
else:
    print(
        f"Duplicate transaction IDs detected: "
        f"{duplicate_count}"
    )


# ---------------------------------------------------------
# 11. Customer transaction counts
# ---------------------------------------------------------

transaction_count_by_customer = {}

for transaction in successful_transactions:

    customer_id = transaction["customer_id"]

    transaction_count_by_customer[customer_id] = (
        transaction_count_by_customer.get(customer_id, 0)
        + 1
    )

print("\nTRANSACTION COUNT BY CUSTOMER")
print("-" * 40)

for customer_id, count in transaction_count_by_customer.items():

    customer = customers_by_id.get(customer_id)

    if customer:
        print(
            f"{customer['name']}: {count}"
        )


# ---------------------------------------------------------
# 12. Final report
# ---------------------------------------------------------

print("\nFINAL REPORT")
print("=" * 60)
print(f"Total customers: {len(customers)}")
print(f"Total transactions: {len(transactions)}")
print(
    f"Successful transactions: "
    f"{len(successful_transactions)}"
)
print(f"Unique customers: {len(unique_customer_ids)}")
print(f"Total sales: ₹{total_sales}")
print(
    f"High-value transactions: "
    f"{len(high_value_transactions)}"
)
print("=" * 60)
10.28 Running the Project

From PowerShell:

cd "E:\Books-By-Chirag\Data Engineering - The Complete Journey"

Run:

python .\code\01-python-foundations\01-python-fundamentals\10_python_collections.py

You should see output similar to:

============================================================
NOVAMART CUSTOMER AND TRANSACTION SYSTEM
============================================================

COMPANY INFORMATION
----------------------------------------
Company: NovaMart
Country: India
Currency: INR

CUSTOMER LOOKUP
----------------------------------------
501 Amit Delhi
502 Priya Mumbai
503 Rahul Pune
504 Neha Bengaluru

UNIQUE CUSTOMERS
----------------------------------------
{501, 502, 503, 504}

SUCCESSFUL TRANSACTIONS
----------------------------------------
5

TOTAL SALES
----------------------------------------
₹10200

SALES BY CUSTOMER
----------------------------------------
Amit: ₹3000
Priya: ₹4000
Neha: ₹3200

HIGH-VALUE TRANSACTIONS
----------------------------------------
1002 2500
1005 3200

DUPLICATE TRANSACTION CHECK
----------------------------------------
No duplicate transaction IDs found
10.29 What the Project Demonstrates

The project combines the four major collection types.

List

Used for records:

customers = [...]
transactions = [...]
Tuple

Used for fixed configuration:

COMPANY_CONFIG = (
    "NovaMart",
    "India",
    "INR"
)
Set

Used for unique customer IDs:

unique_customer_ids = {
    transaction["customer_id"]
    for transaction in transactions
}
Dictionary

Used for customer lookup:

customers_by_id = {
    customer["customer_id"]: customer
    for customer in customers
}

This combination is extremely common in real-world Python data processing.

10.30 Why Collections Matter in Data Engineering

Consider a typical API response:

response = {
    "status": "success",
    "customers": [
        {
            "id": 101,
            "name": "Amit",
            "orders": [
                {
                    "order_id": 1001,
                    "amount": 1200
                }
            ]
        }
    ]
}

This single object uses:

Dictionary for the response.
List for customers.
Dictionary for each customer.
List for orders.
Dictionary for each order.

Understanding collections therefore becomes a prerequisite for working with:

REST APIs.
JSON.
MongoDB.
Configuration files.
ETL pipelines.
Pandas.
Spark.
Cloud services.
10.31 Documentation Update

Update the main book file:

E:\Books-By-Chirag\Data Engineering - The Complete Journey\book\01-python-foundations\01-python-fundamentals.md


10.32 Section 10 Completion Checklist
 Understood Python collections.
 Learned lists.
 Practiced list indexing.
 Practiced list slicing.
 Used list methods.
 Learned tuples.
 Practiced tuple unpacking.
 Learned sets.
 Practiced set operations.
 Learned dictionaries.
 Practiced dictionary methods.
 Worked with nested collections.
 Worked with lists of dictionaries.
 Worked with dictionaries containing lists.
 Learned list comprehensions.
 Learned dictionary comprehensions.
 Learned set comprehensions.
 Learned collection unpacking.
 Understood shallow vs deep copies.
 Understood mutable vs immutable collections.
 Compared collection performance.
 Practiced data-engineering use cases.
 Completed 20 practice exercises.
 Completed interview questions.
 Built the Customer and Transaction Data Management System.
 Created the implementation file.
 Ran the project.
 Updated the book documentation.
 Committed and pushed the section.
 
10.33 Key Takeaways

The four core Python collections should now be easy to distinguish:

List       → Ordered, mutable, duplicates allowed
Tuple      → Ordered, immutable, duplicates allowed
Set        → Unique values, unordered, mutable
Dictionary → Key-value pairs, mutable

A practical way to remember them:

Need a sequence that changes?
→ List

Need a fixed sequence?
→ Tuple

Need unique values?
→ Set

Need key → value mapping?
→ Dictionary

For data engineering, one of the most important structures is:

[
    {
        "id": 101,
        "name": "Amit",
        "amount": 1200
    },
    {
        "id": 102,
        "name": "Priya",
        "amount": 2500
    }
]

This list of dictionaries pattern appears frequently when working with JSON, APIs, databases, and data pipelines.