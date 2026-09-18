
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