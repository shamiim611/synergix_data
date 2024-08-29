import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    url = 'https://github.com/shamiim611/synergix_data/upload/main'
    return pd.read_csv(url)

data = load_data()

# Title and description
st.title('Exploratory Data Analysis of Synergix Dataset')
st.write('This Streamlit app visualizes the patterns in the Synergix dataset.')

# Display the dataset
if st.checkbox('Show raw data'):
    st.write(data)

# Distribution plots
st.header('Distribution of Numerical Features')
feature = st.selectbox('Select a feature to plot', data.select_dtypes(include=['float64', 'int64']).columns)
fig, ax = plt.subplots()
sns.histplot(data[feature], kde=True, ax=ax)
st.pyplot(fig)

# Scatter plot between features
st.header('Scatter Plot')
x_axis = st.selectbox('Select X-axis', data.select_dtypes(include=['float64', 'int64']).columns)
y_axis = st.selectbox('Select Y-axis', data.select_dtypes(include=['float64', 'int64']).columns)
fig, ax = plt.subplots()
sns.scatterplot(x=data[x_axis], y=data[y_axis], hue=data['Segment'], ax=ax)
st.pyplot(fig)

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

