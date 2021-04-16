setup:
	conda env create --file environment.yml || conda env update --file environment.yml

run_exploratory_data_analysis:
	cd notebooks \
		&& ipython "Exploratory Data Analysis.ipynb" \
		&& jupyter nbconvert --to html "Exploratory Data Analysis.ipynb"
