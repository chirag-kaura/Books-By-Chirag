
# Part 1 — Python Foundations

> **From writing your first Python program to building reliable data-processing pipelines.**

Python is one of the foundational tools in modern data engineering. It allows engineers to automate tasks, process data, build pipelines, interact with databases, and work with distributed data-processing frameworks.

But learning Python for data engineering is not simply about learning syntax.

It is about understanding how to write programs that can process data reliably, handle failures, scale to larger workloads, and become part of production systems.

In this part of the book, we will build that foundation through the story of **NovaMart**, our fictional e-commerce company.

---

## 1. Welcome to Python Foundations

### The business problem at NovaMart

NovaMart receives data from multiple sources every day:

- Customer registrations.
- Product catalogs.
- Customer orders.
- Payment transactions.
- Warehouse inventory.
- Delivery updates.
- Customer support records.

Initially, many of these tasks are handled manually.

An operations employee downloads an order file, opens it in a spreadsheet, calculates revenue, identifies invalid records, and prepares a report for the business team.

As NovaMart grows, this approach creates problems:

- Manual work takes too much time.
- Different employees may apply different business rules.
- Invalid data can go unnoticed.
- Repeating the same task becomes difficult.
- Processing larger datasets becomes inefficient.
- There is no reliable, reusable pipeline.

The engineering team needs a way to automate these tasks.

**Python becomes one of the first tools NovaMart uses to solve this problem.**

Before we introduce databases, ETL pipelines, Apache Spark, or cloud platforms, we need to understand the programming foundations that make those systems possible.

---

## 2. What You Will Learn

By the end of Part 1, you should be able to:

1. Understand Python syntax, variables, data types, and operators.
2. Write programs using conditions, loops, and comprehensions.
3. Work with Python data structures such as lists, dictionaries, tuples, and sets.
4. Create reusable functions and organize code into modules.
5. Read and write files, CSV data, and JSON data.
6. Understand object-oriented programming and reusable components.
7. Handle errors and implement logging.
8. Write basic automated tests.
9. Manage Python environments and dependencies.
10. Process data using generators and memory-efficient techniques.
11. Build a small local data-processing pipeline.
12. Understand how Python concepts connect to data engineering systems.

The goal is not just to write Python code that works once.

The goal is to develop the habits required to write code that can be understood, tested, maintained, and eventually used in production.

---

## 3. How This Part Is Organized

Part 1 contains eight chapters.

Each chapter introduces a concept, explains why NovaMart needs it, and gradually builds toward practical data-processing workflows.

### Chapter 1 — Python Fundamentals

**File:** `01-python-fundamentals.md`

We begin with the basics of Python.

Topics include:

- What Python is.
- Running Python programs.
- Variables and naming.
- Numbers, strings, and booleans.
- Data types.
- Type conversion.
- Operators.
- Input and output.
- Basic debugging.

**NovaMart problem:** Calculate order revenue and apply basic business rules.

---

### Chapter 2 — Control Flow and Problem Solving

**File:** `02-control-flow-and-problem-solving.md`

Programs need to make decisions and repeat tasks.

Topics include:

- `if`, `elif`, and `else`.
- Comparison operators.
- Logical operators.
- `for` loops.
- `while` loops.
- `break` and `continue`.
- Comprehensions.
- Nested conditions.
- Problem-solving patterns.

**NovaMart problem:** Identify valid orders, calculate discounts, and determine shipping eligibility.

---

### Chapter 3 — Python Data Structures

**File:** `03-python-data-structures.md`

Data engineers work with structured and semi-structured data.

Topics include:

- Lists.
- Tuples.
- Dictionaries.
- Sets.
- Indexing and slicing.
- Nested data structures.
- Mutable and immutable objects.
- Choosing the right data structure.

**NovaMart problem:** Represent customers, products, orders, and inventory records in Python.

---

### Chapter 4 — Functions and Modular Programming

