import streamlit as st

def main():
    st.title("Tea Farming Model 🍵")
    st.image("img/harvest-per-year.png")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Tea Farming Model",
        page_icon="🍵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    main()