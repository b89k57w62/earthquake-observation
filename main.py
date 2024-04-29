import requests

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWA-AEF21BB7-71F4-4D68-8EA5-AA4F4D1A5A26&format=JSON&AreaName=%E8%87%BA%E5%8C%97%E5%B8%82"

data = requests.get(url)
data_json = data.json()

shake = data_json["records"]["Earthquake"]
for i in shake:
    locations = i["EarthquakeInfo"]["Epicenter"]["Location"]
    magnitude = i["EarthquakeInfo"]["EarthquakeMagnitude"]["MagnitudeValue"]
    depth = i["EarthquakeInfo"]["FocalDepth"]
    time = i["EarthquakeInfo"]["OriginTime"]
    result = f"{locations}, 芮氏規模: {magnitude}, 深度: {depth}, 發生時間: {time}"
    print(result)