**File:** `04-functions-and-modular-programming.md`

As programs grow, writing everything in one file becomes difficult to maintain.

Topics include:

- Functions.
- Parameters and return values.
- Default arguments.
- Keyword arguments.
- `*args` and `**kwargs`.
- Scope.
- Lambda functions.
- Modules and imports.
- Reusable business logic.

**NovaMart problem:** Build reusable functions for order validation and data transformation.

---

### Chapter 5 — Files, Paths, and Data Formats

**File:** `05-files-paths-and-data-formats.md`

Before working with databases and cloud storage, we need to understand how to work with files.

Topics include:

- Files and directories.
- `pathlib`.
- Reading and writing text files.
- CSV files.
- JSON files.
- Character encoding.
- File validation.
- Missing and malformed files.

**NovaMart problem:** Read daily order files and prepare them for processing.

---

### Chapter 6 — Object-Oriented Python

**File:** `06-object-oriented-python.md`

Data engineering projects often contain reusable components such as data ingestion, validation, and transformation classes.

Topics include:

- Classes and objects.
- Attributes and methods.
- Constructors.
- Instance and class attributes.
- Encapsulation.
- Inheritance.
- Composition.
- Dataclasses.
- Designing reusable components.

**NovaMart problem:** Design a reusable data ingestion component.

---

### Chapter 7 — Errors, Logging, Testing, and Environments

**File:** `07-errors-logging-testing-and-environments.md`

A pipeline that works only when everything goes perfectly is not reliable.

Topics include:

- Syntax errors.
- Runtime errors.
- Logical errors.
- Exceptions.
- Custom exceptions.
- Logging.
- Unit testing with `pytest`.
- Virtual environments.
- Dependency management.
- Environment variables.
- Configuration.

**NovaMart problem:** Detect invalid input files, record failures, and test data-processing logic.

---

### Chapter 8 — Python for Data Engineering

**File:** `08-python-for-data-engineering.md`

In this chapter, we connect Python foundations to actual data engineering work.

Topics include:

- Iterables and iterators.
- Generators.
- Memory-efficient processing.
- Type hints.
- Useful built-in functions.
- Performance basics.
- Data transformation patterns.
- Batch processing.
- End-to-end local data pipeline.

**NovaMart problem:** Build a complete local Python pipeline that reads order data, validates records, transforms data, and produces an output dataset.

---

## 4. Practical Implementation

Throughout this part, we will use a local-first approach.

You will write and execute the code on your own machine before introducing cloud services.

### Tools

The main tools used in this part are:

- Python 3.
- VS Code.
- Python virtual environment.
- Jupyter Notebook.
- Git and GitHub.
- `pytest` for testing.

We will introduce additional libraries only when they are needed.

For example, we will not introduce Apache Spark in this part. Spark will be introduced later when NovaMart needs distributed data processing.

---

## 5. Project Structure

The textbook content and practical implementation will be maintained separately.

### Book chapters

```text
book/01-python-foundations/
├── README.md
├── 01-python-fundamentals.md
├── 02-control-flow-and-problem-solving.md
├── 03-python-data-structures.md
├── 04-functions-and-modular-programming.md
├── 05-files-paths-and-data-formats.md
├── 06-object-oriented-python.md
├── 07-errors-logging-testing-and-environments.md
└── 08-python-for-data-engineering.md
```

### Python implementations

```text
code/01-python-foundations/
├── 01_python_fundamentals/
├── 02_control_flow/
├── 03_data_structures/
├── 04_functions/
├── 05_files_and_formats/
├── 06_oop/
├── 07_errors_testing/
└── 08_data_engineering_python/
```

### Notebooks

```text
notebooks/python/
├── 01_python_fundamentals.ipynb
├── 02_control_flow.ipynb
├── 03_data_structures.ipynb
├── 04_functions.ipynb
├── 05_files_and_formats.ipynb
├── 06_oop.ipynb
├── 07_errors_testing.ipynb
└── 08_data_engineering_python.ipynb
```

