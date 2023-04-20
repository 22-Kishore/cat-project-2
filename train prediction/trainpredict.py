import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Set the title of the app
st.title('All Indian Trains')

# Add an introduction to the app
st.write('This app provides an overview of all Indian trains, including train names, starting and ending stations, and the number of trains between each starting and ending station. Use the filters and search bar to find specific trains or stations.')

# Load the dataset into a pandas DataFrame
df = pd.read_csv("./All_Indian_Trains.csv")

# Print the first five rows of the DataFrame
st.header('Train Data')
st.dataframe(df.head())

# Print data types and null values
st.header('Data Types and Null Values')
st.write(df.dtypes)
st.write(df.isnull().sum())

# Print summary statistics
st.header('Summary Statistics')
st.write(df.describe())

# Add a sidebar with options for the user
st.sidebar.header('Filter Data')
train_name = st.sidebar.text_input('Search Train Name')
start_station = st.sidebar.selectbox('Filter by Starting Station', df['Starts'].unique())
end_station = st.sidebar.selectbox('Filter by Ending Station', df['Ends'].unique())

# Filter the data based on the user's inputs
filtered_df = df[(df['Starts'] == start_station) & (df['Ends'] == end_station)]
if train_name != '':
    filtered_df = filtered_df[filtered_df['Train name'].str.contains(train_name)]

# Print the filtered data
st.header('Filtered Data')
st.dataframe(filtered_df)

# Create a bar chart of the Train name distribution
st.header('Train Name Distribution')
train_name_count = df['Train name'].value_counts()
st.bar_chart(train_name_count)

# Create a bar chart of the number of trains starting at each station
st.header('Number of Trains Starting at Each Station')
starts_count = df['Starts'].value_counts()
st.bar_chart(starts_count)


