# Tools and Environment

> Before NovaMart can build reliable data systems, the engineering team needs a reliable workspace.

Data engineering is not only about understanding concepts.

It is also about being able to:

- Write code.
- Run SQL queries.
- Create databases.
- Inspect data.
- Build pipelines.
- Debug failures.
- Track changes.
- Reproduce results.
- Package applications.
- Deploy systems.

For this reason, this book follows a **local-first learning approach**.

We will first learn and implement concepts on our own computer. Later, when the concepts become clear, we will move toward cloud platforms, distributed systems, managed services, and production architectures.

This approach keeps the learning process practical without making the beginner dependent on expensive cloud infrastructure from day one.

---

## 1. The NovaMart Problem

NovaMart has hired several engineers, but everyone is using a different setup.

One engineer writes Python code in one editor.

Another engineer runs SQL queries using a different database tool.

A third engineer stores notebooks in random folders.

Someone else keeps project files only on their laptop.

When the team tries to reproduce a result, they face several problems:

- The Python versions are different.
- Required libraries are missing.
- Database configurations are inconsistent.
- File paths work only on one computer.
- Nobody knows which code version produced a result.
- Secrets are accidentally written inside source code.
- A notebook works for one person but fails for another.

Aisha, the engineering lead, identifies the problem:

> “Before we build a data platform, we need a consistent engineering environment.”

This is the purpose of this chapter.

---

## 2. What We Will Use

The tools in this book are divided into several groups.

| Category | Tools | Purpose |
|---|---|---|
| Operating system | Windows, macOS, or Linux | Run the development environment |
| Code editor | Visual Studio Code | Write and manage code |
| Programming language | Python | Build data applications and pipelines |
| Environment manager | Conda or `venv` | Isolate project dependencies |
| Notebook environment | Jupyter Notebook | Explore data and test ideas |
| Database | SQLite and PostgreSQL | Store and query structured data |
| Query language | SQL | Read, transform, and analyze data |
| Version control | Git | Track code changes |
| Remote repository | GitHub | Store and share the project |
| Containerization | Docker | Package services consistently |
| Documentation | Markdown | Explain concepts and workflows |
| Data processing | pandas and PySpark | Process structured and distributed data |
| Cloud platforms | AWS, Azure, or GCP | Learn deployment and managed services |
| Orchestration | Airflow and similar tools | Schedule and monitor pipelines |
| Visualization | Matplotlib and other tools | Understand data and pipeline results |

We will not use every tool immediately.

Each tool will be introduced when NovaMart encounters a problem that requires it.

---

# Part I — Local Development Environment

## 3. Why Start Locally?

Cloud platforms are important in modern data engineering.

However, starting directly in the cloud can create unnecessary difficulties:

- Cloud accounts may require payment details.
- Services can be expensive if not deleted correctly.
- Permissions and IAM policies can be confusing.
- Networking introduces additional complexity.
- Beginners may focus more on configuration than learning.
- Debugging becomes harder when many managed services are involved.

Local development gives us a simpler starting point.

We can:

- Run code on our own computer.
- Create sample datasets.
- Build small databases.
- Test SQL queries.
- Debug pipelines.
- Delete files and services freely.
- Repeat experiments without worrying about cloud costs.

This does not mean local development is the same as production.

It means local development helps us understand the fundamentals before introducing infrastructure complexity.

---

## 4. Recommended Learning Strategy

This book follows the following progression:

