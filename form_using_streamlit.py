import streamlit as st

# heading of the app/ page
st.title("---AKGEC Student Details---")
# subheading of the page
st.subheader("Enter the details below:")

with st.form("form1", clear_on_submit=True):	# here key='form1' 
												# clear_on_submit=True, resets all widgets after submission
	name=st.text_input("Enter Name")	# text input
	email=st.text_input("Enter AKGEC Email ID")
	message=st.text_input("Enter Student No.")
	
	gender=st.radio("Select Gender", ('Male', 'Female'))	# select using radio buttons
	
	age=st.slider("Enter your Age", min_value=10, max_value=100)	# slider input
	
	submit=st.form_submit_button("Submit Form")	# submit data entered
