import psycopg2
import streamlit as st
import bcrypt
import os
from dotenv import load_dotenv
from kafka_producer import send_user_event
import json

load_dotenv()

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="RaiseUp - CRM",
    layout="wide"
)







# ==================================================
# POSTGRESQL CONNECTION
# ==================================================

def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


# ==================================================
# LOGIN FUNCTION
# ==================================================

def login(email, password):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """         SELECT id, username, email, role, password
            FROM app_users
            WHERE email = %s
        """

        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if not user:
            return None

        stored_password = user[4]
        password_bytes = password.encode("utf-8")


        if stored_password.startswith(("$2a$", "$2b$", "$2y$")):
            if bcrypt.checkpw(
                password_bytes,
                stored_password.encode("utf-8")
            ):
                return user[:4]

            return None


        if password == stored_password:
            password_hash = bcrypt.hashpw(
                password_bytes,
                bcrypt.gensalt()
            ).decode("utf-8")

            cursor.execute(
                """
                UPDATE app_users
                SET password = %s
                WHERE id = %s
                """,
                (password_hash, user[0])
            )

            connection.commit()
            return user[:4]

        return None

    finally:
        cursor.close()
        connection.close()


# ==================================================
# AUTHENTICATION
# ==================================================

if not st.session_state.get(
    "logged_in",
    False
):

    st.title("Login")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )


    # ==================================================
    # LOGIN BUTTON
    # ==================================================

    if st.button("Login"):

        user = login(
            email,
            password
        )


        # ==================================================
        # LOGIN SUCCESS
        # ==================================================

        if user:

            st.session_state["logged_in"] = True

            st.session_state["user_id"] = user[0]

            st.session_state["username"] = user[1]

            st.session_state["email"] = user[2]

            st.session_state["role"] = user[3]

            # ارسال الإيفنت للكافكا فور تسجيل الدخول بنجاح
            send_user_event(user[1], user[2])

            st.success(
                "Login Successfully"
            )

            st.rerun()


        # ==================================================
        # LOGIN FAILED
        # ==================================================

        else:

            st.error(
                "Invalid Email or Password"
            )


# ==================================================
# AUTHORIZED APPLICATION
# ==================================================

else:

    # ==================================================
    # CURRENT USER
    # ==================================================

    username = st.session_state["username"]

    role = st.session_state["role"]


    # ==================================================
    # SIDEBAR USER INFORMATION
    # ==================================================

    st.sidebar.write(
        f"Welcome {username}"
    )

    st.sidebar.write(
        f"Role: {role}"
    )


    # ==================================================
    # LOGOUT
    # ==================================================

    if st.sidebar.button("Logout"):

        st.session_state.clear()

        st.rerun()


    # ==================================================
    # PAGES
    # ==================================================

    mongo_page = st.Page(
        "Mongodb.py",
        title="NoSQL Data",
        icon="🍃"
    )


    postgres_page = st.Page(
        "postgres.py",
        title="SQL Data",
        icon="🐘"
    )


    etl_page = st.Page(
        "ETL.py",
        title="ETL"
    )


    oltp_olap_page = st.Page(
        "OLTP_OLAP.py",
        title="OLTP VS OLAP"
    )


    hadoop_demo = st.Page(
        "hadoop.py",
        title="Hadoop Demo"
    )


    partitioned = st.Page(
        "partitioned.py",
        title="Partitioned"
    )


    add_user_pg = st.Page(
        "add_user_page.py",
        title="Add User PG"
    )


    # ==================================================
    # COMMON PAGES
    # ==================================================

    pages = [

        mongo_page,

        postgres_page,

        etl_page,

        oltp_olap_page,

        hadoop_demo,

        partitioned,

    ]


    # ==================================================
    # ADMIN ONLY PAGE
    # ==================================================

    if role == "super-admin":

        pages.append(
            add_user_pg
        )


    # ==================================================
    # NAVIGATION
    # ==================================================

    pg = st.navigation(
        {
            "Database": pages
        }
    )


    # ==================================================
    # RUN APPLICATION
    # ==================================================

    pg.run()