# The Fictional Company

## Meet NovaMart

Throughout this book, we will follow the journey of a fictional company called **NovaMart**.

NovaMart is an online retail company that sells products directly to customers through its website and mobile application.

The company begins as a small business with a simple technology setup.

As the company grows, its data becomes more important and more difficult to manage.

The problems faced by NovaMart will introduce the concepts, tools, architectures, and engineering practices covered in this book.

---

## 1. NovaMart at the Beginning

NovaMart starts with a small team:

- 2 founders.
- 5 customer support employees.
- 3 warehouse employees.
- 2 marketing employees.
- 2 software developers.
- 1 finance employee.

The company sells a limited number of products and receives approximately:

```text
1,000 orders per day

Its technology setup is simple:

Website
   ↓
Application Database
   ↓
Manual Excel Reports

The application database stores:

Customer information.

Product information.

Orders.

Payments.

Addresses.

Every evening, an employee exports data from the database and prepares reports manually.

At this stage, the process appears manageable.

However, the company is already creating data that may become valuable later.

2. The First Technology Setup

NovaMart initially uses the following systems:

System

	

Purpose




Website

	

Customers browse and purchase products




Application backend

	

Handles business logic




Relational database

	

Stores transactional data




Payment gateway

	

Processes payments




Excel files

	

Used for manual reporting




Email

	

Used for internal communication

The initial data flow looks like this:

Customer
   ↓
Website
   ↓
Application Backend
   ↓
Relational Database
   ↓
Manual Export
   ↓
Excel Report
   ↓
Business Team

This architecture works for a small company.

But it contains a major weakness:

Reporting depends on manual data extraction and manual processing.

As the number of orders increases, this process becomes slower and less reliable.

3. The First Business Questions

NovaMart's leadership team wants answers to questions such as:

How much revenue was generated yesterday?

Which products sold the most?

Which regions generated the highest sales?

How many orders were cancelled?

How many customers made repeat purchases?

Which marketing campaign performed best?

How much inventory remains?

Which shipments are delayed?

Initially, employees answer these questions by combining spreadsheets.

This creates several problems:

Different reports use different definitions.

Data may be outdated.

Manual calculations may contain errors.

Reports take too long to prepare.

Employees repeat the same work every day.

The company begins to understand that data is not only an operational requirement.

Data is also a business asset.

4. NovaMart Begins to Grow

After successful early operations, NovaMart expands.

The company now receives:

10,000 orders per day

It also introduces:

More products.

More warehouses.

More delivery partners.

More payment methods.

More marketing campaigns.

A mobile application.

Customer loyalty programs.

The technology landscape becomes more complex.

The company now has multiple systems:

Website
Mobile Application
Order Database
Payment System
Warehouse System
Delivery System
Marketing Platform
Customer Support System

Each system generates data.

The data is useful, but it is distributed across different locations and formats.

5. The Data Sources

NovaMart's main data sources are:

5.1 Website

The website generates:

Page views.

Product searches.

Product clicks.

Cart additions.

Checkout events.

Customer purchases.

Example:

customer_id, event_type, product_id, event_timestamp
101, product_view, 501, 2026-01-10 10:15:00
101, add_to_cart, 501, 2026-01-10 10:17:00
101, purchase, 501, 2026-01-10 10:20:00
5.2 Mobile Application

The mobile application generates similar events:

App opens.

Product views.

Searches.

Purchases.

Notifications.

User interactions.

Mobile events may have a different structure from website events.

This creates a data integration challenge.

5.3 Order Database

The order database stores transactional information.

Example:

order_id, customer_id, order_date, order_amount, order_status
10001, 101, 2026-01-10, 2499.00, delivered
10002, 102, 2026-01-10, 1599.00, cancelled

This data is important for:

Revenue reporting.

Order analysis.

Customer analysis.

Business performance.

5.4 Payment System

The payment system stores:

Payment ID.

Order ID.

Payment method.

Payment amount.

Payment status.

Refund information.

Transaction timestamp.

Example:

payment_id, order_id, payment_status, payment_amount
P9001, 10001, successful, 2499.00
P9002, 10002, refunded, 1599.00

Payment data may not be stored in the same database as order data.

5.5 Warehouse System

The warehouse system stores:

Product stock.

Warehouse location.

Picking status.

Packing status.

Inventory movements.

Example:

product_id, warehouse_id, available_quantity
501, WH01, 250
502, WH02, 175

Inventory information must be updated accurately.

Incorrect inventory data can lead to:

Overselling.

Delayed shipments.

Customer complaints.

Financial losses.

5.6 Delivery System

The delivery system stores:

Shipment ID.

Order ID.

Delivery partner.

Shipment status.

Dispatch time.

Delivery time.

Return information.

Example:

shipment_id, order_id, shipment_status, delivery_partner
S7001, 10001, delivered, Partner_A
S7002, 10003, in_transit, Partner_B

This data helps NovaMart analyze delivery performance.

5.7 Marketing Platform

The marketing platform stores:

Campaign names.

Customer interactions.

Advertisement clicks.

Email opens.

Coupon usage.

Campaign conversions.

Example:

customer_id, campaign_name, event_type, event_timestamp
101, Summer_Sale, email_open, 2026-01-08 09:00:00
101, Summer_Sale, coupon_used, 2026-01-10 10:20:00

The marketing team wants to connect this information with customer purchases.

5.8 Customer Support System

The customer support system stores:

Customer complaints.

Support tickets.

Issue categories.

Resolution status.

Resolution time.

Customer feedback.

Example:

ticket_id, customer_id, issue_type, status
T5001, 101, delayed_delivery, resolved
T5002, 102, payment_failure, open

This data can help NovaMart improve customer experience.

6. The Data Engineering Challenge

NovaMart now has many data sources.

The leadership team wants a single analytical view of the business.

For example:

Which marketing campaigns generated customers who placed profitable orders and received their shipments on time?

Answering this question requires data from:

Marketing Platform
       +
Customer Data
       +
Order Database
       +
Payment System
       +
Warehouse System
       +
Delivery System

The data must be:

Extracted.

Transferred.

Cleaned.

Validated.

Joined.

Transformed.

Stored.

Made available to analysts and business users.

This is where data engineering becomes essential.

7. The People at NovaMart

To understand the problems clearly, we will follow several fictional employees.

7.1 Aisha — Business Analyst

Aisha prepares business reports and dashboards.

Her responsibilities include:

Revenue reporting.

Sales analysis.

Campaign analysis.

Business presentations.

Dashboard maintenance.

Her main problem:

The data she needs is spread across different systems.

7.2 Rahul — Software Engineer

Rahul maintains the website and backend services.

His responsibilities include:

Application development.

API development.

Database operations.

Application performance.

Business logic.

His main problem:

Analytical queries are slowing down the application database.

The transactional database was designed for application operations, not for every analytical workload.

7.3 Meera — Data Engineer

Meera joins NovaMart when the company starts facing serious data problems.

Her responsibilities include:

Data ingestion.

Data transformation.

Data storage.

Data quality.

Pipeline automation.

Monitoring.

Data platform development.

Her main question is:

How can we build a reliable system that delivers the right data to the right people at the right time?

7.4 Arjun — Data Scientist

Arjun builds machine learning models for:

Customer churn prediction.

Product recommendations.

Demand forecasting.

Fraud detection.

His main problem:

Machine learning models require clean, consistent, and regularly updated data.

Without reliable data pipelines, his models cannot be trusted.

7.5 Priya — Cloud and Platform Engineer

Priya helps NovaMart move from local infrastructure to cloud-based systems.

Her responsibilities include:

Cloud infrastructure.

Security.

Networking.

Deployment.

Monitoring.

Cost management.

Her main question is:

How can NovaMart scale its data platform without creating unnecessary operational complexity and cost?

8. NovaMart's Growth Stages

The company will evolve throughout the book.

Stage 1: Small Business
1,000 orders per day

Technology:

One application.

One relational database.

Manual reports.

Small engineering team.

Main problems:

Manual reporting.

Basic data organization.

Repeated spreadsheet work.

Stage 2: Growing Business
10,000 orders per day

Technology:

Multiple applications.

More databases.

More operational systems.

Scheduled scripts.

Basic reporting pipelines.

Main problems:

Data integration.

Duplicate data.

Inconsistent definitions.

Slow reports.

Stage 3: Large Business
100,000 orders per day

Technology:

Large datasets.

Distributed processing.

Data lake storage.

Data warehouse.

Orchestration.

Cloud infrastructure.

Main problems:

Scalability.

Reliability.

Data quality.

Pipeline failures.

Cost management.

Stage 4: Data-Driven Organization
Millions of events per day

Technology:

Batch pipelines.

Streaming pipelines.

Apache Spark.

Kafka or similar event systems.

Lakehouse architecture.

Data governance.

Monitoring and alerting.

Main problems:

Real-time processing.

Security.

Governance.

High availability.

Schema evolution.

Production operations.

9. The Architecture Will Evolve

NovaMart's architecture will not be designed all at once.

It will evolve as new problems appear.

Initial Architecture
Application
    ↓
Relational Database
    ↓
Manual Reports
Intermediate Architecture
Operational Systems
    ↓
Data Ingestion
    ↓
Data Transformation
    ↓
Analytical Database
    ↓
Dashboards
Advanced Architecture
Operational Systems
        ↓
Batch and Streaming Ingestion
        ↓
Message Brokers and Data Connectors
        ↓
Data Lake / Data Lakehouse
        ↓
Distributed Processing
        ↓
Data Warehouse / Serving Layer
        ↓
Analytics, Machine Learning, and Applications

Production capabilities will be added around this architecture:

Orchestration.

Testing.

Monitoring.

Security.

Governance.

Access control.

Cost management.

Disaster recovery.

10. The Rules of the NovaMart Story

To keep the learning journey consistent, we will follow these rules.

Rule 1: Every Technology Must Solve a Problem

We will not introduce a tool simply because it is popular.

First, NovaMart will face a problem.

Then we will examine possible solutions.

Finally, we will introduce the relevant technology.

Rule 2: Start Simple

We will begin with simple systems.

Complex architecture will be introduced only when the business requires it.

This helps us understand why complexity exists.

Rule 3: Understand Before Implementing

Before writing code, we will understand:

The business requirement.

The data flow.

The system components.

The expected output.

The possible failures.

Rule 4: Build Incrementally

NovaMart's platform will grow in stages.

Each stage will build on the previous one.

We will not jump directly from a Python script to a complex cloud architecture.

Rule 5: Discuss Trade-offs

For important design decisions, we will discuss:

Simplicity.

Cost.

Scalability.

Reliability.

Performance.

Maintainability.

Security.

Rule 6: Keep the Story Realistic

NovaMart is fictional, but its engineering problems are based on common real-world scenarios.

The examples are educational and may simplify certain production systems.

11. The First Major Incident

One Monday morning, NovaMart's leadership team requests the previous day's revenue report.

Aisha opens the reporting spreadsheet.

The reported revenue is:

₹48,50,000

However, the finance team reports:

₹46,80,000

The two numbers do not match.

The teams begin investigating.

They discover that:

Some cancelled orders were included.

Some refunded payments were not removed.

A few duplicate records existed.

The report was generated before all orders were loaded.

Different teams used different revenue definitions.

The problem is not simply an incorrect spreadsheet formula.

The deeper problem is:

NovaMart does not have a reliable and consistently defined data pipeline.

This incident becomes the starting point for our data engineering journey.

12. What We Will Build

Throughout the book, we will gradually help NovaMart build:

Reliable data ingestion.

Structured data storage.

SQL-based analytical workflows.

Batch ETL pipelines.

Incremental data loading.

Data validation.

Data quality checks.

Distributed processing.

Spark-based transformations.

NoSQL storage solutions.

Cloud data platforms.

Data warehouses.

Data lakes.

Lakehouse architecture.

Streaming pipelines.

Workflow orchestration.

Monitoring and alerting.

Security and governance.

End-to-end production projects.

Each component will be introduced when NovaMart needs it.

13. Why a Fictional Company?

A fictional company provides a consistent environment for learning.

Instead of learning isolated examples, we can observe:

How requirements change.

How architecture evolves.

Why technical debt appears.

Why simple solutions eventually become insufficient.

How systems interact.

How engineering decisions affect business outcomes.

The story also allows us to connect different topics.

For example:

SQL
  ↓
Databases
  ↓
ETL
  ↓
Data Warehouses
  ↓
Spark
  ↓
Cloud
  ↓
Streaming
  ↓
Production Architecture

These are not unrelated topics.

They are connected parts of a larger data engineering system.

Conclusion

NovaMart is the company we will follow throughout this book.

Its journey will begin with spreadsheets and a small relational database.

It will gradually grow into a complex organization with:

Multiple data sources.

Large-scale data.

Distributed processing.

Cloud infrastructure.

Real-time requirements.

Production data platforms.

Every new problem will create an opportunity to learn a new concept.

Every new technology will be introduced with context.

Every implementation will be followed by production considerations.

Our goal is not only to build NovaMart's data platform.

Our goal is to develop the ability to recognize data problems and design reliable engineering solutions.