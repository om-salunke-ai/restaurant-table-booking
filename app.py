import streamlit as st
import pandas as pd
import os


# Title
st.title("🍽️ Restaurant Table Booking System")
st.markdown("## Welcome to Smart Restaurant Booking System 🍴")
st.write("Book your table easily and avoid waiting!")
st.divider()


# File Name 
file = "booking.csv"


# Load or Create Data
if os.path.exists(file):
    df = pd.read_csv(file)
else:
    df = pd.DataFrame(columns=["Name", "Table", "Time"])


# Input Fields
name = st.text_input("Enter your name")
table = st.selectbox("Select Table Number", [1, 2, 3, 4, 5])
time = st.selectbox("Select Time Slot", ["7PM", "8PM", "9PM"])


# Available Tables
st.subheader("🟢 Available Tables")

booked_tables = df[df["Time"] == time]["Table"].tolist()
all_tables = [1, 2, 3, 4, 5]

available_tables = [t for t in all_tables if t not in booked_tables]

st.write("Available Tables:", available_tables)


# Booking Logic
if st.button("Book Table", key="book_btn"):
    if name.strip() == "":
        st.warning("⚠️ Please enter your name!")

    elif table not in available_tables:
        st.error("❌ This table is already booked for this time!")

    else:
        new_data = pd.DataFrame([[name, table, time]], columns=["Name", "Table", "Time"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(file, index=False)
        st.success("✅ Booking Successful!")
        st.rerun()


# Show Bookings
st.subheader("📋 All Bookings")
st.dataframe(df)


# DELETE ONE BOOKING 
st.subheader("❌ Delete a Booking")

if not df.empty:
    # Create display labels without modifying the original dataframe
    display_labels = df["Name"].astype(str) + " | Table " + df["Table"].astype(str) + " | " + df["Time"].astype(str)

    selected = st.selectbox("Select booking to delete", display_labels)

    if st.button("Delete Selected Booking", key="delete_one_btn"):
        idx = display_labels[display_labels == selected].index
        df = df.drop(idx).reset_index(drop=True)
        df.to_csv(file, index=False)
        st.success("Selected booking deleted!")
        st.rerun()

else:
    st.info("No bookings available to delete.")


# DELETE ALL BOOKINGS 
st.subheader("🗑️ Clear All Bookings")

if st.button("Delete All Bookings", key="delete_all_btn"):
    df = pd.DataFrame(columns=["Name", "Table", "Time"])
    df.to_csv(file, index=False)
    st.success("All bookings cleared!")
    st.rerun()



# python -m streamlit run app.py
