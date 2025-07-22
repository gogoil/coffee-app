import streamlit as st

st.title("Coffee Grinder Calculator")

big_cups = st.number_input("Number of big coffee cups", min_value=0, step=1)
small_cups = st.number_input("Number of small coffee cups", min_value=0, step=1)
extra = st.checkbox("Extra coffee required?")

# Simple grind logic
grind_per_big = 18  # grams
grind_per_small = 12  # grams

total = big_cups * grind_per_big + small_cups * grind_per_small
if extra:
    total *= 1.2  # 20% more

st.markdown(f"### Total coffee to grind: **{total:.1f} grams**")

