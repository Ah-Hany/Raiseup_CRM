import psycopg2
import streamlit as st
from datetime import datetime, time
import bcrypt
import os
from dotenv import load_dotenv
from kafka_producer import send_user_event

load_dotenv()

# ==================================================
# PAGE AUTHORIZATION
# ==================================================

if not st.session_state.get("logged_in", False):
    st.error("You must login first")
    st.stop()

role = st.session_state.get("role")

if role != "super-admin":
    st.error("You don't have permission to access this page.")
    st.stop()

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
# ADD USER
# ==================================================

def add_user(name, email, password, created_at):

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO users_partitioned
            (
                username,
                email,
                password,
                created_at,
                updated_at
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                name,
                email,
                password_hash,
                created_at,
                created_at
            )
        )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# ==================================================
# PAGE
# ==================================================

st.title("PostgreSQL Partitioning")

st.write(f"Current Role: **{role}**")

# ==================================================
# USER FORM
# ==================================================

name = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
created_at = st.date_input("Created At")

# ==================================================
# ADD USER
# ==================================================

if st.button("Add User"):

    if not name or not email or not password:
        st.warning("Please fill all fields.")

    else:

        try:

            add_user(
                name,
                email,
                password,
                datetime.combine(created_at, time.min)
            )

            st.success("User added successfully.")

            # Send event to Kafka
            try:
                st.info("Attempting to send Kafka event...")
                send_user_event(name, email, "user_added")
                st.success("Kafka event sent successfully on UI.")

            except Exception as kafka_error:
                st.error(f"KAFKA ERROR: {kafka_error}")

        except Exception as e:
            st.error(f"Error: {e}")