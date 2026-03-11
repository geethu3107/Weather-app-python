import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        result_label.config(
            text=f"""
City: {city.title()}
Temperature: {temp} °C
Feels Like: {feels} °C
Humidity: {humidity} %
Condition: {condition}
"""
        )

    except Exception as e:
        messagebox.showerror("Error", "Something went wrong")


# ---------------- GUI ----------------
app = tk.Tk()
app.title("Weather App")
app.geometry("350x350")
app.resizable(False, False)

tk.Label(app, text="Weather Application", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(app, text="Enter City Name").pack()
city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 11))
result_label.pack(pady=10)

app.mainloop()
