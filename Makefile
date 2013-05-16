SRCS=report.tex             \
     introduction.tex       \
     abstract.tex

all: report.pdf

report.pdf: $(SRCS)
	pdflatex report
	#bibtex report
	#pdflatex report
	pdflatex report

clean:
	@rm -f *.aux *.toc *.log *.blg report.pdf
