# Write the code for creating the EMI calculator app
import streamlit as st

#create a function calculate_emi() that accepts three inputs (p, n, r) 
#and calculates the emi based on the formula given below. Print the calculated emi (rounded off to 3 decimal places).
def calculate_emi(p,n,r) :
  emi = p * (r / 100) * (((1 + (r/100))** n) / (((1 + r/100) ** n) - 1))
  return round(emi, 3)

# Add title to the app
st.title("EMI Calculator App")  

# Add sliders for selecting the values for 3 inputs
principal = st.slider('Principal', 10000, 50000)
tenure = st.slider('Tenure', 1, 30)
roi = st.slider('Rate of interest', 1.00, 15.00)

n = tenure * 12
r = roi / 12

if st.button('Calculate') :
  calculated_emi = calculate_emi(principal, n, r)
  st.write('If the Principal Amount borrowed is ', principal, 'for the tenure of ', n, 'months with Rate of interest as ', r, 'percent per annum then the Emi will be ', calculated_emi)

