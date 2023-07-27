from django.shortcuts import render
from django.conf import settings
from opencage.geocoder import OpenCageGeocode


def index(request):
    if request.method == 'POST':
        search_location = request.POST.get('location')
        try:
            key = settings.OPENCAGE_KEY
            geocoder = OpenCageGeocode(key)
            query = search_location
            result = geocoder.geocode(query)
            print(type(result))
            data = dict()
            data['lat'] = result[0]['geometry']['lat']
            data['lng'] = result[0]['geometry']['lng']
            data['country'] = result[0]['components']['country']
            data['country_code'] = result[0]['components']['country_code']
            data['state'] = result[0]['components']['state']
            data['state_code'] = result[0]['components']['state_code']
            data['district'] = result[0]['components']['state_district']
            data['type'] = result[0]['components']['_type']
            data['pincode'] = result[0]['components']['postcode']
            data['time_zone'] = result[0]['annotations']['timezone']['name']
            data['currency'] = result[0]['annotations']['currency']['name']
            data['currency_symbol'] = result[0]['annotations']['currency']['symbol']
            context = {
                "geo_data": data
            }
        except Exception as e:
            print("ERROR: ", e)
        return render(request, 'geodata/index.html', context=context)
    else:
        return render(request, 'geodata/index.html')
