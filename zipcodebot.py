import json
import re
import requests
import string
import sys
import time
import tqdm
import traceback
import unidecode


def onetengrill():
    sesh = requests.Session()
    response = sesh.get("https://www.110grill.com/locations2/")
    zips = []
    for link in re.findall('href\="(https\://www\.110grill\.com/locations/.*?)"', response.content):
        response = sesh.get(link)
        if "Opening Soon" in response.content:
            continue
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except:
            print response.url
    return list(set(zips))


def onethreeonemain():
	sesh = requests.Session()
	response = sesh.get("https://www.131-main.com")
	urls = list(set(re.findall('Location" href\="(https:\/\/www\.131-main\.com\/.*?)"', str(response.content))))
	zips = []
	for url in urls:
		response = sesh.get(url)
		try:
			zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
		except Exception:
			print(response.url)
	return zips


def fourriverssmokehouse():
    response = requests.get("https://4rsmokehouse.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def seventeenthstreetbbq():
    return ["62966", "62559"]


def abuelos():
    response = requests.get("https://www.abuelos.com/restaurants/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def alexanderssteakhouse():
	headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
	response = requests.get("https://alexanderssteak.com/locations/", headers=headers)
	zips = list(set(re.findall('\w{2} (\d{5})', str(response.content))))
	return zips


def alicartrestaurantgroup():
	sesh = requests.Session()
	response = sesh.get("https://www.carminesnyc.com")
	urls = list(set(re.findall('"(https:\/\/www\.carminesnyc\.com\/locations\/.*?)"', str(response.content))))
	response = sesh.get("https://www.virgilsbbq.com")
	urls = urls + list(set(re.findall('"(https:\/\/www\.virgilsbbq\.com\/locations\/.*?)"', str(response.content))))
	zips = []
	for url in urls:
	    response = sesh.get(url)
	    try:
	        zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
	    except Exception:
	        continue
	return zips


def alspizza():
    response = requests.get("https://www.alspizza.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def amctheatres():
    sesh = requests.Session()
    response = sesh.get("https://www.amctheatres.com/movie-theatres")
    links = list(set(re.findall('href\="(/movie-theatres/.*?)"', response.content)))
    zips = []
    for link in links:
        response = sesh.get("https://www.amctheatres.com" + link)
        zips += list(set(re.findall('postalCode"\:"(\d{5})"', response.content)))
    return list(set(zips))


def amfbowling():
    response = requests.get("https://www.amf.com/bowlero-location/finder?_format=json").json()
    zips = []
    for store in response:
        zips.append(str(store["zip"]))
    return list(set(zips))

#def anchorbar():

def aquitainegroup():
	response = requests.get("http://www.aquitainegroup.com/our-restaurants/")
	zips = list(set(re.findall('\w{2} (\d{5})', str(response.content))))
	zips += list(set(re.findall('\w{2}, (\d{5})', str(response.content))))
	return zips


def arbys():
    sesh = requests.Session()
    response = sesh.get("https://locations.arbys.com/index.html")
    states = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.arbys.com/" + state)
        if "/" in state:
            zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
        else:
            cities = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
            for city in cities:
                response = sesh.get("https://locations.arbys.com/" + city)
                zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return list(set(zips))


def arnoldpalmersrestaurant():
	return ['92253']


def aroogas():
    response = requests.get("http://www.aroogas.com/locations")
    zips = re.findall('postal-code"\>(\d+)', response.content)
    return list(set(zips))


def atriasrestaurants():
	response = requests.get("http://atrias.com/wp/locations/")
	zips = list(set(re.findall('\w{2} (\d{5})', str(response.content))))
	return zips


def avenirrestaurant():
	return ['94301']


def baggerdavesburgertavern():
	sesh = requests.Session()
	response = sesh.get("https://www.baggerdaves.com")
	urls = list(set(re.findall('"(https:\/\/www\.baggerdaves\.com\/locations\/.*?)"', str(response.content))))
	zips = []
	for url in urls:
	    response = sesh.get(url)
	    try:
	        zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
	    except Exception:
	        continue
	return zips

def bakerscrust():
    sesh = requests.Session()
    response = sesh.get('https://bakerscrust.com')
    urls = list(set(re.findall('"\/locations\/(.*?)"', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://bakerscrust.com/locations/' + url)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def bamboosushi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    sesh = requests.Session()
    response = sesh.get('https://bamboosushi.com/restaurants/', headers=headers)
    urls = list(set(re.findall('href\="https:\/\/bamboosushi\.com\/restaurant\/(.*?)"', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://bamboosushi.com/restaurant/' + url, headers=headers)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def barillarestaurants():
    sesh = requests.Session()
    response = sesh.get('https://www.casabarilla.com')
    urls = list(set(re.findall('href\="\/(location-.*?)"', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://www.casabarilla.com/' + url)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def barlouie():
    response = requests.get("https://www.barlouie.com/locations/states")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def barneysgourmethamburgers():
    response = requests.get("http://www.barneyshamburgers.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips

def barrybagels():
    sesh = requests.Session()
    response = sesh.get('https://barrybagels.com/locations/')
    urls = list(set(re.findall('href\="(.*?)" class\="icon', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://barrybagels.com/locations/' + url)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def beachesrestaurantbar():
    response = requests.get("http://beachesrestaurantandbar.com")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips

def beaujospizza():
    sesh = requests.Session()
    response = sesh.get('https://www.beaujos.com')
    urls = list(set(re.findall('\/pizza-locations\/(.*?)/', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://www.beaujos.com/pizza-locations/' + url)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def bigoniontaverngroup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    response = requests.get("https://www.bigoniontaverngroup.com", headers=headers)
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips

def biscuitscafe():
    sesh = requests.Session()
    states = ['arizona', 'oregon', 'washington']
    zips = []
    for state in states:
        response = sesh.get("http://www.biscuitscafe.com/" + state + "/")
        zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def blackbeardiner():
    response = requests.get("https://passport.blackbeardiner.com/api/locations?callback=callback_for_jsonp")
    zips = list(set(re.findall('zip":"(\d+)"', response.content)))
    return zips

def blackrockbargrill():
    sesh = requests.Session()
    response = sesh.get('https://www.blackrockrestaurants.com')
    urls = list(set(re.findall('href="(https:\/\/\www.blackrockrestaurants\.com\/.*?)" target\="_self" id\="comp', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get(url)
        try:
            zips.append(re.search('\w{2} (\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def blackwalnutcafe():
    response = requests.get("https://www.blackwalnutcafe.com/locations/")
    zips = list(set(re.findall('(\d{5})</p>', response.content)))
    return zips


def blakeslotaburger():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.lotaburger.com/locations/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    data = {
        'action': 'find_locations',
        'address': '',
        'radius_val': '0'
    }
    response = requests.post('https://www.lotaburger.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips

def blazepizza():
    response = requests.get("https://www.blazepizza.com/locations/")
    zips = list(set(re.findall('zip":"(\d+)"', response.content)))
    return zips

def blindbarber():
    sesh = requests.Session()
    response = sesh.get('https://blindbarber.com')
    urls = list(set(re.findall('href="(\/pages\/.*?)" class="nav-link sub-nav-link"', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://blindbarber.com/' + url)
        try:
            zips.append(re.search('\w{2} (\d{5})</p>', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def bluewatergrill():
    sesh = requests.Session()
    response = sesh.get('https://www.bluewatergrill.com/locations')
    urls = list(set(re.findall('href="(\/locations\/.*?)"', str(response.content))))
    zips = []
    for url in urls:
        response = sesh.get('https://www.bluewatergrill.com' + url)
        try:
            zips.append(re.search('class\="zip-code">(\d{5})', str(response.content)).group(1))
        except Exception:
            continue
    return zips

def bobssteakandchop():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://bobs-steakandchop.com/locations/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get("http://bobs-steakandchop.com/locations/", headers=headers)
    cords = re.findall('lng\: (-\d+\.\d+), lat\: (\d+\.\d+)\}', response.content)
    del cords[1]
    zips = []
    sesh = requests.Session()
    for cord in cords:
        response = sesh.get("http://api.geonames.org/findNearbyPostalCodesJSON?lat=" + cord[1] + "&lng=" + cord[0] + "&username=r0cketm4n&maxRows=1").json()
        zips.append(str(response["postalCodes"][0]["postalCode"]))
        time.sleep(1)
    return list(set(zips))


def breakfastrepublic():
    response = requests.get("http://www.breakfastrepublic.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def beansbrewscoffeehouse():
    response = requests.get("http://www.beansandbrews.com/coffee-shops/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def bigcityburrito():
    response = requests.get("http://www.bigcityburrito.com/find.php")
    zips = re.findall('Avenue (\d+)', response.content)
    return zips


def blackshoehospitality():
    response = requests.get("https://blackshoehospitality.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def broadwaypizza():
    response = requests.get("http://www.broadwaypizza.com/locations.html")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def brueggersbagels():
    sesh = requests.Session()
    response = sesh.get("https://locations.brueggers.com/us")
    states = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.brueggers.com/" + state)
        if state.count("/") > 1:
            zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
        else:
            cities = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
            for city in cities:
                city = city.replace("../", "")
                response = sesh.get("https://locations.brueggers.com/" + city)
                zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
    return list(set(zips))


def burgersandbeer():
    return ['92270', '85364', '92591', '92243', '92201']


def burgerlounge():
    response = requests.get("https://www.burgerlounge.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def burntwoodtavern():
    response = requests.get("https://www.burntwoodtavern.com/locations-1/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def capriottissandwichshop():
    response = requests.get("https://www.capriottis.com/wp-content/uploads/lr-geo-content/locations-data.json").json()["locations"]
    zips = []
    for store in zips:
        zips.append(str(store["postal_code"]))
    return list(set(zips))


def cariboucoffee():
    sesh = requests.Session()
    response = sesh.get("https://locations.cariboucoffee.com/us")
    states = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.cariboucoffee.com/" + state)
        if state.count("/") > 1:
            zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
        else:
            cities = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
            for city in cities:
                city = city.replace("../", "")
                response = sesh.get("https://locations.cariboucoffee.com/" + city)
                zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
    return list(set(zips))


def chuystexmex():
    response = requests.get("https://www.chuys.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def cowboychicken():
    response = requests.get("https://www.cowboychicken.com/locations/")
    zips = list(set(re.findall('\w{2}, (\d{5})', response.content)))
    return zips


# def chamagaucha():
#     response = requests.get("")

def dintaifung():
    response = requests.get("http://dintaifungusa.com/locations_us/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def districttaco():
    response = requests.get("https://www.districttaco.com/pages/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def doolittleswoodfiredgrill():
    sesh = requests.Session()
    response = sesh.get("https://doolittles.com/locations/")
    zips = []
    for link in re.findall('href\="(https\://doolittles\.com/locations/.*?)"', response.content):
        response = sesh.get(link)
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except:
            pass
    return list(set(zips))


def elcholo():
    sesh = requests.Session()
    response = sesh.get("http://elcholo.com")
    zips = []
    for link in re.findall('href\="(http\://elcholo\.com/location/.*?)"', response.content):
        response = sesh.get(link)
        zips.append(re.search('\w{2}(?:,)? (\d{5})', response.content).group(1))
    return list(set(zips))


def empireeats():
    return ['27601', '27701', '27607']


def einsteinbrosbagels():
    sesh = requests.Session()
    response = sesh.get("https://locations.einsteinbros.com/us")
    states = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.einsteinbros.com/" + state)
        print response.url
        if state.count("/") > 1:
            zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
        else:
            cities = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
            for city in cities:
                city = city.replace("../", "")
                response = sesh.get("https://locations.einsteinbros.com/" + city)
                print response.url
                zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
    return list(set(zips))


def fatheadsbrewery():
    response = requests.get("https://fatheads.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def fatzsouthernkitchen():
    response = requests.geet("https://fatz.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def floyds99barbershop():
    zips = []
    data = {
        'StartIndex': '0',
        'EndIndex': '10000',
        'Longitude': '0',
        'Latitude': '0',
        'F': 'GetAllLocations'
    }
    response = requests.post('https://www.floydsbarbershop.com/modules/staff/ajax.aspx', data=data).json()
    for store in response:
        zips.append(str(store["Zip"]))
    return list(set(zips))


def flyingstarcafe():
    response = requests.get("https://www.flyingstarcafe.com/find-us/")
    zips = re.findall('postal-code"\>(\d+)', response.content)
    return zips


def frischsbigboy():
    response = requests.get("https://www.frischs.com/locations/")
    zips = list(set(re.findall('\w{2}, (\d{5})', response.content)))
    return zips


def froyoyogurt():
    response = requests.get("http://www.froyoyogurt.com/locations/")
    zips = list(set(re.findall('\w{2}, (\d{5})', response.content)))
    return zips


def fuddruckers():
    response = requests.get("https://www.fuddruckers.com/locations/all")
    zips = list(set(re.findall('\w{2}, (\d{5})', response.content)))
    return zips


def garretpopcornshops():
    response = requests.get("https://www.garrettpopcorn.com/api/v1/dealers?").json()["dealers"]
    zips = []
    for store in response:
        if store["properties"]["sectionName"] == "UNITED STATES":
            zips.append(str(store["postalCode"]))
    return list(set(zips))


def goodwoodbbq():
    response = requests.get("https://goodwoodbbq.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def graetersicecream():
    response = requests.get("https://www.graeters.com/neighborhood-locations")
    zips = list(set(re.findall(', (\d{5})', response.content)))
    return zips


def granitecitycadillacranch():
    sesh = requests.Session()
    response = sesh.get("https://www.gcfb.com/locations/")
    states = re.findall('value="([A-Za-z ]+)"', re.search('locationSelect"\>(.*?)\</select\>', response.content, re.DOTALL).group(1))
    zips = []
    for state in states:
        response = sesh.get("https://www.gcfb.com/locations/?l=" + state)
        zips += list(set(re.findall(state + ' (\d{5})', response.content)))
    zips += ['15205', '55425', '20745', '33183']
    return list(set(zips))


def grimadlispizzeria():
    response = requests.get("https://www.grimaldispizzeria.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def harrysseafoodgrille():
    response = requests.get("https://hookedonharrys.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def hillstonerestaurantgroup():
    response = requests.get("https://hillstone.com/locations/")
    zips = re.findall("postalCode'\>(\d+)", response.content)
    return list(set(zips))


def hopjacks():
    response = requests.get("http://hopjacks.net/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def houlihans():
    sesh = requests.Session()
    response = sesh.get("https://www.houlihans.com/find-a-location")
    zips = []
    for link in re.findall('"(/my\-houlihans/.*?)"', response.content):
        response = sesh.get("https://www.houlihans.com" + link)
        zips.append(re.search('postalCode"\>(\d+)', response.content).group(1))
    return list(set(zips))


def huckleberrys():
    response = requests.get("http://huckleberrys.org/locations.html")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def hurricanegrillwings():
    response = requests.get("https://hurricanewings.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def jambajuice():
    response = requests.get("https://momentfeed-prod.apigee.net/api/llp.json?auth_token=PQUBOCBNLKOUIYUP&country=US&sitemap=true").json()
    zips = []
    for store in response:
        zips.append(str(store["store_info"]["postcode"]))
    return list(set(zips))


def jeffrubyssteakhouse():
    sesh = requests.Session()
    response = sesh.get("https://www.jeffruby.com/restaurants")
    places = re.findall('(https\://www\.jeffruby\.com/.*?)/private\-dining', response.content)
    zips = []
    for place in places:
        response = sesh.get(place)
        zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
    return list(set(zips))


def jimnnicksbbq():
    response = requests.get("https://www.jimnnicks.com/wp-content/themes/jnn/jnn-locations/locations.php").json()
    zips = []
    for store in response:
        zips.append(str(store["properties"]["zip"]))
    return list(set(zips))


def jimsrestaurants():
    response = requests.get("https://www.jimsrestaurants.com/locations")
    zips = re.findall('postal-code"\>(\d+)', response.content)
    return zips


def kabukirestaurants():
    sesh = requests.Session()
    response = sesh.get("https://www.kabukirestaurants.com/locations/")
    zips = []
    for link in re.findall('"(/location/.*?/)"', response.content):
        response = sesh.get("https://www.kabukirestaurants.com" + link)
        zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
    return list(set(zips))


def krystal():
    sesh = requests.Session()
    response = sesh.get("https://locations.krystal.com/index.html")
    states = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.krystal.com/" + state)
        if "/" in state:
            zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
        else:
            cities = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
            for city in cities:
                response = sesh.get("https://locations.krystal.com/" + city)
                zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return list(set(zips))


def larkburger():
    response = requests.get("http://larkburger.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def larosaspizzeria():
    response = requests.get("https://www.larosas.com/pizzeria.aspx")
    return list(set(re.findall('zip="(\d+)"', response.content)))


def lupetortilla():
    response = requests.get("https://tex-mex.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def mainevent():
    response = requests.get("https://www.mainevent.com/MEOne/GetPageContentByPageId/?PageId=5&LanguageId=1&StoreCode=")
    zips = list(set(re.findall('Zip":"(\d+)"', response.content)))
    return zips


def mamamargies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    response = requests.get("https://www.mamamargies.com/locations/", headers=headers)
    zips = list(set(re.findall('\<br \/\>\\n(\d{5})', response.content)))
    return zips


def manhattanbagels():
    sesh = requests.Session()
    response = sesh.get("https://locations.manhattanbagel.com/us")
    states = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.manhattanbagel.com/" + state)
        if state.count("/") > 1:
            zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
        else:
            cities = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
            for city in cities:
                city = city.replace("../", "")
                response = sesh.get("https://locations.manhattanbagel.com/" + city)
                zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
    return list(set(zips))


def marcustheatres():
    response = requests.get("http://www.marcustheatres.com/theatre-locations")
    zips = list(set(re.findall('postal\-code"\>(\d+)', response.content)))
    return zips


def maxiesrestaurants():
    return ['53213']


def meatheadsburgerfries():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    response = requests.get("https://www.meatheadsburgers.com/locations-2/", headers=headers)
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def missionbbq():
    sesh = requests.Session()
    response = sesh.get('https://mission-bbq.com/locations')
    ids = re.findall('(\d+)', re.search('\<select id\="categories\-1".*?Select State(.*?)\</select\>', response.content, re.DOTALL).group(1))
    zips = []
    for _id in ids:
        params = (
            ('option', 'com_jbusinessdirectory'),
            ('Itemid', '240'),
        )
        data = {
            'option': 'com_jbusinessdirectory',
            'view': 'search',
            'resetSearch': '1',
            'preserve': '0',
            'geo-latitude': '',
            'geo-longitude': '',
            'geolocation': '',
            'categorySearch': _id
        }
        response = sesh.post('https://mission-bbq.com/index.php', params=params, data=data)
        zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def mjrtheatres():
    response = requests.get("https://www.mjrtheatres.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def motomaki():
    sesh = requests.Session()
    response = sesh.get("http://motomaki.com")
    zips = []
    for link in re.findall("href\='(/location/.*?)'", response.content):
        response = sesh.get("http://motomaki.com" + link)
        zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
    return list(set(zips))


def mshackburgers():
    return ['32801', '32204', '32246', '32233']


def nandosperiperi():
    response = requests.get("https://www.nandosperiperi.com/eat/restaurants")
    zips = list(set(re.findall('\w, (\d{5})', response.content)))
    return zips


def newkseatery():
    response = requests.get("https://newks.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def noahsbagels():
    sesh = requests.Session()
    response = sesh.get("https://locations.noahs.com/us")
    states = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.noahs.com/" + state)
        if state.count("/") > 1:
            zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
        else:
            cities = re.findall('Directory\-listLink" href\="(.*?)"', response.content)
            for city in cities:
                city = city.replace("../", "")
                response = sesh.get("https://locations.noahs.com/" + city)
                zips += list(set(re.findall('c\-address\-postal\-code" \>(\d{5})\<', response.content)))
    return list(set(zips))


def noodlescompany():
    sesh = requests.Session()
    response = sesh.get("https://locations.noodles.com/index.html")
    states = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.noodles.com/" + state)
        if "/" in state:
            zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
        else:
            cities = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
            for city in cities:
                response = sesh.get("https://locations.noodles.com/" + city)
                zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return list(set(zips))


def nyxprofessionalmakeup():
    response = requests.get("https://stores.nyxcosmetics.com/directory/index.html")
    zips = list(set(re.findall('c-address-postal-code" \>(\d+)', response.content)))
    return zips


def ojoslocos():
    sesh = requests.Session()
    response = sesh.get("https://www.ojoslocos.com/Locations.aspx")
    ids = list(set(re.findall('Location\.aspx\?Id\=(\d+)', response.content)))
    zips = []
    for _id in ids:
        response = sesh.get("https://www.ojoslocos.com/Location.aspx?Id=" + _id)
        try:
            zips.append(re.search('\w{2}(?: )? (\d{5})', response.content).group(1))
        except Exception:
            print response.url
    return list(set(zips))


def oklahomajoes():
    sesh = requests.Session()
    response = sesh.get("http://okjoes.com/")
    zips = []
    for link in re.findall('"(http\://okjoes\.com/locations/.*?)"', response.content):
        response = sesh.get(link)
        zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
    return list(set(zips))


def parryspizza():
    response = requests.get("https://parryspizza.com/locations/")
    zips = re.findall('postalCode"\>(\d+)', response.content)
    return list(set(zips))


def pashamediterraneangrill():
    response = requests.get("https://www.gopasha.com/locations/")
    zips = list(set(re.findall('TX (\d{5})', response.content)))
    return zips


def patxispizza():
    response = requests.get("https://www.patxispizza.com/Pages/OcLocations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def perryssteakhouse():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }
    response = requests.get("https://perryssteakhouse.com/locations/", headers=headers)
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def piadaitalianstreetfood():
    response = requests.get("https://mypiada.com/locations")
    zips = list(set(re.findall('zip\: "(\d+)"', response.content)))
    return zips


def pinchers():
    sesh = requests.Session()
    sesh.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = sesh.get("https://www.pinchersusa.com/locations.php")
    links = re.findall('href\="(.*?)"', re.search('\<div class\="locstt"\>(.*?)\</div\>', response.content, re.DOTALL).group(1))
    zips = []
    for link in links:
        response = sesh.get("https://www.pinchersusa.com/" + link)
        zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
    return list(set(zips))


def planetsub():
    response = requests.get("https://planetsub.com/locations/")
    cords = re.findall("\@(\d+\.\d+),(\-?\d+\.\d+),\d+z", response.content)
    zips = []
    sesh = requests.Session()
    for cord in cords:
        response = sesh.get("htt    print response.contentp://api.geonames.org/findNearbyPostalCodesJSON?lat=" + cord[0] + "&lng=" + cord[1] + "&username=r0cketm4n&maxRows=1").json()
        zips.append(str(response["postalCodes"][0]["postalCode"]))
        time.sleep(1)
    return list(set(zips))


def potbelly():
    response = requests.get("https://api-origin.potbelly.com/proxy/all-locations").json()
    zips = []
    for store in response:
        zips.append(str(store["location"]["postal_code"]))
    return list(set(zips))


def punchpizza():
    response = requests.get("https://punchpizza.nuorders.com/service/locations.json").json()["locations"]
    zips = []
    for store in response:
        zip = str(store["postal_code"])
        if len(zip) == 5:
            zips.append(zip)
    return list(set(zips))


def quakersteaklube():
    response = requests.get("http://thelube.com/category/locations/")
    zips = re.findall(' \/\>[A-Za-z \.]+, \w+ (\d+)', response.content)
    return list(set(zips))


def redrockbrewing():
    response = requests.get("http://redrockbrewing.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def romanosmacaronigrill():
    response = requests.get("https://www.macaronigrill.com/locations/all-locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def sallybeautysupply():
    response = requests.get("https://maps.sallybeauty.com/api/getAutocompleteData")
    return list(set(re.findall('(\d{5})', response.content)))


def salsaritas():
    response = requests.get("https://salsaritas.com/locations/")
    zips = list(set(re.findall('postal_code":"(\d+)"', response.content)))
    return zips


def saltcreekgrille():
    return ['92629', '90245', '91355', '08540', '07760']


def saltiron():
    return ['98020']


def sakesushi():
    response = requests.get("http://www.sushisakemiami.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def schnuckmarkets():
    response = requests.get("https://nourish.schnucks.com/store-info-api/stores/").json()["data"]
    zips = []
    for store in response:
        zips.append(str(store["zip"]))
    return zips


def scottysbrewhouse():
    response = requests.get("https://www.scottysbrewhouse.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def scramblermaries():
    response = requests.get("http://scramblersrestaurants.com/wp-content/plugins/superstorefinder-wp/ssf-wp-xml.php?wpml_lang=")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def seaislandshrimphouse():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get("https://www.shrimphouse.com/locations/", headers=headers)
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def shoneys():
    response = requests.get("https://www.shoneys.com/stores.json").json()
    zips = []
    for place in response:
        zips.append(str(place["zip"]))
    return list(set(zips))


def skylinechili():
    sesh = requests.Session()
    places = ["OH", "KY", "FL", "IN"]
    zips = []
    for place in places:
        response = sesh.get("https://www.skylinechili.com/locations.php?loc=" + place)
        zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def soundendbuttery():
    response = requests.get("http://southendbuttery.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def souplantation():
    response = requests.get("https://souplantation.com/wp-admin/admin-ajax.php?action=store_search&lat=37.09024&lng=-95.71289100000001&max_results=999&search_radius=25&autoload=1").json()
    zips = []
    for store in zips:
        zips.append(str(store["zip"]))
    return zips


def spangles():
    response = requests.get("https://www.spanglesinc.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def stansdonuts():
    response = requests.get("https://stansdonuts.com/wp-admin/admin-ajax.php?action=store_search&lat=41.87811&lng=-87.6298&max_results=25&search_radius=100&autoload=1").json()
    zips = []
    for store in zips:
        zips.append(str(store["zip"]))
    return zips


def starkys():
    return ['59715']


def starrrestaurants():
    sesh = requests.Session()
    sesh.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = sesh.get("https://starr-restaurants.com/")
    zips = []
    for link in re.findall('href\="(https\://starr\-restaurants\.com/restaurants/.*?/)"', response.content):
        response = sesh.get(link)
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except:
            pass
    zips += ['33139', '20002', '19103']
    return list(set(zips))


def strizzis():
    return ['94550', '94538', '94556']


def tacodeli():
    sesh = requests.Session()
    response = requests.get("https://www.tacodeli.com/locations/", headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"})
    zips = []
    for rest in re.findall('lat":"(.*?)","lng":"(.*?)"', response.content):
        response = sesh.get("http://api.geonames.org/findNearbyPostalCodesJSON?lat=" + rest[0] + "&lng=" + rest[1   ] + "&username=r0cketm4n&maxRows=1").json()
        zips.append(str(response["postalCodes"][0]["postalCode"]))
        time.sleep(1)
    return list(set(zips))


def tacomacrestaurants():
    sesh = requests.Session()
    response = sesh.get("https://locations.tacomac.com/index.html")
    states = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
    zips = []
    for state in states:
        response = sesh.get("https://locations.tacomac.com/" + state)
        if "/" in state:
            zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
        else:
            cities = re.findall('c-directory-list-content-item-link" href\="(.*?)"', response.content)
            for city in cities:
                response = sesh.get("https://locations.tacomac.com/" + city)
                zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return list(set(zips))


def tahoejoes():
    response = requests.get("https://www.tahoejoes.com/wp-content/plugins/superstorefinder-wp/ssf-wp-xml.php?wpml_lang=&t=1544157620042")
    zips = list(set(re.findall('\w (\d{5})', response.content)))
    return zips


def tarkaindiankitchen():
    response = requests.get("https://tarkaindiankitchen.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def tastidlite():
    response = requests.get("https://www.kahalamgmt.com/locator/index.php?brand=td&mode=map&latitude=37.09024&longitude=-95.712891&q=&pagesize=0")
    zips = list(set(re.findall('"Zip":"(\d{5})"', response.content)))
    return zips


def tedshotdogs():
    response = requests.get("https://www.tedshotdogs.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def tedsmontanagrill():
    response = requests.get("https://www.tedsmontanagrill.com/locations.html")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def tendergreens():
    response = requests.get("https://www.tendergreens.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thaibamboo():
    response = requests.get("https://thaibamboorestaurant.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thaibloom():
    return ['97005', '97210']


def theboyntonrestaurantspirits():
    return ['01609']


def thebrokenyolkcafe():
    response = requests.get("https://www.thebrokenyolkcafe.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thechophouse():
    response = requests.get("http://www.thechophouse.com/locations.html")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thecrackedegg():
    response = requests.get("https://www.thecrackedegg.com/contact-us/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thedalrae():
    return ['90660']


def thefifty50restaurantgroup():
    sesh = requests.Session()
    response = sesh.get("https://www.thefifty50group.com/")
    pages = re.findall('page\_id\=(\d+)', response.content)
    zips = []
    for page in pages:
        response = sesh.get("https://www.thefifty50group.com/?page_id=" + page)
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except Exception:
            pass
    return list(set(zips))


def thefreshmarket():
    response = requests.get("https://www.thefreshmarket.com/your-market/store-locator")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thefriendlytoast():
    response = requests.get("https://thefriendlytoast.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def themelt():
    response = requests.get("https://themelt.com/locations/all")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def themeltingpot():
    response = requests.get("https://www.meltingpot.com/restaurant-locations.aspx")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def theoldspaghettifactory():
    response = requests.get("https://www.osf.com/locations-map/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thepastahouse():
    response = requests.get("https://pastahouse.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def therockwoodfiredpizza():
    sesh = requests.Session()
    states = ['colorado', 'oregon', 'texas', 'washington']
    zips = []
    for state in states:
        response = sesh.get("https://www.therockwfp.com/" + state)
        zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def thewhitechocolategrill():
    return ['85054', '60563', '80124']


def thewingdome():
    return ['98033', '98103']


def togos():
    params = (
        ('auth_token', 'NUUXHLIDRMYBVBHD'),
        ('country', 'US'),
        ('sitemap', 'true'),
    )
    response = requests.get('https://momentfeed-prod.apigee.net/api/llp.json', params=params).json()
    zips = []
    for store in response:
        zips.append(str(store["store_info"]["postcode"]))
    return list(set(zips))


def tokyojoes():
    response = requests.get("https://tokyojoes.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def tomchee():
    response = requests.get("http://www.tomandchee.com/all-locations/")
    zips = list(set(re.findall('zipcode"\>(\d+)\<', response.content)))
    return zips


def tomdouglasrestaurants():
    sesh = requests.Session()
    response = requests.get("https://www.tomdouglas.com/restaurants.json").json()
    zips = []
    for rest in response["data"]:
        response = sesh.get("http://api.geonames.org/findNearbyPostalCodesJSON?lat=" + rest["lat"] + "&lng=" + rest["lng"] + "&username=r0cketm4n&maxRows=1").json()
        zips.append(str(response["postalCodes"][0]["postalCode"]))
        time.sleep(1)
    return list(set(zips))


def tonypackos():
    response = requests.get("https://www.tonypacko.com/locations.php")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def trudystexmex():
    response = requests.get("http://www.trudys.com/locations.php")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def truefoodkitchen():
    response = requests.get("https://www.truefoodkitchen.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def trulucksseafoodsteakcrabhouse():
    sesh = requests.Session()
    response = sesh.get("https://trulucks.com/locations/")
    zips = []
    for link in re.findall('href\="(https\://trulucks\.com/locations/.*?)"', response.content):
        response = sesh.get(link)
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except:
            pass
    return list(set(zips))


def tsunamirestaurantsushibar():
    response = requests.get("https://www.tsunamiutah.com/locations")
    zips = list(set(re.findall('\w (\d{5})', response.content)))
    return zips


def tupelohoneycafe():
    response = requests.get("https://tupelohoneycafe.com/locations/")
    zips = re.findall('postalCode"\>(\d+)', response.content)
    return list(set(zips))


def uchirestaurants():
    return ['78704', '77006', '75201', '80205', '78756']


def unleavenedfreshkitchen():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get("http://unleavened.com/", headers=headers)
    zips = list(set(re.findall('\w{2,5}(?: )? (\d{5})', response.content)))
    return zips


def urbancookhouse():
    response = requests.get("http://www.urbancookhouse.com/location/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def veggiegrill():
    response = requests.get("https://www.veggiegrill.com/all-locations.html")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def velvettaco():
    response = requests.get("https://velvettaco.com/locations/")
    zips = list(set(re.findall('\w (\d{5})', response.content)))
    return zips


def viewhouseeatery():
    response = requests.get("http://www.viewhouse.com/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def villageinn():
    response = requests.get("https://www.villageinn.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def virgilsbbq():
    return ['10036', '89109']


def vivachicken():
    response = requests.get("http://vivachicken.com/wp-admin/admin-ajax.php?action=asl_load_stores&nonce=9d0163d17b&load_all=1&layout=1").json()
    zips = []
    for store in response:
        zips.append(str(store["postal_code"]))
    return list(set(zips))


def walkonsbistreaux():
    response = requests.get("https://walk-ons.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def wasabijapanesesteakhouse():
    return ['32246', '37934', '37919']


def waterlooicehouse():
    response = requests.get("https://waterlooicehouse.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def waterworksfooddrink():
    return ['05404']


def wecks():
    sesh = requests.Session()
    response = sesh.get("https://wecksinc.com/locations/")
    links = re.findall('location-button"\>\<a href\="(.*?)"', response.content)
    zips = []
    for link in links:
        response = sesh.get("https://wecksinc.com" + link)
        try:
            zips.append(re.search('[A-Za-z \.]+, \w+ (\d+)', response.content).group(1))
        except Exception:
            try:
                zips.append(re.search('postalCode"\>(\d+)', response.content).group(1))
            except Exception:
                print response.url
    zips = list(set(zips))
    return zips


def whiskeycakekitchenbar():
    response = requests.get("https://whiskeycake.com/wp-json/wp/v2/location/")
    zips = []
    for store in response.json():
        zips.append(str(store["afc"]["zip"]))
    return list(set(zips))


def wildflowerbreadcompany():
    response = requests.get("https://www.wildflowerbread.com/locations/")
    zips = re.findall('postalCode"\>(\d+)', response.content)
    return list(set(zips))


def winkinglizardrestauranttavern():
    response = requests.get("https://www.winkinglizard.com/locations")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def worldofbeer():
    response = requests.get("https://worldofbeer.com/Locations")
    zips = list(set(re.findall('"zip"\:"(\d+)', response.content)))
    return zips


def yogurtland():
    response = requests.get("https://franchise.yogurt-land.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def yogurtmountain():
    response = requests.get("http://yogurtmountain.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def zaxbys():
    sesh = requests.Session()
    response = sesh.get("https://www.zaxbys.com/locations/")
    states = re.findall('value\="(\w{2})"', re.search('state-selector"\>(.*?)\</select\>', response.content, re.DOTALL).group(1))
    zips = []
    for state in states:
        response = sesh.get("https://www.zaxbys.com/locations/" + state + "/")
        zips += list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def zinburger():
    response = requests.get("https://zinburger.com/locations/")
    zips = list(set(re.findall('\w{2} (\d{5})', response.content)))
    return zips


def zoeskitchen():
    sesh = requests.Session()
    response = sesh.get("https://zoeskitchen.com/locations/sitemap")
    links = re.findall('href\="(locations/store/.*?)"', response.content)
    zips = []
    for link in links:
        response = sesh.get("https://zoeskitchen.com/" + link)
        try:
            zips.append(re.search('\w{2} (\d{5})', response.content).group(1))
        except Exception:
            print response.url
    return list(set(zips))


def ztejassouthwesterngrill():
    return ['85226', '85028', '78759', '78703']


try:
    arg = sys.argv[1]
except Exception:
    print "no arg specified!"
if arg == "create" or arg == "list":
    hits = 0
    zipcode_data = {}
    stores = [x.strip() for x in open("places_full.txt", "r").readlines()]
    for store in (tqdm.tqdm(stores) if arg == "create" else stores):
        original_name = store
        try:
            store = str(unidecode.unidecode(unicode(store)))
        except Exception:
            pass
        if "110 Grill" in store:
            store = "onetengrill"
        elif "4 Rivers" in store:
            store = "fourriverssmokehouse"
        elif "17th Street" in store:
            store = "seventeenthstreetbarbecue"
        elif "131" in store:
            store = "onethreeonemain"
        else:
            store = store.translate(None, string.punctuation).lower().replace(" ", "")
        try:
            globals()[store]
            hits += 1
            if arg == "create":
                store_zips = globals()[store]()
                for zipcode in store_zips:
                    if zipcode in zipcode_data:
                        zipcode_data[zipcode].append(original_name)
                    else:
                        zipcode_data[zipcode] = [original_name]
        except Exception:
            if arg == "list":
                print original_name
            continue
    if arg == "list":
        print str(hits) + " other stores in data"
    else:
        output_file = open("zipcode_data.json", "w+")
        output_file.write(json.dumps(zipcode_data, sort_keys=True))
        output_file.close()
        data = {
            'api_option': 'paste',
            'api_paste_code': open("zipcode_data.json", "r").read().strip(),
            'api_dev_key': '9efefa9735abafab975c7dd47e777913',
            'api_user_key': '85afd7fb397361876fea0356ca7fc406'
        }
        response = requests.post("https://pastebin.com/api/api_post.php", data=data)
        print "uploaded to: " + response.content
else:
    try:
        store_zips = globals()[arg]()
        print store_zips
        print arg + ": " + str(len(store_zips)) + " stores"
    except Exception:
        print traceback.format_exc()
        print "invalid arg!"
