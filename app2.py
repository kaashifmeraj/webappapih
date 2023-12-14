import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

def get_weather(city, country, units):
    api_key = '55aae6de3718fd1bcad31bd28e40ddeb'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': f'{city},{country}', 'appid': api_key, 'units': units}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        result_label.config(text=f'Temperature: {temperature}°C\nDescription: {weather_description}')

    except Exception as e:
        messagebox.showerror('Error', 'Error fetching weather data')

# Create the main application window
app = tk.Tk()
app.title('Advanced Weather App')

# Set background color
app.config(bg='#3498db')

##
# Load and display the background image
background_image_path = "C:/Users/kaash/Desktop/images.jpeg"  # Replace with the path to your image
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to place the image
canvas = tk.Canvas(app, width=background_image.width, height=background_image.height)
canvas.pack()

# Place the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
##

# Menu bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Exit', command=app.destroy)

# Create and pack widgets with styling
title_label = tk.Label(app, text='Weather App', bg='#3498db', fg='white', font=('Helvetica', 18, 'bold'))
title_label.pack(pady=100)

city_label = tk.Label(app, text='City:', bg='#3498db', fg='white', font=('Helvetica', 14))
city_label.pack()

city_entry = tk.Entry(app, font=('Helvetica', 12))
city_entry.pack(pady=5)

country_label = tk.Label(app, text='Country (optional):', bg='#3498db', fg='white', font=('Helvetica', 14))
country_label.pack()

country_entry = tk.Entry(app, font=('Helvetica', 12))
country_entry.pack(pady=5)

units_label = tk.Label(app, text='Units (metric/imperial):', bg='#3498db', fg='white', font=('Helvetica', 14))
units_label.pack()

units_entry = tk.Entry(app, font=('Helvetica', 12))
units_entry.insert(0, 'metric')  # Default to metric units
units_entry.pack(pady=5)

get_weather_button = tk.Button(app, text='Get Weather', command=lambda: get_weather(city_entry.get(), country_entry.get(), units_entry.get()),
                            bg='#2ecc71', fg='white', font=('Helvetica', 12))
get_weather_button.pack(pady=20)

result_label = tk.Label(app, text='', bg='#3498db', fg='white', font=('Helvetica', 14))
result_label.pack(pady=10)

# Load and display an image
image_url = "C:/Users/kaash/Desktop/images.jpeg" # Replace with the path to your image
try:
    image = Image.open(image_url)
    image = image.resize((150, 150), Image.images)
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(app, image=img, bg='#3498db')
    panel.image = img
    panel.pack(pady=20)
except Exception as e:
    print(f"Error loading image: {e}")

# Run the application
app.mainloop()
