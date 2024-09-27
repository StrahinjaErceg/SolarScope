import requests
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta

# Parameters Monthly
# All Sky Insolation Clearness Index (ALLSKY_KT) ---- 0.9 ---- Higher is Better
# All Sky Surface Shortwave Diffuse Irradiance (ALLSKY_SFC_SW_DIFF) ---- 0.7 ---- Higher is Better
# Clear Sky Day (CLRSKY_DAYS) ---- 0.8 ---- Higher is Better
# Cloud Amount (CLOUD_AMT) ---- 0.9 ---- Lower is Better
# Land Snowcover Fraction (FRSNO) ---- 0.7 ---- Lower is Better
# Top-Of-Atmosphere Shortwave Direct Normal Radiation (TOA_SW_DNI) ---- 0.7 ---- Higher is Better
# Surface Solar Radiation (ALLSKY_SFC_SW_DWN) ---- 1 ---- Higher is Better

# Parameters Monthly
# Surface Pressure (PS) ---- 2 ---- Minimal impact on solar panel efficiency; more related to weather patterns.
# Air Temperature at 2 Meters (T2M) ---- 6 ---- Affects solar panel efficiency as higher temperatures can reduce efficiency.
# Relative Humidity at 2 Meters (RH2M) ---- 5 ---- Moderate impact; high humidity can lead to cloud formation, reducing solar radiation.
# Surface Wind Speed at 10 Meters (WS10M) ---- 4 ---- Minor impact; can cool panels slightly, improving efficiency in hot conditions.



# NASA POWER API URLs
NASA_POWER_API_URL_MONTHLY = 'https://power.larc.nasa.gov/api/temporal/monthly/point'
NASA_POWER_API_URL_HOURLY = 'https://power.larc.nasa.gov/api/temporal/hourly/point'

# Fetch monthly parameter data (for historical analysis)
def fetch_monthly_parameter_data(latitude, longitude, parameter):
    request_url = f"{NASA_POWER_API_URL_MONTHLY}?start=2010&end=2022&latitude={latitude}&longitude={longitude}&community=ag&parameters={parameter}&format=json&header=true"
    print(f"Request URL (Monthly): {request_url}")  # Debugging: Print the request URL
    response = requests.get(url=request_url, verify=True, timeout=30.0)

    if response.status_code == 200:
        data = response.json()
        parameter_data = data['properties']['parameter'][parameter]
        return parameter_data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")  # Debugging: Print error message
        return None


# Fetch hourly parameter data (for current analysis)
def fetch_hourly_parameter_data(latitude, longitude, parameter):
    today = datetime.utcnow()
    one_month_ago = today - timedelta(days=30)
    start_date = one_month_ago.strftime('%Y%m%d')
    end_date = (one_month_ago + timedelta(days=7)).strftime('%Y%m%d')

    request_url = f"{NASA_POWER_API_URL_HOURLY}?start={start_date}&end={end_date}&latitude={latitude}&longitude={longitude}&community=ag&parameters={parameter}&format=json&header=true&time-standard=lst"
    print(f"Request URL (Hourly): {request_url}")  # Debugging: Print the request URL
    response = requests.get(url=request_url, verify=True, timeout=30.0)

    if response.status_code == 200:
        data = response.json()
        parameter_data = data['properties']['parameter'][parameter]
        return parameter_data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")  # Debugging: Print error message
        return None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historical')
def historical():
    return render_template('historical.html')

@app.route('/current')
def current():
    return render_template('current.html')

@app.route('/overall')
def overall():
    return render_template('overall.html')

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')


# API endpoint for monthly data (for historical analysis)
@app.route('/api/data/monthly/<parameter>')
def get_monthly_data(parameter):
    latitude = request.args.get('latitude', '0')
    longitude = request.args.get('longitude', '0')
    data = fetch_monthly_parameter_data(latitude, longitude, parameter)

    if data:
        datesList = list(data.keys())
        valuesList = list(data.values())

        # Reformat the dates to 'YYYY/MM'
        datesList = [f"{date[:4]}/{date[4:]}" for date in datesList]

        # Remove yearly data points
        i = 1
        while i < len(datesList):
            if i % 12 == 0:
                datesList.pop(i)
                valuesList.pop(i)
            i += 1

        formatted_data = {
            'dates': datesList,
            'values': valuesList
        }
        return jsonify(formatted_data)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500


# API endpoint for hourly data (for current analysis)
@app.route('/api/data/hourly/<parameter>')
def get_hourly_data(parameter):
    latitude = request.args.get('latitude', '0')
    longitude = request.args.get('longitude', '0')
    data = fetch_hourly_parameter_data(latitude, longitude, parameter)

    if data:
        datesList = list(data.keys())
        valuesList = list(data.values())

        # Reformat the dates to 'YYYY/MM/DD HH'
        datesList = [f"{date[:4]}/{date[4:6]}/{date[6:8]} {date[8:]}" for date in datesList]

        formatted_data = {
            'dates': datesList,
            'values': valuesList
        }
        return jsonify(formatted_data)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

# Print the current date in 'YYYYMMDD' format when the app is launched
current_time = datetime.now().strftime('%Y%m%d')
print(f"App launched at: {current_time}")

if __name__ == '__main__':
    app.run(debug=True)

