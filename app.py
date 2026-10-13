import pandas as pd
import streamlit as st
class RoadAccidentDashboard:
   def __init__(self,file_path):
       self.file_path = file_path
       self.data = none
   def load_data(self):
       try:
           self.data =
pd.read_csv(self.file_path)
            return true
          except file not found error:
              st.error("csv file nahi mili file name check kren.")
              return false
          except pd.errors.emptydata error:
              st.error("csv file khaali hai.")
              return false
 
    def show_tittle(self):
        st.title("road accident data visualisation")
        st.write("road accident data basic analysis")
    def show_summary(self):
         st.subheader("dataset summary")
         col1,col2= st.column(2)
         col1.metric("total rows",self.data.shapoe[0])
         col2.metric("total columns",self.data.shape[1]
    def show_data(self):
        st.subheadher(self.data.head(10))
    def show_columns(self):
        st.subheader("dataset columns")
st.write(self.data.columns.tolist())
    def run(self):
        self.show_title()
        if self.load_data():
             self.show_summary()
             self.show_data()
            self.show_columns()
if __name__++""main__"":
     dashboard= RoadAccidentDashboard( 
 "road-accidents-2024-states-road-accidents.csv"
 )
  dashbord.run()
      

   
