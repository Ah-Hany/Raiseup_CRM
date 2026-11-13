import psycopg2
from pymongo import MongoClient
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import os
from dotenv import load_dotenv

# ============================================================
# 1. PostgreSQL Connection
# ============================================================

load_dotenv()

pg_conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

pg_cursor = pg_conn.cursor()


# ============================================================
# 2. MongoDB Connection
# ============================================================

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["crm"]

users_collection = db["users"]

posts_collection = db["posts"]


# ============================================================
# 3. Extract - PostgreSQL
# ============================================================

import pandas as pd
import streamlit as st

st.subheader("Top Users - Most posts in the last 6 Month")

try:
    pg_cursor.execute("""
        SELECT u.username AS name, COUNT(p.id) AS posts_count 
        FROM public.app_users u
        LEFT JOIN public.posts p ON u.id = p.user_id
        GROUP BY u.username
        ORDER BY posts_count DESC;
    """)
    sql_users = pg_cursor.fetchall()

    if sql_users:
        df = pd.DataFrame(sql_users, columns=["name", "posts_count"])
        df["posts_count"] = pd.to_numeric(df["posts_count"], errors="coerce").fillna(0)
        st.bar_chart(df.set_index("name"))
    else:
        st.warning("No data available to display the chart.")

except Exception as e:
    st.error(f"Error loading chart data: {e}")




# ============================================================
# 4. Extract - MongoDB Users
# ============================================================

mongo_users = list(
    users_collection.find(
        {},
        {
            "_id": 1,
            "name": 1,
            "email": 1,
            "age": 1,
            "created_at": 1,
            "updated_at": 1
        }
    )
)


# ============================================================
# 5. Extract - MongoDB Posts
# ============================================================

mongo_posts = list(
    posts_collection.find(
        {},
        {
            "_id": 1,
            "user_id": 1,
            "title": 1,
            "content": 1,
            "created_at": 1,
            "updated_at": 1
        }
    )
)


all_emails = set()


for user in sql_users:

    user_id = user[0]

    username = str(user[1]).strip().lower()

    if len(user) > 2 and user[2]:
        email = str(user[2]).strip().lower()
    else:
        email = ""

    all_emails.add(email)


# --------------------------------------------------------
# Posts From the last 6 month
# --------------------------------------------------------

six_month_ago = (
    datetime.now() -
    timedelta(days=182)
)


top_users = list(
    posts_collection.aggregate([

        {
            # 1. Filter Posts From the last 6 month

            "$match": {

                "created_at": {

                    "$gte": six_month_ago

                }

            }

        },

        # 2. Group posts by user

        {

            "$group": {

                "_id": "$user_id",

                "posts_count": {

                    "$sum": 1

                }

            }

        },

        # 3. Sort from The Highest to lowest

        {

            "$sort": {

                "posts_count": -1

            }

        },

        # 4. Get top 10 users

        {

            "$limit": 10

        },

        # 5. Join with users collections

        {

            "$lookup": {

                "from": "users",

                "localField": "_id",

                "foreignField": "_id",

                "as": "user"

            }

        },

        # 6. convert user array to object

        {

            "$unwind": "$user"

        },

        # 7. SELECT FILEDS

        {

            "$project": {

                "_id": 0,

                "name": "$user.name",

                "email": "$user.email",

                "posts_count": 1

            }

        }

    ])
)


# --------------------------------------------------------
# Statistics
# --------------------------------------------------------

sql_users_count = len(sql_users)

mongo_users_count = len(mongo_users)

total_users = (
    sql_users_count +
    mongo_users_count
)

total_unique_users = len(all_emails)


st.title(
    "Users Integration Dashboard"
)


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "SQL Users",
        sql_users_count
    )


with col2:

    st.metric(
        "NoSQL Users",
        mongo_users_count
    )


with col3:

    st.metric(
        "total Users",
        total_users
    )


with col4:

    st.metric(
        "total unique Users",
        total_unique_users
    )


with col5:

    st.metric(
        "total Posts ",
        len(mongo_posts)
    )


st.divider()


st.subheader(
    "Top Users - Most post in the last 6 Month "
)


df = pd.DataFrame(
    top_users
)



import pandas as pd

if sql_users:
    df = pd.DataFrame(sql_users, columns=["name", "posts_count"])
    df["posts_count"] = pd.to_numeric(df["posts_count"], errors="coerce").fillna(0)
    st.bar_chart(df.set_index("name"))
else:
    st.warning("No data available to display the chart.")


st.dataframe(
    df,
    use_container_width=True
)