import os
from pyquery import PyQuery as pq
from unidecode import unidecode
import xml.etree.ElementTree as ET

def createFullPath(season, country):
  myPath = "/Users/afe/projects/long-view/standings/{0}".format(season)

  if country == "French_Division_1":
    country = "Ligue_1"
  elif country == "Alpha_Ethniki":
    country = "Superleague_Greece"

  fullPath = os.path.join(myPath, "{0}.xml".format(country))
  return fullPath

if __name__ == "__main__":
  # conn = psycopg2.connect(database="long-view", user="afe", password="1bellazio", host="localhost")
  # cur = conn.cursor()

  # query = "INSERT INTO clubs (full_name, country_id) VALUES ('Inter', 3) RETURNING id;"

  # try:
  #   cur.execute(query)
  #   print cur.fetchone()[0]
  #   conn.commit()
  # except psycopg2.IntegrityError as ie:
  #   print "Already present"

  # cur.close()
  # conn.close()

  # #$("#League_table").parent().next().html()
  # d = pq(url="https://en.wikipedia.org/wiki/2014%E2%80%9315_Serie_A")
  # p = d("#League_table").parent().next().html()
  # print p

  seasons = ["1516"]
  countries = ["G1"]

  for season in seasons:
    for country in countries:
      path = createFullPath(season, country)
      # path = "/Users/afe/projects/long-view/test.html"
      tree = ET.parse(path)
      root = tree.getroot()
      header = []
      for row in root:
        rowParsed = []
        for data in row:
          if data.tag != "th" and len(list(data)) == 0:
            d = data.text
            if type(d) == unicode:
              d = unidecode(d)
            rowParsed.append(d)
          elif len(list(data)) > 0 and data[0].tag == "a":
            d = data[0].text
            if type(d) == unicode:
              d = unidecode(d)
            rowParsed.append(d)
          elif data.tag == 'th' and len(list(data)) > 0 and data[0].tag == "abbr":
            header.append(data[0].text)
        if rowParsed:
          if len(rowParsed) == 10:
            print rowParsed[:-1]
          elif len(rowParsed) < 10:
            print rowParsed
          else:            
            print path
            break
      print header