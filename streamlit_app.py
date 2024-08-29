import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    url = 'https://github.com/shamiim611/synergix_data/upload/main'
    return pd.read_csv(url,on_bad_lines='skip')

data = load_data()

# Title and description
st.title('Exploratory Data Analysis of Synergix Dataset')
st.write('This Streamlit app visualizes the patterns in the Synergix dataset.')

# Display the dataset
if st.checkbox('Show raw data'):
    st.write(data)



# Correlation heatmap
st.header('Correlation Heatmap')
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Box plot for segments
st.header('Box Plot of Features by Segment')
boxplot_feature = st.selectbox('Select a feature for box plot', data.select_dtypes(include=['float64', 'int64']).columns)
fig, ax = plt.subplots()
sns.boxplot(x='Segment', y=boxplot_feature, data=data, ax=ax)
st.pyplot(fig)

