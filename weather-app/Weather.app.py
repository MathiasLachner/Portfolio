import requests

# Your WeatherAPI key
api_key = "Insert your API key here"

# Function to get weather for a specific location
def get_weather(city):
    # URL to query the weather data
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    # Make the request
    response = requests.get(weather_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract some weather information from the response
        location_name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        
        # Display the weather information
        print(f"\n{'-'*50}")
        print(f"Weather for {location_name}, {region}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
        print(f"{'-'*50}")
    else:
        print(f"\nError: Unable to fetch weather data for '{city}' (Status Code: {response.status_code})")

# Main function to get user input and show weather
def main():
    print("\nWelcome to the Weather App!\n")
    print("You can get the current weather by typing the city name.\n")
    print("To exit the app, type 'exit' at any time.\n")
    
    # Loop to keep asking for city input
    while True:
        city = input("Enter the city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("\nThank you for using the Weather App! Goodbye!")
            break
        elif city:
            get_weather(city)
        else:
            print("\nPlease enter a valid city name!\n")

# Run the program
if __name__ == "__main__":
    main()
D