```text
Local Python
    ↓
Local SQL Database
    ↓
Local ETL Pipeline
    ↓
Local Data Processing
    ↓
Dockerized Services
    ↓
Cloud Storage
    ↓
Cloud Data Warehouse or Lakehouse
    ↓
Distributed Processing
    ↓
Streaming and Orchestration
    ↓
Production Architecture

At every stage, we will ask:

What problem are we solving?

Why is this tool needed?

What happens internally?

How do we implement it?

How do we test it?

What can fail?

How would production systems improve it?

Part II — Installing the Core Tools
5. Operating System

You can follow this book using:

Windows.

macOS.

Linux.

The exact installation commands may differ between operating systems.

Most concepts remain the same:

Python works across operating systems.

SQL follows common standards.

Git works across operating systems.

Docker works across operating systems.

Cloud services are generally platform-independent from the user's perspective.

Windows Users

PowerShell or Windows Terminal is recommended.

macOS and Linux Users

Terminal is recommended.

Throughout this book, commands will be shown in a way that is easy to adapt to your operating system.

6. Visual Studio Code

We will use Visual Studio Code as the primary code editor.

Visual Studio Code helps us:

Create files and folders.

Write Python code.

Write SQL queries.

Edit Markdown documentation.

Open notebooks.

Use the terminal.

Work with Git.

Debug applications.

Install useful extensions.

Recommended Extensions

The following extensions are useful:

Extension

	

Purpose




Python

	

Python language support




Pylance

	

Python intelligence and type analysis




Jupyter

	

Run notebooks inside VS Code




SQLTools or database extension

	

Work with SQL databases




GitLens

	

Explore Git history




Markdown All in One

	

Improve Markdown writing




Docker

	

Manage Docker files and containers




YAML

	

Edit YAML configuration files

Extensions are optional.

The book should remain understandable even if you use another editor.

Why Use One Main Editor?

Using one primary editor reduces unnecessary switching.

For NovaMart, the team wants engineers to be able to open the repository and understand:

Where the code is.

Where the datasets are.

Where the notebooks are.

Where the documentation is.

How to run the project.

A consistent editor helps establish that habit.

7. Python

Python will be one of the main programming languages used in this book.

We will use Python for:

Reading files.

Cleaning data.

Calling APIs.

Connecting to databases.

Building ETL pipelines.

Automating tasks.

Writing tests.

Processing data with pandas.

Processing large data with PySpark.

Building production services.

Python Version

Use a currently supported Python version.

For most chapters, Python 3.11 or a compatible newer version should work.

Some libraries may have version-specific requirements. When a chapter requires a particular version, the chapter will mention it.

Check Python Installation

Run:

python --version

On some systems, use:

python3 --version

Example output:

Python 3.12.x

The exact patch version is not important for the early chapters.

8. Conda Environments

A Python project may require many libraries.

For example:

pandas
numpy
sqlalchemy
psycopg2
jupyter
pyspark
pytest

Different projects may require different versions of these libraries.

Installing everything globally creates dependency conflicts.

For example:

Project A requires pandas 2.x
Project B requires pandas 1.x

If both projects use the same global environment, one project may break when the other project is updated.

This is why we use isolated environments.

What Is an Environment?

A Python environment is an isolated workspace containing:

A Python interpreter.

Installed packages.

Package versions.

Project-specific configuration.

Create a Conda Environment
conda create -n data-engineering-book python=3.12

Activate it:

conda activate data-engineering-book

Verify the Python version:

python --version
Why the Environment Name Matters

The environment name is only a label.

You may choose another name, such as:

data_engineering

or:

nova-mart-data

The important thing is that the project uses a separate environment.

Deactivate the Environment
conda deactivate
List Environments
conda env list
9. Alternative: Python venv

Conda is not mandatory.

Python includes a built-in environment tool called venv.

Create an environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Activate it on macOS or Linux:

source .venv/bin/activate

Install packages:

python -m pip install --upgrade pip

The book will generally use Conda in examples, but the concepts apply to venv as well.

10. Package Management

Python packages are external libraries that provide reusable functionality.

Instead of writing every feature from scratch, we can install packages.

For example:

pip install pandas

Check installed packages:

pip list

Export the environment:

pip freeze > requirements.txt

Install dependencies from a file:

pip install -r requirements.txt
Why Dependency Files Matter

Imagine that Rahul builds a pipeline that works on his laptop.

Meera tries to run the same pipeline but receives:

ModuleNotFoundError: No module named 'pandas'

The code is not necessarily wrong.

The environment is incomplete.

A dependency file helps another engineer recreate the required environment.

Example requirements.txt
pandas
numpy
sqlalchemy
jupyter
pytest

For production projects, dependency versions should usually be pinned or managed using a stronger dependency-management strategy.

Part III — Notebooks and Code Files
11. Jupyter Notebooks

Jupyter Notebook is useful for experimentation.

We will use notebooks to:

Load datasets.

Inspect columns.

Explore missing values.

Run SQL queries.

Test transformations.

Visualize data.

Compare approaches.

Explain concepts interactively.

A notebook allows us to combine:

Markdown.

Python code.

SQL.

Tables.

Charts.

Explanations.

Example Notebook Workflow
Read the problem
    ↓
Load sample data
    ↓
Inspect the data
    ↓
Test a transformation
    ↓
Check the result
    ↓
Document the observation
Why Not Use Notebooks for Everything?

Notebooks are excellent for exploration, but production pipelines usually require:

Reusable functions.

Clear configuration.

Logging.

Testing.

Error handling.

Deployment.

Scheduling.

Monitoring.

Therefore, this book will use both:

Notebook → Exploration and learning
Python file → Reusable implementation
SQL file → Database logic
Recommended Notebook Naming

Use descriptive names:

01_load_orders.ipynb
02_clean_orders.ipynb
03_analyze_customers.ipynb
04_build_features.ipynb

Avoid names such as:

final.ipynb
final_final.ipynb
new_version.ipynb
test2.ipynb

Descriptive names make the workflow easier to understand.

12. Python Files

Python files use the .py extension.

Example:

data_ingestion.py

A Python file is more suitable than a notebook when code needs to be:

Reused.

Tested.

Imported.

Scheduled.

Deployed.

Reviewed by another engineer.

Example:

def load_orders(file_path):
    """
    Load orders from a CSV file.
    """
    import pandas as pd

    return pd.read_csv(file_path)

Later, the same function can be imported into another pipeline.

13. SQL Files

SQL files use the .sql extension.

Example:

customer_revenue.sql

SQL files help us store database logic separately from application code.

Example:

SELECT
    customer_id,
    SUM(order_amount) AS total_revenue
FROM orders
GROUP BY customer_id;

Keeping SQL in files makes it easier to:

Review queries.

Version-control database logic.

Reuse transformations.

Test queries.

Share work with analysts and engineers.

Part IV — Databases
14. SQLite

SQLite is a lightweight relational database.

It stores the database in a file instead of requiring a separate database server.

This makes it useful for:

Learning SQL.

Testing database concepts.

Building small prototypes.

Running local experiments.

Understanding tables and relationships.

Why NovaMart Starts with SQLite

NovaMart wants to track its first customer orders.

The team does not need a large database server yet.

A local database file is enough to learn:

Tables.

Rows.

Columns.

Primary keys.

Foreign keys.

Joins.

Aggregations.

Transactions.

Example SQLite Database
datasets/
└── novamart.db
Limitations of SQLite

SQLite is not a replacement for every production database.

It has limitations related to:

Concurrent writes.

Large-scale workloads.

Distributed access.

High availability.

Enterprise operations.

We will use SQLite for learning and small local examples.

15. PostgreSQL

PostgreSQL is a powerful open-source relational database.

It supports:

SQL.

Transactions.

Constraints.

Indexes.

Joins.

Views.

Stored procedures.

Extensions.

Concurrent users.

Production workloads.

We will introduce PostgreSQL when NovaMart needs a more realistic database server.

SQLite vs PostgreSQL

Feature

	

SQLite

	

PostgreSQL




Installation

	

Very simple

	

Requires server setup




Storage

	

Local file

	

Database server




Best use

	

Learning and prototypes

	

Applications and production systems




Concurrent writes

	

Limited

	

Stronger support




Scalability

	

Limited

	

More capable




Administration

	

Minimal

	

More operational work

The goal is not to choose one database forever.

The goal is to understand why different databases exist.

16. Database Client Tools

A database client helps us connect to and inspect databases.

Examples include:

VS Code database extensions.

DBeaver.

pgAdmin.

SQLite browser tools.

Command-line clients.

A client can help us:

Browse tables.

Run queries.

Inspect schemas.

View query results.

Check indexes.

Debug database issues.

The exact client is less important than understanding the database itself.

Part V — Git and GitHub
17. Git

Git is a version-control system.

It tracks changes to files over time.

Without Git, an engineer may create folders like:

project_final
project_final_new
project_final_latest
project_final_latest_2

This quickly becomes difficult to manage.

Git provides a structured history of changes.

Common Git Commands

Check repository status:

git status

Add files:

git add .

Create a commit:

git commit -m "Add SQL learning examples"

View commit history:

git log --oneline

Push changes:

git push origin main

Pull changes:

git pull origin main
What Is a Commit?

A commit is a saved checkpoint in the project history.

A good commit message explains what changed.

Good examples:

Add customer orders dataset
Implement first batch pipeline
Document database normalization
Add PySpark transformation examples

Poor examples:

changes
update
done
final
18. GitHub

GitHub is a platform for hosting Git repositories.

We will use GitHub to:

Store the book.

Track project progress.

Share code.

Review changes.

Document learning.

Collaborate with others.

Publish the completed book.

The repository should contain enough information for another person to clone it and understand how to use it.

Basic Workflow
Create or edit files
    ↓
Review changes
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
Changes available on GitHub
Why Version Control Matters in Data Engineering

Data pipelines change frequently.

For example:

A source column is renamed.

A transformation rule changes.

A database schema is updated.

A bug is fixed.

A new data source is added.

A performance improvement is introduced.

Git allows the team to answer:

Who changed the code?

What changed?

When did it change?

Why did it change?

Which version worked previously?

Part VI — Documentation
19. Markdown

Markdown is a simple text-formatting language.

We will use Markdown for:

Book chapters.

Project documentation.

Setup instructions.

Architecture explanations.

Exercises.

Troubleshooting guides.

Design decisions.

Example:

# Customer Data Pipeline

## Objective

Load customer data into a database.

## Steps

1. Read the CSV file.
2. Validate the columns.
3. Clean missing values.
4. Load the data.
5. Verify the row count.

Markdown is useful because it is:

Easy to read.

Easy to edit.

Supported by GitHub.

Suitable for documentation.

Compatible with documentation websites.

20. Project Documentation

Every practical project should explain:

What problem it solves.

What data it uses.

How to install dependencies.

How to run the code.

What outputs are produced.

What assumptions were made.

What limitations exist.

How the project can be improved.

A project that works but cannot be understood by others is difficult to maintain.

Documentation is part of engineering, not an optional decoration.

Part VII — Configuration and Secrets
21. Configuration Files

A pipeline often needs configuration values such as:

Database host
Database port
Database name
Input file path
Output file path
Batch size
Log level

These values should not always be hardcoded inside the code.

Instead, configuration can be stored separately.

Example:

config/
├── config.yaml
└── settings.py

This allows the same code to run in different environments.

Development
Testing
Production
22. Environment Variables

Environment variables allow configuration to be supplied outside the source code.

Example:

DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=novamart

Python can read environment variables using the os module:

import os

database_host = os.getenv("DATABASE_HOST")
Why Use Environment Variables?

The same code may connect to different databases depending on the environment.

For example:

Local database
    ↓
Testing database
    ↓
Production database

The code should not need to be rewritten every time the database changes.

23. Secrets Must Not Be Committed

Passwords, API keys, access tokens, and private connection strings should not be committed to GitHub.

Bad example:

DATABASE_PASSWORD = "my-secret-password"

Better approach:

import os

database_password = os.getenv("DATABASE_PASSWORD")

A local .env file may be used during development:

DATABASE_HOST=localhost
DATABASE_USER=admin
DATABASE_PASSWORD=secret

The .env file should normally be added to .gitignore.

Example:

.env
.venv/
__pycache__/
*.pyc

A safe repository may include:

.env.example

Example:

DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=

The example file documents required variables without exposing real secrets.

Part VIII — Docker
24. Why Docker?

A common engineering problem is:

“It works on my machine.”

The application works on one computer but fails on another because the environments are different.

Docker helps package an application together with its dependencies.

A Docker image can contain:

Application code.

Required libraries.

Runtime configuration.

System dependencies.

A running instance of an image is called a container.

Basic Docker Concept
Dockerfile
    ↓
Docker Image
    ↓
Docker Container
Why NovaMart Needs Docker

Later, NovaMart will run multiple services:

Database.

Data ingestion service.

Processing service.

API service.

Orchestration service.

Installing every service manually can become difficult.

Docker allows the team to create more consistent environments.

25. Docker Compose

Docker Compose helps run multiple containers together.

For example:

PostgreSQL
    +
Airflow
    +
Data pipeline

A Compose file can describe how these services work together.

Example structure:

docker-compose.yml

We will introduce Docker after the basic Python, SQL, and database concepts are clear.

Part IX — Data Engineering Libraries
26. pandas

pandas is a Python library used for working with structured data.

We will use it to:

Read CSV files.

Read Excel files.

Load JSON data.

Clean missing values.

Filter rows.

Create columns.

Group data.

Merge datasets.

Export results.

Example:

import pandas as pd

df = pd.read_csv("orders.csv")

print(df.head())
print(df.shape)
print(df.columns)

pandas is especially useful for:

Learning.

Data exploration.

Small and medium datasets.

Prototyping transformations.

27. PySpark

PySpark is the Python interface for Apache Spark.

We will use PySpark when NovaMart's data becomes too large or too complex for a simple local pandas workflow.

PySpark helps us learn:

Distributed processing.

DataFrames.

Transformations.

Actions.

Lazy evaluation.

Partitions.

Shuffles.

Fault tolerance.

Cluster execution.

The important point is that PySpark is not introduced merely because it is popular.

It is introduced because NovaMart encounters a scale and processing problem.

28. SQLAlchemy

SQLAlchemy is a Python toolkit for working with databases.

It can help us:

Connect Python applications to databases.

Execute SQL.

Manage database connections.

Work with database metadata.

Integrate database operations into pipelines.

Example:

from sqlalchemy import create_engine

engine = create_engine("sqlite:///novamart.db")

We will first learn SQL directly, then use Python database libraries to connect SQL with applications and pipelines.

29. pytest

pytest is a Python testing framework.

We will use tests to verify:

Functions return expected results.

Data transformations behave correctly.

Invalid inputs are handled.

Pipelines fail safely.

Row counts remain consistent.

Schema assumptions are respected.

Example:

def add_numbers(a, b):
    return a + b

A test could be:

def test_add_numbers():
    assert add_numbers(2, 3) == 5

Testing becomes increasingly important as the pipeline grows.

Part X — Cloud and Production Tools
30. Why Introduce Cloud Later?

Cloud platforms provide managed infrastructure such as:

Object storage.

Databases.

Data warehouses.

Compute services.

Streaming services.

Monitoring.

Identity and access management.

However, cloud services can hide important implementation details.

For example, a managed data warehouse may make it easy to query data, but beginners may not understand:

Where the data is stored.

How files are organized.

How partitions work.

How data is transferred.

How permissions are applied.

What happens when a job fails.

We will first understand the concepts locally, then map them to cloud services.

## 31. Cloud Platforms

This book may use examples from:

- Amazon Web Services.
- Microsoft Azure.
- Google Cloud Platform.

The exact provider may vary by chapter or project.

The main concepts are more important than memorizing provider-specific names.

For example:

| General Concept | Possible Cloud Service |
|---|---|
| Object storage | Amazon S3, Azure Blob Storage, Google Cloud Storage |
| Virtual machines | EC2, Azure VM, Compute Engine |
| Managed Spark | EMR, Databricks, managed Spark services |
| Data warehouse | Redshift, Synapse, BigQuery |
| Orchestration | Managed Airflow or cloud workflow services |
| Monitoring | Cloud-native monitoring tools |

We will distinguish between:

```text
General data engineering concept

and:

Provider-specific implementation

For example, the general concept is object storage.

AWS S3 is one implementation of object storage.

Azure Blob Storage and Google Cloud Storage solve a similar category of problem.

This distinction is important because data engineers often move between cloud providers.

32. Databricks

Databricks is a platform commonly used for:

Data engineering.

Big data processing.

Analytics.

Machine learning.

Streaming.

Lakehouse development.

We will study Databricks after understanding:

SQL.

DataFrames.

Apache Spark.

Storage systems.

Data lakes.

Lakehouses.

Batch processing.

Streaming.

Otherwise, Databricks may feel like a collection of buttons rather than a system whose architecture we understand.

What We Will Learn Later

The Databricks section may cover:

Workspace concepts.

Notebooks.

Compute resources.

Spark execution.

Delta Lake.

Medallion architecture.

Batch pipelines.

Streaming pipelines.

Job scheduling.

Data quality.

Access control.

Cost awareness.

The goal is not simply to learn how to click through a platform.

The goal is to understand why a team would use it and what happens behind the interface.

33. Airflow and Orchestration

A pipeline may contain many steps:

Extract orders
    ↓
Validate orders
    ↓
Clean orders
    ↓
Load database
    ↓
Build reporting table
    ↓
Send completion notification

Running these steps manually is unreliable.

