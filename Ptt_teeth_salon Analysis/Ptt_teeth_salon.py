import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import time

url_list=[]
for num in range(1200,1551):
    next_url = "https://www.ptt.cc/bbs/teeth_salon/index"+str(num)+".html"
    url_list.append(next_url)
length=len(url_list)

def get_web(url):
    time.sleep(0.5)  
    resp = requests.get(url=url)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_data(data):
    soup = BeautifulSoup(data , 'html.parser')
    articles = []
    catch = soup.select('.title a')
    articles.append(catch)
    return articles

if __name__ == '__main__':
    title_1 = "智齒"
    title_2 = "牙周病"
    title_3 = "矯正"
    title_4 = "蛀牙"
    title_5 = "根管"
    title_6 = "根尖"
    title_7 = "植牙"

    sum_title_1 = 0
    sum_title_2 = 0
    sum_title_3 = 0
    sum_title_4 = 0
    sum_title_5 = 0
    sum_title_6 = 0
    sum_title_7 = 0

    articles = []
    for i in range(length):
        current_page = get_web(url_list[i])

        if current_page:
            text = get_data(current_page)
            sum_title_1 += str(text[0]).count(title_1)
            sum_title_2 += str(text[0]).count(title_2)
            sum_title_3 += str(text[0]).count(title_3)
            sum_title_4 += str(text[0]).count(title_4)
            sum_title_5 += str(text[0]).count(title_5)
            sum_title_6 += str(text[0]).count(title_6)
            sum_title_7 += str(text[0]).count(title_7)
    sum_all = sum_title_1 + sum_title_2 + sum_title_3 + sum_title_4 + sum_title_5 + sum_title_6 + sum_title_7

    percent1 = round((sum_title_1*100)/sum_all,2)
    percent2 = round((sum_title_2*100)/sum_all,2)
    percent3 = round((sum_title_3*100)/sum_all,2)
    percent4 = round((sum_title_4*100)/sum_all,2)
    percent5 = round((sum_title_5*100)/sum_all,2)
    percent6 = round((sum_title_6*100)/sum_all,2)
    percent7 = round((sum_title_7*100)/sum_all,2)

    print("總搜尋個數為:",sum_all)
    print("\n")
    print("智齒(Wisdom Tooth)出現個數為:",sum_title_1,"百分比為",percent1,"%")
    print("牙周病(Periodontal Disease)出現個數為:",sum_title_2,"百分比為",percent2,"%")
    print("矯正(Orthodontics)出現個數為:",sum_title_3,"百分比為",percent3,"%")
    print("蛀牙(Tooth Decay) 出現個數為:",sum_title_4,"百分比為",percent4,"%")
    print("根管(Endodontics) 出現個數為:",sum_title_5,"百分比為",percent5,"%")
    print("根尖(Apicoectomy) 出現個數為:",sum_title_6,"百分比為",percent6,"%")
    print("植牙(Implant)     出現個數為:",sum_title_6,"百分比為",percent6,"%")

    plt.title("Rough Analysis of Taiwanese Teeth Problems Through PTT") 
    labels = ['Wisdom Tooth','Periodontal Disease','Orthodontics','Tooth Decay','Endodontics','Apicoectomy','Implant']
    sizes  = [percent1,percent2,percent3,percent4,percent5,percent6,percent7]
    colors=['yellow','green','blue','red','pink','orange','purple']
    explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.legend(labels, loc=2)
    plt.axis('equal')
    plt.show()