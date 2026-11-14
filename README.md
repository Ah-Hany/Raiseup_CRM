<div align="center">

# 🚀 Raiseup CRM
### CRM & Data Engineering Platform

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248?logo=mongodb&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-231F20?logo=apachekafka&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

</div>

A CRM and Data Engineering project integrating PostgreSQL, MongoDB, Python ETL, Kafka, and Streamlit for data management and analytics.

## 📊 Project Screenshots

| Users Analytics | OLTP vs OLAP |
|:---:|:---:|
| ![Users Analytics](screenshots/users_analytics.png) | ![OLTP vs OLAP](screenshots/oltp_vs_olap_dashboard.png) |

| ETL Pipeline | Kafka Integration |
|:---:|:---:|
| ![ETL Pipeline](screenshots/etl_pipeline.png) | ![Kafka](screenshots/add_user_kafka.png) |

<details>
<summary>🔐 CRM Login</summary>

![CRM Login](screenshots/crm_login.png)

</details>

## 🏗️ Architecture

```mermaid
flowchart LR
    A[(PostgreSQL)] --> C[Python ETL]
    B[(MongoDB)] --> C
    C --> D[(Data Warehouse)]
    D --> E[OLTP vs OLAP]
    E --> F[Streamlit Dashboard]
```

## 📁 Project Structure

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
├── dags/
│   └── crm_test_dag.py
│
├── app.py
├── add_user_page.py
├── chatbot.py
├── crud.py
├── ETL.py
├── hadoop.py
├── Mongodb.py
├── OLTP_OLAP.py
├── Orchestrations.py
├── partitioned.py
├── postgres.py
│
├── docker-compose.yaml
└── requirements.txt
```

## 🛠️ Tech Stack

- Python & SQL
- PostgreSQL
- MongoDB
- Apache Kafka
- ETL & Data Warehousing
- Star Schema
- PySpark
- Streamlit
- Docker & Docker Compose
- Apache Airflow

## ▶️ Run Locally

```bash
git clone https://github.com/Ah-Hany/Raiseup_CRM.git

cd Raiseup_CRM

docker compose up -d

pip install -r requirements.txt

streamlit run app.py
```

## 👨‍💻 Author

**Ahmed Hany**

- GitHub: [Ah-Hany](https://github.com/Ah-Hany)
- LinkedIn: [Ahmed Hany](https://www.linkedin.com/in/ahmed-hany-b30692431/)

