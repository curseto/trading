from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        
        print("Kiwoom 클래스입니다") 
        ################ event loop 모음 ################
    
        self.login_event_loop = None

        #################################################
        
        ############### 변수 모음 #######################
        self.account_num = None
        #################################################
        
        
        self.get_OCX_instance()
        self.event_slots()
        self.signal_login_commConnect()
        self.get_account_info()
        # self.detail_account_info()
        
        
    def get_OCX_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")   #setcontrol은 QAxWidget에 있는 매써드 파이썬에서 Open API를 제어하겠다는 코드
       
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        
    def login_slot(self, errCode):

        print(errors(errCode))
        
        self.login_event_loop.exit()
        
    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()") # dynamicCall은 네트워크 혹은 다른 응용프로그램에 데이터를 전송할수 있게 만든 함수임 , PyQt5에서 제공함. 로그인을 위한 메서드 이름은 CommConnect입니다. 파이썬에서 OCX 객체는 COM 객체와 달리 메서드를 직접 호출 할 수 없고 dynamicCall이라는 메서드를 통해 호출해야합니다.
        
        self.login_event_loop = QEventLoop() 
        self.login_event_loop.exec_() #QEventLoop(): 로그인이 완료될때까지 프로그램이 기다리게 하는것.
    

        
    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(String)","ACCNO")
        self.account_num = account_list.split(';')[0]
        print("나의 보유 계좌번호는 %s" % self.account_num)
    
        
        
    # def detail_account_info(self):
    
    
