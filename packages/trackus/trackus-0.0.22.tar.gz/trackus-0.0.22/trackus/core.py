import requests

routeUrl = "http://10.0.0.60:5002/api/track"

def fetch(url, info):
  resp = requests.post(
    url,
    json=info["body"],
    headers=info["headers"]
  )

  return resp

class Trackus:
  def __init__(self, apiKey):
    self.apiKey = apiKey

  def welcome(self):
    return "Trackus Python Library works!!"

  # all functions point to developer side
  def register(self, projectToken, userInfo):
    # userInfo: email, user id

    if self.apiKey == "":
      return "API Key is missing"

    resp = fetch(routeUrl + "/register", {
      "headers": { "Content-Type": "application/json" },
      "body": { "projectToken": projectToken, "userInfo": userInfo }
    })

    if resp.status_code == 200:
      return resp.json()

    return False
  
  def track(self, type, name, action):
    # page visits, user actions

    if self.apiKey == "":
      return "API Key is missing"
    
    resp = fetch(routeUrl + "/track_action", {
      "headers": { "Content-Type": "application/json" },
      "body": { "type": type, "name": name, "action": action }
    })

    if resp.status_code == 200:
      return resp.json()
    
    return False

trackus = Trackus("")
    