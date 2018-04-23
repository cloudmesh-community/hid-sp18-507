#
# Naturally you need to adapt this to make work for your project
#

setup:
	@echo "This will run all setup commands within the makefile..."
	@echo
	make install-mongo
	make install-py-packages
	@echo
	@echo "..."
	@echo "Setup Complete"
	@echo "You can now run 'make run-part1' to begin..."

run-part1:
	@echo "This will use python to scrape data from Twitter, store the data on a MongoDB Atlas cloud database, and then start a REST service on localhost so the data can be analysed in Part 2."
	@echo
	make start-scrape
	@echo
	make start-rest
	@echo
	@echo "Part 1 complete. Without closing or ending services, you may run Part 2 with 'make run-part2'."

run-part2:
	@echo "This will use python to pull data from the ACTIVE REST address, save the data in the local directory as CSV files, and conduct analysis on the pulled data."
	@echo
	make start-pull
	@echo
	make start-analysis
	@echo
	@echo "Part 2 complete."
	@echo
	@echo "If you no longer wish to utilize the Twitter data, the REST service, or the optional MongoDB Atlas Shell, please close the respective terminals (Ctrl+c)."
	@echo
	@echo
	@echo

options:
	@echo "make [target] commands:"
	@echo
	@echo "--[STANDARD PROCESS COMMANDS]--"
	@echo
	@echo "  - setup                :: Will install and setup all required processes prior to executing accompanying code."
	@echo "  - run-part1            :: Will run the first step which scrapes, stores, and then produces the data locally--prior to analysis."
	@echo "  - run-part2            :: Will use the active REST service to pull and save data as CSV files for analysis, then conduct the analysis."
	@echo
	@echo
	@echo "--[INDIVIDUAL COMMANDS]--"
	@echo
	@echo "  - install-mongo        :: Installs MongoDB on your system (required for mongo functionality and MongoDB Atlas"
	@echo "  - atlas-shell          :: Will open a new terminal and connect you to the project-specific MongoDB Atlas database. The credentials used come with administrative privileges."
	@echo "  - pre-matplotlib       ::  Installs python packages required to run matplotlib"
	@echo "  - install-py-packages  :: Installs python packges per the accompanying requirements document."
	@echo
	@echo "  - start-scrape         :: Will scrape Twitter for tweet and user data and will automatically store the data on the Atlas cloud."
	@echo "  - start-rest           :: Will initiate the REST service so that data on the cloud can be pulled and viewed via localhost."
	@echo "  - start-pull           :: Downloads data from the REST service address (localhost) and saved data within two CSV files."
	@echo "  - start-analysis       :: Conducts analysis using the data within the created CSV files. WILL PRODUCE THREE HISTOGRAMS."
	@echo


install-mongo:
	@echo
	@echo "==Installing MongoDB on your system...=="
	@echo
	@echo "Importing MongoDB public key..."
	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
	@echo "Creating list file for MongoDB (assumes Ubuntu 16.04)..."
	deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
	@echo "Reloading local package database..."
	sudo apt-get update
	@echo 
	@echo "Installing MongoDB Community Edition..."
	@echo
	sudo apt-get install -y mongodb-org


atlas-shell:
	@echo "Connecting to MongoDB Atlas Cloude Service via mongo-shell in new terminal. Changes to the database are not recommended."
	x-terminal-emulator -e "mongo --host Cluster524-shard-0/cluster524-shard-00-00-vl3t1.mongodb.net:27017,cluster524-shard-00-01-vl3t1.mongodb.net:27017,cluster524-shard-00-02-vl3t1.mongodb.net:27017 --ssl --username hidsp18507 --password hidsp18507! --authenticationDatabase admin"

pre-matplotlib:
	sudo apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev libsqlite3-dev tk-dev
	sudo apt-get install -y libpng-dev libfreetype6-dev

install-py-packages:
	@echo "Using requirements document to install required python packages..."
	@echo
	@echo "Installing specific packages required for 'matplotlib' use (per pizza post 431)..."
	make pre-matplotlib
	@echo
	@echo "Installing from requirements.txt"
	pip install -r requirements.txt

start-scrape:
	@echo "Scraping Twitter for user Data..."
	@echo 
	python mongoinsert.py
	@echo
	@echo "Data scraped and stored on MongoDB's Atlas Cloud."
	@echo "Ready to start REST service to access and display data locally."

start-rest:
	@echo "Executing Python-REST service in new terminal."
	x-terminal-emulator -e "python rest.py"
	@echo "RESTful service now available via 127.0.0.1:5000"
	@echo "See the README file for available requests."

start-pull:
	@echo "Reading and pulling data from running REST Service."
	python ippull.py
	@echo "Data has been pulled and save in CSV formats for analysis."

start-analysis:
	@echo "Using data pulled and stored as CSV files from REST calls."
	@echo "## WARNING ## - 3 Histograms will be produced, which you will need to close to proceed."
	@echo "These histograms are examples of what is published within the project paper."
	@echo
	@echo
	@echo
	@echo
	@echo
	@echo
	@echo
	python twitteranalysis.py
