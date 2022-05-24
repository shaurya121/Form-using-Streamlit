
# Form using Streamlit

Create an online form to store student data using Streamlit library.


## Screenshots
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Form-using-Streamlit/main/Screenshots/streamlit_form.png)



## Installation

Install required module using:

```bash
pip insatll streamlit
```
    
## Usage/Examples

Import module using:
```python
import streamlit as st
```

Create Heading and Sub-Heading using:
```python
st.title("---AKGEC Student Details---")
st.subheader("Enter the details below:")
```

Accept different data by:
```python
name=st.text_input("Enter Name")
gender=st.radio("Select Gender", ('Male', 'Female'))
age=st.slider("Enter your Age", min_value=10, max_value=100)
```

Finally, submit form:
```python
submit=st.form_submit_button("Submit Form")
```


## Acknowledgements

 - [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)

