import requests
import json
import csv
import pandas as pd
import time
from tqdm import tqdm


def run(file_path, key, user_name):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    result_100 = []

    # 记录开始时间
    start_time = time.time()
    error_smiles = []

    smiles = df["smiles"].tolist() 
    with open(
        "2025.4.8/output_4.8_{}.csv".format(user_name), "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["pre_smile", "opt_smile", "smi_list"])

        for i, smile in enumerate(
            tqdm(smiles, desc="Processing", total=len(smiles)), 1
        ):
            flag = True
            temp = []
            smile = smile.strip()
            # API URL
            api_url = "http://localhost/v1/workflows/run"

            # API Key
            api_key = key

            # Request headers
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }

            # Request payload
            data = {
                "inputs": {"smiles": smile},
                "response_mode": "blocking",
                "user": "{}".format(user_name),
            }

            try:
                # Send the POST request
                response = requests.post(
                    api_url, headers=headers, data=json.dumps(data), timeout=99999
                )
                # Check the response
                if response.status_code == 200:
                    outputs = json.loads(response.text)["data"]["outputs"]
                    temp.append(smile)
                    temp.append(outputs["text"])
                    temp.append(outputs["smi_list"])
                else:
                    temp.append(smile)
                    temp.append("error")
                    temp.append("error")
            except Exception as e:
                try:
                    temp = []
                    # Send the POST request
                    response = requests.post(
                        api_url, headers=headers, data=json.dumps(data), timeout=99999
                    )
                    # Check the response
                    if response.status_code == 200:
                        outputs = json.loads(response.text)["data"]["outputs"]
                        temp.append(smile)
                        temp.append(outputs["text"])
                        temp.append(outputs["smi_list"])
                    else:
                        temp.append(smile)
                        temp.append("error")
                        temp.append("error")
                except Exception as e:
                    flag = False
                    error_smiles.append(smile)
                    print(f"An error occurred at {i}/{len(smiles)}: {e}")

            if flag:
                writer.writerow(temp)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

    try:
        with open(
            "data/error_smiles_{}.csv".format(user_name), "w", newline=""
        ) as error_file:
            error_writer = csv.writer(error_file)
            error_writer.writerow(["error_smiles"])  
            error_writer.writerows([[error_smile] for error_smile in error_smiles])
    except Exception as e:
        print(error_smiles)


if __name__ == "__main__":
    import argparse
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='smiles.csv')
    parser.add_argument('--key', type=str, default=None)
    parser.add_argument('--user_name', type=str, default="root")
    args = parser.parse_args()

    run(args.file_path,args.key,args.user_name)
