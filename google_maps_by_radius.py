import sys
import time

import requests
import json
import livepopulartimes

def scrape_paid(lat, long, radius, category  ):
    next_page_token = ''
    # lat = lat
    # long =long
    location = lat +', ' + long,
    # radius = radius
    # category = category
    # language = 'en'
    all_data = []
    loop2=0
    while True:
        loop2+=1
        print(loop2)
        if loop2 > 5:
            break
        if next_page_token:
            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken="+str(next_page_token)+"&key=AIzaSyDypiRJ2xKH3qpOMs_iFefikOfj7-P8eo8"
            response_first = requests.get(url)
        else:
            params = {
                'location': location,
                'radius': radius,
                'type': category,
                'key': 'AIzaSyDypiRJ2xKH3qpOMs_iFefikOfj7-P8eo8',
                # 'language' : 'language',
                # 'keyword': 'cruise',
            }
            response_first = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=params)

        loop=0
        for data in response_first.json()['results'] :
            loop+=1
            print(loop)
            place_id = data['place_id']
            popular_time = ''
            facilities = []

            headers = {
                'Content-Type': 'application/json',
                'X-Goog-Api-Key': 'AIzaSyDypiRJ2xKH3qpOMs_iFefikOfj7-P8eo8',
                'X-Goog-FieldMask': '*',
                # 'X-Goog-FieldMask': 'photos,displayName,reviews,types,googleMapsUri,websiteUri,nationalPhoneNumber,shortFormattedAddress,currentOpeningHours',
            }

            response = requests.get('https://places.googleapis.com/v1/places/' + place_id, headers=headers)
            detail_data = response.json()


            data_photo = []
            try :
                displayName = detail_data['displayName']['text']
                for photo in detail_data['photos']:
                    photo_reference = photo['name'].split('photos/')[1]
                    author = photo['authorAttributions'][0]['displayName']
                    if displayName == author:
                        response_photo = requests.get("https://maps.googleapis.com/maps/api/place/photo?maxwidth=1280&photo_reference="+photo_reference+"&key=AIzaSyDypiRJ2xKH3qpOMs_iFefikOfj7-P8eo8")
                        data_photo.append(response_photo.url)
            except:
                pass
            try:
                popular_time = livepopulartimes.get_populartimes_by_formatted_address(detail_data['displayName']['text'] + ", " + detail_data['shortFormattedAddress'])['populartimes']
            except :
                pass

            try:
                link_web =  detail_data['websiteUri']
            except:
                link_web = ""
            try:
                operational_time = detail_data['currentOpeningHours']['weekdayDescriptions']
            except:
                operational_time = ""
            try:
                no_telp = detail_data['nationalPhoneNumber']
            except:
                no_telp = ""
            try:
                review =detail_data['reviews']
            except:
                review = ""
            for key, value in detail_data.items():
                if type(value) == bool:
                    facilities.append({key : value})

            try:
                accessibilityOptions = detail_data['accessibilityOptions']
                facilities.append({'accessibilityOptions': accessibilityOptions})
            except:
                pass
            try:
                parkingOptions = detail_data['parkingOptions']
                facilities.append({'parkingOptions': parkingOptions})
            except:
                pass
            try:
                paymentOptions = detail_data['paymentOptions']
                facilities.append({'paymentOptions': paymentOptions})
            except:
                pass
            result = {
                "place_id": place_id,
                "image": data_photo,
                "place_name": detail_data['displayName']['text'],
                "operational_time": operational_time,
                "review": review,
                "category": detail_data['types'],
                "link_menu": detail_data['googleMapsUri'],
                "link_web":link_web,
                "no_telp": no_telp,
                "popular_time": popular_time,
                "facilities": facilities
            }
            all_data.append(result)

        try :
            next_page_token = response_first.json()['next_page_token']
            continue
        except:
            break


    with open("data_google_"+category+'_radius'+radius+'.json', 'w', encoding="utf-8") as outfile:
            json.dump(all_data, outfile, ensure_ascii=False, indent=4)
    return all_data