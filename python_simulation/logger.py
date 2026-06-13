import pandas as pd

def save_log(records):

    df = pd.DataFrame(records)

    df.to_csv(
        "outputs/location_history.csv",
        index=False
    )