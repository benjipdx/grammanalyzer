#make a pdf
build: clean
	mkdir build
	pdflatex -output-directory build writeup.tex
	cp build/writeup.pdf ~/cs/public_html/
	cp build/writeup.pdf writeup.pdf
	chmod 744 ~/cs/public_html/writeup.pdf

#clean the build dir
clean:
	rm -rf build
