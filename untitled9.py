# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BkUfZKOtImbrFVXp3SN8Dqk_ki1qUTKw
"""

# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PFJUUQn5MkJwVyyc5ca3kM6P9WhrEsKU
"""

import subprocess

# Define function to install dependencies from requirements.txt
def install_dependencies():
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

# Install dependencies
install_dependencies()

import requests
import pandas as pd
import streamlit as st
import plotly.express as px
import json
#API key
#pip install streamlit

api_key = '1d5f783796626d6b77e59be548a8f73a7576a37d'

# Base URL for the US Census Bureau API
base_url = 'https://api.census.gov/data'

# Function to fetch data from the US Census Bureau API for a specific year
def fetch_census_data_for_year(year, api_key):
    url = f"{base_url}/{year}/cps/basic/may"
    params = {
        'get': 'PRTAGE,PXSEX,PRFAMNUM,PTDTRACE,PEEDUCA,PEMLR,HEFAMINC,GTCBSA,PEMLR,PWSSWGT,PEMARITL',
        'for': 'state:*',
        'key': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json()[1:], columns=response.json()[0])
    else:
        print(f"Failed to fetch data for {year}")
        return pd.DataFrame()

# Dictionary containing cities with their corresponding codes
cities = {

     "12420": "Austin-Round Rock, TX",
      "14540": "Bowling Green, KY",
      "29940": "Lawrence, KS",
      "48060": "Watertown-Fort Drum, NY",
      "19340": "Davenport-Moline-Rock Island, IA-IL",
      "36500": "Olympia, WA",
      "14260": "Boise City, ID",
      "24020": "Glen Falls, NY",
      "26820": "Idaho Falls, ID",
      "31700": "Manchester-Nashua, NH",
      "41180": "St. Louis, MO-IL",
      "12540": "Bakersfield, CA",
      "13820": "Birmingham-Hoover, AL",
      "33660": "Mobile, AL",
      "11300": "Anderson, IN",
      "27100": "Jackson, MI",
      "37460": "Panama City, FL",
      "49660": "Youngstown-Warren-Boardman, OH-PA",
      "49740": "Yuma, AZ",
      "49180": "Winston-Salem, NC",
      "29740": "Las Cruces, NM",
      "33460": "Minneapolis-St Paul-Bloomington, MN-WI",
      "39300": "Providence-Warwick, RI-MA",
      "33340": "Milwaukee-Waukesha-West Allis, WI",
      "34900": "Napa, CA",
      "12700": "Barnstable, MA",
      "17420": "Cleveland, TN",
      "20260": "Duluth, MN-WI",
      "26100": "Holland-Grand Haven, MI",
      "37340": "Palm Bay-Melbourne-Titusville, FL",
      "71650": "Boston-Cambridge-Quincy, MA-NH",
      "19820": "Detroit-Warren-Dearborn, MI",
      "39340": "Provo-Orem, UT",
      "29460": "Lakeland-Winter Haven, FL",
      "29540": "Lancaster, PA",
      "36740": "Orlando, FL",
      "41700": "San Antonio, TX",
      "46940": "Vero Beach, FL",
      "73450": "Hartford-West Hartford-East Hartford, CT",
      "17980": "Columbus, GA-AL",
      "32580": "McAllen-Edinburg-Mission, TX",
      "22420": "Flint, MI",
      "26420": "Houston-Baytown-Sugar Land, TX",
      "30460": "Lexington-Fayette, KY",
      "37860": "Pensacola-Ferry Pass-Brent, FL",
      "39100": "Poughkeepsie-Newburgh-Middletown, NY",
      "44100": "Springfield, IL",
      "11540": "Appleton, WI",
      "40140": "Riverside-San Bernardino-Ontario, CA",
      "10900": "Allentown-Bethlehem-Easton, PA-NJ",
      "28020": "Kalamazoo-Portage, MI",
      "41420": "Salem, OR",
      "41860": "San Francisco-Oakland-Fremont, CA",
      "47380": "Waco, TX",
      "15680": "California-Lexington Park, MD",
      "17860": "Columbia, MO",
      "30780": "Little Rock-North Little Rock, AR",
      "35980": "Norwich-New London, CT",
      "79600": "Worcester, MA-CT",
      "29820": "Las Vegas-Paradise, NV",
      "28700": "Kingsport-Bristol, TN-VA",
      "39740": "Reading, PA",
      "43620": "Sioux Falls, SD",
      "16580": "Champaign-Urbana, IL",
      "22900": "Fort Smith, AR-OK",
      "35620": "New York-Newark- Jersey City, NY-NJ-PA (White Plains central city recoded to balance of metropolitan)",
      "36100": "Ocala, FL",
      "37100": "Oxnard-Thousand Oaks-Ventura, CA",
      "39380": "Pueblo, CO",
      "41060": "St. Cloud, MN",
      "48620": "Wichita, KS",
      "22660": "Fort Collins, CO",
      "47260": "Virginia Beach-Norfolk-Newport News, VA-NC",
      "30020": "Lawton, OK",
      "71950": "Bridgeport-Stamford-Norwalk, CT",
      "10180": "Abilene, TX",
      "45460": "Terre Haute, IN",
      "10580": "Albany-Schenectady-Troy, NY",
      "21500": "Erie, PA",
      "78700": "Waterbury, CT",
      "18140": "Columbus, OH",
      "25260": "Hanford-Corcoran, CA",
      "41620": "Salt Lake City, UT",
      "42060": "Santa Barbara-Santa Maria-Goleta, CA",
      "42140": "Santa Fe, NM",
      "12020": "Athens-Clarke County, GA",
      "19100": "Dallas-Fort Worth-Arlington, TX",
      "22500": "Florence, SC",
      "25540": "Hartford-West Hartford-East Hartford, CT",
      "30980": "Longview, TX",
      "36220": "Odessa, TX",
      "76450": "Norwich-New London, CT-RI",
      "20100": "Dover, DE",
      "23580": "Gainesville, GA",
      "47940": "Waterloo-Cedar Falls, IA",
      "13380": "Bellingham, WA",
      "31180": "Lubbock, TX",
      "44060": "Spokane-Spokane Valley, WA",
      "11340": "Anderson, SC",
      "21340": "El Paso, TX",
      "23020": "Fort Walton Beach-Crestview-Destin, FL",
      "42020": "San Luis Obispo-Paso Robles, CA",
      "42540": "Scranton--Wilkes-Barre, PA",
      "46220": "Tuscaloosa, AL",
      "47220": "Vineland-Bridgeton, NJ",
      "10420": "Akron, OH",
      "46540": "Utica-Rome, NY",
      "12100": "Atlantic City-Hammonton, NJ",
      "12220": "Auburn-Opelika, AL",
      "22220": "Fayetteville-Springdale-Rogers, AR-MO",
      "35300": "New Haven-Milford, CT",
      "24780": "Greenville, NC",
      "31540": "Madison, WI",
      "36140": "Ocean City, NJ",
      "36540": "Omaha-Council Bluffs, NE-IA",
      "76750": "Portland-South Portland, ME",
      "13740": "Billings, MT",
      "16980": "Chicago-Naperville-Elgin, IL-IN-WI",
      "35840": "North-Port-Sarasota-Bradenton, FL",
      "23060": "Fort Wayne, IN",
      "32780": "Medford, OR",
      "74500": "Leominster-Fitchburg-Gardner, MA",
      "31420": "Macon, GA",
      "44180": "Springfield, MO",
      "12940": "Baton Rouge, LA",
      "27740": "Johnson City, TN",
      "41940": "San Jose-Sunnyvale-Santa Clara, CA",
      "47580": "Warner Robins, GA",
      "35380": "New Orleans-Metairie, LA",
      "14500": "Boulder, CO",
      "25500": "Harrisonburg, VA",
      "36260": "Ogden-Clearfield, UT",
      "29340": "Lake Charles, LA",
      "29700": "Laredo, TX",
      "42660": "Seattle-Tacoma-Bellevue, WA",
      "10500": "Albany, GA",
      "14010": "Bloomington, IL",
      "17140": "Cincinnati, OH-KY-IN",
      "19660": "Deltona-Daytona Beach-Ormond Beach, FL",
      "34740": "Muskegon-Norton Shores, MI",
      "45300": "Tampa-St. Petersburg-Clearwater, FL",
      "70900": "Barnstable Town, MA",
      "46340": "Tyler, TX",
      "78100": "Springfield, MA-CT",
      "26180": "Honolulu, HI",
      "33740": "Monroe, LA",
      "38940": "Port St. Lucie-Fort Pierce, FL",
      "11500": "Anniston-Oxford-Jacksonville, AL",
      "12580": "Baltimore-Columbia-Towson, MD",
      "25180": "Hagerstown-Martinsburg, MD-WV",
      "46140": "Tulsa, OK",
      "48660": "Wichita Falls, TX",
      "27140": "Jackson, MS",
      "19300": "Daphne-Fairhope-Foley, AL",
      "17660": "Coeur d'Alene, ID",
      "27780": "Johnstown, PA",
      "29180": "Lafayette, LA",
      "33780": "Monroe, MI",
      "10740": "Albuquerque, NM",
      "17900": "Columbia, SC",
      "19460": "Decatur, AL",
      "19500": "Decatur, IL",
      "39140": "Prescott, AZ",
      "43900": "Spartanburg, SC",
      "14860": "Bridgeport-Stamford-Norwalk, CT",
      "11020": "Altoona, PA",
      "40420": "Rockford, IL",
      "45220": "Tallahassee, FL",
      "28420": "Kennewick-Richland, WA",
      "40380": "Rochester, NY",
      "41740": "San Diego-Carlsbad-San Marcos, CA",
      "46700": "Vallejo-Fairfield, CA",
      "72850": "Danbury, CT",
      "29100": "La Crosse, WI-MN",
      "31140": "Louisville, KY-IN",
      "34820": "Myrtle Beach-Conway-North Myrtle Beach, SC-NC",
      "77200": "Providence-Fall River-Warwick, RI-MA",
      "28740": "Kingston, NY",
      "33860": "Montgomery, AL",
      "40220": "Roanoke, VA",
      "42100": "Santa Cruz-Watsonville, CA",
      "49020": "Winchester, VA-WV",
      "46060": "Tucson, AZ",
      "32820": "Memphis, TN-MS-AR",
      "12260": "Augusta-Richmond County, GA-SC",
      "20500": "Durham-Chapel Hill, NC",
      "22520": "Florence-Muscle Shoals, AL",
      "77350": "Rochester-Dover, NH-ME",
      "24340": "Grand Rapids-Wyoming, MI",
      "19740": "Denver-Aurora-Lakewood, CO",
      "28100": "Kankakee-Bradley, IL",
      "24140": "Goldsboro, NC",
      "28140": "Kansas City, MO-KS",
      "42260": "Sarasota-Bradenton-Venice, FL",
      "49340": "Worcester, MA-CT",
      "15980": "Cape Coral-Fort Myers, FL",
      "33700": "Modesto, CA",
      "39460": "Punta Gorda, FL",
      "11700": "Asheville, NC",
      "14060": "Bloomington-Normal, IL",
      "15540": "Burlington-South Burlington, VT",
      "27500": "Janesville-Beloit, WI",
      "34980": "Nashville-Davidson-Murfreesboro, TN",
      "47900": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
      "18580": "Corpus Christi, TX",
      "35660": "Niles-Benton Harbor, MI",
      "12060": "Atlanta-Sandy Springs-Roswell, GA",
      "16620": "Charleston, WV",
      "17460": "Cleveland-Elyria, OH",
      "34580": "Mount Vernon-Anacortes, WA",
      "46520": "Urban Honolulu, HI",
      "19380": "Dayton, OH",
      "25060": "Gulfport-Biloxi, MS",
      "41500": "Salinas, CA",
      "45060": "Syracuse, NY",
      "16060": "Carbondale-Marion, IL",
      "20700": "East Stroudsburg, PA",
      "26980": "Iowa City, IA",
      "20740": "Eau Claire, WI",
      "15380": "Buffalo-Cheektowaga-Niagara Falls, NY",
      "24580": "Green Bay, WI",
      "44140": "Springfield, MA",
      "22180": "Fayetteville, NC",
      "26620": "Huntsville, AL",
      "28660": "Killeen-Temple-Fort Hood, TX",
      "70750": "Bangor, ME",
      "75700": "New Haven, CT",
      "12620": "Bangor, ME",
      "30340": "Lewiston-Auburn, ME",
      "45820": "Topeka, KS",
      "25420": "Harrisburg-Carlisle, PA",
      "31100": "Los Angeles-Long Beach-Santa Ana, CA",
      "31460": "Madera, CA",
      "17820": "Colorado Springs, CO",
      "42340": "Savannah, GA",
      "49420": "Yakima, WA",
      "15500": "Burlington, NC",
      "16820": "Charlottesville, VA",
      "23540": "Gainesville, FL",
      "40980": "Saginaw, MI",
      "45940": "Trenton, NJ",
      "48700": "Williamsport, PA",
      "27900": "Joplin, MO",
      "44220": "Springfield, OH",
      "12980": "Battle Creek, MI",
      "19780": "Des Moines-West Des Moines, IA",
      "27980": "Kahului-Wailuku-Lahaina, HI",
      "40060": "Richmond, VA",
      "43300": "Sherman-Dennison, TX",
      "17020": "Chico, CA",
      "27340": "Jacksonville, NC",
      "13140": "Beaumont-Port Arthur, TX",
      "24860": "Greenville, SC",
      "15180": "Brownsville-Harlingen, TX",
      "34940": "Naples-Immokalee-Marco Island, FL",
      "43340": "Shreveport-Bossier City, LA",
      "20940": "El Centro, CA",
      "29200": "Lafayette-West Lafayette, IN",
      "33100": "Miami-Fort Lauderdale-West Palm Beach, FL",
      "43780": "South Bend-Mishawaka, IN-MI",
      "24540": "Greeley, CO",
      "33260": "Midland, TX",
      "37900": "Peoria, IL",
      "38900": "Portland-Vancouver-Hillsboro, OR-WA",
      "17300": "Clarksville, TN-KY",
      "36780": "Oshkosh-Neenah, WI",
      "47020": "Victoria, TX",
      "11100": "Amarillo, TX",
      "31340": "Lynchburg, VA",
      "41100": "St. George, UT",
      "45780": "Toledo, OH",
      "23420": "Fresno, CA",
      "41540": "Salisbury, MD",
      "16540": "Chambersburg-Waynesboro, PA",
      "47300": "Visalia-Porterville, CA",
      "13980": "Blacksburg-Christiansburg-Radford, VA",
      "25940": "Hilton Head Island-Bluffton-Beaufort, SC",
      "39580": "Raleigh, NC",
      "16860": "Chattanooga, TN-GA",
      "44700": "Stockton, CA",
      "72400": "Burlington-South Burlington, VT",
      "46660": "Valdosta, GA",
      "16700": "Charleston-North Charleston, SC",
      "21660": "Eugene, OR",
      "26580": "Huntington-Ashland, WV-KY-OH",
      "38860": "Portland-South Portland, ME",
      "40900": "Sacramento--Arden-Arcade-Roseville, CA",
      "11460": "Ann Arbor, MI",
      "26900": "Indianapolis, IN",
      "33140": "Michigan City-La Porte, IN",
      "36420": "Oklahoma City, OK",
      "22020": "Fargo, ND-MN",
      "13780": "Binghamton, NY",
      "37980": "Philadelphia-Camden-Wilmington, PA-NJ-DE",
      "14020": "Bloomington, IN",
      "14460": "Boston-Cambridge-Newton, MA-NH",
      "17780": "College Station-Bryan, TX",
      "21140": "Elkhart-Goshen, IN",
      "27260": "Jacksonville, FL",
      "42220": "Santa Rosa-Petaluma, CA",
      "49620": "York-Hanover, PA",
      "16740": "Charlotte-Concord-Gastonia, NC-SC",
      "31080": "Los Angeles-Long Beach-Anaheim, CA (Note the CBSA code change between 2003 and 2013)",
      "34060": "Morgantown, WV",
      "38220": "Pine Bluff, AR",
      "22140": "Farmington, NM",
      "24660": "Greensboro-High Point, NC",
      "29620": "Lansing-East Lansing, MI",
      "32900": "Merced, CA",
      "38300": "Pittsburgh, PA",
      "25860": "Hickory-Morganton-Lenoir, NC",
      "28940": "Knoxville, TN",
      "14740": "Bremerton-Silverdale, WA",
      "15940": "Canton-Massillon, OH",
      "38060": "Phoenix-Mesa-Scottsdale, AZ",
      "39900": "Reno-Sparks, NV",
      "13460": "Bend-Redmond, OR",
      "21780": "Evansville, IN-KY",
      "39540": "Racine, WI",
      "48140": "Wausau, WI",
      "16300": "Cedar Rapids, IA",
      "39820": "Redding, CA"
}

