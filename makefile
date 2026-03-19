.PHONY: 
	all
	download 
	filter-buffer
	process-census
	choropleth
	clean-figures 
	clean-raw-data 
	clean-processed-data 
	clean

all: download filter-buffer process-census choropleth

download:
	python scripts/01-data_download.py

filter-buffer:
	python scripts/02-filter_buffer_parks.py

process-census:
	python scripts/03-process_census_data.py

choropleth:
	python scripts/04-generate-choropleth.py

clean-figures:
	rm -f report/figures/*

clean-raw-data:
	rm -f data/raw/*

clean-processed-data:
	rm -f data/processed/*

clean: clean-figures clean-raw-data clean-processed-data