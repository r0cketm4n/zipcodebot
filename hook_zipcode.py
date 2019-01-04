import ast
import requests
import sys


zipcode_data = requests.get("https://pastebin.com/raw/Je0uGEyX").json()
incoming_order = Hook['params']
convert_frac = 0.621371
try:
    input_zip = incoming_order['zipcode']
    input_zip[4]
    if len(input_zip) != 5:
        raise IndexError()
    for c in input_zip:
        c = int(c)
except Exception:
    print("invalid zipcode or not supplied!")
    sys.exit(0)
nearby_zips = requests.get("https://secure.geonames.net/findNearbyPostalCodesJSON?postalcode=" + input_zip + "&country=US&radius=50&username=r0cketm4n&maxRows=15").json()["postalCodes"]
print("state: " + nearby_zips[0]["adminName1"])
try:
    print(nearby_zips[0]["placeName"] + ": " + ", ".join(zipcode_data[input_zip]))
except Exception:
    print(nearby_zips[0]["placeName"] + ": no locations found!")
print("")
print("nearby zip codes")
del nearby_zips[0]
for zipcode in nearby_zips:
    if zipcode["postalCode"] != input_zip:
        try:
            print(zipcode["placeName"] + " (" + zipcode["postalCode"] + "): " + ", ".join(zipcode_data[zipcode["postalCode"]]) + " | distance " + str(round(float(zipcode["distance"]) * convert_frac, 2)) + " miles")
        except Exception:
            print(zipcode["placeName"] + " (" + zipcode["postalCode"] + "): " + "no locations found | distance " + str(round(float(zipcode["distance"]) * convert_frac, 2)) + " miles")