# Iterate over each year from 2010 to 2023
for year in range(2010, 2024):
    # Fetch data for the current year
    yearly_data = fetch_census_data_for_year(year, api_key)

    # Add a 'Year' column to the DataFrame
    yearly_data['Year'] = year

    # Add a 'City' column to the DataFrame based on the GTCBSA code
    yearly_data['City'] = [cities.get(str(code), 'Not in a metro area') for code in yearly_data['GTCBSA']]

    # Drop duplicate columns (if any)
    yearly_data = yearly_data.loc[:,~yearly_data.columns.duplicated()]

    # Save the DataFrame to a JSON file with a name including the year
    file_name = f'census_data_{year}.json'
    yearly_data.to_json(file_name, orient='records')



# Function to load data from a JSON file into a DataFrame
def load_census_data(year):
    file_name = f'census_data_{year}.json'
    return pd.read_json(file_name)

# Iterate over each year from 2010 to 2023
for year in range(2010, 2024):
    # Load data for the current year
    yearly_data = load_census_data(year)

    # Display the data
    print(f"Data for the year {year}:")
    print(yearly_data.head())  # Display the first few rows of the DataFrame
    print("\n")  # Add a newline for better readability


# Function to load and aggregate data from JSON files for all years
def load_and_aggregate_all_years(start_year, end_year):
    aggregated_data = pd.DataFrame(columns=['City', 'PRTAGE', 'PRFAMNUM', 'PTDTRACE', 'PEEDUCA', 'PEMLR', 'HEFAMINC'])
    for year in range(start_year, end_year + 1):
        file_name = f'census_data_{year}.json'
        with open(file_name, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data)


        aggregated_data = pd.concat([aggregated_data, df], ignore_index=True)
    return aggregated_data

