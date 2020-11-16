TARGETS = \
	cairoexample.pdf \
	running-average.pdf \



all: ${TARGETS}

clean:
	touch ${TARGETS}
	RM    ${TARGETS}

mrproper: clean
	touch d~
	rm    *~



2020118194823303242491FODDAG77873904000.csv:
	curl 'https://www.statistikbanken.dk/statbank5a/temp/2020118194823303242491FODDAG77873904000.csv' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.statistikbanken.dk/statbank5a/selectvarval/saveselections.asp' -H 'Connection: keep-alive' -H 'Cookie: ASPSESSIONIDQWDABASB=PBOKAGLDHMBPMDGPDDLLPBKB' -H 'Upgrade-Insecure-Requests: 1' -H 'TE: Trailers' > 2020118194823303242491FODDAG77873904000.csv

cairoexample.pdf: cairoexample.py
	python3 cairoexample.py

dkbirths2019.csv: simplify-birthdata.py 2020118194823303242491FODDAG77873904000.csv
	python3 simplify-birthdata.py

running-average.pdf: pandas-example.py dkbirths2019.csv
	python3 pandas-example.py

