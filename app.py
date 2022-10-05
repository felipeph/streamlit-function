# Import the streamlit library to the app as st
import streamlit as st
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
from sympy.abc import *
from sympy import *
# x, y, z = symbols("x y z")

# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)


# -------------- The texts of the app goes here ----------------

# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze. You can use x, y and z as variables."

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
"The raw input:"
st.text(function_input)

if not function_input:
    st.stop()

# Parse the string of the raw input
function_parsed = parse_expr(function_input, transformations='all')

# Show the function parsed
"The parsed input:"
function_parsed

"Derivative of the function with respect to x"
derivative = diff(function_parsed, x)
derivative

"Integral of the function with respect to x"
integral = integrate(function_parsed, x)
integral


# Show the render 
"LaTeX render:"
st.latex(function_parsed)



"LaTeX expression for this function"
function_latex = latex(function_parsed)
function_latex



"Data saved"
st.session_state