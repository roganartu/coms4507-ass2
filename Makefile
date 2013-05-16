SRCS=report.tex             \
     introduction.tex       \
     abstract.tex           \
		 conclusion.tex         \
		 question1.tex          \
		 question2.tex          \
		 question3.tex          \
		 question4.tex          \
		 question5.tex          \
		 question6.tex

all: report.pdf

report.pdf: $(SRCS)
	pdflatex report
	#bibtex report
	#pdflatex report
	pdflatex report

clean:
	@rm -f *.aux *.toc *.log *.blg report.pdf
