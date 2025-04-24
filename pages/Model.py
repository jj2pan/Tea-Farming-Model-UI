import streamlit as st
import numpy as np
import pickle
import sklearn

def main():
    crop_area = st.number_input(
        label="Crop Area (Ha) : ",
        min_value=0.1,
        value=0.1,
        step=0.01,
        format="%.2f"
        )
    
    month = st.slider(
        label="Month : ",
        min_value=1,
        max_value=12,
        value=1,
        step=1,
        format="%d"
        )
    
    values = np.array([crop_area, month])
    values = values.reshape(1, -1)

    predict = st.button("Predict")
    
    with open("knn_model.pkl", "rb") as f:
        model = pickle.load(f)

    if predict:
        model.predict(values)
        st.success(f"Predicted Quantity: {round(model.predict(values)[0], 2)} kg")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Tea Farming Model",
        page_icon="🍵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    main()
