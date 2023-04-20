import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Set the title of the app
st.title('All Indian Trains')

# Add an introduction to the app
st.write('This app provides an overview of all Indian trains, including train names, starting and ending stations, and the number of trains between each starting and ending station. Use the filters and search bar to find specific trains or stations.')

# Load the dataset into a pandas DataFrame
df = pd.read_csv("E:\\6thsem\\data mining\\All_Indian_Trains.csv")

# Convert the "Count" column to int type to fix Arrow serialization error
df['Count'] = df['Count'].astype('int')

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

# Group data by starts and ends
grouped_data = df.groupby(['Starts', 'Ends']).size().reset_index(name='Count')

# Create a bar chart of the grouped data
st.header('Train Count by Route')
st.bar_chart(grouped_data, x='Starts', y='Count', color='Ends')

# Add a new column called Route
df['Route'] = df['Starts'] + '-' + df['Ends']
st.dataframe(df.head())

# Save the updated dataframe to a pickle file
with open('all_indian_trains.pkl', 'wb') as f:
    pickle.dump(df, f)
