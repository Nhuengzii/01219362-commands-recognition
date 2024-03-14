import pandas as pd
import os
import glob
from argparse import ArgumentParser

def get_dataset_dataframe(data_path: str):
    datas = []
    for sid in os.listdir(data_path):
        all_files = glob.glob(os.path.join(data_path, sid, "**/*.wav"))

        for f in all_files:
            command = f.split(os.path.sep)[-2]

            datas.append({
                "sid": sid,
                "command": command,
                "path": f
            })
    df = pd.DataFrame(datas)
    return df

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data_path", type=str, default="./data")
    args = parser.parse_args()
    data_path = args.data_path

    df = get_dataset_dataframe(data_path)
    print(df)