# Load and aggregate data for all years
start_year = 2010
end_year = 2023
all_years_data = load_and_aggregate_all_years(start_year, end_year)

# Clean the data (handle non-logical values and outliers)
# For example, replace non-logical or missing values with NaN

all_years_data['PRTAGE'] = pd.to_numeric(all_years_data['PRTAGE'], errors='coerce')
all_years_data['PRFAMNUM'] = pd.to_numeric(all_years_data['PRFAMNUM'], errors='coerce')
all_years_data['HEFAMINC'] = pd.to_numeric(all_years_data['HEFAMINC'], errors='coerce')

# Aggregate Data by City
city_data = all_years_data.groupby('City').agg({
    'PRTAGE': 'mean',       # Average age
    'PRFAMNUM': 'mean',     # Total count of families
    'PTDTRACE': lambda x: x.mode().iloc[0],  # Most common race/ethnicity
    'PEEDUCA': lambda x: x.mode().iloc[0],   # Most common education level
    'PEMLR': lambda x: x.mode().iloc[0],     # Most common employment status
    'HEFAMINC': 'mean'      # Average household income
}).reset_index()

# Streamlit App
st.title('US Demographic Changes Dashboard (2010-2023)')

# Sidebar for selecting visualizations
visualization_option = st.sidebar.radio('Select Visualization Type', ('Average Age Distribution', 'Employment Status Distribution', 'Household Income Distribution', 'Average Household Income vs. Average Age', 'Race/Ethnicity Distribution'))