Orchestration tools help manage:

Scheduling.

Dependencies.

Retries.

Logging.

Monitoring.

Failure handling.

Backfills.

Apache Airflow will be introduced when NovaMart needs to coordinate multiple pipeline tasks.

Without Orchestration

An engineer may need to:

Run the ingestion script.

Wait for it to finish.

Check whether it succeeded.

Run the transformation script.

Check the output.

Load the database.

Send a report.

This process is slow and error-prone.

With Orchestration

The workflow can be represented as a directed acyclic graph, commonly called a DAG.

Ingestion
    ↓
Validation
    ↓
Transformation
    ↓
Loading
    ↓
Quality Checks

The orchestrator can:

Run tasks in the correct order.

Retry failed tasks.

Record execution history.

Alert the team.

Run jobs on a schedule.

Later, we will also discuss alternatives to Airflow and how orchestration differs from data processing.

Part X — Data Engineering Libraries
34. pandas

pandas is a Python library used for working with structured data.

We will use it to:

Read CSV files.

Read Excel files.

Load JSON data.

Clean missing values.

Filter rows.

Create columns.

Group data.

Merge datasets.

Export results.

Example:

import pandas as pd

df = pd.read_csv("orders.csv")

print(df.head())
print(df.shape)
print(df.columns)

pandas is especially useful for:

