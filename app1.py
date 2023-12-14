import tkinter as tk
import requests

def get_weather(city):
    api_key = '55aae6de3718fd1bcad31bd28e40ddeb'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        # Display the weather information
        result_label.config(text=f'Temperature: {temperature}°C\nDescription: {weather_description}')

    except Exception as e:
        result_label.config(text='Error fetching weather data')

# Create the main application window
app = tk.Tk()
app.title('Simple Weather App')

# Create and pack widgets

##city_label = tk.Label(app, text='Enter City:')
##city_label.pack(pady=10)

##city_entry = tk.Entry(app)
##city_entry.pack(pady=10)

##get_weather_button = tk.Button(app, text='Get Weather', command=lambda: get_weather(city_entry.get()))
##get_weather_button.pack(pady=10)

##result_label = tk.Label(app, text='')
##result_label.pack(pady=10)//////
city_label = tk.Label(app, text='Enter City:', bg='#3498db', fg='white', font=('Helvetica', 14))
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=('Helvetica', 12))
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text='Get Weather', command=lambda: get_weather(city_entry.get()),
                            bg='#2ecc71', fg='white', font=('Helvetica', 12))
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text='', bg='#3498db', fg='white', font=('Helvetica', 14))
result_label.pack(pady=10)

# Load and display an image
image_url = "C:\Users\kaash\Desktop\weatherapp\web\images.jpeg"  # Replace with the path to your image
try:
    image = Image.open(image_url)
    image = image.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(app, image=img, bg='#3498db')
    panel.image = img
    panel.pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Run the application
app.mainloop()
