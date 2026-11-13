import psycopg2
import streamlit as st
from datetime import datetime
import math
import pandas as pd
import os
from dotenv import load_dotenv

# =========================
# PostgreSQL Connection
# =========================

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()


# query = """ SELECT * FROM users_partitioned ; """

# Parent Table


# query = """ SELECT * FROM users_partitioned
# WHERE created_at >= '2026-01-01'
# AND created_at < '2027-01-01' ; """

# Partition Pruning


query = """
SELECT
    tableoid::regclass AS partition_name,
    *
FROM users_partitioned ;
"""


# Partition tables


users_df = pd.read_sql(
    query,
    conn
)


partition_count = (

    users_df

    .groupby(
        "partition_name"
    )

    .size()

    .reset_index(
        name="users_count"
    )

)


selected_partition = st.selectbox(
    "Select Partition",
    users_df[
        "partition_name"
    ].unique()
)


selected_users = users_df[
    users_df["partition_name"]
    == selected_partition
]


st.title(
    "PostgreSQL  Partitioning"
)


st.subheader(
    f"Data from {selected_partition}"
)


st.dataframe(
    selected_users,
    use_container_width=True
)


st.header(
    "Users per Parition"
)


st.dataframe(
    partition_count,
    use_container_width=True
)


st.dataframe(
    users_df,
    use_container_width=True
)


st.bar_chart(
    partition_count,
    x="partition_name",
    y="users_count"
)