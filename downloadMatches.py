import os
import urllib

def constructUrl(season, country):
  baseUrl = "http://www.football-data.co.uk/mmz4281/"
  return "{0}/{1}/{2}.csv".format(baseUrl, season, country)

def downloadAndSave(season, country):
  url = constructUrl(season, country)
  myPath = "/Users/afe/projects/long-view/matches/{0}".format(season)
  fullPath = os.path.join(myPath, "{0}.csv".format(country))
  file = urllib.urlretrieve(url, fullPath)

if __name__ == "__main__":
  seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  countries = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  os.makedirs("matches")

  for season in seasons:
    os.makedirs("matches/{0}".format(season))
    for country in countries:
      downloadAndSave(season, country)