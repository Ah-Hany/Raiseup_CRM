<div align="center">

# 🚀 Raiseup CRM
### A CRM & Data Engineering Platform

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248?logo=mongodb&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

</div>

A CRM application that combines **PostgreSQL, MongoDB, Python ETL, and Streamlit** to manage user data and explore analytics.

## 📊 Project Screenshots

| Users Analytics | OLTP vs OLAP |
|:---:|:---:|
| ![Users Analytics](screenshots/users_analytics.png) | ![OLTP vs OLAP](screenshots/oltp_vs_olap_dashboard.png) |

| ETL Pipeline | Kafka Integration |
|:---:|:---:|
| ![ETL Pipeline](screenshots/etl_pipeline.png) | ![Kafka Integration](screenshots/add_user_kafka.png) |

<details>
<summary>Login Screen</summary>

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

## 🧰 Tech Stack

- **Languages:** Python, SQL
- **Databases:** PostgreSQL, MongoDB
- **Data Engineering:** ETL, Data Warehousing, Star Schema
- **Streaming:** Apache Kafka
- **Processing:** PySpark
- **Dashboard:** Streamlit
- **Infrastructure:** Docker Compose

## 📁 Project Structure

```text
Raiseup_CRM/
├── sql/
│   ├── app_users.sql
│   ├── posts.sql
│   ├── users.sql
│   └── partitioned.sql
├── screenshots/
├── ETL.py
├── OLTP_OLAP.py
├── app.py
├── docker-compose.yaml
└── requirements.txt
```

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

- [GitHub](https://github.com/Ah-Hany)
- [LinkedIn](https://www.linkedin.com/in/ahmed-hany-b30692431/)
-
