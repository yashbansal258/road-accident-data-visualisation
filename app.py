
import streamlit as st
import pandas as pd


class RoadAccidentDashboard:

    def __init__(self):
        self.data = pd.read_csv(
            "road-accidents-2024-states-road-accidents.csv"
        )

    def home(self):
        st.title("Road Accident Data Visualization")
        st.write("Welcome to Road Accident Dashboard")

        st.subheader("Total Records")
        st.write(len(self.data))

        st.subheader("Road Accident Data")
        st.dataframe(self.data.head())

    def show_data(self):
        st.header("View Road Accident Data")
        st.dataframe(self.data)

    def search_data(self):
        st.header("Search Road Accident Data")

        column = st.selectbox(
            "Select Column",
            self.data.columns
        )

        value = st.text_input("Enter Search Value")

        if value:
            result = self.data[
                self.data[column].astype(str).str.contains(
                    value, case=False, na=False
                )
            ]

            st.dataframe(result)

    def download_data(self):
        st.header("Download Data")

        csv = self.data.to_csv(index=False)

        st.download_button(
            "Download CSV File",
            csv,
            "road_accident_data.csv",
            "text/csv"
        )

    def about(self):
        st.header("About Project")
        st.write(
            "This project displays and explores "
            "road accident data using Python, Pandas "
            "and Streamlit."
        )

    def run(self):
        st.sidebar.title("Menu")

        choice = st.sidebar.selectbox(
            "Choose Page",
            ["Home", "View Data", "Search Data",
             "Download Data", "About"]
        )

        if choice == "Home":
            self.home()

        elif choice == "View Data":
            self.show_data()

        elif choice == "Search Data":
            self.search_data()

        elif choice == "Download Data":
            self.download_data()

        elif choice == "About":
            self.about()


app = RoadAccidentDashboard()
app.run()
