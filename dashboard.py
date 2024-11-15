import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os


# Load data
@st.cache_resource
def load_data():
    # Adjust the file path as necessary
    df = pd.read_csv('data/bulk_predictions.csv')
    return df


def dashboard_page():
    """Create the dashboard page for the Telco Churn project."""
    st.title("Telco Churn Dashboard")
    st.sidebar.title("The Dashboard View")
    st.sidebar.write("These shows the insight generated from the predictions made.")

    # Display data
    st.header("Data Overview")
    st.write("Here is a quick summary of the dataset")

    data = load_data()
    st.write(data.head())


    # Summary Statistics
    st.header("Churn Overview")
    churn_count = data['Predictions'].value_counts()
    st.write(f"Total Customers: {data.shape[0]}")
    st.write(f"Churned Customers: {churn_count.get(1, 0)}")
    st.write(f"Non-Churned Customers: {churn_count.get(0, 0)}")


     # 1. Pie chart for Churn Distribution
    st.subheader("Churn Distribution")
    pie_data = data['Predictions'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(pie_data, labels=['Not Churned', 'Churned'], autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)


    # 2. Churn by Contract Type
    st.subheader("Churn Rate by Contract Type")
    contract_churn = data.groupby('Contract')['Predictions'].value_counts(normalize=True).unstack()
    contract_churn_plot = contract_churn.plot(kind='bar', stacked=True)
    plt.title('Churn Rate by Contract Type')
    plt.xlabel('Contract Type')
    plt.ylabel('Proportion')
    plt.legend(title='Churn Status', labels=['Not Churned', 'Churned'])
    st.pyplot(contract_churn_plot.figure)

    # 3. Monthly Charges Distribution
    st.subheader("Monthly Charges Distribution")
    fig2 = px.histogram(data, x='MonthlyCharges', color='Predictions', barmode='overlay', 
                         title='Monthly Charges Distribution by Churn Status',
                         labels={'MonthlyCharges': 'Monthly Charges', 'Predictions': 'Churn Status'})
    st.plotly_chart(fig2)

     # Additional Insights
    st.header("Additional Insights")

    # 4. Average Monthly Charges by Churn Status
    st.subheader("Average Monthly Charges by Churn Status")
    avg_monthly_charges = data.groupby('Predictions')['MonthlyCharges'].mean().reset_index()
    avg_fig = plt.figure()
    sns.barplot(x='Predictions', y='MonthlyCharges', data=avg_monthly_charges)
    plt.title('Average Monthly Charges by Churn Status')
    plt.xticks(ticks=[0, 1], labels=['Not Churned', 'Churned'])
    st.pyplot(avg_fig)

    # 5. MonthlyCharges by Gender
    st.subheader("MonthlyCharges by Gender")
    gender_monthly_charge = data.groupby('gender')['MonthlyCharges'].mean().reset_index()
    gender_fig = plt.figure()
    sns.barplot(x='gender', y='MonthlyCharges', data=gender_monthly_charge)
    plt.title('MonthlyCharges by Gender')
    st.pyplot(gender_fig)

     # 6. Total Charges vs. Churn Status
    st.subheader("Total Charges vs. Churn Status")
    fig3 = px.scatter(data, x='TotalCharges', y='Predictions', color='Predictions',
                      title='Total Charges vs. Churn Status',
                      labels={'TotalCharges': 'Total Charges', 'Churn': 'Churn Status'})
    st.plotly_chart(fig3)


    # Plot correlation

    st.subheader("Correlation Heatmap")
    corr = data[["tenure", "TotalCharges"]].corr()
    plt.figure(figsize=(10,6))
    sns.heatmap(corr, annot=True, cmap ="coolwarm")
    st.pyplot(plt)


# Run the dashboard page
if __name__ == "__main__":
    dashboard_page()