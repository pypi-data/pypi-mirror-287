class Trackus:
  def __init__(self, apiKey):
    self.apiKey = apiKey

  def listdir(self):
    if self.apiKey != "":
      return "Api key: " + self.apiKey
    else:
      return "Api key not set"

trackus = Trackus("")