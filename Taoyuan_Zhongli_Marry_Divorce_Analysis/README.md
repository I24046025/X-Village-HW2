1.抓取103-105年離婚與結婚對數的csv連結。
    資料來源：政府資料開放平臺
    桃園市各區結婚統計 https://data.gov.tw/dataset/27396

2.由於區的數量有點多，若將之呈現於同一張圖表則會顯得過於凌亂，但若將之拆成三張圖表又顯得沒有意義，因此最後決定選擇桃園最大的兩個區：桃園區、中壢區來做視覺化分析。

3.先呼叫 get_data function，利用 requests 拿到 url 再來寫入 csv 檔案，再來讓 pandas 讀取csv 檔，接著將讀到的 datafram 存放到 df 變數中。

4.呼叫 display function，將拿到桃園區、中壢區的一到十二月資料用 matplotlib.pyplot 畫出六張圖表，以折線圖方式呈現，接下來進行分析部分！