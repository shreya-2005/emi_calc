# Write the code for creating the Improvised EMI calculator app
import streamlit as st

# Create a function calculate_emi() 

def calculate_emi(p,n,r) :
  emi = p * (r / 100) * (((1 + (r/100))** n) / (((1 + r/100) ** n) - 1))
  return round(emi, 3)

# Create a function calculate_outstanding_balance()

def calculate_outstanding_emi(p, n, r, m) :
  numerator = (p * ((1 + r/100)**n) - (1 + r/100) **m)
  denominator = ((1 + r/100) **n - 1)	
  balance = numerator/denominator
  return round(balance, 3)

# Add title to the app
st.title("Improvised EMI Calculator App")  

# Add sliders for selecting the values for 3 inputs
principal = st.slider('Principal', 10000, 50000)
tenure = st.slider('Tenure', 1, 30)
roi = st.slider('Rate of interest', 1.00, 15.00)
m = st.slider('Period after which the Outstanding Loan Balance is calculated(in months)',1, (tenure * 12))

n = tenure * 12
r = roi / 12

if st.button('Calculate EMI'):
  calculated_emi = calculate_emi(principal, n, r)
  st.write('If the Principal Amount borrowed is ', principal, 'for the tenure of ', n, 'months with Rate of interest as ', r, 'percent per annum then the Emi will be ', calculated_emi)
if st.button('Calculate Outstanding Loan Balance')  :
  loan = calculate_outstanding_emi(principal, n, r, m)
  st.write('Outstanding Balance Amount is ', loan)	