Learning.

Data exploration.

Small and medium datasets.

Prototyping transformations.

Important Limitation

pandas generally works within the memory available to the machine.

If a dataset is too large for memory, the program may become slow or fail.

This limitation will eventually lead NovaMart to explore:

Chunk processing.

Database processing.

Distributed processing.

Apache Spark.

Cloud data platforms.

The important lesson is:

Use the simplest tool that can handle the current workload.

35. PySpark

PySpark is the Python interface for Apache Spark.

We will use PySpark when NovaMart's data becomes too large or too complex for a simple local pandas workflow.

PySpark helps us learn:

Distributed processing.

DataFrames.

Transformations.

Actions.

Lazy evaluation.

Partitions.

Shuffles.

Fault tolerance.

Cluster execution.

The important point is that PySpark is not introduced merely because it is popular.

It is introduced because NovaMart encounters a scale and processing problem.

Example Problem

NovaMart initially processes a small orders file using pandas.

Later, the orders dataset grows significantly.

The pipeline now experiences:

High memory usage.

Long processing times.

Difficulties handling large joins.

Slow aggregations.

Limited ability to scale vertically.

The team begins investigating distributed processing.

This creates the reason to learn Spark.

36. SQLAlchemy

SQLAlchemy is a Python toolkit for working with databases.

