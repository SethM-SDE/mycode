#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    #startdate = "start_date=2019-11-11"

    # prompt for start and end dates
    print("Enter a start date for your search(YYYY-MM-DD):")
    startdate = input('>')

    print('Enter an end date for your search (YYYY-MM-DD)(options, default 7 days after start):')
    enddate = input('>')

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    # print(neodata)
    
    #get the largest and closest info
    largest = ""
    largest_date = ""
    largest_name = ""
    closest = ""
    closest_date = ""
    closest_name = ""

    for day in neodata['near_earth_objects']:
        for obj in neodata['near_earth_objects'][day]:
            if largest == "":
                largest = obj["estimated_diameter"]["miles"]["estimated_diameter_max"]
                largest_date = obj["close_approach_data"][0]["close_approach_date"]
                largest_name = obj["name"]
            elif obj["estimated_diameter"]["miles"]["estimated_diameter_max"] > largest:
                largest = obj["estimated_diameter"]["miles"]["estimated_diameter_max"]
                largest_date = obj["close_approach_data"][0]["close_approach_date"]
                largest_name = obj["name"]

            if closest == "":
                closest = obj["close_approach_data"][0]["miss_distance"]["miles"]
                closest_date = obj["close_approach_data"][0]["close_approach_date"]
                closest_name = obj["name"]
            elif obj["close_approach_data"][0]["miss_distance"]["miles"] < closest:
                closest = obj["close_approach_data"][0]["miss_distance"]["miles"]
                closest_date = obj["close_approach_data"][0]["close_approach_date"]
                closest_name = obj["name"]

    print(f'Data for range {startdate} to {enddate}:')
    print(f'Number of close objects: {neodata["element_count"]}')
    print(f'Largest object is {largest_name} on {largest_date} at {largest} miles in max diameter.')
    print(f'Closest object is {closest_name} on {closest_date} at {closest} miles from Earth.')

if __name__ == "__main__":
    main()

