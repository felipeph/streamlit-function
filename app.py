# Import the streamlit library to the app as st
import streamlit as st

# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)

# -------------- The texts of the app goes here ----------------

# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze:"

# Text for the output legend
txt_output = "You wrote: "

# Text for the button SUBMIT
txt_submit_button = "Submit"

# -------------- End of the text of the app --------------------

# Write the title of the page
st.title("Functions")

# Get the input of the user and save into the session state
function_input = st.text_input(txt_input, key="function_input")

# Show the raw input
st.write("The raw input:")
st.write(function_input)


# Show the render 
st.write("LaTeX render:")
st.latex(function_input)

st.write("Data saved")
st.write(st.session_state)