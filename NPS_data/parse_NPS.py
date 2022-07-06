import requests


response = requests.get("")
data=response.json()["data"]


for campground in data:
    if campground["fees"]==[]:
        print(f'{campground["name"]}: Fees is an empty list')
    else:
        print(campground["fees"][0]['cost'])

# for campground in data:
    if campground["amenities"]['cellPhoneReception']=="":
        print(f'{campground["name"]}: cellPhoneReception is an empty string')
    else:
        print(campground["amenities"]['cellPhoneReception'])

# for campground in data:
    if campground["amenities"]['toilets']==[]:
        print(f'{campground["name"]}: toilets is an empty string')
    else:
        print(campground["amenities"]['toilets'][0])

# for campground in data:
    if campground["numberOfSitesReservable"]=="":
        print(f'{campground["name"]}: "numberOfSitesReservable" is an empty string')
    else:
        print(campground["numberOfSitesReservable"])

# for campground in data:
    if campground["numberOfSitesFirstComeFirstServe"]=="":
        print(f'{campground["name"]}: "numberOfSitesFirstComeFirstServe" is an empty string')
    else:
        if campground["numberOfSitesFirstComeFirstServe"]=="0":
            print(f'{campground["name"]} is 0')

for campground in data:
    if campground["amenities"]['showers']==[]:
        print(f'{campground["name"]}: showers is an empty string')
    else:
        print(f"Showers: {campground['amenities']['showers'][0]}")
        



