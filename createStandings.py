import os
import pandas
import psycopg2
import numpy
import sys
import numpy
from unidecode import unidecode
import xml.etree.ElementTree as ET

def createFullPath(season, league):
  myPath = "/Users/afe/projects/long-view/standings/{0}".format(season)

  if league == "French_Division_1":
    league = "Ligue_1"
  elif league == "Alpha_Ethniki":
    league = "Superleague_Greece"

  fullPath = os.path.join(myPath, "{0}.xml".format(league))
  return fullPath

def cleanRow(row):
  for i in range(0, len(row)):
    if type(row[i]) is str and "'" in row[i]:
      row[i] = row[i].replace("'", " ")
    elif str(row[i]) == 'nan':
      row[i] = None

  return row

def getSeasonId(season):
  # SELECT id FROM seasons WHERE period='0001' LIMIT 1;
  query = "SELECT id FROM seasons WHERE period='{0}' LIMIT 1;".format(season)
  
  return getId(query)

def getTeamId(teamName):
  teamName = teamName.replace("'", " ")

  # SELECT id FROM clubs WHERE full_name='Juventus' LIMIT 1;
  words = teamName.split(" ")
  query = "SELECT id FROM clubs WHERE full_name ~ '{0}' LIMIT 1;".format(words[0])
  
  idTeam = getId(query)

  if idTeam == None:
    if len(words) > 1:
      query = "SELECT id FROM clubs WHERE full_name ~ '{0}' LIMIT 1;".format(words[1])  
      idTeam = getId(query)

  if idTeam == None:
    return False
  return idTeam

def getLeagueId(teamName):
  # SELECT id FROM clubs WHERE abbreviation='E0' LIMIT 1;
  query = "SELECT id FROM leagues WHERE abbreviation='{0}' LIMIT 1;".format(teamName)

  return getId(query)

def getId(query):
  conn = psycopg2.connect(database="long-view", user="afe", password="1bellazio", host="localhost")
  cur = conn.cursor()

  cur.execute(query)
  idRow = cur.fetchone()

  cur.close()
  conn.close()

  if idRow:
    return idRow[0]
  return None

def addRow(query):
  query = query.replace("None", "NULL")

  conn = psycopg2.connect(database="long-view", user="afe", password="1bellazio", host="localhost")
  cur = conn.cursor()

  succeeded = -1

  try:
    cur.execute(query)
    succeeded = cur.fetchone()[0]
    conn.commit()
  except psycopg2.IntegrityError as ie:
    pass

  cur.close()
  conn.close()

  if succeeded != -1:
    return succeeded
  return False

def getHeader(root):
  header = []
  for data in root[0]:
    if data.tag == 'th' and len(list(data)) > 0 and data[0].tag == "abbr":
      header.append(data[0].text)
    elif data.tag == 'th':
      header.append(data.text)
  return convertHeader(header)

def convertHeader(header):
  endIteration = len(header)
  for i in range(0, endIteration):
    field = header[i]
    if field == "Pos":
      header[i] = "position"
    elif field == "Pld":
      header[i] = "played"
    elif field == "W":
      header[i] = "won"
    elif field == "D":
      header[i] = "drawn"
    elif field == "L":
      header[i] = "lost"
    elif field == "GF":
      header[i] = "goal_scored"
    elif field == "GA":
      header[i] = "goal_against"
    elif field == "GD":
      header[i] = "goal_difference"
    elif field == "Pts":
      header[i] = "point"
    elif field == "Team" or field == "Team\n":
      header[i] = "club_id"

  prefix = ["season_id", "league_id"]

  return prefix + header[:10]

def getRows(root):
  rows = []

  for row in root[1:]:
    rowParsed = []
    for data in row:
      dataStr = data
      while len(list(dataStr)) > 0:
        dataStr = dataStr[0]
      d = dataStr.text
      if type(d) == unicode:
        d = unidecode(d)
      rowParsed.append(d)
    # print rowParsed
    if len(rowParsed) >= 10:
      rows.append(rowParsed[:10])
    else:
      return False

  return rows

def parseTable(root):
  header = getHeader(root)
  # print header
  rows = getRows(root)

  if not rows:
    return False

  rows.insert(0, header)
  return rows

def addPosition(season, league, header, row):
  if (len(header) - 2) != len(row):
    sys.exit("{0}\t{1}\t{2}\t{3}".format(season, league, header, row))

  season_id = getSeasonId(season)
  league_id = getLeagueId(league)
  insertList = []
  insertList.append(season_id)
  insertList.append(league_id)
  for i in range(0, len(header)-2):
    field = header[i+2]
    if field == "club_id":
      club_id = getTeamId(row[i])
      if not club_id:
        sys.exit(row[i])
      insertList.append(club_id)
    elif field == "position":
      insertList.append(row[i])
    elif field == "played":
      insertList.append(row[i])
    elif field == "won":
      insertList.append(row[i])
    elif field == "drawn":
      insertList.append(row[i])
    elif field == "lost":
      insertList.append(row[i])
    elif field == "goal_scored":
      insertList.append(row[i])
    elif field == "goal_against":
      insertList.append(row[i])
    elif field == "goal_difference":
      insertList.append(row[i])
    elif field == "point":
      insertList.append(row[i])

  return insertList

def addStandingRow(header, values):
  query = "INSERT INTO standings ({0}) VALUES {1} RETURNING id;".format(", ".join(header), tuple(values))

  try:
    addRow(query)
  except Exception as e:
    print query
    print header
    print values
    sys.exit(e)

if __name__ == "__main__":
  # seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  # leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]
  seasons = ["1011"]
  leagues = ["E0", "G1"]

  for season in seasons:
    for league in leagues:
      path = createFullPath(season, league)
      # path = "/Users/afe/projects/long-view/test.html"
      try:
        tree = ET.parse(path)
      except IOError as i:
        # print path
        continue

      root = tree.getroot()
      try:
        table = parseTable(root)
      except:
        # print path
        continue

      if not table:
        # print path
        continue
      header = table[0]
      for row in table[1:]:
        insertList = addPosition(season, league, header, row)
        addStandingRow(header, insertList)

