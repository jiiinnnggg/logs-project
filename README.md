## Logs project
Udacity FSND logs project (a postgresql exercise)

This code looks to interact with some data by making queries to answer questions about contents in a news database. The tables included in the database consist of:

1. A list of articles and their attributes - `articles`
2. A list of authors and brief descriptions - `authors`
3. A log tracking visits to a website where the articles are posted - `log`

We'll use python and the [psycopg2](http://initd.org/psycopg/) package to interact with the database. The project also makes use of the Vagrant/VirtualBox VM environment. 

----
## Getting started

**I. Setting up VM**

To get everything up and running, we'll need to install VirtualBox and Vagrant. If you have already done this, skip to the next section.

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads), install the platform package.
2. Install [Vagrant](https://www.vagrantup.com/downloads.html), then run `vagrant --version` in your terminal to confirm proper installation (it should say something like `Vagrant 2.0.0`.
3. Clone the VM config files from the Udacity [repository](https://github.com/udacity/fullstack-nanodegree-vm) to your local environment. Then from your terminal, navigate to the `vagrant` subdirectory and run `vagrant up`. This will initiate the download and setup of the vagrant linux environment.
4. Once that's completed, run `vagrant ssh` from the `vagrant` subdirectory to log into the VM to confirm proper setup.

![vagrant ssh success](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58fa90dd_screen-shot-2017-04-21-at-16.06.30/screen-shot-2017-04-21-at-16.06.30.png)(*source: Udacity tutorial*)

**II. Setting up database** (detailed instructions [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91))

1. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and put the `newsdata.sql` file into a subdirectory within the `vagrant` directory.
2. Log in to the vagrant VM, navigate to the folder containing the `newsdata.sql` file and run:

>
    psql -d news -f newsdata.sql

This will connect  to the database named `news` from the source `newsdata.sql` file. You can then access the news database by running the command:

>
    psql news


**III. Running the code from this repo**

1. Clone this repo and copy the `logsproject.py` file to the same folder where the news database and `newsdata.sql` are.
2. Log in to the vagrant VM and run:

>
    python logsproject.py

If the program runs correctly the output should read something like the [sample output](https://github.com/jiiinnnggg/logs-project/blob/master/sample_output.txt) file in this repository.
