# address2geocoord
Addr_to_Coord_GUI.py application is intended for conversion of home addresses to approximate location coordinates (latitude and longitude).
GeoPy Nominatim API is used for this purpose (https://operations.osmfoundation.org/policies/nominatim/).

The program accepts a CSV input file containing the following columns: 
	id, address, city, state, zip

A separate geopy query is consecutively executed for each row of input data with a 1-second pause in between to accommodate Nominatim user policy.
Each query returns latitude and longitude, which are saved in a data frame along with the input parameters.
Once all queries are executed, data frame is saved to a CSV file.

The program outputs a CSV file "Converted_data.csv" containing the following columns:
	id, address, city, state, zip, latitude, longitude

DEPENDENCIES:
Python command prompt environment
Packages:
	numpy
	pandas
	csv
	tkinter
	time
	geopy

 Based on LocationEngineering code from RIS application by Vanessa Nobles and Dr. Li Liu (https://github.com/liliulab/ris).
