import streamlit as st

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")
st.title("🧮 Advanced Calculator")
st.write("Perform basic and advanced operations")

# Input numbers
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# Select operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Modulus", "Power"])

# Calculation history
if "history" not in st.session_state:
    st.session_state.history = []

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = "Error: Divide by 0" if num2 == 0 else num1 / num2
    elif operation == "Modulus":
        result = "Error: Mod by 0" if num2 == 0 else num1 % num2
    elif operation == "Power":
        result = num1 ** num2

    # Display result
    st.success(f"Result: {result}")
    
    # Add to history
    st.session_state.history.append(f"{num1} {operation} {num2} = {result}")

# Show history
if st.checkbox("Show Calculation History"):
    st.subheader("🕘 History")
    for entry in st.session_state.history[::-1]:
        st.write(entry)
