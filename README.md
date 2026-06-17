# 🍽️ Restaurant Table Booking System

A simple table booking app I built using Python and Streamlit for my 
first-year B.Sc. CS project at Vishwakarma University, Pune.

The idea was to replace the typical "just call the restaurant" approach 
with a small web app where customers can book, view, and cancel table reservations.

---

## What it does

- Book a table by entering your name, picking a table (1–5) and a time slot
- Shows which tables are still free for the selected time
- Lists all current bookings
- Delete one booking or clear everything at once
- All data is saved in a local `booking.csv` file — no database needed

---

## Built with

- **Python** + **Streamlit** — for the entire frontend and logic
- **Pandas** — to read/write the CSV
- **CSV file** — simple local storage that works without any setup

---

## Run it locally

```bash
git clone https://github.com/om-salunke-ai/restaurant-table-booking.git
cd restaurant-table-booking
pip install streamlit pandas
python -m streamlit run app.py
```

Opens at `http://localhost:8501`

---


## About

Made by **Om Salunke** — CS student at Vishwakarma University, Pune.  
This was a university project but I also used it to learn how Streamlit 
handles state and CSV-based persistence.

GitHub: [@om-salunke-ai](https://github.com/om-salunke-ai)

