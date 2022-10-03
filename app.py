# Import the streamlit library to the app as st
import streamlit as st

# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)

# -------------- The texts of the app goes here ----------------

# Text that I'm going to use to ask the input to the user
txt_input = "Write something here and click the submit button"

# Text for the output legend
txt_output = "You wrote: "

# Text for the button SUBMIT
txt_submit_button = "Submit"

# -------------- End of the text of the app --------------------


# Write the title of the page
st.title("Functions")

# Check if there is no session state in this app yet
session_new = "my_input" not in st.session_state

# Clear the value of the input if the session is new
if session_new:
    st.session_state["my_input"] = ""

# Get the input of the user and save into the session state
my_input = st.text_input(txt_input, st.session_state["my_input"])

# Record the state of a button of submit
submit = st.button("Submit")

# If the button is clicked 
if submit:

    # Record the input of the user into a session file
    st.session_state["my_input"] = my_input

    # Write back to the user
    st.write(txt_output, my_input)


with st.form("input_form"):
#    st.write(txt_input)

    my_input = st.text_input(txt_input, st.session_state["my_input"])

    # Every form must have a submit button.
    submitted = st.form_submit_button(txt_submit_button)

    if submitted:
        st.write(txt_output, my_input)