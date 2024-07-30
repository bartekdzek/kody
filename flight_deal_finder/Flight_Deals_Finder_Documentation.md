# Flight Deals Finder Documentation

## Overview

The Flight Deals Finder is a Python program designed to search for the cheapest flight deals from a specified origin airport to various destinations listed in a Google Sheet. It uses the Amadeus API to fetch flight information and updates the Google Sheet with IATA codes for cities. The program also sends notifications if a cheaper flight is found compared to a specified threshold.

## Components

The program consists of several main components, each defined in separate files:

1. `main.py` - The main script that orchestrates the program's execution.
2. `flight_search.py` - Contains the `FlightSearch` class responsible for interacting with the Amadeus API.
3. `flight_data.py` - Defines the `FlightData` class and the `find_cheapest_flight` function.
4. `data_manager.py` - Contains the `DataManager` class responsible for interacting with the Google Sheet via the Sheety API.

## Files and Classes

### `main.py`

The main script that ties everything together.

- **Setup:**
  - Creates instances of `DataManager` and `FlightSearch`.
  - Fetches destination data from the Google Sheet.
  - Sets the origin city IATA code (e.g., "LON" for London).

- **Update IATA Codes:**
  - Iterates over the destination data and updates any missing IATA codes using the `FlightSearch.get_destination_code` method.
  - Updates the Google Sheet with the new IATA codes.

- **Search for Flights:**
  - Defines the date range for the flight search (from tomorrow to six months from today).
  - For each destination, it checks for flights and identifies the cheapest one using `FlightSearch.check_flights` and `find_cheapest_flight`.
  - Prints notifications if a cheaper flight is found.

### `flight_search.py`

Handles interactions with the Amadeus API.

- **Class: `FlightSearch`**
  - **Attributes:**
    - `_api_key` and `_api_secret` for Amadeus API authentication.
    - `_token` to store the authentication token.
  - **Methods:**
    - `_get_new_token`: Fetches a new bearer token from the Amadeus API.
    - `get_destination_code`: Retrieves the IATA code for a given city.
    - `check_flights`: Searches for flights between the origin and destination cities within the specified date range.

### `flight_data.py`

Defines the structure for flight data and a function to find the cheapest flight.

- **Class: `FlightData`**
  - **Attributes:**
    - `price`: Flight price.
    - `origin_airport`: Origin airport IATA code.
    - `destination_airport`: Destination airport IATA code.
    - `out_date`: Departure date.
    - `return_date`: Return date.

- **Function: `find_cheapest_flight`**
  - Takes flight data and finds the flight with the lowest price.
  - Returns an instance of `FlightData`.

### `data_manager.py`

Handles interactions with the Google Sheet via the Sheety API.

- **Class: `DataManager`**
  - **Methods:**
    - `get_destination_data`: Fetches destination data from the Google Sheet.
    - `update_destination_codes`: Updates the Google Sheet with IATA codes for each city.

## How to Use

1. **Setup:**
   - Ensure you have the necessary API keys for the Amadeus API and access to the Sheety API.
   - Update the `ORIGIN_CITY_IATA` in `main.py` with your desired origin city's IATA code.

2. **Run the Program:**
   - Execute `main.py`. The script will fetch destination data, update IATA codes, search for flights, and notify if cheaper flights are found.

3. **Dependencies:**
   - Install the required Python packages using `pip`:
     ```bash
     pip install requests
     ```

## API References

- **Amadeus API:**
  - [Amadeus Self-Service APIs](https://developers.amadeus.com/self-service)

- **Sheety API:**
  - [Sheety API Documentation](https://sheety.co/docs)

## Example

Here's a sample output of the program:

```
sheet_data:
 [{'city': 'Paris', 'iataCode': 'CDG', 'lowestPrice': 100, 'id': 1}, ...]

Getting flights for {'city': 'Paris', 'iataCode': 'CDG', 'lowestPrice': 100, 'id': 1}
Using this token to get destination YOUR_TOKEN
Status code 200. Airport IATA: ...
Lowest price to CDG is £90
Lower price flight found to Paris!
```

This documentation provides an overview of the Flight Deals Finder, including its components, usage, and example output. The program is designed to automate the process of finding and notifying about the cheapest flight deals, making it a valuable tool for frequent travelers and travel planners.
