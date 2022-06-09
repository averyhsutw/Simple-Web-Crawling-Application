# 簡易爬蟲及其應用


## 前情提要

我前陣子很喜歡在平板上用 HyRead 借臺大出版中心的電子書來看，但最近越來越懶惰，就停止了。因此希望可以每個星期日早上讓 Line 發通知給我，推薦好的電子書給我看，這樣我看到喜歡的就可以加入自己的「買書清單」，同時也是提醒自己該去看書了。
會選擇博客來的暢銷榜是因為台大的電子書館藏有限，無法滿足我「跟上熱銷排行」的需求；並且應該有不少人用博客來這個平台購書，熱銷榜又是每日更新，因此推薦書單的可信度算是不錯。

## 功能說明

用網路爬蟲，抓取博客來中文電子書暢銷榜的資料，過濾出前五名並只存取書名和此書的介紹網址，之後用 LINE Notify API 傳給我自己就完成了（如下圖）。

![](https://i.imgur.com/qQfvFgT.jpg)
![](https://i.imgur.com/MmEbSLM.jpg)

## 使用套件

- requests
    - get( <url> ): 抓取目標網站的所有資訊。設置 timeout，避免網站在維修中或故障時，程式停留太久。
    - post: 做 HTTP POST。在 LINE Notify 用到，寄送訊息到指定地址。

- BeautifulSoup: 
    - 屬性 text: 抓取到的 html 文檔。或者是抓到的物件的文字內容。
    - 方法 find_all, find, get：用來選特定資訊。
    
- html5lib：HTML解析器。

- Line Notify API：透過簡單的設定拿到 token 後，就可以跑程式傳訊息給自己。
    
- crontab: 設定定時執行文件。
    - 例如，我可以設定：`30 08 * * 0 bash <path of *.sh>`  (設定星期日早上 8:30 執行 .sh file)。
    - 在 .sh file：`python3 web_crawler.py`