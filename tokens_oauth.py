# -*- coding:utf-8 -*-
import requests
import json


from flask import Flask, render_template, request


app = Flask(__name__)

clientID = "C86b8039e91670fa3a94e5ca7146b0f612a769c2d9e2a7a245fa9e6e09a09085a"
secretID = "4f98ff1eaa5670d38554c988733b60cf4901fc5ffa45ef261d768f1f35fea3bc"
redirectURI = "http://localhost:10060/oauth" #This could be different if you publicly expose this endpoint.


def get_tokens(code):
    """Gets access token and refresh token"""
    print("code", code)
    url = "https://api.ciscospark.com/v1/access_token"
    headers = {'accept':'application/json','content-type':'application/x-www-form-urlencoded'}
    payload = (f"grant_type=authorization_code&client_id={clientID}&client_secret={secretID}&"
                    "code={code}&redirect_uri={redirectURI}")
    req = requests.post(url=url, data=payload, headers=headers)
    results = json.loads(req.text)
    print(results)
    access_token = results["access_token"]
    refresh_token = results["refresh_token"]
    return access_token, refresh_token

def oauth():
    """Retrieves oauth code to generate tokens for users"""
    i = 1
    if i == 1:
        #state = request.args.get("state") #Captures value of the state.
        #code = request.args.get("code") #Captures value of the code.
        code = "test"
        state = "test"
        print (f"OAuth code: {code}")
        print (f"OAuth state:{state}")
        access_token, refresh_token = get_tokens(code) #As you can see, get_tokens() uses the code and returns access and refresh tokens.

        #Now, let's do something with the generated token: Get the user's info: PersonId, Email Address and DisplayName.
        personID, emailID, displayName = get_oauthuser_info(access_token)
        print (f"personID:{personID}") 
        print (f"email ID:{emailID}")
        print (f"display Name{displayName}")
        return access_token
    else:
        return "Did not work"

import os
import warnings


DEFAULT_BASE_URL = 'https://api.ciscospark.com/v1/'

DEFAULT_SINGLE_REQUEST_TIMEOUT = 60

DEFAULT_WAIT_ON_RATE_LIMIT = True

ACCESS_TOKEN_ENVIRONMENT_VARIABLE = 'WEBEX_TEAMS_ACCESS_TOKEN'

LEGACY_ACCESS_TOKEN_ENVIRONMENT_VARIABLES = [
    'SPARK_ACCESS_TOKEN',
    'CISCO_SPARK_ACCESS_TOKEN',
]

WEBEX_TEAMS_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


# Helper Functions
def _get_access_token():
    """Attempt to get the access token from the environment.
    Try using the current and legacy environment variables. If the access token
    is found in a legacy environment variable, raise a deprecation warning.
    Returns:
        The access token found in the environment (str), or None.
    """
    access_token = os.environ.get(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
    if access_token:
        return access_token

    else:
        for access_token_variable in LEGACY_ACCESS_TOKEN_ENVIRONMENT_VARIABLES:
            access_token = os.environ.get(access_token_variable)
            if access_token:
                env_var_deprecation_warning = PendingDeprecationWarning(
                    "Use of the `{legacy}` environment variable will be "
                    "deprecated in the future.  Please update your "
                    "environment(s) to use the new `{new}` environment "
                    "variable.".format(
                        legacy=access_token,
                        new=ACCESS_TOKEN_ENVIRONMENT_VARIABLE,
                    )
                )
                warnings.warn(env_var_deprecation_warning)
                return access_token


# Package Environment Variables
WEBEX_TEAMS_ACCESS_TOKEN = _get_access_token()

x = oauth()
print(x)