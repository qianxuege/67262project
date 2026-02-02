# Airline Operations & Analytics System

This repository contains a **Python and PostgreSQL–based data systems project** that implements core airline operational and analytical use cases. The project demonstrates SQL schema design, data querying, and modular Python scripts to support both transactional workflows and analytics.

## Project Overview

The system supports a variety of airline-related scenarios, including:
- Identifying available flights and hotels
- Minimizing travel costs
- Updating flight times and availability
- Managing user accounts and profile information
- Running analytical queries over structured airline data

Each use case is implemented as a standalone Python script backed by a shared PostgreSQL database.

## Tech Stack

- **Python** – business logic and data processing
- **PostgreSQL** – relational database
- **SQL** – schema creation, initialization, and querying
- **psycopg2** – database connectivity

## Repository Structure
```
67262project/
├── data/ # Dataset files
├── common.py # Shared database utilities
├── create.sql # Database schema creation
├── initialize.sql # Data initialization
├── show_all.sql # Utility query script
├── us1-update_time-simple-operational.py
├── us2-identify-flights-simple-analytical.py
├── us3-minimize-cost-simple-analytical.py
├── us4-identify-hotel-simple-analytical.py
├── us5-update-availability-simple-operational.py
├── us6-maintain-consistency-complex-operational.py
├── us7-create-account-complex-operational.py
├── us8-anticipating-wedding-complex-analytical.py
├── us9-ensure-wifi-complex-analytical.py
├── us10-change-email-simple-operational.py
└── 67262 Project_ Intermediate Deliverable.pdf
```


Each `us*.py` file corresponds to a specific **user story**, categorized as:
- **Simple / Complex Operational**
- **Simple / Complex Analytical**

## Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/qianxuege/67262project.git
cd 67262project
```

### 2. Create the database schema
```bash
psql -U <username> -d <database_name> -f create.sql
```

### 3. Initialize the database
```bash
psql -U <username> -d <database_name> -f initialize.sql
```

### 4. Run a use case script
```bash
python us2-identify-flights-simple-analytical.py
```

Database connection settings can be configured in `common.py`.

## Example Use Cases

### Operational
- Update flight times  
- Update seat or hotel availability  
- Create and modify user accounts  

### Analytical
- Identify flights matching user constraints  
- Minimize travel costs  
- Analyze amenities (e.g., WiFi availability)  

## Notes
- SQL is used for database operations, and Python is used for application logic, ensuring clear separation of concerns.
- Scripts are designed to be run independently against the same database.  
- The project emphasizes correctness, schema design, and query logic over UI.

