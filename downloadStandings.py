import os
import io
from pyquery import PyQuery as pq

def createFullPath(season, country):
  myPath = "/Users/afe/projects/long-view/standings/{0}".format(season)

  nameConversion = {
    "Premier_League": "E0",
    "Bundesliga": "D1",
    "Serie_A": "I1",
    "La_Liga": "SP1",
    "Ligue_1": "F1",
    "Eredivisie": "N1",
    "Primeira_Liga": "P1",
    "Superleague_Greece": "G1",
    "French_Division_1": "French_Division_1",
    "Alpha_Ethniki": "Alpha_Ethniki"
  }

  # if country == "French_Division_1":
  #   country = "Ligue_1"
  # elif country == "Alpha_Ethniki":
  #   country = "Superleague_Greece"

  fullPath = os.path.join(myPath, "{0}.xml".format(nameConversion[country]))
  return fullPath

def insertDash(string, index):
  return string[:index] + '-' + string[index:]

def getTable(season, country):

  if country == "French_Division_1":
    tagId = "Final_table"
  elif country == "Alpha_Ethniki":
    tagId = "Standings"
  else:
    tagId = "League_table"

  try:
    d = pq(url="https://en.wikipedia.org/wiki/20{0}_{1}".format(insertDash(season,2), country))
    p = d("#{0}".format(tagId)).parent().next().outerHtml();
    return p
  except:
    #print "https://en.wikipedia.org/wiki/20{0}_{1}".format(season, country)
    return

if __name__ == "__main__":

  seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  countries = ["Premier_League", "Bundesliga", "Serie_A", "La_Liga", "Ligue_1", "Eredivisie", "Primeira_Liga", "Superleague_Greece", "French_Division_1", "Alpha_Ethniki"]

  # os.makedirs("standings")

  for season in seasons:
    os.makedirs("standings/{0}".format(season))
    for country in countries:
      p = getTable(season, country)
      if p != None:
        path = createFullPath(season, country)
        with io.open(path, "w", encoding='utf8') as f:
          if type(p) == str:
            p = unicode(p, "utf-8")
          f.write(p)