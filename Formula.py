import requests
import json
import openpyxl

my_wb = openpyxl.Workbook()
sheet = my_wb.active
url = "https://fapi.binance.com/fapi/v1/exchangeInfo"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
a = json.dumps(parsed, indent=10)
b = eval(a)
print(b)
list = []
for i in b:
    if i=='symbols':
        list.append(b[i])
symbol = []
status = []
maintMarginPercent = []
requiredMarginPercent = []
baseAsset = []
quoteAsset = []
pricePrecision = []
quantityPrecision = []
baseAssetPrecision = []
quotePrecision = []

for t in list:
    print(t[1])
    x = str(t)
    y = eval(x)
    for j in y:
        # for k in j:
            for d in j['symbol']:
                symbol.append(j['symbol'])
            for d in j['status']:
                status.append(j['status'])
            for d in j['maintMarginPercent']:
                maintMarginPercent.append(j['maintMarginPercent'])
            for d in j['requiredMarginPercent']:
                requiredMarginPercent.append(str(j['requiredMarginPercent']))
            for d in j['baseAsset']:
                baseAsset.append(str(j['baseAsset']))
            for d in str(j['pricePrecision']):
                pricePrecision.append(j['pricePrecision'])
            for d in str(j['quantityPrecision']):
                quantityPrecision.append(str(j['quantityPrecision']))
            for d in str(j['baseAssetPrecision']):
                baseAssetPrecision.append(str(j['baseAssetPrecision']))
            for d in str(j['quotePrecision']):
                quotePrecision.append(str(j['quotePrecision']))
            for d in str(j['quoteAsset']):
                quoteAsset.append(str(j['quoteAsset']))



print(symbol)
print(status)
print(maintMarginPercent)
print(requiredMarginPercent)
print(baseAsset)
print(pricePrecision)
print(quoteAsset)
print(quantityPrecision)
print(quotePrecision)
print(baseAssetPrecision)

my_wb.save(filename="TradingSheet.xlsx")