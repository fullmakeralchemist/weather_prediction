<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the tinyml-mapping-backlight and create a pull request or simply open
*** an issue with the tag "suggest".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** fullmakeralchemist, tinyml-mapping-backlight, twitter_handle
-->

<!--#     The TensorFlow Microcontroller Challenge    -->
   <h1>Data Insights and Real-Time Predictive Analytics with Streamlit</h1>

<!-- PROJECT LOGO -->

<br />
<p align="center">

  <a href="https://github.com/fullmakeralchemist/">
    <img src="media/logo.png" alt="Logo" width="720">
  </a>
  -->
  <br />
  

  <img src="https://img.shields.io/github/languages/top/fullmakeralchemist/handsspelling?style=for-the-badge" alt="License" height="25">
  <img src="https://img.shields.io/github/repo-size/fullmakeralchemist/handsspelling?style=for-the-badge" alt="GitHub repo size" height="25">
  <img src="https://img.shields.io/github/last-commit/fullmakeralchemist/handsspelling?style=for-the-badge" alt="GitHub last commit" height="25">
  <img src="https://img.shields.io/github/license/fullmakeralchemist/handsspelling?style=for-the-badge" alt="License" height="25">
  <a href="https://www.linkedin.com/in/padrondata/">
    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn" height="25">
  </a>
  <!--
  <a href="https://twitter.com/makeralchemist/">
    <img src="https://img.shields.io/twitter/follow/makeralchemist?label=Twitter&logo=twitter&style=for-the-badge" alt="Twitter" height="25">
  </a>
  -->
  
  <!-- <h3 align="center">Tiny ML in Mapping Dance, Visual Arts and interactive museums</h3>-->
  <p align="center">
    <h3>Demo de la app con el Dashboard en Streamlit Share -------></h3>
    <br />
    <a href="https://objectdetectionwebcam.streamlit.app/"><strong>Proyecto Dashboard»</strong></a>
    <br />
  </p>
  <!--
  <p align="center">
  <a href="https://experiments.withgoogle.com/mapping-dance">
    <img src="assets/TFChallengeWinners.png" alt="Logo" width="720">
  </a>
  </p>
  -->
  <br />
