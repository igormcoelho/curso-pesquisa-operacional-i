MDFILE=5-fundamentos.md
OUTHTML=index.html
OUTPDF=5-fundamentos.pdf
FILTERS= --filter ../../libs/pandoc-plot --filter pandoc-source-exec \
            --filter ../../libs/comments-to.py #--filter pandoc-latex-color
FILTERS_WEB= --filter pandoc-katex  

all: deps
	cp -r figs/ /tmp/
	/usr/bin/pandoc -s --self-contained -V theme=beige -s -t revealjs \
	--metadata to="revealjs" $(FILTERS) $(FILTERS_WEB) --css katex.min.css \
	$(MDFILE) -o $(OUTHTML) --slide-level 2
	#
	#
	# -F pandoc-crossref
	/usr/bin/pandoc --toc -s --self-contained -V theme:Warsaw -t beamer \
	--metadata to="beamer" $(FILTERS)  -H header.tex \
	$(MDFILE) -o $(OUTPDF) --slide-level 2

run:
	python3 -m http.server 8081
	#python2 -m SimpleHTTPServer 8081

env:
	source ~/.cargo/env
	conda activate

deps:
	wget -nc https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css
	wget -nc https://github.com/hakimel/reveal.js/archive/master.tar.gz
	# tar -xzvf master.tar.gz && mv reveal.js-master reveal.js
