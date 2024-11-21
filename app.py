import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (replace with actual file path or file uploader)
@st.cache
def load_data():
    # Replace 'path_to_your_file.csv' with the correct path or allow the user to upload the file
    df = pd.read_csv('2023_Walk___Bike_Count_Data.csv')  # Use appropriate file path
    return df

# Load data
df = load_data()

# Streamlit App Interface
st.title('Los Angeles Walking, Biking, and Scooter Data Analysis')

# Show the raw data
if st.checkbox('Show raw data'):
    st.write(df)

# User input: Select location for analysis
location = st.selectbox('Select a location', df['Full Location Names 2023'].unique())

# Filter data by selected location
selected_location_data = df[df['Full Location Names 2023'] == location]

# Display the counts for pedestrians, bikes, and scooters
ped_count = selected_location_data['Ped_Total'].sum()
bike_count = selected_location_data['Bike_Total'].sum()
scooter_count = selected_location_data['Scooter_Total'].sum()

st.write(f"### Selected Location: {location}")
st.write(f"**Total Pedestrians:** {ped_count}")
st.write(f"**Total Bikes:** {bike_count}")
st.write(f"**Total Scooters:** {scooter_count}")

# Create bar plots for Pedestrian, Bike, and Scooter counts
st.subheader('Counts by Category')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Pedestrian Plot
sns.barplot(x=['Pedestrians'], y=[ped_count], ax=ax[0], color='b')
ax[0].set_title('Pedestrian Counts')
ax[0].set_ylim(0, max(ped_count, bike_count, scooter_count) + 50)  # Adjust the scale to match the max value

# Bike Plot
sns.barplot(x=['Bikes'], y=[bike_count], ax=ax[1], color='g')
ax[1].set_title('Bike Counts')
ax[1].set_ylim(0, max(ped_count, bike_count, scooter_count) + 50)

# Scooter Plot
sns.barplot(x=['Scooters'], y=[scooter_count], ax=ax[2], color='r')
ax[2].set_title('Scooter Counts')
ax[2].set_ylim(0, max(ped_count, bike_count, scooter_count) + 50)

# Show the plot
st.pyplot(fig)

# Show summary statistics for selected location
st.subheader('Summary Statistics')
summary_stats = selected_location_data[['Ped_Total', 'Bike_Total', 'Scooter_Total']].describe()
st.write(summary_stats)
