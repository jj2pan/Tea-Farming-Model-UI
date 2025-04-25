import streamlit as st

def main():
    st.subheader("Harvest per Year")
    st.markdown("""
        - 2020 had the highest cumulative harvest, while 2022 had the lowest.
        - The trend isn't linear.
    """)
    st.image("img/harvest-per-year.png")
    
    st.subheader("Farmers per Year")
    st.markdown("""
        - The number of farmers remained relatively consistent over the years with minor flactuations.
        - 2023 had the highest number of recorded farmers but its harvest was lower than 2020.
        - One might assume that there is no correlation between these two metrics, however, 2020 also had a relatively high record of farmers suggesting that the number of farmers does indeed impact the total recorded quantity for the year.
        - But clearly other factors are at play here.
    """)
    st.image("img/farmers-per-year.png")

    st.subheader("Comparison of Harvest and Land Size")
    st.write("Here I try to find out whether there is a linear relationship between the harvest quantity and the land size.")
    st.write("The regressor shows no clear linear relationship, therefore a linear regressor model would not be the best fit for this data.")
    st.image("img/harvest-land-size.png")

    st.subheader("Seasonal Harvest")
    st.write("The general trend shows that harvest is lower in the earlier weeks of the year and increases as the year progresses.")
    st.image("img/quantity-per-week.png")
    st.write("The same can be seen if we look at the yield per hectare monthly.")
    st.image("img/yield-per-ha.png")

    st.subheader("Harvest Efficiency")
    st.markdown("""
        - The harvest efficiency has been calculated here as the ratio of the harvest quantity to the land size (yield per hectare).
        - The graph shows that farmers with smaller land sizes tend to have a higher harvest efficiency, while those with larger land sizes have lower efficiency.       
    """)
    st.image("img/harvest-efficiency.png")
    st.divider()

    st.subheader("Conclusion")
    st.write("""
        - After carrying out exploratory data analysis, I have come to the conclusion that the harvest quantity is primarily influened by the land size and time of the year (season).
        - However, these relationships are not linear.
    """)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Tea Farming Model",
        page_icon="🍵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    main()