import requests
import streamlit as st


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

pickup_datetime = st.text_input("Enter the pickup date and time (YYYY-MM-DD HH:MM:SS)")
pickup_longitude = st.number_input("Enter the pickup longitude", format="%.6f")
pickup_latitude = st.number_input("Enter the pickup latitude", format="%.6f")
dropoff_longitude = st.number_input("Enter the dropoff longitude", format="%.6f")
dropoff_latitude = st.number_input("Enter the dropoff latitude", format="%.6f")
passenger_count = st.slider("Select the number of passengers", 1, 6, 1)
}

'''


## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

"""
🤔 How could we call our API ? Off course... The `requests` package 💡
"""
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

# Prepare API parameters
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count

3. Let's call our API using the `requests` package...

# Send API request and handle response
if st.button("Get Fare Prediction"):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        prediction = response.json().get("fare", "No prediction available")
        st.success(f"The predicted fare is: ${prediction}")
    else:
        st.error("Error in API request. Please try again.")

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