It can help us:

Connect Python applications to databases.

Execute SQL.

Manage database connections.

Work with database metadata.

Integrate database operations into pipelines.

Example:

from sqlalchemy import create_engine

engine = create_engine("sqlite:///novamart.db")

We will first learn SQL directly, then use Python database libraries to connect SQL with applications and pipelines.

Why Not Hide SQL Completely?

Some tools allow developers to work with databases without writing much SQL.

These tools can be useful, but data engineers should still understand SQL because:

SQL is used across many databases.

SQL helps debug data problems.

SQL is important for analytics.

SQL is useful for performance analysis.

SQL makes transformations easier to inspect.

SQLAlchemy should support our database work, not replace our understanding of SQL.

37. pytest

pytest is a Python testing framework.

We will use tests to verify:

Functions return expected results.

Data transformations behave correctly.

Invalid inputs are handled.

Pipelines fail safely.

Row counts remain consistent.

Schema assumptions are respected.

Example:

def add_numbers(a, b):
    return a + b

A test could be:

def test_add_numbers():
    assert add_numbers(2, 3) == 5

Testing becomes increasingly important as the pipeline grows.

Data Engineering Tests

A data pipeline may need to test more than normal Python functions.

Examples include:

Does the expected column exist?

Are customer IDs unique?

Are order amounts non-negative?

Did the row count unexpectedly drop?

Are required fields missing?

Is the output schema correct?

Did the pipeline produce duplicate records?

These checks are commonly called data quality checks.

Part XI — Repository Structure
38. Where Each Tool Belongs

The book repository follows a structured layout.

Data Engineering - The Complete Journey/
├── README.md
├── requirements.txt
├── pyproject.toml
├── mkdocs.yml
├── book/
├── code/
├── notebooks/
├── datasets/
├── diagrams/
├── exercises/
└── projects/
book/

Contains the written chapters.

book/
├── 00-preface/
├── 01-python-foundations/
├── 02-sql/
└── ...
code/

Contains reusable implementation files.

code/
├── 01-python-foundations/
├── 02-sql/
├── 03-databases/
└── ...
notebooks/

Contains interactive experiments.

notebooks/
├── sql/
├── pyspark/
├── databases/
└── databricks/
datasets/

Contains sample data and dataset documentation.

datasets/
├── README.md
└── sample_data/
diagrams/

Contains architecture and system diagrams.

diagrams/
├── architecture/
├── database/
└── distributed_systems/
exercises/

Contains practice problems.

exercises/
├── sql/
├── python/
├── spark/
└── system_design/
projects/

Contains larger end-to-end projects.

