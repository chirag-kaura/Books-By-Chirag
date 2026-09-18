
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