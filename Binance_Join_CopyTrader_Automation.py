import requests
import time
import json
import simpleaudio as sa
from typing import Optional


# Script Default value 
# You can be ignore these in the profiles settings if the values are the same
# "copyModel": "FIXED_RATIO", 
# "investAsset": "USDT", 
# "costPerOrder": 0, 
# "marginMode": "FOLLOW_LEAD",
# "leverageMode": "FOLLOW_LEAD",
# "totalStopLossRate": None,
# "leverageValue": None,
# "takeProfitRate": None,
# "stopLostRate": None,
# "maxPositionPerSymbolRate": None,

#Available values for "copyModel": "FIXED_RATIO", "FIXED_AMT"
# for fixed amount, costPerOrder is required
# for fixed ratio, set costPerOrder to 0 (default, so it can be removed)
#Available values for "totalStopLossRate": 0-95 % (Optional, can be removed and the value will be None)

#Advanced Settings
#Available values for "marginMode": "FOLLOW_LEAD", "CROSS", "ISOLATED"
#Available values for "leverageMode": "FOLLOW_LEAD", "FIX_LEVERAGE"
#Available values for "leverageValue": 1-10 X (Optional, can be removed and the value will be None), only available when "leverageMode" is "FIX_LEVERAGE"
#Available values for "takeProfitRate": 0-2000 % ROI (Optional, can be removed and the value will be None)
#Available values for "stopLostRate": 5-95 % ROI (Optional, can be removed and the value will be None)
#Available values for "maxPositionPerSymbolRate": 5-95 % (Optional, can be removed and the value will be None)



# List of leadPortfolioIds to check **IMPORTANT** - You need to add your the trader's leadPortfolioId in your favorite list
# Portifolio ID can be found in the URL when you click on the trader's profile

PROFILES_SETTINGS = {
    "3708884547500009217": {
        "leadPortfolioId": "3708884547500009217",
        "investAmount": 100, 
        "copyModel": "FIXED_RATIO", # can be removed since it's the default value
        "investAsset": "USDT",  # can be removed since it's the default value
        "costPerOrder": 0,  # can be removed since it's the default value
        "marginMode": "FOLLOW_LEAD",  # can be removed since it's the default value
        "leverageMode": "FOLLOW_LEAD",  # can be removed since it's the default value
        "totalStopLossRate": None,  # can be removed since it's the default value
        "leverageValue": None,  # can be removed since it's the default value
        "takeProfitRate": None,  # can be removed since it's the default value
        "stopLostRate": None,  # can be removed since it's the default value
        "maxPositionPerSymbolRate": None, # can be removed since it's the default value
    },
    "3746309621504731393": {
        "leadPortfolioId": "3746309621504731393",
        "investAmount": 100, 
    },
}

# Open Inspect > network tab and copy the following headers after hitting the Favorite copy traders list page
csrftoken = ""
bncuuid = ""
fvideoid = ""
fvideotoken = ""
cookie = ''


completed_list = []
sound_file = "beep-07a.wav"
headers = {
    "authority": "www.binance.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "bnc-uuid": bncuuid,
    "clienttype": "web",
    "content-type": "application/json",
    "csrftoken": csrftoken,
    "fvideo-id": fvideoid,
    "fvideo-token": fvideotoken,
    "lang": "en",
    "origin": "https://www.binance.com",
    "referer": "https://www.binance.com/en/copy-trading",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "cookie": cookie,
}


def join_lead(
    leadPortfolioId: str,
    investAmount: int,
    copyModel: str = "FIXED_RATIO",
    costPerOrder: int = 0,
    investAsset: str = "USDT",
    leverageMode: str = "FOLLOW_LEAD",
    marginMode: str = "FOLLOW_LEAD",
    totalStopLossRate: Optional[int] = None, 
    leverageValue: Optional[int] = None, 
    takeProfitRate: Optional[int] = None, 
    stopLostRate: Optional[int] = None, 
    maxPositionPerSymbolRate: Optional[int] = None,
):
    url = "https://www.binance.com/bapi/futures/v1/private/future/copy-trade/copy-portfolio/create"
    join_params = {
        "leverageMode": leverageMode,
        "marginMode": marginMode,
        "investAmount": investAmount,
        "copyModel": copyModel,
        "costPerOrder": costPerOrder,
        "investAsset": investAsset,
        "leadPortfolioId": leadPortfolioId,
        "totalStopLossRate": totalStopLossRate, 
        "leverageValue": leverageValue, 
        "takeProfitRate": takeProfitRate, 
        "stopLostRate": stopLostRate, 
        "maxPositionPerSymbolRate": maxPositionPerSymbolRate,
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(join_params))
        if response.status_code == 200 and response.json()["success"] == True:
            r = response.json()
            print(
                f"Joined {leadPortfolioId} successfully!, amount: {investAmount} {investAsset}"
            )
            # print(r)
            completed_list.append(leadPortfolioId)
            return r
        else:
            print(f"Error joining {leadPortfolioId}!")
            print(response.json()["message"])
            return None
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def fetch_data():
    url = "https://www.binance.com/bapi/futures/v1/friendly/future/copy-trade/home-page/query-list"
    data = {
        "pageNumber": 1,
        "pageSize": 21,
        "timeRange": "90D",
        "dataType": "ROI",
        "favoriteOnly": True,
        "hideFull": False,
        "nickname": "",
        "order": "DESC",
        "apiKeyOnly": False,
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def play_sound(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def check_portfolio(data):
    if data and "data" in data and "list" in data["data"]:
        for profile in data["data"]["list"]:
            if profile["leadPortfolioId"] in PROFILES_SETTINGS and profile["leadPortfolioId"] not in completed_list:
                if profile["currentCopyCount"] < profile["maxCopyCount"]:
                    print(
                        f"Alarm! {profile['nickname']} has available slots! {profile['currentCopyCount']} / {profile['maxCopyCount']} -- Profile Link: https://www.binance.com/en/copy-trading/copy-setting?portfolioId={profile['leadPortfolioId']}"
                    )
                    play_sound(sound_file)
                    # Comment the below line if you want to join the profile manually.
                    join_lead(**PROFILES_SETTINGS[profile["leadPortfolioId"]])


def main():
    start_time = time.time()
    print("Script started!")
    while True:
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {int(elapsed_time)} seconds", end="\r")
        data = fetch_data()
        check_portfolio(data)
        if len(completed_list) == len(PROFILES_SETTINGS):
            print("All profiles are joined successfully!")
            break
        time.sleep(2)  # Wait for 2 seconds before next request, can be removed, but I didnt test if there is a rate limit.


if __name__ == "__main__":
    main()
