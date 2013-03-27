# format [name, domain, data_type, socrata_id, options]

datasets_core = [
 # pg_dumps from Cory's scrapers - disabled for now
 # see https://github.com/maschinenmensch/edifice/issues/21
 # ['cook_county','','pgdump','',{}],
 # ['assessor','','pgdump','',{}],
 # ['landuse','','pgdump','',{}],

 # gazeeter for address matching
 # see: https://github.com/maschinenmensch/edifice/issues/23
 ['street_gazetteer','Chicago','csv','i6bp-fvbx',{}],
 ['building_permits','Chicago','csv','ydr8-5enu',{}],

 # core buildings datasets
 #['Building Footprints','Chicago','shp','w2v3-isjw',{'encoding': 'LATIN1'}],
 #['Building Permits','Chicago','csv','ydr8-5enu',{}],
 #['Building Violations','Chicago','csv','22u3-xenr',{}],
 #['zoning_aug2012','Chicago','shp','p8va-airx',{}]
]
