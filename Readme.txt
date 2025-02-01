# 👉 Project: Weather API - Forecast Data Storage & Retrieval
This API provides **daily weather data** for different countries. It fetches data daily from **WeatherAPI.com** and allows registered users to retrieve weather data for any requested country.

---

## **1️⃣ API Setup**
### **Installation & Setup**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Nodirbek1212/weather-api.git
   cd weather-api
   ```

2. **Create a Virtual Environment & Install Dependencies**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up the Database & Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server**
   ```sh
   python manage.py runserver
   ```

---

## **2️⃣ User Authentication APIs**
### **📌 Register User**
- **Endpoint:** `POST /api/auth/register/`
- **Request Body:**
  ```json
  {
    "name": "Data",
    "surname": "Gaze",
    "username": "datagaze",
    "password": "securepassword",
    "password2": "securepassword"
  }
  ```
- **Response (201 Created):**
  ```json
  {
    "name": "Data",
    "surname": "Gaze",
    "username": "datagaze"
  }
  ```

### **📌 Login User**
- **Endpoint:** `POST /api/auth/login/`
- **Request Body:**
  ```json
  {
    "username": "datagaze",
    "password": "securepassword"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }
  ```
- **Use the `access` token in API requests:**
  ```
  Authorization: Bearer your_access_token
  ```

---

## **3️⃣ Weather API**
### **📌 Fetch Weather Data for One or More Countries**
- **Endpoint:** `GET /api/weather/get-weather/`
- **Authentication Required:** ✅ Yes
- **Request Format:**  
  ```
  GET /api/weather/get-weather/?country=Uzbekistan&country=Russia
  ```
- **Example Response:**  
  ```json
  [
    {
    "name": "Tashkent",
    "country": "Uzbekistan",
    "lat": 41.317,
    "lon": 69.25,
    "temp_c": 10.2,
    "temp_color": "#D1F2D3",
    "wind_kph": 12.6,
    "wind_color": "#B2EBF2",
    "cloud": 20,
    "cloud_color": "#FFF176"
    },
    {
    "name": "Moscow",
    "country": "Russia",
    "lat": 55.7558,
    "lon": 37.6173,
    "temp_c": -5.4,
    "temp_color": "#B3DFFD",
    "wind_kph": 5.6,
    "wind_color": "#E0F7FA",
    "cloud": 30,
    "cloud_color": "#FFF176"
    }
  ]
  ```

---

## **4️⃣ Cron Job for Daily Data Update**
The cron job runs **daily at midnight (00:00 UTC)** to fetch and store the next day's **hourly forecast** for all countries.

- **Manually Run the Cron Job:**  
  ```sh
  python manage.py runcrons
  ```

---