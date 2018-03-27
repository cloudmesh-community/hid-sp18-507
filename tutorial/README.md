# Openchain

Openchain is a company and blockchain technology developed so that individuals or enterprises could stand up and maintain a customizable blockchain platform.


## Purpose

The purpose of this tutorial is to provide the steps necessary to spin up an Openchain server as well as create a wallet-user account to interact with the openchain.

This tutorial includes a number of assumptions as well as a list of required software requirements. Although specific software is required for the purposes of this tutorial, the tutorial will not provide the steps necessary to use the software. Where appropriate, links to additional resources will be provided.

**Note to the User**  
Openchain offers both a container-based setup, using a Docker image, as well as a more in-depth and customizable setup process for advanced users. This tutorial will go through the setup process using the Docker image.

## Assumptions

+ User is working with a Linux (Debian) operating system
+ User is capable of using a terminal/command line
+ User is capable of using a virtual environment
+ User has root privileges or is capable of acquiring necessary permissions
+ Python 3+ is installed (necessary packages will be identified)
+ user is familiar with git/github
+ User is familiar with unix-based text editors (nano, emacs, vi, vim)
+ Port 8080 is available (default for Openchain Server)
+ User maintains a constant internet connection
+ Openchain 0.7 Deployment (version)

## Software Requirements

+ Python 3.*
+ Pip
+ Docker (Community Edition)
+ Docker-Compose
+ Git
+ Emacs (or similar text editors)

## Pre-set-up

First, update package index: `sudo apt-get update`  
Second, install Docker  

 - Docker installation steps are available in the Docker Section of the handbook as well as the [Docker Installation Documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1) published by Docker.

