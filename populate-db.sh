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

DATABASE_HOST=${DATABASE_HOST:-"localhost"}
DATABASE_USER=${DATABASE_USER:-"postgres"}
DATABASE_NAME=${DATABASE_NAME:-"postgres"}

psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" <<EOF
SET client_min_messages TO WARNING;

TRUNCATE
  "backmarker_result",
  "backmarker_qualifying",
  "backmarker_pitstop",
  "backmarker_driverstanding",
  "backmarker_laptime",
  "backmarker_constructorstanding",
  "backmarker_constructorresult",
  "backmarker_race",
  "backmarker_status",
  "backmarker_season",
  "backmarker_constructor",
  "backmarker_driver",
  "backmarker_circuit"
RESTART IDENTITY;

\\COPY backmarker_circuit FROM '$CSV_DIR/circuits.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_driver FROM '$CSV_DIR/drivers.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_constructor FROM '$CSV_DIR/constructors.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_season FROM '$CSV_DIR/seasons.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_status FROM '$CSV_DIR/status.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_race FROM '$CSV_DIR/races.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_constructorresult FROM '$CSV_DIR/constructor_results.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_constructorstanding FROM '$CSV_DIR/constructor_standings.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_laptime FROM '$CSV_DIR/lap_times.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_driverstanding FROM '$CSV_DIR/driver_standings.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_pitstop FROM '$CSV_DIR/pit_stops.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_qualifying FROM '$CSV_DIR/qualifying.csv' WITH (FORMAT CSV, NULL '\\N');
\\COPY backmarker_result FROM '$CSV_DIR/results.csv' WITH (FORMAT CSV, NULL '\\N');
EOF

rm -rf "$CSV_DIR"