</p>
<br />

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Tiny ML in Mapping Dance](https://i9.ytimg.com/vi/3YUVTDTo-Zk/mq1.jpg?sqp=CNTs2IcG&rs=AOn4CLBiPsvQ2bGNVZvn_j-nJXj8d81hLA)](https://www.youtube.com/watch?v=3YUVTDTo-Zk) -->

Create a foundational methodology to collect environmental data with an open-source protocol. Conduct an exploratory data analysis to gain deeper insights into the data. Leveraging my knowledge in hydraulics, I will create a data model (structure) that is valuable for hydraulic engineering and hydrology. Once the EDA is complete and if the data proves to be of sufficient quality, I will train a model and deploy it on an Arduino board. Subsequently, I will deploy that model in Streamlit to create a web app that receives data through a communication protocol. This web app will use the real-time input data to predict the current weather status.

### Motivation

This project endeavors to establish a foundational methodology for environmental data collection through open-source protocols. It encompasses key phases, from data exploration and analysis to the development of a specialized data model designed to serve the field of hydraulics engineering and hydrology. Ultimately, the project's goal is to deploy a real-time weather prediction system by harnessing the power of machine learning models integrated into Arduino boards and Streamlit web applications.

#### Empowering Through AIoT: Inclusive Data Solutions

AIoT, the fusion of AI and IoT, conquers data challenges. It enables real-time decision-making, customization for specific issues, and predictive insights, spanning industries. Yet, security and privacy are key. AIoT is a transformative force, making technology universally accessible and useful, with boundless potential.



### Built With

With a lot of love 💖, motivation to help others 💪🏼 and [Python](https://www.python.org/) 🐍, using:

* [Arduino Nano 33 BLE Sense](https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense)
* [Arduino Opla IoT Kit](https://store-usa.arduino.cc/products/arduino-opla-iot-kit)
* [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Google Colab](https://colab.research.google.com/) <img src="https://colab.research.google.com/img/favicon.ico" width="15"> (with its wonderful GPUs)
* Phone with HotSpot
* [Streamlit](https://streamlit.io/)

<!-- GETTING STARTED -->
## Getting Started

Weather prediction has always been a complex puzzle, and the integration of Artificial Intelligence of Things (AIoT) is transforming the way we approach it. Beyond traditional forecasts, AIoT leverages IoT sensor data to enhance our understanding of weather dynamics.

The Power of AIoT
In the realm of weather forecasting, AIoT marks a significant advancement. It seamlessly collects real-time data at the edge, offering deeper insights. Sensors, from those monitoring temperature to wind speed, contribute to a holistic understanding of weather patterns. This is where AIoT shines, enabling us to customize AI models to address specific challenges.

Machine Learning for Weather Prediction
Machine learning takes center stage in deciphering the intricate dance of weather patterns. AI models, trained on vast datasets, can predict everything from temperature fluctuations to storm developments. The key to accurate predictions lies in the data and creating it can be a challenge.

The Role of Exploratory Data Analysis (EDA)
EDA is the compass for weather data analysis. It's the vital first step that uncovers the dimensions of your dataset. From understanding the structure to identifying essential features, EDA equips you with the knowledge to tailor AI models. By exploring the correlations between variables, EDA guides the selection of influential factors, ensuring precise weather forecasts.

In this journey of weather prediction powered by AIoT and machine learning, crafting and fine-tuning your dataset is akin to crafting the pieces of a puzzle. Once it fits perfectly, the picture becomes clear, and the forecast becomes accurate.


## Prerequisites

This is short list things you need to use the guide. 

* Google Acount for Google Colab
* Kaggle 
* Raspberry Pi 4
* Arduino IDE
* Micro USB Cable 
* Arduinos Boards mentioned above

## Introduction 
As a hydraulic engineer, I understand the challenges of sourcing high-quality data, particularly in the context of Mexico, where accessing reliable data can be a formidable task. Many professionals, including my friends working in civil protection, often find themselves manually copying and pasting information from various government portals into Excel, a time-consuming and error-prone process.

In light of these challenges, I embarked on a mission to revolutionize data collection within the environmental and hydraulic domains. Leveraging the capabilities of Arduino-based open-source hardware platforms equipped with sensors for temperature, pressure, humidity, and more, I discovered an efficient method to easily collect historical data. These data streams not only offer convenience but also have the potential to provide robust datasets for developing cutting-edge machine learning models.

This project aims to empower professionals like me and my colleagues in civil protection by integrating this wealth of data into a streamlined workflow. It combines exploratory data analysis (EDA) techniques with TensorFlow, a powerful machine learning framework, to produce actionable insights and real-time predictive analytics, all presented through a user-friendly interface built with Streamlit.

By doing so, we aspire to transform the way hydraulic engineers and environmentalists access and utilize data, making it more accessible, actionable, and capable of driving informed decision-making in critical areas such as flood prevention, water resource management, and environmental risk assessment.



## Prerequisites 
Before getting a local copy up and running the project you need to first follow this simple steps: 
This is a list of things you need to use the software and how to install them. First we're gonna start with the configuration for our Raspberry Pi.

### Raspberry Pi 4 configuration to run the code: 
We need to use Buster version of Raspberry Pi OS or another distribution such as Debian for the MQTT Broker. Before installing the libraries in your Linux Machine run the following code lines in the terminal: 

```
sudo apt update   
sudo apt upgrade   

```

After updating and upgrading we will write the following command to install the Mosquitto Broker enter these next commands: 

```
sudo apt install -y mosquitto mosquitto-clients   
```

Then type the following command, we have to modify a document that was installed to able the MQTT Broker as a public broker in your local WIFI network: 

```
sudo nano /etc/mosquitto/mosquitto.conf   
```

Now add the following lines at the end, without modify the rest of the document (Ctrl+x to save changes): 

```
listener 1883   
allow_anonymous true   
```

Then after saving the document, you have to restart the Mosquitto Broker run the following command and restart your Linux Machine: 

```
sudo systemctl restart mosquitto.service   
```

Also to configure the Broker to start when you start up your Linux machine you have to run the following command in the terminal: 

```
sudo systemctl enable mosquitto.service   
```

To get the IP address that work for us as the direction of our broker run in the terminal the command: 

```
hostname -I   
```

One last thing to check if the Mosquitto broker is running and available run in the terminal the command: 

```
mosquitto -v   
```

Now finishing with the MQTT configuration we need to install the Library Paho-MQTT for Python to control and connect to the Broker, run the following command: 

```
sudo pip install paho-mqtt  
```

