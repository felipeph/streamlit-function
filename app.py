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

# ----------- TEXT PARAMETERS -----------------
# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze. You can use x, y and z as variables."
# ----------------------------------------------

# Write the title of the page
st.title("Functions")

# Get the input of the user and save into the session state
function_input = st.text_input(txt_input, key="function_input")

if not function_input:
    st.stop()


# ------------- OPERATIONS WITH THE INPUT -------------------
# Parse the string of the raw input
function_parsed = parse_expr(function_input, transformations='all')

# Convert function to latex
function_latex = latex(function_parsed)

# Derivative with respect to x
derivative = diff(function_parsed, x)

# Integral of the function with respect to x
integral = integrate(function_parsed, x)

# -----------------------------------------------------------

# Show the function parsed
"The parsed input:"
function_parsed

"Derivative of the function with respect to x"
derivative

"Integral of the function with respect to x"
integral

"LaTeX expression for this function"
function_latex

"Data saved"
st.session_state