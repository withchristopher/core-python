# -*- coding:utf-8 -*-
import requests
import json


from flask import Flask, render_template, request


app = Flask(__name__)

clientID = "C86b8039e91670fa3a94e5ca7146b0f612a769c2d9e2a7a245fa9e6e09a09085a"
secretID = "4f98ff1eaa5670d38554c988733b60cf4901fc5ffa45ef261d768f1f35fea3bc"
redirectURI = "http://localhost:10060/oauth" #This could be different if you publicly expose this endpoint.
code = "code"

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

print(get_tokens())
def get_oauthuser_info(access_token):
    """Retreives OAuth user's details."""
    url = "https://api.ciscospark.com/v1/people/me"
    headers = {'accept':'application/json','Content-Type':'application/json','Authorization': 'Bearer '+ access_token}
    req = requests.get(url=url, headers=headers)
    results = json.loads(req.text)
    personID = results["id"]
    emailID = results["emails"][0]
    displayName = results["displayName"]
    return personID, emailID, displayName

@app.route("/") 

def main_page():
    """Main Grant page"""
    return render_template("index.html")


@app.route("/oauth") #Endpoint acting as Redirect URI.

def oauth():
    """Retrieves oauth code to generate tokens for users"""
 
    if "code" in request.args and state == "YOUR_STATE_STRING":
        state = request.args.get("state") #Captures value of the state.
        code = request.args.get("code") #Captures value of the code.
        print ("OAuth code:", code)
        print ("OAuth state:", state)
        access_token, refresh_token = get_tokens(code) #As you can see, get_tokens() uses the code and returns access and refresh tokens.

        #Now, let's do something with the generated token: Get the user's info: PersonId, Email Address and DisplayName.
        personID, emailID, displayName = get_oauthuser_info(access_token)
        print ("personID:", personID)
        print ("email ID:", emailID)
        print ("display Name", displayName)
        return render_template("granted.html")
    else:
        return render_template("index.html")
  

if __name__ == '__main__':
    app.run("0.0.0.0", port=10060, debug=False)
