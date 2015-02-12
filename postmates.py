import httplib, urllib
import requests
import json

def deliveryQuote():
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/delivery_quotes'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {'pickup_address':'202 McAllister St. San Francisco, CA', 'dropoff_address':'101 Market St. San Francisco, CA'}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()

def deliveryPlace( quote_id ):
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {'manifest':'a box of kittens', 'manifest_reference' : 'Optional ref', 'pickup_name': 'The Warehouse',\
     'pickup_address':'202 McAllister St. San Francisco, CA', \
     'pickup_phone_number':'555-555-5555',\
     'pickup_business_name':'Optional nameee',\
     'pickup_notes':'Optional notes',\
     'dropoff_name':'Alice',\
     'dropoff_phone_number':'232-323-2222',\
     'dropoff_business_name':'Optional Business name',\
     'dropoff_address':'101 Market St. San Francisco, CA',\
     'quote_id':quote_id}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()

# Lists all the deliveries ever placed by a user
def deliveryListAll():
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries'
    # url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries?filter=ongoing'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {}
    r = requests.get(url, data=payload, headers=headers)
    print(r.url)
    return r.json()

# Lists ongoing deliveries for a given user
def deliveryListOngoing():
    # url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries'
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries?filter=ongoing'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {'filter':'ongoing'}
    r = requests.get(url, data=payload, headers=headers)
    return r.json()

# Show details of a given delivery, USE THIS FOR STATUS/LAT/LNG AS WELL
def deliveryDetails( delivery_id ):
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries/'+delivery_id
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {}
    r = requests.get(url, data=payload, headers=headers)
    return r.json()

# Note: deliveries can only be cancelled prior to pickup
def deliveryCancel( delivery_id ):
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries/'+ delivery_id + '/cancel'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()

def deliveryDeleteAll():
    deliveries = deliveryListAll()["data"]
    for element in deliveries:
        deliveryCancel(element['id'])


def deliveryReturn():
    url = 'https://api.postmates.com/v1/customers/cus_KAgGPlHZ6tZmzF/deliveries/'+ delivery_id + '/return'
    headers = { 'Authorization':'Basic NWUzODM3Y2MtNzM0MS00MzRkLThlNGUtNTA2MjYwYTQyMjVkOg==',"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    payload = {}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()

def prettyprint(inputtext):
    print json.dumps(inputtext, indent=4, sort_keys=True)

def main():
    # deliveryInfo = deliveryQuote()
    # placedeliv = deliveryPlace(deliveryInfo['id'])
    # print json.dumps(deliveryListAll(), indent=4, sort_keys=True)
    prettyprint(deliveryDetails('del_KCoBvWs3IQpkG-'))



if __name__ == "__main__":
    main()