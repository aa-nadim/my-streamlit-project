import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Welcome to my awesome data science project!")
    st.text("In this project I look into the transactions of taxis in NYC. ...")


with dataset:
    st.header("NYC taxi dataset")
    st.text("I foudn this dataset on blablabla.com, ...")

    taxi_data = pd.read_csv("data/taxi+_zone_lookup.csv")
    st.write(taxi_data.head())

    st.subheader("Pick-up location ID distribution on the NYC dataset")
    pulocation = pd.DataFrame(taxi_data["LocationID"].value_counts()).head(50)
    st.bar_chart(pulocation)


with features:
    st.header("The features I created")

    st.markdown(
        "* **first feature:** I created this feature because of this... I calculated it using "
    )
    st.markdown(
        "* **second feature:** I created this feature because of this... I calculated it using "
    )

with model_training:
    st.header("Time to train the model!")
    st.text(
        "Here you get to choose the hyperparameters of the model and see how the performance changes!"
    )

    sel_col, disp_col = st.columns(2)

    max_dapth = sel_col.slider(
        "What should be the max_depth of the model?",
        min_value=10,
        max_value=100,
        value=20,
        step=10,
    )

    n_estimators = sel_col.selectbox(
        "How many trees should there be?", options=[100, 200, "No limit"], index=0
    )

    input_feature = sel_col.text_input(
        "Which feature should be used as the input feature?"
    )
