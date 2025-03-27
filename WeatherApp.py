#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests  #Import request to library to make HTTP requests

#Function to get weather data for a given city
def get_weather(city):
    API_KEY = "3dcb2c7319d889b59e58eb2e64bd907a"  #API key to access the weather service
    BASE_URL = "http://api.weatherstack.com/current"  #Base URL of the weather API

    #Parameters to send with the request
    params = {'access_key': API_KEY, 'query': city}

    try:
        #Make a GET request to the weather API with the given parameters
        response = requests.get(BASE_URL, params=params)
        
        #Raise an exception if an HTTP error occurs
        response.raise_for_status()
        
        #Convert response data to Python 
        data = response.json()

        #Check if the API returned an error message
        if "error" in data:
            print(f"Error: {data['error']['info']}")
            return None  #Stop function

        #Return the weather data if everything is okay
        return data

    except requests.exceptions.RequestException:
        print("Error occurred while fetching data.")
        return None  #Return None if there are any errors

#Function to display weather data in a formatted output
def display_weather(data):
    if data: 
        
        #Extracting necessary weather details from the JSON response
        city_name = data['location']['name']  #Name of the city
        country = data['location']['country']  #Name of the country
        temp = data['current']['temperature']  #Current temperature in Celsius
        humidity = data['current']['humidity']  #Humidity percentage
        weather_description = data['current']['weather_descriptions'][0]  #Weather condition
        wind_speed = data['current']['wind_speed']  #Wind speed in km/h

        #Formatting the weather information
        weather_info = (
            "\n-------------------------------\n"
            f"Weather in {city_name}, {country}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {weather_description}\n"
            f"Wind Speed: {wind_speed} km/h\n"
            "-------------------------------\n"
        )

        #Print formatted weather info
        print(weather_info)
        return weather_info
    else:
        
        print("Could not retrieve weather data.")
        return None

#Main part of the program
if __name__ == "__main__":
    print("Welcome to Ezen's Weather App! Type 'exit' to stop.")

    #Starting an infinite loop to keep asking for city names
    while True:
        
        #Asking user to enter a city name
        city = input("\nEnter city name: ").strip()

        #If user types 'exit', stop program
        if city.lower() == "exit":
            break

        #Check if the user entered an empty city name
        if not city:
            print("City name cannot be empty.")
            continue  #Ask again for a valid city name

        #Call the function to get weather data for the entered city
        weather_data = get_weather(city)

        #Call the function to display the weather information
        display_weather(weather_data)


# In[ ]:




