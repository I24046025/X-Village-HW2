import matplotlib.pyplot as plt
import pandas as pd
import requests
url_103_marry='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=c9ad2822-8a15-42f3-bacc-0454f2c09380'
url_104_marry='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=47690572-fa4f-4352-ab94-e35dbc633454'
url_105_marry='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=642ff4ab-3fdd-4d3d-be1a-311180f3aca3'

url_103_divorce='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=ea8bc9c7-e57c-44a6-b36f-83b96c735746'
url_104_divorce='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=b83a3bee-44dc-4dfe-a65e-95dcfa76a29a'
url_105_divorce='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f95d1a33-ec56-44c5-a9ec-3afba8157e39&rid=84179892-ed10-430c-905f-60ab689e513a'
def get_data(url, year, status):
    r = requests.get(url, verify=False)
    r.encoding = 'utf-8'

    with open(str(year)+str(status)+'.csv','w',encoding='utf-8') as f:
        f.write(r.text+'\n')
    df = pd.read_csv(str(year)+str(status)+'.csv')
    return df

def display(df, year, status):
    x = range(1,13)
    y1 = df.iloc[0,:] #桃園區
    y1 = list(y1)[1:13]

    y2 = df.iloc[1,:] #中壢區
    y2 = list(y2)[1:13]

    plt.title(str(year)+" Years- Numbers of "+str(status)+" of Taoyuan & Zhongli District")
    plt.plot(x, y1, color='orange', marker='o', label='Taoyuan District')
    plt.plot(x, y2, color='purple', marker='*', label='Zhongli District')
    plt.legend()

    plt.xlabel('Month')
    plt.ylabel('Pairs')
    plt.show()
#103-marry
a = get_data(url_103_marry, "103", "Marry")
display(a, "103", "Marry")
#104-marry
a = get_data(url_103_marry, "104", "Marry")
display(a, "104", "Marry")
#105-marry
a = get_data(url_105_marry, "105", "Marry")
display(a, "105", "Marry")
    #103-divorce
a = get_data(url_103_divorce, "103", "Divorce")
display(a, "103", "Divorce")
    #104-divorce
a = get_data(url_104_divorce, "104", "Divorce")
display(a, "104", "Divorce")
    #105-divorce
a = get_data(url_105_divorce, "105", "Divorce")
display(a, "105", "Divorce")