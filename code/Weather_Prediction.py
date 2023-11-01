import paho.mqtt.client as mqtt
import streamlit as st
import csv
import json
import datetime
import numpy as np
import tensorflow as tf

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="/home/pi/Desktop/ard-tf-streamlit/code/model/tflite_model.tflite")
interpreter.allocate_tensors()


#MQTT broker configuration
broker_address = "192.168.106.4"  # Replace with your MQTT broker address
broker_port = 1883
topic = "your_topic/all_data"  # Replace with the topic used by your Arduino

# CSV file configuration
csv_file_path = "sensor_data.csv"

st.title('Dynamic Metrics Streamlit App')

col1, col2, col3 = st.columns(3)

temp_metric = col1.metric("Temperature", f"{0} °C")
humidity_metric = col2.metric("Humidity", f"{0}%")
pressure_metric = col3.metric("Pressure", f"{0} KPa")

# Initialize variables to store received sensor data
received_temperature = 0.0
received_humidity = 0.0
received_pressure = 0.0


st.header("Weather Prediction")
# Create a metric card
weather_status = st.metric("Predicted weather:", "Waiting for Input data")


# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

# Callback when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    global received_temperature, received_humidity, received_pressure

    payload = json.loads(msg.payload.decode())
    received_temperature = payload["temperature"]
    received_humidity = payload["humidity"]
    received_pressure = payload["pressure"]

    # Update the metric values
    temp_metric.write(f"Temperature: {received_temperature:.2f} °C")
    humidity_metric.write(f"Humidity: {received_humidity:.2f} %")
    pressure_metric.write(f"Pressure: {received_pressure:.2f} KPa")

    # Save data to CSV file
    save_to_csv(datetime.datetime.now(), received_temperature, received_humidity, received_pressure)

    # Call the weather prediction function with the received data
    predict_and_display_weather(received_temperature, received_humidity, received_pressure)


def predict_weather(temperature, humidity, pressure):
    # Convert input data to a TensorFlow Lite tensor
    input_data = np.array([[temperature, humidity, pressure]], dtype=np.float32)  # Add an extra dimension
    input_tensor = tf.convert_to_tensor(input_data)

    # Set the input tensor
    interpreter.set_tensor(interpreter.get_input_details()[0]["index"], input_tensor)

    # Run inference
    interpreter.invoke()

    # Get the output tensor and convert it to a numpy array
    output_tensor = interpreter.get_tensor(interpreter.get_output_details()[0]["index"])
    output_data = output_tensor.astype(np.float32)

    # Get the predicted class index
    predicted_class_index = np.argmax(output_data)

    # Convert the predicted class index to a weather condition label
    weather_conditions = ["Sunny", "Partly cloudy", "Cloudy", "Overcast", "Patchy rain possible"]
    predicted_weather = weather_conditions[predicted_class_index]

    return predicted_weather

def save_to_csv(timestamp, temperature, humidity, pressure):
    # Open the CSV file in append mode
    with open(csv_file_path, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Check if the file is empty, write headers if needed
        if csv_file.tell() == 0:
            csv_writer.writerow(["Timestamp", "Temperature (C)", "Humidity (%)", "Pressure (KPa)"])

        # Write the sensor data to the CSV file
        csv_writer.writerow([timestamp.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity, pressure])

def predict_and_display_weather(temperature, humidity, pressure):
    try:
        predicted_weather = predict_weather(temperature, humidity, pressure)
        weather_status.metric("Predicted weather:", predicted_weather)
    except Exception as e:
        st.error(f"Failed to predict weather: {e}")



# Create and configure the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Loop to maintain the connection and process incoming messages
client.loop_forever()