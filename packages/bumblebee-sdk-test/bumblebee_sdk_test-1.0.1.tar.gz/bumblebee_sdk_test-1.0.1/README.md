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

## Installation/Setup Steps:
1. Set up and activate your virtual environment
    - On macOS/Linux:
        - python3 -m venv <virtual-environment-name>
        - source venv/bin/activate
    - On Windows:
        - python -m venv venv
        - venv\Scripts\activate
2. Install the package using pip
    - pip install bumblebee-sdk-test
3. Install the required packages: pip install -r requirements.txt
4. Configure your env variables by creating an .env file in the root directory and listing your login information as following:
    - username="your-email"
    - password="your-password"