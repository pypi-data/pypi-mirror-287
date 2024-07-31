# Bumblebee Networks SDK

## Purpose:
* This is a Python package that simplifies interaction with the Bumblebee Networks controller API by streamlining the steps of making API requests and handling responses.

## Directory Details:
* /src
    * account.py - initializes a class representing an account
    * app_service.py - initializes a class representing an app service
    * ep.py - initializes a class representing an endpoint
    * service_node.py - initializes a class representing a service node
    * user.py - initializes a class representing a user
    * bbt.py - defines an object that accesses the controller API to translate method calls into HTTP requests and procceses responses
* /test
    * account_bbt_test.py - tests account-related GET operations of the API when accessed through the SDK
        * GET operations tested: get_account
    * app_service_bbt_test.py - tests app service-related GET operations of the API when accessed through the SDK
        * GET operations tested: get_app_service, get_app_service_detail, get_app_service_hosting
    * ep_bbt_test.py - tests endpoint and endpoint node-related GET operations of the API when accessed through the SDK
        * GET operations tested: get_ep_node_groups, get_ep_nodes, get_endpoint_node_detail, get_eps, get_endpoint_detail
    * service_node_bbt_test.py - tests service node-related GET operations of the API when accessed through the SDK
        * GET operations tested: get_service_node, get_service_node_detail

## Getting Started:
### Installation/Setup Steps:
1. Set up and activate your virtual environment
    - On macOS/Linux:
        - python3 -m venv <virtual-environment-name>
        - source venv/bin/activate
    - On Windows:
        - python -m venv venv
        - venv\Scripts\activate
2. Install the package using pip
    - pip install bumblebee-sdk-test
3. Install the required packages listed in requirements.txt: pip install -r requirements.txt
4. Configure your env variables by creating an .env file in the root directory and listing your login information as following:
    - username="your-email"
    - password="your-password"
5. Import the required classes/methods
    - import bbt

## The bbt class
The bbt class is used to simplify interactions with the Bumblebee Networks controller API by providing methods that manage accounts, IAM users, SAML SSO, service node groups, service nodes, app services, endpoint node groups, endpoint nodes, endpoints, user agents. It also provides methods to manage the database, get messages, download OVA files, get stats, billing, and contact information.

## Example GET Methods
##### First import bbt and create an instance of the bbt class
```
from bbt import * 
bt = get_bt(api_url=api_url, access_key_id=username, access_key_secret=password)
```

1. Account methods
```
accounts, error_msg = bt.get_account(username=username)
assert error_msg == None, f"Account get failed, error = {error_msg}"
for act in accounts:
    print("\nAccount Information: ", act.to_dict())
```

2. Service node groups methods
```
service_node_group, error_msg = bt.get_service_node_groups("PCpractice")
assert error_msg == None, f"Account IdP get failed, error = {error_msg}"
for sng_data in service_node_group:
    print("\nService Node Group: ", sng_data.to_dict())
```

3. Service node methods
```
service_node, error_msg = bt.get_service_node("sng-194230442600549", "PCpractice")
assert error_msg == None, f"Service node get failed, error = {error_msg}"
for sn_data in service_node:
    print("\nService Node: ", sn_data.to_dict())
```

4. App service methods
```
app_service, error_msg = bt.get_app_service("PCpractice")
assert error_msg == None, f"App service get failed, error = {error_msg}"
for as_data in app_service:
    print("\nApp Service: ", as_data.to_dict())
```

```
app_service_detail, error_msg = bt.get_app_service_detail("app-107527704987863")
assert error_msg == None, f"App service details get failed, error = {error_msg}"
print("\nApp Service Details: ", app_service_detail)
```

```
app_service_hosting, error_msg = bt.get_app_service_hosting(app_service_id='app-107527704987863', hosting_type='onprem')
assert error_msg == None, f"App service hosting get failed, error = {error_msg}"
print("\nApp Service Hosting: ", app_service_hosting)
```

5. Endpoint node groups methods
```
ep_node_group, error_msg = bt.get_ep_node_groups("practice")
assert error_msg == None, f"Endpoint node groups get failed, error = {error_msg}"
for epng_data in ep_node_group:
    print("\nEndpoint Node Group: ", epng_data.to_dict())
```

6. Endpoint node methods
```
ep_node, error_msg = bt.get_ep_nodes("epng-209808940081286", "practice")
assert error_msg == None, f"Endpoint node get failed, error = {error_msg}"
for epn_data in ep_node:
    print("\nEndpoint Node: ", epn_data.to_dict())
```

```
ep_node_detail, error_msg = bt.get_endpoint_node_detail("epn-54162734144921")
assert error_msg == None, f"Endpoint node details get failed, error = {error_msg}"
print("\nEndpoint Node Details: ", ep_node_detail)
```

7. Endpoint methods
```
ep, error_msg = bt.get_eps("app-107527704987863", "epn-228936703715895", "test-ep")
assert error_msg == None, f"Endpoints get failed, error = {error_msg}"
for ep_data in ep:
    print("\nEndpoint: ", ep_data.to_dict())
```

```
ep_detail, error_msg = bt.get_endpoint_detail("ep-127856265075043")
assert error_msg == None, f"Endpoint details get failed, error = {error_msg}"
print("\nEndpoint Details: ", ep_detail)
```