import requests
import config
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/health/getData")
def getData():
    token = getAuth()
    healthdata = []
    url = "https://health-api.cloud.huawei.com/healthkit/v1/dataCollectors?dataTypeName=com.huawei.continuous.steps.delta"
    requests.get(url)
    html = render_template("healthdata.html", healthdata=healthdata)
    return html


def getAuth():
    authURL = "https://login.cloud.huawei.com/oauth2/v2/token"
    headers = {
        "grant_type": "authorization_code",
        "client_id": config.clientID,
        "client_secret": config.clientSecret,
        "content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    authResp = requests.post(authURL, headers=headers)
    if authResp.status_code == 200:
        authToken = authResp.json()["access_token"]
    else:
        print("Auth Error: ")
        print(authResp.text)
    return authToken
