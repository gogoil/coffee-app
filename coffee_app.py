import streamlit as st

st.title("Coffee Grinder Calculator")

big_cups = st.number_input("Number of big coffee cups", min_value=0, step=1)
small_cups = st.number_input("Number of small coffee cups", min_value=0, step=1)
extra = st.checkbox("Is Alexi participating?")

# Simple grind logic
grind_per_big = 18  # grams
grind_per_small = 12  # grams

extra = int(extra)
total = 10 * (big_cups - extra)
water_total = 14 * (big_cups - extra)


st.markdown(f"### Total coffee to grind: **{total:.1f} grams**")
st.markdown(f"### Total water to pour: **{water_total} ml**")
