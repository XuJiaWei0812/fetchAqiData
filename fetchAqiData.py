import requests
import csv

# 設定檔案名稱，將檔案儲存到執行程式碼的當前資料夾中
fileName = 'fetchAqiData.csv'

# 建立一個空白的 CSV 檔案並設定為可寫入模式
with open(fileName, 'w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile)

    # 設定 API 網址，包含 API 金鑰、限制資料筆數、排序方式和格式
    apiUrl = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

    # 發送請求並將回應轉換為 JSON 格式
    response = requests.get(apiUrl)
    responseJson = response.json()

    # 準備 CSV 檔案的標題列
    headerRow = ['縣市', '測站名稱', 'AQI', '空氣品質']
    csvWriter.writerow(headerRow)

    # 迴圈遍歷 API 回應中的資料記錄
    for record in responseJson['records']:
        # 將每筆資料記錄轉換為 CSV 檔案中的一行
        row = [record['county'], record['sitename'], record['aqi'], record['status']]
        csvWriter.writerow(row)

    print(f'資料已成功儲存至 {fileName}')
