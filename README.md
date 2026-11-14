# 🚀 Raiseup CRM | Data Engineering Platform

<p align="center">
  <img src="screenshots/crm_login.png" width="100%" alt="CRM Login">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker">
</p>

## 📌 About

A CRM and Data Engineering platform integrating PostgreSQL and MongoDB through Python-based ETL pipelines, with interactive Streamlit dashboards.

## 🏗️ Architecture

```text
PostgreSQL ──┐
             ├──> Python ETL ──> Data Warehouse
MongoDB ─────┘                       |
                              OLTP vs OLAP
                                     |
                              Streamlit Dashboard
```

## 📂 Repository Structure

```text
Raiseup_CRM/
│
├── sql/
│   ├── app_users.sql
│   ├── posts.sql
│   ├── users.sql
│   └── partitioned.sql
│
├── screenshots/
│   ├── crm_login.png
│   ├── users_analytics.png
│   ├── oltp_vs_olap_dashboard.png
│   ├── etl_pipeline.png
│   └── add_user_kafka.png
│
├── ETL.py
├── OLTP_OLAP.py
├── app.py
├── docker-compose.yaml
└── requirements.txt
```

## 📸 Project Screenshots

| Users Analytics | OLTP vs OLAP |
|---|---|
| ![Users](screenshots/users_analytics.png) | ![Analytics](screenshots/oltp_vs_olap_dashboard.png) |

| ETL Pipeline | Kafka Integration |
|---|---|
| ![ETL](screenshots/etl_pipeline.png) | ![Kafka](screenshots/add_user_kafka.png) |

## 🛠️ Tech Stack

- Python & SQL
- PostgreSQL & MongoDB
- ETL & Data Warehousing
- Star Schema
- PySpark
- Streamlit
- Docker

## 🚀 Getting Started

```bash
git clone https://github.com/Ah-Hany/Raiseup_CRM.git
cd Raiseup_CRM
docker-compose up -d
pip install -r requirements.txt
streamlit run app.py
```

## 👨‍💻 Author

**Ahmed Hany**

- GitHub: [Ah-Hany](https://github.com/Ah-Hany)
- LinkedIn: [Ahmed Hany](https://www.linkedin.com/in/ahmed-hany-b30692431/)
-
