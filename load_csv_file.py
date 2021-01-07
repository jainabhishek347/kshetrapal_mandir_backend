# import psycopg2
# conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
# cur = conn.cursor()
# with open('user_accounts.csv', 'r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f) # Skip the header r
     #cur.copy_from(f, 'users', sep=',')
# = gp_conn.fetchall()

# conn.commit()
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'composeexample.settings'

import django
django.setup()
import psycopg2
import psycopg2.extras
from resturent.models import Resturent

#from forms import SearchForm

conn = psycopg2.connect(database='postgres',
                        host='test_db',
                        user='postgres',
                        password='postgres',
                        port='5432',
                        cursor_factory=psycopg2.extras.RealDictCursor)

cur = conn.cursor()

query ="""drop table if exists main_raw_resturent;
create table main_raw_resturent 
( raw_id             character varying(100),
 dateAdded          character varying(100),
 dateUpdated        character varying(100),
 address            character varying(1000),
 categories         character varying(1000),
 primaryCategories  character varying(100),
 city               character varying(100),
 country            character varying(100),
 keys               character varying(100),
 latitude           character varying(100),
 longitude          character varying(100),
 name               character varying(100),
 postalCode         character varying(100),
 province           character varying(100),
 sourceURLs         text,
 websites           character varying(1000)
 );

 copy main_raw_resturent from '/Datafiniti_Fast_Food_Restaurants_May19.csv'  WITH (FORMAT csv);"""

cur.execute(query)

query = "select * from main_raw_resturent offset 1 limit 10000;"
cur.execute(query)
result = cur.fetchall()
for data in result:
	
	p = Resturent(
	location_id = data['raw_id'],	
	address = data['address'],
	categories =data['categories'],
	primaryCategories =data['primarycategories'],
	city =data['city'],
	country =data['country'],
	keys =data['keys'],
	latitude =data['latitude'],
	longitude =data['longitude'],
	name =data['name'],
	postalCode =data['postalcode'],
	province = data['province'],
	sourceURLs= data['sourceurls'],
	websites = data['websites'] if data['websites'] else ''
	)
	p.save()
