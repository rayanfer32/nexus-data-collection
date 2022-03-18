# The Data collected could be used to show the historical charts / produce analytics  of nexus project
# Run all the apis and append the result to a csv
# Collectibles
# 1. info - system/get/info
# 2. metrics - system/get/metrics
# 3. mining - ledger/get/info

import time
import config
import requests
import pandas as pd
from os.path import exists

def get_info():
    """Get the system info"""
    return requests.get(f"{config.MAINNET_SERVER}/system/get/info").json()["result"]


def get_metrics():
    """Get the system metrics"""
    return requests.get(f"{config.MAINNET_SERVER}/system/get/metrics").json()["result"]


def get_mining():
    """Get the mining info"""
    return requests.get(f"{config.MAINNET_SERVER}/ledger/get/info").json()["result"]


def main():
    """Run all the API's and append the data to a csv file"""

    print("Colleting data...")
    # Create the dataframe
    df = pd.DataFrame(
        [
            {
                "captured_at": int(time.time()),
                "info": f"{get_info()}",
                "metrics": f"{get_metrics()}",
                "mining": f"{get_mining()}",
            }
        ]
    )

    # Append the dataframe to the csv file
    df.to_csv(
        config.SAVE_PATH,
        mode="a",
        index=False,
        header=False if exists(config.SAVE_PATH) else True,
    )

    print(f"Written to {config.SAVE_PATH}")


if __name__ == "__main__":
    main()
