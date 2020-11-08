TARGETS = \
	Enigma\ -\ Python\ Introduction\ Webinar\ Handouts.pdf \
	Enigma\ -\ Python\ Introduction\ Webinar\ Presentation.pdf \



all: ${TARGETS}

clean:
	rm -f ${TARGETS}

mrproper: clean
	touch d.aux d.log d~ d.nav d.out d.snm d.toc includes.d
	rm -f *.aux *.log *~ *.nav *.out *.snm *.toc includes.*



includes:
	rm -Rf includes
	mkdir includes

includes.webinar.timestamp: ../bin/generate-tex-includes includes webinar_*.tex shared.tex # figs/*.svg
	cd .. ; bin/generate-tex-includes PDF doc/webinar_handouts.tex doc
	touch includes.webinar.timestamp



Enigma\ -\ Python\ Introduction\ Webinar\ Handouts.pdf: webinar_*.tex shared.tex includes.webinar.timestamp
	pdflatex -shell-escape webinar_handouts.tex
	pdflatex -shell-escape webinar_handouts.tex
	mv webinar_handouts.pdf Enigma\ -\ Python\ Introduction\ Webinar\ Handouts.pdf

Enigma\ -\ Python\ Introduction\ Webinar\ Presentation.pdf: webinar_*.tex shared.tex includes.webinar.timestamp
	pdflatex -shell-escape webinar_presentation.tex
	pdflatex -shell-escape webinar_presentation.tex
	mv webinar_presentation.pdf Enigma\ -\ Python\ Introduction\ Webinar\ Presentation.pdf
