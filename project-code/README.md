## Twitter Scrape, Storage, RESTful Query, and Analysis
The purposes of this README file is to accompany the Twitter scrape and analysis project as part of Indiana University's Spring 2018 I524 course.
**To reads steps necessary to run the code, jump to the "Execute Code" subsection.** --Please review the assumptions and disclaimer sections prior to executing commands.

## Disclaimer
The project completed by hid-sp18-507 began development in early spring 2018 and any replications of this project **will result in differing statistics and figures** than those presented in the accompanying paper. This is because the nature of the project is designed to pull recent data from Twitter, as allowed by Twitter's free developer accounts. 

The storage of scraped data will be stored on an existing cloud database, hosted by AWS and available through MongoDB Atlas. Pre-existing data may be available on the database and new data can be stored and accessed on this database free of charge. 

Developer accounts and service-specific keys have already been produced and built into the project's code and should not be altered. Additionally, per the requirements for replication, the accounts created are intended to be used for this project only and have been given administrative rights.  


# Setup
Included with this project are five (5) python files, a requirements file, a makefile, and this README. 
## Assumptions
In order to use the makefile as intended, the user may require root privileges and a clean/functional working environment (python). 
The makefile will open alternative terminals for services such as REST and managing the MongoDB cloud database. 
> If the code fails in a new terminal, you may have to re-activate the virtual environment and manually re-run the code
## Makefile
The makefile includes a number of options. The recommended process in using this file is outlined below. Additionally, you can run "**make options**" to display a number of make [target] commands.

--[STANDARD PROCESS COMMANDS]--

  - setup                :: Will install and setup all required processes prior to executing accompanying code.
  - run-part1            :: Will run the first step which scrapes, stores, and then produces the data locally--prior to analysis.
  - run-part2            :: Will use the active REST service to pull and save data as CSV files for analysis, then conduct the analysis.


--[INDIVIDUAL COMMANDS]--

  - install-mongo        :: Installs MongoDB on your system (required for mongo functionality and MongoDB Atlas
  - atlas-shell          :: Will open a new terminal and connect you to the project-specific MongoDB Atlas database. The credentials used come with administrative privileges.
  - pre-matplotlib       ::  Installs python packages required to run matplotlib
  - install-py-packages  :: Installs python packges per the accompanying requirements document.

  - start-scrape         :: Will scrape Twitter for tweet and user data and will automatically store the data on the Atlas cloud.
  - start-rest           :: Will initiate the REST service so that data on the cloud can be pulled and viewed via localhost.
  - start-pull           :: Downloads data from the REST service address (localhost) and saved data within two CSV files.
  - start-analysis       :: Conducts analysis using the data within the created CSV files. WILL PRODUCE THREE HISTOGRAMS.

# REST Service
The rest.py file uses flask to expose the stored data on localhost and port 5000. The following are the available addresses for GET requests. Data is available in JSON format and can be queried using curl.
**Example**: "curl -i http://localhost:5000/users"

> http://localhost:5000/tweets/data
> http://localhost:5000/users
> http://localhost:5000/users/names
> http://localhost:5000/tweets/text
> http://localhost:5000/tweets/userhistory
> http://localhost:5000/tweets/ratios

# Execute Code
**A new terminal will open in the foreground once the REST service begins. Leave this active and return to the original terminal to continue make commands.**
Once the virtual environment is set up and the directory is active, run the following commands in order. [**Note:** the processes and python files may take time to complete the tasks---please allow adequate time between commands.]
- Display the options within the makefile
> make options
- Setup/Install all requirements
> make setup
- Scraped Twitter, stores data on MongoDB Atlas Cloud, starts REST service
> make run-part1
- Pulls data from REST address and saves data to local CSV files, performs analysis on the CSVs and produces histograms.
> make run-part2

## Closing Out
Once the code has been tested and replicated, you will need to manually end active services/tasks. Because the services were started in new terminals, for status purposes, you must execute '**Ctrl+c**' to end these processes.