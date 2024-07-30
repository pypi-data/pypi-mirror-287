import requests, json

routeUrl = "http://10.0.0.60:5002/api/track"

def fetch(url, info):
  resp = requests.post(
    url,
    json=info["body"],
    headers=info["headers"]
  )

  return resp

class Trackus:
  def __init__(self, apiKey, projectToken):
    self.apiKey = apiKey
    self.projectToken = projectToken

  # all functions point to developer side
  def register(self, userInfo):
    # userInfo: email, user id

    if self.apiKey == "":
      return "API Key is missing"
    
    if self.projectToken == "":
      return "Project Token is missing"

    resp = fetch(routeUrl + "/register", {
      "headers": { "Content-Type": "application/json" },
      "body": { "projectToken": self.projectToken, "userInfo": userInfo }
    })

    if resp.status_code == 200:
      return resp.json()

    return False
  
  def track_action(self, type, name, action):
    # page visits, user actions

    if self.apiKey == "":
      return "API Key is missing"

    resp = fetch(routeUrl + "/track_action", {
      "headers": { "Content-Type": "application/json" },
      "body": { "type": type, "name": name, "action": action }
    })

    if resp.status_code == 200:
      return True
    
    return False
  
  def track_error(self, type, name, action, info):
    # track any error if occurred

    if self.apiKey == "":
      return "API Key is missing"
    
    resp = fetch(routeUrl + "/track_error", {
      "headers": { "Content-Type": "application/json" },
      "body": { "type": type, "name": name, "action": action, "info": json.dumps(info) }
    })

    if resp.status_code == 200:
      return resp.json()
    
    return False
  
  def get_datas(self):
    if self.apiKey == "":
      return "API Key is missing"
    
    if self.projectToken == "":
      return "Project Token is missing"
    
    resp = fetch(routeUrl + "/get_datas", {
      "headers": { "Content-Type": "application/json" },
      "body": { "userApiKey": self.apiKey, "projectId": self.projectToken, "type": "Page", "name": "Landing" }
    })

    if resp.status_code == 200:
      return resp.json()
    
    return False
  
trackus = Trackus(__name__, __name__)
    