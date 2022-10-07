# Framework that creates the app
import streamlit as st

# Parser that correct the users writing
from sympy.parsing.sympy_parser import parse_expr

# Plotting library from sympy
from sympy.plotting.plot import plot

# All the letters as symbols
from sympy.abc import *

# Makes the algebraic computation
import sympy as sp

# Plot the functions
import matplotlib as mpl
import matplotlib.pyplot as plt

# Numerical calculations for the plot
import numpy as np

# ------------- CONFIGURATIONS -----------------

# Set matplotlib parameters to default
mpl.rcParams.update(mpl.rcParamsDefault)
mpl.rcParams.update({"font.family": "serif"})


# Set the configuration of the page with TITLE and ICON
st.set_page_config(
    page_title="Functions",
    page_icon="👨‍🏫",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

# ----------- TEXT PARAMETERS -----------------
# Write down the function you want to analyze and press ENTER
txt_input = "Write the function you want to analyze. You can use x, y and z as variables."
# ----------------------------------------------

# Write the title of the page
# st.title("Functions")

with st.form("input"):

    function_input = st.text_input(txt_input, "x^2 + 50", key="function_input")    
    
    submitted = st.form_submit_button("Submit")

# Get the input of the user and save into the session state
# function_input = st.text_input(txt_input, "x^2 + 3x + exp(x)", key="function_input")

#if not function_input:
#    st.stop()


# ------------- OPERATIONS WITH THE INPUT -------------------
# Parse the string of the raw input and convert to latex
function_parsed = parse_expr(function_input, transformations='all')
function_latex = sp.latex(function_parsed)

# Derivative with respect to x and convert to latex
derivative = sp.diff(function_parsed, x)
derivative_latex = sp.latex(derivative)

# Integral of the function with respect to x and convert to latex
integral = sp.integrate(function_parsed, x)
integral_latex = sp.latex(integral)

x_values = np.linspace(-10, 10, 640)
function_numpy = sp.lambdify(x, function_parsed, "numpy")
y_values = function_numpy(x_values)

# -----------------------------------------------------------

tab_function, tab_derivative, tab_integral, tab_plot = st.tabs(["Function", "Derivative", "Integral", "Plot"])

# Show the function parsed
with tab_function:
    st.latex(r'''f(x)=''' + function_latex)

# Show the derivative
with tab_derivative:
    st.latex(r'''\frac{d}{dx} \left(''' + function_latex + r'''\right) = ''' + derivative_latex)

# Show the integral
with tab_integral:
    st.latex(r'''\int \left(''' + function_latex + r'''\right)dx = ''' + integral_latex)

# Plot the function
with tab_plot:
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set(xlabel='$x$', ylabel='$f(x)$')
    ax.grid()
    st.latex(r'''f(x)=''' + function_latex)
    st.pyplot(fig)


# Show the data saved
"Data saved"
st.session_state