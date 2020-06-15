# gmapspot
This is a tool that convert `scrape47` output to `quiz47` quiz data.

## Usage
```bash
# Please set your google maps api key.
export MAPS_JAVASCRIPT_API="YOUR_GOOGLE_MAPS_API_KEY"

# Add the place estimated by Google Maps to the last column in json format.
cat scrape.tsv | python src/gmaps.py > gmaps.tsv

# Output checksheet.
cat gmaps.tsv | python src/checksheet.py > checksheet.csv

# Output json for quiz47.
cat checksheet.csv | python src/output.py | nkf -s > spot.csv
```
