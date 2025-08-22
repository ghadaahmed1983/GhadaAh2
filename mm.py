import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# البيانات
data = {
    'Name': ['John', 'Sara', 'Ali', 'Mona', 'Omar', 'Laila', 'Adam'],
    'Age':  [25, 30, 22, 28, 35, 40, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'Chicago']
}
df = pd.DataFrame(data)

st.title("👥 Personal Info Dashboard")
st.subheader("Data Table")
st.dataframe(df)

st.subheader("📈 Line Chart (Age by Name)")
st.line_chart(df, x="Name", y="Age")

st.subheader("🥧 Pie Chart (People by City)")
city_counts = df["City"].value_counts()

fig, ax = plt.subplots()
ax.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis("equal")
st.pyplot(fig)