#!/bin/sh -e

# Download and extract CSV files
CSV_URL=http://ergast.com/downloads/f1db_csv.zip
CSV_FILE=f1db_csv.zip
CSV_DIR=$(PWD)/csv

curl $CSV_URL > $CSV_FILE
rm -rf "$CSV_DIR"
unzip $CSV_FILE -d "$CSV_DIR"
rm -f $CSV_FILE

# Remove header line from each file
for f in csv/*.csv; do
  tail -n +2 "$f" > "$f.tmp"
  mv "$f.tmp" "$f"
done

# For lap times and pit stops, we have to enumerate the lines
sed "=" "$CSV_DIR/lap_times.csv" | sed 'N;s/\n/,/' > tmp && mv tmp "$CSV_DIR/lap_times.csv"
sed "=" "$CSV_DIR/pit_stops.csv" | sed 'N;s/\n/,/' > tmp && mv tmp "$CSV_DIR/pit_stops.csv"

TABLE_CIRCUITS=backmarker_circuit
TABLE_CONSTRUCTOR_RESULTS=backmarker_constructorresult
TABLE_CONSTRUCTOR_STANDINGS=backmarker_constructorstanding
TABLE_CONSTRUCTORS=backmarker_constructor
TABLE_DRIVER_STANDINGS=backmarker_driverstanding
TABLE_DRIVERS=backmarker_driver
TABLE_LAP_TIMES=backmarker_laptime
TABLE_PIT_STOPS=backmarker_pitstop
TABLE_QUALIFYINGS=backmarker_qualifying
TABLE_RACES=backmarker_race
TABLE_RESULTS=backmarker_result
TABLE_SEASONS=backmarker_season
TABLE_STATUSES=backmarker_status

DATABASE_HOST=${DATABASE_HOST:-"localhost"}
DATABASE_USER=${DATABASE_USER:-"postgres"}
DATABASE_NAME=${DATABASE_NAME:-"postgres"}

psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" <<EOF
SET client_min_messages TO WARNING;

TRUNCATE TABLE "$TABLE_CIRCUITS" CASCADE;
TRUNCATE TABLE "$TABLE_DRIVERS" CASCADE;
TRUNCATE TABLE "$TABLE_CONSTRUCTORS" CASCADE;
TRUNCATE TABLE "$TABLE_SEASONS" CASCADE;
TRUNCATE TABLE "$TABLE_STATUSES" CASCADE;
TRUNCATE TABLE "$TABLE_RACES" CASCADE;
TRUNCATE TABLE "$TABLE_CONSTRUCTOR_RESULTS" CASCADE;
TRUNCATE TABLE "$TABLE_CONSTRUCTOR_STANDINGS" CASCADE;
TRUNCATE TABLE "$TABLE_LAP_TIMES" CASCADE;
TRUNCATE TABLE "$TABLE_DRIVER_STANDINGS" CASCADE;
TRUNCATE TABLE "$TABLE_PIT_STOPS" CASCADE;
TRUNCATE TABLE "$TABLE_QUALIFYINGS" CASCADE;

\\COPY $TABLE_CIRCUITS FROM '$CSV_DIR/circuits.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_DRIVERS FROM '$CSV_DIR/drivers.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_CONSTRUCTORS FROM '$CSV_DIR/constructors.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_SEASONS FROM '$CSV_DIR/seasons.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_STATUSES FROM '$CSV_DIR/status.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_RACES FROM '$CSV_DIR/races.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_CONSTRUCTOR_RESULTS FROM '$CSV_DIR/constructor_results.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_CONSTRUCTOR_STANDINGS FROM '$CSV_DIR/constructor_standings.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_LAP_TIMES FROM '$CSV_DIR/lap_times.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_DRIVER_STANDINGS FROM '$CSV_DIR/driver_standings.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_PIT_STOPS FROM '$CSV_DIR/pit_stops.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_QUALIFYINGS FROM '$CSV_DIR/qualifying.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY $TABLE_RESULTS FROM '$CSV_DIR/results.csv' WITH (FORMAT CSV, NULL '\\N');
EOF

rm -rf "$CSV_DIR"
