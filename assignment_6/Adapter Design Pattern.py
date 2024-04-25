class WeatherData:
    def __init__(self, temperature, humidity, wind_speed, conditions):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.conditions = conditions

class WeatherDataAdapter:
    def get_weather_data(self, location):
        pass

class WeatherAPI1Adapter(WeatherDataAdapter):
    def get_weather_data(self, location):
        api_data = weather_api_1.fetch_weather_data(location)
        
        common_data = map_and_convert_to_common_model(api_data)
        
        return common_data

class WeatherAPI2Adapter(WeatherDataAdapter):
    def get_weather_data(self, location):
        api_data = weather_api_2.fetch_weather_data(location)
        
        common_data = map_and_convert_to_common_model(api_data)
        
        return common_data

def map_and_convert_to_common_model(api_data):
    common_data = WeatherData(
        temperature=api_data['temperature'],
        humidity=api_data['humidity'],
        wind_speed=api_data['wind_speed'],
        conditions=api_data['conditions']
    )
    
    return common_data

def display_weather(adapter, location):
    try:
        weather_data = adapter.get_weather_data(location)
        display(weather_data)
    except Exception as e:
        handle_error(e)

api1_adapter = WeatherAPI1Adapter()
api2_adapter = WeatherAPI2Adapter()

display_weather(api1_adapter, "New York")
display_weather(api2_adapter, "London")
