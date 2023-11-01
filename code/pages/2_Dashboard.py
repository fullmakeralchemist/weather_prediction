import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

st.set_page_config(page_title="Weather EDA dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv('/home/pi/Desktop/ard-tf-streamlit/code/data/Istanbul Weather Data.csv')

df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d.%m.%Y')

# ---- SIDEBAR ----
st.sidebar.header("Please Select Variables Here:")

# Use multiselect to choose the variables you want to plot
variables = st.sidebar.multiselect(
    "Select Variables to Plot:",
    options=['Rain', 'MaxTemp', 'MinTemp', 'AvgWind', 'AvgHumidity', 'AvgPressure'],
    default=['Rain']
)

# MAIN PAGE
st.title(":bar_chart: Weather Data Dashboard")
st.markdown("###")

# Calculate the average of Rain, MaxTemp, and MinTemp
average_rain = round(df["Rain"].mean(), 2)
average_max_temp = round(df["MaxTemp"].mean(), 2)
average_min_temp = round(df["MinTemp"].mean(), 2)

left_column, center_column, right_column = st.columns(3)

with left_column:
    st.markdown('<span style="font-size: 16px;">Average Rain (mm):</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="font-size: 14px;">{average_rain}</span>', unsafe_allow_html=True)

with center_column:
    st.markdown('<span style="font-size: 16px;">Average Max Temperature (C°):</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="font-size: 14px;">{average_max_temp}</span>', unsafe_allow_html=True)

with right_column:
    st.markdown('<span style="font-size: 16px;">Average Min Temperature (C°):</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="font-size: 14px;">{average_min_temp}</span>', unsafe_allow_html=True)

# Create a line chart for the selected time series data
if variables:
    fig_time_series = px.line(df, x="DateTime", y=variables, title="Time Series Data")
    st.plotly_chart(fig_time_series)
else:
    st.warning("No data available for the selected variables.")

# Use selectbox to choose the variable you want to plot
selected_variable = st.sidebar.selectbox(
    "Select Variable:",
    options=['Rain', 'MaxTemp', 'MinTemp', 'AvgWind', 'AvgHumidity', 'AvgPressure'],
    index=0  # Default to 'Rain'
)

# MAIN PAGE
st.subheader(":bar_chart: Averages by month")
st.markdown("##")

# Calculate the average of the selected variable by month
if selected_variable:
    # Calculate the average by month
    average_by_month = df.groupby(df['DateTime'].dt.month)[selected_variable].mean().reset_index()
    
    # Get month names based on the numeric month values
    average_by_month['Month'] = average_by_month['DateTime'].apply(lambda x: calendar.month_name[x])
    
    # Create a bar plot using Plotly
    fig_bar_plot = px.bar(average_by_month, x='Month', y=selected_variable, title=f'Average {selected_variable} by Month')
    st.plotly_chart(fig_bar_plot)
else:
    st.warning("Please select a variable to plot.")

df['Month'] = df['DateTime'].dt.month

# ---- SIDEBAR ----
st.sidebar.header("Please Select Rainfall Categories to Plot:")

# Use multiselect to choose the rainfall categories you want to plot
rainfall_categories = st.sidebar.multiselect(
    "Select Rainfall Categories:",
    options=['Light Rain', 'Moderate Rain', 'Heavy Rain'],
    default=['Light Rain']
)

# MAIN PAGE
st.title(":bar_chart: Weather Data Dashboard")
st.markdown("##")

# Define thresholds for different levels of rainfall intensity
moderate_threshold = 0.5
heavy_threshold = 4.0

# Create columns for different storm categories
df['Light Rain'] = (df['Rain'] > 0) & (df['Rain'] <= moderate_threshold)
df['Moderate Rain'] = (df['Rain'] > moderate_threshold) & (df['Rain'] <= heavy_threshold)
df['Heavy Rain'] = (df['Rain'] > heavy_threshold)


# Plot the count of storm days for the selected categories per month
if rainfall_categories:
    # Melt the DataFrame for better visualization
    storm_counts = df.groupby('Month')[rainfall_categories].sum().reset_index()
    storm_counts_melted = pd.melt(storm_counts, id_vars='Month', var_name='Rain Category', value_name='Count')
    
    # Create a bar plot using Plotly Express with 'barmode' set to 'group'
    fig_bar_plot = px.bar(storm_counts_melted, x='Month', y='Count', color='Rain Category',
                          title='Monthly Storm Counts by Rain Category', barmode='group')
    st.plotly_chart(fig_bar_plot)
else:
    st.warning("Please select at least one rainfall category to plot.")