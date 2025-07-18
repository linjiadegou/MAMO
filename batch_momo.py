import requests
import json
import csv
import pandas as pd
import time
from tqdm import tqdm


def run(file_path, key, user_name):
    # 读取CSV文件
    # df = pd.read_csv('2024.12.7/smiles_100_gsk3b_jnk_qed_sa.csv')
    # df = pd.read_csv('2024.10.30/smiles.csv')
    df = pd.read_csv(file_path)

    result_100 = []

    # 记录开始时间
    start_time = time.time()
    error_smiles = []

    smiles = df["smiles"].tolist()  # 假设我们只处理前100个SMILES
    with open(
        "2025.4.8/output_4.8_{}.csv".format(user_name), "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头
        writer.writerow(["pre_smile", "opt_smile", "smi_list"])
        # 使用tqdm创建进度条，并显示当前进度/总进度
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
                "user": "ltl_4.8_{}".format(user_name),
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

    # 记录结束时间并计算总时间
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

    try:
        # 将error_smiles存入hh.csv文件中
        with open(
            "2025.4.8/error_smiles_4.8_{}.csv".format(user_name), "w", newline=""
        ) as error_file:
            error_writer = csv.writer(error_file)
            error_writer.writerow(["error_smiles"])  # 写入列名
            error_writer.writerows([[error_smile] for error_smile in error_smiles])
    except Exception as e:
        print(error_smiles)


# run('2024.10.30/smiles_100.csv', 'app-rAbK1aFdN7oqvVMUngBj6bLv', 'QED')
# run('2024.12.7/smiles_100_gsk3b_jnk_qed_sa.csv', 'app-5pKu7i1HVHVEYT0bUcfP2wTW', 'GSK3B')
# run('2024.12.7/smiles_100_gsk3b_jnk_qed_sa.csv', 'app-xbBIgkRj73j5QblzzR7lwfJg', 'JNK3')

# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-opjnWXbHprvmrUz6so0jtcGJ', 'GSK3B_JNK3_4o_mini')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-Ek9WWWfikdMOM2pRTpJ4XCGx', 'GSK3B_JNK3_QED_4o_mini')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-l066KHWl4Awm8vQ3eeUDSnij', 'GSK3B_JNK3_QED_SA_4o_mini')

# 消融
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-pXziANrtVZ86XkWdp5Ss1aBX', 'GSK3B_JNK3_QED_wu_central_2')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-s5ceCLVDh8dQQYbe9lLDxjoy', 'GSK3B_JNK3_QED_SA_wu_central_2')

# MAMO
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-0UF6m8bcOcpnh6DqZY49PIBW', 'QED_SA_mamo')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-zqEDdA1CN3jyott6LDrO2H1E', 'GSK3B_JNK3_mamo')

# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-YO4faqZzl0vu3zxHdcJoiQwY', 'GSK3B_JNK3_QED_mamo')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-BcdOqeY8U2MpNn1BxaPWbNtx', 'GSK3B_QED_SA_mamo')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-gY78ivOBbCpEvkEIBx62WXel', 'JNK3_QED_SA_mamo')

# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-CUbVXM1K3mcMQtAYCssesqjF', 'GSK3B_JNK3_QED_SA_mamo')
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-Xt130Z9yjgHT7bDOagcbqyCn', 'GSK3B_QED_mamo')

# gpt-4o-mini / deepseek
# run(
#     "2024.11.22/smiles_gsk3b_jnk3_100.csv",
#     "app-0UF6m8bcOcpnh6DqZY49PIBW",
#     "QED_SA_mamo_deepseek",
# )
# run(
#     "2024.11.22/smiles_gsk3b_jnk3_100.csv",
#     "app-zqEDdA1CN3jyott6LDrO2H1E",
#     "GSK3B_JNK3_mamo_deepseek",
# )
# run('2024.11.22/smiles_gsk3b_jnk3_100.csv', 'app-PF6oUQKM5qMRpK5X7ZnwVHao', 'GSK3B_QED_mamo_deepseek')

run(
    "2024.11.22/smiles_gsk3b_jnk3_100.csv",
    "app-YO4faqZzl0vu3zxHdcJoiQwY",
    "GSK3B_JNK3_QED_mamo_deepseek",
)
run(
    "2024.11.22/smiles_gsk3b_jnk3_100.csv",
    "app-BcdOqeY8U2MpNn1BxaPWbNtx",
    "GSK3B_QED_SA_mamo_deepseek",
)
run(
    "2024.11.22/smiles_gsk3b_jnk3_100.csv",
    "app-gY78ivOBbCpEvkEIBx62WXel",
    "JNK3_QED_SA_mamo_deepseek",
)

run(
    "2024.11.22/smiles_gsk3b_jnk3_100.csv",
    "app-CUbVXM1K3mcMQtAYCssesqjF",
    "GSK3B_JNK3_QED_SA_mamo_deepseek",
)
