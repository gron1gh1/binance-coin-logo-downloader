import requests
import os.path
coinData = requests.get('https://www.binance.com/bapi/asset/v1/public/asset/asset/get-asset-logo').json()['data']
MissingCoinList = []

for coin in coinData:
    if os.path.isfile('./png/{0}.png'.format(coin['asset'])) == False:
        MissingCoinList.append(coin)

print('[ 가지고 있지 않는 코인 아이콘 목록 ]')
if len(MissingCoinList) == 0:
    print("모든 코인이 존재합니다.")
    exit(0)
for MissingCoin in MissingCoinList:
    print('\033[31m{0}\033[0m'.format(MissingCoin['asset']),end=', ')

print()
print('아무 키 입력 시 다운 진행')
input('')

for MissingCoin in MissingCoinList:
    if MissingCoin['pic']:
        imgData = requests.get(MissingCoin['pic'], headers={"Referer": "https://www.binance.com/"})
        if imgData.status_code == 200:
            with open("./png/{0}.png".format(MissingCoin['asset']), 'wb') as f:
               f.write(imgData.content)
               print('\033[96m{0} /png/{1}.png Success !\033[0m'.format(MissingCoin['pic'],MissingCoin['asset']))
        else:
            print('\033[31m/png/{0}.png Fail - ${1} Error\033[0m'.format(MissingCoin['asset'], imgData.status_code))
    else:
        print('\033[31m/png/{0}.png Fail - pic 정보가 없음\033[0m'.format(MissingCoin['asset']))