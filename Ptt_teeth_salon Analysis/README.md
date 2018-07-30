!!!注意!!!因為爬取的頁數有點多，因此程式執行需花一點時間。

1. 抓取ptt teeth_salon 版的 url，觀察到每下一頁的網址是有規律的，因此寫了一個 for 迴圈，去抓我設定要的頁數，並且放進 url_list。

2. get_web function 將 url_list 裡面的資料回傳成 text。

3. get_data function 利用 BeautifulSoup、python 的解析程序 "html.parser" 去抓取裡面的 ".title a"，也就是ptt每一篇文章的標題。
並將每一篇的標題放進 articles 這個 list 裡面。

4. 接下來就是判斷、計算每一個標題有沒有出現我所設定的七個關鍵字，以百分比的方式（取到小數點第二位）呈現出圓餅圖～。