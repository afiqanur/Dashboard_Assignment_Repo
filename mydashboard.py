import streamlit as st
import numpy as np
import pandas as pd

st.header("Student Performance in Examination ")
st.subheader('This is a random data about Students Performance during examination.')
with st.expander("See explanation"):
   st.write("""
         The examination was held during Spring season. 
         """)
   col1, col2, col3 = st.columns(3)
   col1.metric("Temperature", "70 °F", "1.6 °F")
   col2.metric("Wind", "10 mph", "-7%")
   col3.metric("Humidity", "86%", "4%") 
  
st.markdown('Remember that : Life is **the most difficult examination**.')



option = st.sidebar.selectbox(
    'Select the data visualization',
     ['Successful Students','Failure Students','Overall Performances'])

if option=='Successful Students':
    chart_data = pd.DataFrame(
    np.random.randn(90, 3),
    columns=['University A', 'University B', 'University C'])

    st.balloons()
    st.line_chart(chart_data)
    

elif option=='Failure Students':
    chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['University A', 'University B', 'Univeristy C'])

    st.bar_chart(chart_data)

elif option=='Overall Performances':

    st.write('Before you continue, please read the [terms and conditions](https://www.exin.com/uploads/content/General_Terms_and_Conditions_for_participation_in_EXIN_exams.pdf)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'University': ['Univerisity A', 'Univerisity B', 'University B'],
        'Overall Performances': [70, 86, 93,]
        })),

   