# Plot Meaningful Visualizations based on user selection
if visualization_option == 'Average Age Distribution':
  # Bar Plot: Average Age Distribution by City
  fig = px.bar(city_data, x='City', y='PRTAGE', title='Average Age Distribution by City')
  st.plotly_chart(fig, use_container_width=True)

elif visualization_option == 'Employment Status Distribution':
  # Count of each Employment Status by City
  employment_status_counts = city_data.groupby(['City', 'PEMLR']).size().unstack(fill_value=0)
  
  # Plotting
  fig = px.bar(employment_status_counts, x=employment_status_counts.index, 
            y=employment_status_counts.columns,
            labels={'x': 'City', 'y': 'Frequency'}, 
            title='Employment Status Distribution by City')
  fig.update_layout(barmode='stack')  # Stack bars for each city
  st.plotly_chart(fig, use_container_width=True)

elif visualization_option == 'Household Income Distribution':
  # Box Plot: Household Income Distribution by City
  fig = px.box(city_data, x='City', y='HEFAMINC', title='Average Household Income Distribution by City')
  st.plotly_chart(fig, use_container_width=True)

elif visualization_option == 'Average Household Income vs. Average Age':
  # Calculate average household income and average age by city
  avg_income_age = city_data.groupby('City')[['HEFAMINC', 'PRTAGE']].mean().reset_index()

  # Scatter Plot: Average Age vs Average Household Income by City
  fig = px.scatter(avg_income_age, x='HEFAMINC', y='PRTAGE', color='City',
                   title='Average Household Income vs. Average Age by City',
                   hover_data=['City', 'HEFAMINC', 'PRTAGE'],
                   labels={'HEFAMINC': 'Average Household Income', 'PRTAGE': 'Average Age'})
  st.plotly_chart(fig, use_container_width=True)

elif visualization_option == 'Race/Ethnicity Distribution':
  # Bar Plot: Race/Ethnicity Distribution by City
  fig = px.bar(city_data, x='City', y='PTDTRACE', title='Most Common Race/Ethnicity by City', color='PTDTRACE', color_discrete_map={
      "07": "White-AI",
      "20": "W-AI-HP",
      "08": "White-Asian",
      "17": "W-B-A",
      "16": "W-B-AI",
      "06": "White-Black",
      "12": "Black-HP",
      "18": "W-B-HP",
      "21": "W-A-HP",
      "02": "Black only",
      "05": "Hawaiian/Pacific Islander Only",
      "22": "B-AI-A",
      "09": "White-HP",
      "14": "AI-HP",
      "10": "Black-AI",
      "23": "W-B-AI-A",
      "11": "Black-Asian",
      "13": "AI-Asian",
      "04": "Asian only",
      "15": "Asian-HP",
      "25": "Other 3 Race Combinations",
      "01": "White only",
      "26": "Other 4 and 5 Race Combinations",
      "19": "W-AI-A",
      "24": "W-AI-A-HP",
      "03": "American Indian, Alaskan Native Only"
  })
  fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
  st.plotly_chart(fig, use_container_width=True)
