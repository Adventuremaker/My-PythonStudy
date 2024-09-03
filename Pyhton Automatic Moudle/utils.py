class TEST:
    def __init__(self, ip_list, host_list, user_db):
        self.ip_list = ip_list
        self.host_list = host_list
        self.user_db = user_db
        self.new_ip_host()
        print(self.ip_list, self.host_list)
        self.show_inventory()
        self.add_user()


    # 新的IP与新的HOSTNAME
    def new_ip_host(self):
        '''
        增加新的IP与HOSTNAME
        Params:
        # ip_list: list, 里面都是IP地址
        # host_list: list, 里面都是设备名称 
        '''
        new_str = input("请输入'IP地址@设备名称'：")
        new_ip, new_host = new_str.split('@')
        self.ip_list.append(new_ip)
        self.host_list.append(new_host)

    # 列表同步循环显示当前资产
    def show_inventory(self):
        for i in range(len(self.ip_list)):
            print(f"{self.ip_list[i]}@{self.host_list[i]}")


    # 新增用户名密码
    def add_user(self, user_doc_path='user.txt'):
        with open(user_doc_path) as f:
            user_data = f.read()
        new_list = user_data.split('\n')
        new_list.pop()
        for user in new_list:
            split_data = user.split()
            #print(f"当前循环到：{user}")
            username = split_data[0]
            password = split_data[1]
            if len(password) < 8:
                print(f"用户{username}的密码不符合安全规定！")
            elif '@' not in password:
                print(f"用户{username}的密码不符合安全规定")
            else:
                self.user_db[username] = password
