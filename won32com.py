import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True

word = win32com.client.Dispatch("Word.Application")
word.Visible = True

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행': 'A00100'}

    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self, name):
        return self.stocks[name]


instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))
