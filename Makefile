# run the coverage report and open results in a browser
cov:
	pytest --cov-report html --cov messageboxex
	# on mac, this will open the coverage report in a browser
	open htmlcov/index.html
