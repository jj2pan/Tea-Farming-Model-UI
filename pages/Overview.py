import streamlit as st
import pandas as pd

def main():
    st.header("Project Overview")
    st.write("This is a predictive model that estimates a farmer's harvest based on their crop area and the month.")

    st.subheader("Data Source")
    st.write("The data used to train this model was obtained from tea processing factories in Nandi county.")
    df = pd.read_csv("data.csv")
    st.dataframe(df.head())

    st.subheader("Modules")
    st.markdown("""
        - I used the **pandas** and **matplotlib** libraries for EDA.
        - I used the **scikit-learn** library to train the model.
        - I used the **Streamlit** library to create the web app.
    """)

    st.subheader("Model Performance")
    st.markdown("""
        The model was trained using a **K Neighbors Regressor**. The performance metrics are as follows:
        - **Mean Absolute Error**: 91.09
        - **Mean Squared Error**: 27861.98
        - **R2 Score**: 0.81
    """)

    st.subheader("Applications")
    st.markdown("""
        - Tea processing factories can leverage this model to predict their farmers' harvests. These insights can help them make informed managerial decisions and optimize their operations.
        - Farmer can also use this model to predict their seasonal harvests and plan accordingly.
    """)

    st.subheader("Future Work")
    st.markdown("""
        - The nature of this dataset and its context leaves a lot of room for further development.
        - I plan to use a weather API to get historical weather data for the region and add it to the dataset.
        - I also want to add lag features to enable the model to learn from previous harvests.
        - These features will add more depth to the data and in combinination with a much more complex model such as a neural network, I believe I can produce much more reliable predictions.     
    """)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Tea Farming Model",
        page_icon="🍵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    main()