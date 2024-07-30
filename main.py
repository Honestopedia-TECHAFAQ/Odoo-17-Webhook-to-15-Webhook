import streamlit as st
import requests
import json

st.title('Odoo Webhook Trigger')

url = st.text_input('Webhook URL', 'http://localhost:8069/webhook')
data = st.text_area('Data to send', '{"example": "data"}')

def validate_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False

if st.button('Send Webhook'):
    if not url:
        st.error('Please enter a webhook URL.')
    elif not validate_json(data):
        st.error('Invalid JSON data. Please correct the JSON format.')
    else:
        try:
            response = requests.post(url, json=json.loads(data))
            if response.status_code == 200:
                st.success('Webhook sent successfully')
                st.json(response.json())
            else:
                st.error(f'Failed to send webhook. Status code: {response.status_code}')
                st.write(response.text)
        except requests.exceptions.RequestException as e:
            st.error(f'Error sending webhook: {e}')
