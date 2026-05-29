import json
import requests
from config import config

TIMESTAMPS = {
    # "T1": "1574231830", # 貌似专家公寓不开放查询了
    # "T2": "1574231833",
    # "T3": "1574231835",
    "S1": "1503975832",
    "S2": "1503975890",
    "S5": "1503975967",
    "S6": "1503975980",
    "S7": "1503975988",
    "S8": "1503975995",
    "S9": "1503976004",
    "S10": "1503976037",
    "S11": "1599193777",
    "B1": "1661835249",
    "B2": "1661835256",
    "B5": "1661835273",
    "B9": "1693031698",
    "B10": "1693031710",
}


def building_to_id(building: str) -> str:
    if building in TIMESTAMPS:
        return TIMESTAMPS[building] + "%26" + building
    else:
        print("ERROR: Wrong building number")


def query(building, room, Synjones_Auth=config["Synjones-Auth"]):
    URL = "https://mcard.sdu.edu.cn/charge/feeitem/getThirdData"

    HEADERS = {
        "Synjones-Auth": Synjones_Auth,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/plain, */*",
    }

    data = f"feeitemid=410&type=IEC&level=3&campus=%E9%9D%92%E5%B2%9B%E6%A0%A1%E5%8C%BA%26%E9%9D%92%E5%B2%9B%E6%A0%A1%E5%8C%BA&building={building_to_id(building)}&room={room}"

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            data=data,
        )
        response.raise_for_status()
        msg = json.loads(response.text)["map"]["showData"]["信息"]
        return msg.split("：")[1].replace("度", "")
    except Exception as e:
        print(e)
        return None
