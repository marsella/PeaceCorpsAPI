"""
  Initial features of interest

  slug
  region
  sectors
  languages

"""

import urllib2
import json
from collections import namedtuple

# id : unique country ID (integer)
# name : human-readable country name (string)
# slug : unique country ID (string)
# region : unique region ID (string)
# current : program is active? (bool)
# volunteers : number of PC volunteers (int)
# pcr : is Peace Corps Response available (bool)
# sectors : PC sectors availabble (list of string)
# langs : languages spoken (list of string)
Opportunity = namedtuple('Opportunity', 'id, name, slug, region, current, \
  volunteers, pcr, sectors, langs')

# enumeration for sectors
NUMSECTORS = 6
class Sectors:
  Agriculture, Community, Education, Environment, Health, Youth = \
    range(NUMSECTORS)

# parses single opportunity as described in PCCR REST API into interesting
# features
# opp : JSON object
# rets : Opportunity object
def parseOpportunity(opp):
  print 'parsing opportunity now'
  country_id = opp['id']
  name = opp['name']
  slug = opp['slug']
  region = opp['region']
  current = opp['current']
  volunteers = opp['volunteers']
  pcr = opp['pcr']
  sectors = parseSectors(opp['sectors'])
  langs = parseLanguages(opp['languages'])

  return Opportunity(country_id, name, slug, region, current, volunteers,
    pcr, sectors, langs)


# sectors : sectors field from request
# rets : list of sectors
def parseSectors(sector_str):
  classes = [u'agriculture', u'community', u'education', 
    u'environment', u'health', u'youth'];

  sectors = [0] * NUMSECTORS
  for i in range(NUMSECTORS):
    if classes[i] in sector_str.lower():
      sectors[i] = 1
    
  return sectors

# lang_str : language field from request
# rets : list of languages
# notes : sometimes will return alternate spellings as list item, 
#   i.e., 'also known as Kweyole' 
def parseLanguages(lang_str):
  # TODO: integrate with existing list of languages (standardize results)
  print lang_str
  langs = lang_str.replace('and',',').split(',')
  return langs

# test function to pull from API to parse
# rets : JSON object (ideally one opportunity??)
def getOpportunities():
  print 'getting opportunity'
  url = 'http://www.peacecorps.gov/api/v1/geography/countries/belize'
  url = 'http://www.peacecorps.gov/api/v1/geography/countries/?' \
  + 'region=caribbean&current=true'
  obj = urllib2.urlopen(url).read()
  return json.loads(obj)
  


if __name__ == "__main__":
  opp = getOpportunities()
  for o in opp:
    print parseOpportunity(o)