Optional: Set up virtual environment  

 - The user has the option of setting up a virtual environment prior to setting up the Openchain server. We recommend using `pyenv` or `virtualenv` to set up a specific python environment. Information on installing and using a virtual environment is available on [Pyenv's Git Page](https://github.com/pyenv/pyenv "pyenv") and [Virtualenv's documentation site](https://virtualenv.pypa.io/en/stable/ "Virtualenv").

Finally, install docker-compose for Python: `pip install docker-compose`

## Installing, Setting Up, and Configuring an Openchain Server

First we will need to clone Openchain's git repository for the docker image. For purposes of this tutorial, we will clone the repository to a new folder titled `openchain` to the home directory; however, if you are using a virtual environment, ensure that the environment is activated and you are working in the correct directory.

	git clone https://github.com/openchain/docker.git openchain  
	cd openchain

Once you are in the openchain directory that has just been created, we will copy the docker-compose yaml file to a new yaml file, create a new directory for data storage, and finally the sample template configuration file to the new data directory.
	
	cp templates/docker-compose-direct.yml docker-compose.yml
	mkdir data
	cp templates/config.json data/config.json

Next, we will need to edit the `instance_seed` within the copied config file. This seed should be long and is typically randomly generated for security purposes; however, for purposes of the tutorial, we will use a simple example seed. Open the `config.json` file in your text editor of choice. Ex. `emacs config.json`. The section '//Define transaction validation parameters' should be visible on screen as this is where we will add the instance_seed string. Note the addition of `openchain123tutorial456` in the code below.

	// Define transaction validation parameters
	"validator_mode": {
	 // Required: A random string used to generate the chain namespace
	 "instance_seed": "openchain123tutorial456",
	 "validator": {

At this point, you should be able to initiate the Openchain server.

	docker-compose up

If you would like to run the Openchain Docker container in the background, add the `-d` tag at the end of the command above. In order to monitor the status of the server, open a new terminal and run `docker logs openchain-server` to view the logs.

**Note**  
Depending on the permission settings of the user, root privileges are required to operate the server. If you need to manage Docker as a non-root user, follow the following steps, which are provided on [Docker's Documentation Site](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user "Manage Docker as a non-root user"):

**!!! WARNING !!!** - The following steps enable root-equivalent privileges to a new group, `docker`, which can be a security-compromising addition. Review the implications at Docker's [Daemon Attack Surface](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface) warning.

	sudo groupadd docker
	sudo usermod -aG docker $USER

In order to restart and stop the server, you have two options, depending how you initiated the server (whether you used the '-d' tag or not). If you omitted the -d tag and the terminal is displaying server status information, you can press `Ctrl+c` to stop the server (and once more to force the shutdown immediately) or if the server is running in the background, in a new terminal, simply execute `docker-compose restart` to restart the server and `docker-compose stop` to stop it.

## Configuration for Client Use

Now that the Openchain server is up and running, it needs an administrator and although you'd assume that is you automatically, you first need to create an account and provide the address of your account to the configuration file.

The following steps through the end of the tutorial will utilize Openchain's web-base client interface, or a 'wallet' to manage the asset information you intend to store on your Openchain server. It is crucial that the next steps be followed, in order, to ensure your account is created, given admin rights, and all subsequent steps are taken as an active administrator.

### Account creation and administration rights

Go to [Openchain's Client Site](http://nossl.wallet.openchain.org) to create a new wallet. Note, this is the 'nossl' client because the server has been deployed on a local machine for purposes of this tutorial. Openchain offers a different secured wallet for https-based urls.  

Then, in the 'Endpoint URL' field, enter `http://0.0.0.0:8080/` as this is the default address and port which the server should be running.  
Next, click 'Create new wallet'. This generates a random string used to create the account.

 - **IMPORTANT**  
You will need this passphrase each time you log in as this is your key to getting access to the server. Keep this phrase in a secure place.

Copy the passphrase created and click the 'Back' button. Paste the passphrase in the field and click 'Sign In'.

 - Congratulations, the server's first account has been created. Onto setting up this account as the admin account:
	
Once you are logged in, the page you see will provide a unique path, or address, under 'Receive Funds'. `Ex: XxWCrT1TBUwFtphLmV1qkMwnc9ojQWwtCS`. Copy that address.  

Open the config.json document again and edit the `admin_addresses` line within the `validator_mode` section so that the path you copied is pasted as a string (with quotes).

        Example:
        "admin_addresses": ["XxWCrT1TBUwFtphLmV1qkMwnc9ojQWwtCS"
        ],

Restart the server so that the changes to the config.json file are active.

 - Before continuing, you want to add some information to your server so that the clients, or Openchain Wallets, can interact with the service.

Returning to the wallet client website. Assuming you are still logged in, click the 'Advanced' tab at the top of the page.  
next, click 'Edit Ledger Info'. Here you can add specific information about the ledger that is visible when users connect. For purposes of the tutorial, we can name it `Tutorial Ledger`. Feel feel free to edit the other information as well.

 - Next, we will issue our first asset. Here is where an enterprise can set up the description and quantity of the asset they intend to manage.

Click the 'Assets' tab at the top of the page and select 'Tutorial Ledger' from the drop-down. Note, you may have to re-log-in to the server or restart the server so that the new ledger information is pulled into the web client.  

In the 'Asset Path' field, you'll want to enter the specific path to your address, as if you are issuing an asset for the first time. The path should look something like this:

        /asset/p2pkh/XxWCrT1TBUwFtphLmV1qkMwnc9ojQWwtCS/

Once you click 'Confirm', you will need to add information to the transaction. For purposes of the tutorial, we will issue a fake 'IU Coin'. Enter the following into the three fields, respectively:

        Asset Name:	IU Coin
        Asset Image URL: https://www.iu.edu/images/iu-250x250.png  
        Ticker: IUC  

Finally, scrolling down, click 'Issue Asset', and Enter a quantity that you intend to create. Let's go with 524. Now click 'Issue'.

The transaction should go through. If it fails because you don't have admin rights, verify that you have added your specific path to the config file and have restarted the server to changes are in effect. You can view the asset and transaction information, which is natively in JSON format (and can be queried as such). 

Again, you may need to refresh your connection to the server and log back in. After doing so, you should be able to see that the 'Tutorial Ledger' shows that you have 524 IUCs or 'IU Coin' and if you used the Asset Image URL above, the IU logo should show.

## Openchain, Open for Business

You have successfully implemented your Openchain instance and created an asset that can now be traded and queried from anyone on the chain. New users can created a wallet using the same steps listed above. Adding other users' addresses to the config file can grant them administration rights as well.

You can also created 'Observer Nodes' or servers that act as a repository to viewing thr transactions with no capability to validate any transactions.

The example created in this tutorial is trivial compared to the technology Blockchain is being used for by enterprises today. For additional customizations and capabilities be sure to check out [Openchain's Documentation Site](https://docs.openchain.org/en/latest/index.html), as well as the [Openchain Forum](https://forum.openchain.org/) for assistance and community-based help-desk service.

## Resources

Blockchain - [Wikipedia](https://en.wikipedia.org/wiki/Blockchain)  
Openchain - [Official Site](https://www.openchain.org/)  
Openchain - [Documentation](https://wallet.openchain.org/#/addendpoint)  
Openchain - [Wallet](https://wallet.openchain.org/#/addendpoint)  
Pyenv - [GitHub](https://github.com/pyenv/pyenv)  
Docker - [Official Site](https://www.docker.com/)  