projects/
├── project-01-batch-etl/
├── project-02-cloud-lakehouse/
├── project-03-streaming-pipeline/
└── project-04-capstone/
Part XII — First Environment Checklist
39. Setup Checklist

Before starting the implementation chapters, confirm that the following tools are available.

Core Setup
Python is installed.
Conda or venv is available.
A project environment has been created.
Visual Studio Code is installed.
Git is installed.
A GitHub account is available.
The repository has been cloned locally.
Jupyter is installed.
pandas is installed.
A basic SQL database is available.
The terminal works inside VS Code.
Verify Python
python --version
Verify Git
git --version
Verify Jupyter
jupyter --version
Verify pandas
python -c "import pandas as pd; print(pd.__version__)"
Verify SQLite
python -c "import sqlite3; print(sqlite3.sqlite_version)"

If these commands work, the initial environment is ready.

Part XIII — Common Setup Problems
40. python Is Not Recognized

Possible causes:

Python is not installed.

Python was not added to the system PATH.

The wrong terminal is being used.

The environment is not activated.

Try:

python3 --version

Or activate the Conda environment:

conda activate data-engineering-book

If you are using Windows and installed Python through Conda, open the Anaconda Prompt or initialize Conda for PowerShell.

41. conda Is Not Recognized

Possible causes:

Conda is not installed.

The terminal was opened before installation.

Conda was not initialized for the shell.

Try opening a new terminal.

If the problem continues, use Python's built-in venv environment instead.

You can also check whether Conda is available using:

conda --version
42. ModuleNotFoundError

Example:

ModuleNotFoundError: No module named 'pandas'

Possible causes:

The package is not installed.

The wrong environment is active.

VS Code is using a different Python interpreter.

Check the active environment:

conda env list

Install the package:

pip install pandas

Then verify the interpreter selected in VS Code.

43. Code Works in a Notebook but Not in a Python File

This may happen because:

The notebook uses a different Python interpreter.

The notebook has variables created in previous cells.

The notebook runs cells in a different order.

A required import is missing from the Python file.

A file path is relative to the notebook location.

This is one reason we will gradually convert successful notebook experiments into clean Python files.

A notebook should help us discover and test an idea.

A Python file should help us implement that idea in a reusable way.

44. File Path Problems

Avoid depending on a specific personal path such as:

"C:/Users/Chirag/Desktop/project/data.csv"

Instead, use project-relative paths or configuration.

Example:

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "datasets"
    / "sample_data"
    / "orders.csv"
)

Portable paths make the project easier to run on another computer.

Important Path Concepts

We will distinguish between:

Absolute paths.

Relative paths.

Current working directory.

Project root.

Input paths.

Output paths.

Many pipeline failures are caused by incorrect assumptions about the current working directory.

Part XIV — Development vs Production
45. Local Setup Is Not Production

Our local environment is designed for learning and experimentation.

Production environments require additional concerns:

Security.

Access control.

Monitoring.

Logging.

Scalability.

High availability.

Disaster recovery.

Cost management.

Data quality.

Deployment automation.

Incident response.

For example, a local SQLite database may be enough for a chapter exercise.

However, a production company may need:

A managed relational database.

Replication.

Backups.

Access policies.

Monitoring.

Recovery procedures.

The tool may change, but the engineering question remains the same:

What requirements must the system satisfy?

46. The Principle of Reproducibility

A result is reproducible when another person can follow the documented steps and obtain the same or an acceptably equivalent result.

A reproducible project should specify:

Python version.

Required packages.

Input data.

Configuration.

Execution commands.

Expected output.

Known limitations.

For NovaMart, reproducibility is important because multiple engineers will work on the same data platform.

If only one engineer knows how to run a pipeline, the company has created a dependency on that person.

Good engineering removes unnecessary dependencies on individuals.

47. The Principle of Simplicity

A common mistake in data engineering is choosing a complicated tool too early.

For example:

Using Spark for a tiny CSV file.

Using a distributed database for a small prototype.

Deploying multiple cloud services before understanding the workflow.

Adding orchestration before the pipeline has multiple dependent tasks.

Introducing containers without understanding the application.

A better approach is:

Start simple
    ↓
Measure the problem
    ↓
Identify the limitation
    ↓
Introduce a suitable tool
    ↓
Measure again

This is not an argument against advanced tools.

It is an argument for using advanced tools for a clear reason.

Part XV — NovaMart's Environment Decision
48. The Team's Initial Setup

After discussing the options, NovaMart chooses the following initial setup:

