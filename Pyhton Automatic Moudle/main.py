from utils import TEST

# 初始化资产
IP1 = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
IP2 = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]
IP3 = ["2.1.1.1", "2.1.1.2", "2.1.1.3"]

HOST1 = ["BeijingCore", "ShenzhenCore", "GuangzhouCore"]
HOST2 = ["BeijingEdge", "ShenzhenEdge", "GuangzhouEdge"]
HOST3 = ["BeijingHost", "ShenzhenHost", "GuangzhouHost"]

USER1 = {"yeslab": "yeslab123"}
USER2 = {"cisco": "cisco123"}
USER3 = {"huawei": "huawei123"}

test1 = TEST(IP1, HOST1, USER1) #类的实例
test2 = TEST(IP2, HOST2, USER2)
test3 = TEST(IP3, HOST3, USER3)