Not every chapter requires a notebook.

Some concepts are better learned through Python scripts, while others benefit from interactive experimentation.

---

## 6. How to Study Each Chapter

For every chapter, follow this learning cycle:

### Step 1 — Understand the business problem

Read the NovaMart scenario.

Ask:

> What problem is the engineering team trying to solve?

### Step 2 — Learn the concept

Understand the Python concept from beginner level.

### Step 3 — Explore the deeper technical details

Learn how Python behaves internally where relevant.

### Step 4 — Build the solution

Write the Python code yourself.

### Step 5 — Test the solution

Run the code and verify the output.

### Step 6 — Break the solution

Try invalid inputs, missing values, and unexpected cases.

### Step 7 — Improve the code

Make the solution more readable, reusable, and reliable.

### Step 8 — Practice

Complete the exercises and interview questions.

This approach will help you move from memorizing syntax to understanding how engineers solve problems.

---

## 7. What We Will Build in Part 1

By the end of this part, we will have built a small local Python data-processing project for NovaMart.

The pipeline will gradually evolve as we learn new concepts.

### Initial workflow

```text
NovaMart Order File
        |
        v
Read Order Data
        |
        v
Validate Records
        |
        v
Transform Data
        |
        v
Calculate Business Metrics
        |
        v
Write Processed Output
```

This is a simplified local workflow.

Later in the book, we will extend these ideas into more advanced systems involving:

- SQL databases.
- ETL and ELT pipelines.
- Apache Spark.
- Data lakes.
- Data warehouses.
- Cloud storage.
- Orchestration.
- Streaming.
- Production monitoring.

The concepts learned here will form the foundation for those systems.

---

## 8. Connection to the Next Part

After completing Python Foundations, we will move to:

# Part 2 — SQL

Python helps us write programs and process data.

SQL helps us work with structured data stored in relational databases.

In Part 2, NovaMart will begin storing and querying business data using SQL.

We will learn how to:

- Retrieve data.
- Filter records.
- Aggregate business metrics.
- Join tables.
- Analyze customer and order data.
- Understand relational data processing.

Python and SQL will eventually work together as important tools in NovaMart's data engineering architecture.

---

## 9. Exercises and Interview Preparation

Every chapter will include practical exercises.

The exercises will progress from beginner problems to realistic data engineering scenarios.

Examples include:

- Calculate order totals.
- Validate customer records.
- Process lists of transactions.
- Read and write CSV files.
- Build reusable transformation functions.
- Handle invalid records.
- Write unit tests.
- Process data efficiently.
- Design a local data-processing pipeline.

Each chapter will also include interview questions covering:

- Python fundamentals.
- Data structures.
- Functions.
- Object-oriented programming.
- Error handling.
- Testing.
- Performance.
- Data engineering use cases.

The purpose is to build both practical engineering skills and interview readiness.

---

## 10. Final Goal

By completing Part 1, you should be comfortable writing Python programs that process data and solve practical business problems.

You should also understand the difference between:

- Code that works for a small example.
- Code that is reusable.
- Code that is tested.
- Code that handles failures.
- Code that can become part of a production data pipeline.

That distinction is central to data engineering.

**We are not learning Python just to write Python.**

We are learning Python to build reliable systems that move, transform, and prepare data for the business.

---

## Chapter Navigation

| Chapter | Topic | Status |
|---|---|---|
| 1 | Python Fundamentals | Planned |
| 2 | Control Flow and Problem Solving | Planned |
| 3 | Python Data Structures | Planned |
| 4 | Functions and Modular Programming | Planned |
| 5 | Files, Paths, and Data Formats | Planned |
| 6 | Object-Oriented Python | Planned |
| 7 | Errors, Logging, Testing, and Environments | Planned |
| 8 | Python for Data Engineering | Planned |

---

**Next:** Begin Chapter 1 — Python Fundamentals.