
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