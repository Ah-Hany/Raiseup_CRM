🚀 Raiseup CRM & Data Engineering Platform
<p align="center">
<img src="screenshots/crm_login.png" alt="Raiseup CRM Login" width="100%">
</p>
<p align="center">
<img src="[https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)" alt="Python">
<img src="[https://img.shields.io/badge/PostgreSQL-Star%20Schema-336791?style=for-the-badge&logo=postgresql](https://img.shields.io/badge/PostgreSQL-Star%20Schema-336791?style=for-the-badge&logo=postgresql)" alt="PostgreSQL">
<img src="[https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb](https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb)" alt="MongoDB">
<img src="[https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)" alt="Streamlit">
<img src="[https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)" alt="Docker">
</p>
📌 About The Project
An enterprise-grade CRM and Data Engineering pipeline designed to handle hybrid data sources (Relational & NoSQL), process them through robust ETL workflows, and load them into a centralized Data Warehouse structured as a Star Schema for advanced OLAP analytics.
🏗️ System Architecture & Data Flow
[ PostgreSQL (OLTP) ] ──┐
                         ├──> [ Python ETL Pipelines ] ──> [ Data Warehouse (Star Schema) ] ──> [ Streamlit Analytics ]
[ MongoDB (NoSQL) ]    ──┘

📂 Repository Structure
Raiseup_CRM/
│
├── sql/                    # DDL Scripts for Data Warehouse Schema & Partitioning
│   ├── app_users.sql
│   ├── posts.sql
│   ├── users.sql
│   └── partitioned.sql
│
├── screenshots/            # UI Dashboards and System Visuals
│
├── ETL.py                  # Core Extraction, Transformation & Loading logic
├── OLTP_OLAP.py            # Comparative analytics engine
├── app.py                  # Main Streamlit user interface
├── docker-compose.yaml     # Containerized database & service orchestration
└── requirements.txt        # Project dependencies

📊 Data Warehouse Design (Star Schema)
The data warehouse is optimized for analytical queries (OLAP) featuring:
 * Fact Tables: Transactional and activity logs (posts, user actions).
 * Dimension Tables: Master data entities (users, app_users) with optimized indexing and partitioning (sql/partitioned.sql) to scale high-volume queries.
🚀 Getting Started
Prerequisites
 * Python 3.10+
 * Docker & Docker Compose
Installation & Run
 * Clone the repository:
   git clone https://github.com/Ah-Hany/Raiseup_CRM.git
cd Raiseup_CRM

 * Spin up databases using Docker:
   docker-compose up -d

 * Install dependencies:
   pip install -r requirements.txt

 * Run the Streamlit application:
   streamlit run app.py

📸 Screenshots
| Users Analytics | OLTP vs OLAP Dashboard |
|---|---|
|  |  |
🛠️ Tech Stack
 * Languages: Python, SQL
 * Databases: PostgreSQL, MongoDB
 * Orchestration & ETL: Custom Python Pipelines, Docker
 * Visualization: Streamlit
