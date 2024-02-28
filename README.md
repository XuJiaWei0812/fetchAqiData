# Fetch AQI Data

這個 Python 程式碼用於從環保署的空氣品質指數 (AQI) API 獲取資料並將其儲存到 CSV 檔案中。

## 功能

- 從環保署 AQI API 獲取最新的空氣品質資料。
- 將獲取的資料儲存到 CSV 檔案中，方便後續分析和處理。

## 使用方法

1. 確保您的系統已安裝 Python 3 和 `requests` 庫。
2. 下載 `fetchAqiData.py` 到您的工作目錄。
3. 在終端機或命令提示字元中執行以下命令：

   ```bash
   python fetchAqiData.py
4. 執行後，您將在當前目錄下看到一個名為 `csv-aqi.csv` 的新 CSV 檔案，其中包含從 API 獲取的空氣品質資料。

