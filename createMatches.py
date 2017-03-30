import os
import pandas
import psycopg2
import numpy
import sys
import numpy

def createFullPath(season, country):
  myPath = "/Users/afe/projects/long-view/matches/{0}".format(season)
  fullPath = os.path.join(myPath, "{0}.csv".format(country))
  return fullPath

def parseHeader(header):
  fixed = "season_id,league_id,date,home_id,away_id"

  for i in range(0, len(header)):
    if header[i] == 'AS':
      header[i] = "away_shots"
    elif header[i] == 'HS':
      header[i] = "home_shots"

    if "<" in header[i]:
      header[i] = header[i].replace("<", "l")
    if ">" in header[i]:
      header[i] = header[i].replace(">", "g")
    if "." in header[i]:
      header[i] = header[i].replace(".", "")

  h = ",".join(header[4:])
  h = h.lower()

  h = fixed + "," + h

  return h

def cleanRow(row):
  for i in range(0, len(row)):
    if type(row[i]) is str and "'" in row[i]:
      row[i] = row[i].replace("'", " ")
    elif str(row[i]) == 'nan':
      row[i] = None

  return row

def getCountryId(leagueId):
  # SELECT country_id FROM leagues WHERE abbreviation='E0' LIMIT 1;
  query = "SELECT country_id FROM leagues WHERE abbreviation='{0}' LIMIT 1;".format(leagueId)
  
  return getId(query)

def getSeasonId(season):
  # SELECT id FROM seasons WHERE period='0001' LIMIT 1;
  query = "SELECT id FROM seasons WHERE period='{0}' LIMIT 1;".format(season)
  
  return getId(query)

def getTeamId(teamName):
  teamName = teamName.replace("'", " ")

  # SELECT id FROM clubs WHERE full_name='Juventus' LIMIT 1;
  query = "SELECT id FROM clubs WHERE full_name='{0}' LIMIT 1;".format(teamName)
  
  return getId(query)

def getLeagueId(teamName):
  # SELECT id FROM clubs WHERE abbreviation='E0' LIMIT 1;
  query = "SELECT id FROM leagues WHERE abbreviation='{0}' LIMIT 1;".format(teamName)

  return getId(query)

def getId(query):
  conn = psycopg2.connect(database="long-view", user="afe", password="1bellazio", host="localhost")
  cur = conn.cursor()

  cur.execute(query)
  idRow = cur.fetchone()[0]

  cur.close()
  conn.close()

  return idRow

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

def addTeam(teamName, leagueId):
  teamName = teamName.replace("'", " ")

  # INSERT INTO clubs (full_name, country_id) VALUES ('Juventus', 3);
  country_id = getCountryId(leagueId)

  query = "INSERT INTO clubs (full_name, country_id) VALUES ('{0}', {1}) RETURNING id;".format(teamName, country_id)

  return addRow(query)

def getTeamIdAndAdd(teamName, leagueId):
  addRow = addTeam(teamName, leagueId)
  
  if not addRow:
    return getTeamId(teamName)

  return addRow

def addMatchToDatabase(row, header, season):
  row = list(row)
  h = parseHeader(header)
  leagueId = row[0]
  league_id = getLeagueId(leagueId)
  home_id = getTeamIdAndAdd(row[2], leagueId)
  away_id = getTeamIdAndAdd(row[3], leagueId)
  season_id = getSeasonId(season)
  row[0] = league_id
  row[2] = home_id
  row[3] = away_id
  row.insert(0, season_id)
  row = cleanRow(row)
  query = "INSERT INTO matches ({0}) VALUES {1} RETURNING id;".format(h, tuple(row))

  try:
    addRow(query)
  except Exception as e:
    print season
    print query
    sys.exit(e)

if __name__ == "__main__":
  seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  countries = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  for season in seasons:
    for country in countries:
      fullPath = createFullPath(season, country)
      df = pandas.read_csv(fullPath, index_col=False, header=0)
      header = df.columns.values
      for row in df.itertuples(index=False):
        r = row[0:]
        addMatchToDatabase(r, header, season)