import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
conn = sqlite3.connect("/Users/joshrandhawa/Desktop/gym-analytics-dashboard/data/gym.db")
df = pd.read_sql("SELECT * FROM gym_members_cleaned;", conn)
conn.close()

# Title
st.title("Gym Membership Analytics Dashboard")

# Example: Gender distribution


# Example: Interactive filter
membership_type = st.selectbox("Select Group Type", df['attend_group_lesson'].unique())
filtered_df = df[df['attend_group_lesson'] == membership_type]
age_range = st.selectbox("Select max age", df['age'].unique())
filtered_df = filtered_df[filtered_df['age'] <= age_range]
st.dataframe(filtered_df)

fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='gender', ax=ax)
st.pyplot(fig)
