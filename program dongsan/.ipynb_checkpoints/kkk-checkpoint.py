import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pythoncom

class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)   # 시그널-슬롯 등록
        self.login = False
        

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while self.login is False:
            pythoncom.PumpWaitingMessages()

    def OnEventConnect(self, code):
        self.login = True
        print("login is done", code)
    
        
    def GetCodeListByMarket(self, market):
        ret = self.ocx.dynamicCall("GetCodeListByMarket(QString)", market)
            # ';'를 기준으로 문자열을 나눠서 리스트로 저장
        return 1
    
    def asdf(self):
        return 2


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()