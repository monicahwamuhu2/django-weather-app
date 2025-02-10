

### **🌤 Django Weather App**  
A simple weather application built with Django that fetches real-time weather data using the OpenWeatherMap API.  

---

## **📌 Features**
✅ Search for weather by city name  
✅ Displays temperature, weather description, and icon  
✅ Fetches data from OpenWeatherMap API  
✅ Built using Django and Bootstrap  

---

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/monicahwamuhu2/django-weather-app.git
cd django-weather-app
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
```
Activate it:  
- **Windows:** `venv\Scripts\activate`  
- **Mac/Linux:** `source venv/bin/activate`

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Get an OpenWeatherMap API Key**
1. Sign up at [OpenWeatherMap](https://openweathermap.org/)  
2. Get your **API Key**  
3. Create a `.env` file in the project root and add:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

### **5️⃣ Run Migrations**
```bash
python manage.py migrate
```

### **6️⃣ Start the Server**
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---



## **🛠 Tech Stack**
- **Django** - Backend framework  
- **Bootstrap** - Styling  
- **OpenWeatherMap API** - Fetch weather data  
- **SQLite** - Default database  

---

## **📜 License**
This project is open-source and available under the **MIT License**.

---

