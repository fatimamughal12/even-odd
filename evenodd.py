import streamlit as st

def even_odd():
    st.header("\n********Welcome to Even/Odd*********")
    
 
    number = st.number_input("Enter a number", min_value=0, step=1)
    
    
    if number % 2 == 0:
        st.success(f"{number} is Even")
    else:
        st.success(f"{number} is Odd")
    
    option = st.sidebar.selectbox("Options", ["Run Even/Odd Again", "Exit Software Pack"])
    
    if option == "Run Even/Odd Again":
        st.rerun()
    elif option == "Exit Software Pack":
        st.write("Thank you for using Software Pack")
        st.stop()

if __name__ == "__main__":
    even_odd()
