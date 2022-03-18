> This repo contains code to collect the Nexus blockchain data periodically and store it into a csv file.

### Usage

* Create a cronjob to run this script every hour/day.

### Example
* Open crontab in edit mode: `crontab -e`

* Add the following line:
```sh
0 0 * * * python3 home/john/nexus-data-collection/job.py
```