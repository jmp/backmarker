#!/bin/sh -e

DUMP_URL=http://ergast.com/downloads/f1db_ansi.sql.gz

TABLE_PREFIX=backmarker_
TABLE_CIRCUITS=${TABLE_PREFIX}circuit
TABLE_CONSTRUCTOR_RESULTS=${TABLE_PREFIX}constructorresult
TABLE_CONSTRUCTOR_STANDINGS=${TABLE_PREFIX}constructorstanding
TABLE_CONSTRUCTORS=${TABLE_PREFIX}constructor
TABLE_DRIVER_STANDINGS=${TABLE_PREFIX}driverstanding
TABLE_DRIVERS=${TABLE_PREFIX}driver
TABLE_LAP_TIMES=${TABLE_PREFIX}laptime
TABLE_PIT_STOPS=${TABLE_PREFIX}pitstop
TABLE_QUALIFYINGS=${TABLE_PREFIX}qualifying
TABLE_RACES=${TABLE_PREFIX}race
TABLE_RESULTS=${TABLE_PREFIX}result
TABLE_SEASONS=${TABLE_PREFIX}season
TABLE_STATUSES=${TABLE_PREFIX}status

curl -o mysql_dump.sql.gz $DUMP_URL
zcat < mysql_dump.sql.gz | \
  sed -e "s/\\\'/''/" | \
  sed -e '/^CREATE/,/;$/c\' | \
  sed -e "s/\"circuits\"/\"$TABLE_CIRCUITS\"/" | \
  sed -e "s/\"constructorResults\"/\"$TABLE_CONSTRUCTOR_RESULTS\"/" | \
  sed -e "s/\"constructorStandings\"/\"$TABLE_CONSTRUCTOR_STANDINGS\"/" | \
  sed -e "s/\"constructors\"/\"$TABLE_CONSTRUCTORS\"/" | \
  sed -e "s/\"driverStandings\"/\"$TABLE_DRIVER_STANDINGS\"/" | \
  sed -e "s/\"drivers\"/\"$TABLE_DRIVERS\"/" | \
  sed -e "s/\"lapTimes\"/\"$TABLE_LAP_TIMES\"/" | \
  sed -e "s/\"pitStops\"/\"$TABLE_PIT_STOPS\"/" | \
  sed -e "s/\"qualifying\"/\"$TABLE_QUALIFYINGS\"/" | \
  sed -e "s/\"races\"/\"$TABLE_RACES\"/" | \
  sed -e "s/\"results\"/\"$TABLE_RESULTS\"/" | \
  sed -e "s/\"seasons\"/\"$TABLE_SEASONS\"/" | \
  sed -e "s/\"status\"/\"$TABLE_STATUSES\"/" \
  > tmp.sql

rm -f mysql_dump.sql.gz
OUT_FILE=populate.sql
rm -f $OUT_FILE
touch $OUT_FILE

echo "TRUNCATE TABLE \"$TABLE_CIRCUITS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_DRIVERS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_CONSTRUCTORS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_SEASONS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_STATUSES\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_RACES\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_CONSTRUCTOR_RESULTS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_CONSTRUCTOR_STANDINGS\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_LAP_TIMES\" CASCADE;" >> $OUT_FILE
echo "TRUNCATE TABLE \"$TABLE_DRIVER_STANDINGS\" CASCADE;" >> $OUT_FILE

cat tmp.sql | grep "\"${TABLE_PREFIX}circuit\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}driver\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}constructor\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}season\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}status\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}race\"" >> $OUT_FILE   
cat tmp.sql | grep "\"${TABLE_PREFIX}constructorresult\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}constructorstanding\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}laptime\""| sed "s/VALUES (/VALUES ((SELECT COALESCE(MAX(id)+1, 0) FROM $TABLE_LAP_TIMES),/" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}driverstanding\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}pitstop\""| sed "s/VALUES (/VALUES ((SELECT COALESCE(MAX(id)+1, 0) FROM $TABLE_PIT_STOPS),/" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}qualifying\"" >> $OUT_FILE
cat tmp.sql | grep "\"${TABLE_PREFIX}result\"" >> $OUT_FILE   

rm -f tmp.sql

DATABASE_HOST=localhost
DATABASE_USER=postgres
DATABASE_NAME=postgres

cat $OUT_FILE | psql -h $DATABASE_HOST -U $DATABASE_USER -d $DATABASE_NAME -q -b

rm -f $OUT_FILE