Editor:
    Visual Studio Code

Language:
    Python

Environment:
    Conda

Notebook:
    Jupyter

Local database:
    SQLite

Production-style relational database:
    PostgreSQL

Version control:
    Git

Repository:
    GitHub

Documentation:
    Markdown

Data processing:
    pandas first, PySpark later

Containers:
    Docker later

Cloud:
    Introduced after local fundamentals

This setup is not the only valid setup.

It is simply a consistent starting point.

The important decision is to avoid changing tools without a clear reason.

49. What We Will Not Do Yet

At the beginning, we will not immediately:

Deploy everything to the cloud.

Build a Kubernetes cluster.

Configure a complex distributed system.

Install every database engine.

Use Spark for tiny datasets.

Create an unnecessarily complex architecture.

Add tools only because they are popular.

Optimize systems before measuring the problem.

Instead, we will build the simplest system that helps us understand the current problem.

This is an important engineering principle:

Complexity should be introduced when it solves a real problem.

50. Chapter Summary

In this chapter, we prepared the engineering environment for the rest of the book.

We learned:

Why a consistent environment matters.

Why the book follows a local-first approach.

How Python will be used.

Why isolated environments are important.

How Conda and venv work.

Why notebooks and Python files serve different purposes.

How SQLite and PostgreSQL fit into the learning journey.

Why Git and GitHub are essential.

How Markdown supports documentation.

Why configuration and secrets must be separated.

What Docker and Docker Compose will solve later.

Where pandas, PySpark, SQLAlchemy, and pytest fit.

Why cloud tools are introduced after fundamentals.

How the repository is organized.

What makes a project reproducible.

Why simplicity should guide tool selection.

The environment is now ready.

But the tools are only useful if we understand the problems they solve.

51. Workbook Exercises
Exercise 1 — Verify Your Environment

Run the following commands:

python --version
git --version
jupyter --version

Record the output in your learning journal.

Exercise 2 — Create a Python Environment

Create a new environment named:

data-engineering-book

Activate it and verify the Python version.

Exercise 3 — Install Basic Libraries

Install:

pandas
numpy
jupyter
pytest
sqlalchemy

Then verify that each library can be imported.

Exercise 4 — Create a Project Notebook

Create:

notebooks/databases/01_environment_check.ipynb

Inside the notebook:

Print the Python version.

Import pandas.

Display the pandas version.

Create a small DataFrame.

Display the DataFrame.

Exercise 5 — Create a SQLite Database

Use Python to create a local SQLite database named:

novamart.db

Create a table called:

customers

Add at least three customers.

Then query the table using SQL.

Exercise 6 — Practice Git

Make a small documentation change.

Then run:

git status
git add .
git commit -m "Verify local development environment"
git log --oneline

If the repository is connected to GitHub, push the commit.

52. Engineering Journal

Write short answers to the following questions:

Why should projects use isolated Python environments?

Why are notebooks useful during exploration?

Why should production logic move into Python or SQL files?

What is the difference between Git and GitHub?

Why should secrets not be committed?

Why are local tools useful before cloud tools?

When might SQLite become insufficient?

Why should tools be introduced only when they solve a real problem?

What does reproducibility mean?

Which part of your environment setup caused the most difficulty?

Why might pandas become insufficient for a large dataset?

What is the difference between a general cloud concept and a provider-specific service?

Why is orchestration different from data processing?

Why should a notebook not automatically become the final production pipeline?

What does “start simple and measure” mean in data engineering?

53. Practical Task — Create an Environment Report

Create a file named:

environment-report.md

Inside it, record:

# Environment Report

## Operating System

Write your operating system here.

## Python Version

Write your Python version here.

## Environment Manager

Conda or venv.

## Editor

Write your editor here.

## Git Version

Write your Git version here.

## Jupyter Version

Write your Jupyter version here.

## Installed Libraries

List the installed libraries.

## Database

SQLite or PostgreSQL.

## Problems Encountered

Describe any setup issues.

## How They Were Solved

Describe the solution.

This exercise creates the first piece of project documentation.

It also teaches an important habit:

Document the environment before the project becomes difficult to reproduce.

54. Next Chapter

The environment is ready.

NovaMart now has:

A development workspace.

A programming language.

A version-control system.

A place to document work.

A plan for local and cloud tools.

The next question is:

What will we build first, and how will the entire data engineering journey be organized?

In the next chapter, we will create the roadmap for the book and connect every major topic to NovaMart's growth.