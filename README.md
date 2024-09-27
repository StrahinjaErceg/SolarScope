Project Name: SolarScope

Description:

SolarScope is a web-based application designed to help users assess the solar energy potential of specific locations around the world. By leveraging historical and real-time data from NASA's POWER project, SolarScope allows users to input the latitude and longitude of a location and view detailed analyses of various solar and weather parameters. The app provides insights into whether installing solar panels at the chosen location would be profitable, offering a comprehensive analysis across historical, current, and overall global data.

SolarScope evaluates several key parameters, including:

Solar radiation levels (both clear and cloudy skies)
Cloud cover
Temperature
Humidity
Wind speed
The app also provides installation suggestions based on a percentile scoring system, which ranks the location based on its solar potential. Users are presented with informative charts and analysis that empower data-driven decisions for solar panel installation.

Key Features:

Historical Solar Data Analysis: Explore long-term trends in solar radiation, cloud cover, and other relevant factors.
Real-Time Solar Monitoring: View current solar and weather conditions for installed or planned solar panels.
Overall World Solar Analysis: Visualize global locations and compare solar potential across different regions.
Installation Suggestions: Get location-specific recommendations based on historical, current, and projected solar energy potential.
User-Friendly Interface: Simple, intuitive input of latitude and longitude to generate results.

How It Works:

Input Latitude and Longitude: Users enter the geographical coordinates of the location they want to analyze.
Historical Analysis: Displays historical solar energy potential at the location, providing key data points for long-term assessment.
Current Analysis: Offers real-time weather conditions that impact the efficiency of solar panels installed at the location.
Overall Analysis: Compares solar potential at multiple locations across the globe, helping users identify optimal areas for solar projects.
Installation Suggestions: Provides recommendations on whether it is profitable to install solar panels at the selected location based on percentile rankings of key parameters.
The application utilizes NASA's POWER (Prediction of Worldwide Energy Resources) API to fetch both historical and current solar data, ensuring reliable and scientifically-backed information.

Technologies Used:

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript, Chart.js
Data Source: NASA POWER API for historical and real-time solar and weather data
Mapping: Leaflet.js (for the overall map)


Installation and Setup:

1. Prerequisites
Before running the project, make sure you have the following installed:
Python (version 3.7 or higher)
Flask (Python web framework)

2. Clone the Repository
git clone https://github.com/yourusername/solarscope.git
cd solarscope

3. Install Dependencies
Run the following command to install the required Python libraries:
pip install -r requirements.txt
The requirements.txt file should contain the following:
Flask==2.0.1
requests==2.26.0

4. Running the Application
To run the Flask server, use:
python app.py
The application will be running on http://127.0.0.1:5000/.

Usage Instructions:

Step 1: Launch the application and navigate to the homepage.
Step 2: Enter the latitude and longitude of the location you wish to analyze.
Step 3: Click "Analyze Location" and navigate through the menu to view:
Historical Solar Data: Displays past trends of solar potential.
Current Solar Data: Shows real-time weather and solar parameters at the location.
Overall World Solar Analysis: Offers a comparative global analysis.
Suggestions: Recommends whether to install solar panels based on the analysis.

File Structure:

solarscope/
│
├── app.py                # Main Flask app
├── templates/
│   ├── index.html        # Homepage with latitude/longitude input
│   ├── historical.html   # Displays historical solar data
│   ├── current.html      # Displays current solar and weather data
│   ├── overall.html      # Global solar analysis map
│   ├── suggestions.html  # Installation suggestions page
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet for the app
├── requirements.txt      # Python dependencies
├── README.md             # Project README

API Usage
SolarScope uses NASA's POWER API to fetch solar and weather data for the input coordinates. The data is fetched for the following parameters:

Historical Data: Monthly solar radiation and weather parameters.
Current Data: Hourly updates of current weather conditions affecting solar panel efficiency.

Example API URL used in the project:
https://power.larc.nasa.gov/api/temporal/monthly/point?start=2010&end=2022&latitude=LAT&longitude=LON&parameters=PARAM&format=json
Replace LAT and LON with the latitude and longitude of the location, and PARAM with the specific weather or solar parameter.

Contributing:

We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, feel free to contact the project maintainer:

Name: Strahinja Erceg
Email: sterceg02@gmail.com
