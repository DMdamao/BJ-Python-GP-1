# QQ简易版项目简介


# 功能
- [x] 用AES加密所有的传输内容
- [x] 用MD5 + 加盐 的方式存储密码，加盐字符由客户端和服务器共同生成
- [x] 使用数据库存储用户信息、好友关系、房间信息、加入房间状态、所有聊天记录
- [x] tkinter GUI
- [x] 有新消息时自动好友列表提示
- [x] 窗口放大缩小
- [x] 联系人列表；未读的消息用彩色文本标注
- [x] 加好友功能，对方收到通知，通过/拒绝，并将添加记录添加到数据库
- [x] 右键好友名可以删除好友关系
- [x] 防止重复打开窗口，如果已经打开则使窗口获得焦点
- [x] 用户离线时收到的未读的消息，再次登录时用彩色文本标注
- [x] 支持多行内容（Enter换行，Ctrl+Enter发送）；支持聊天字体的设置
- [x] 群聊功能、加群、创建群
- [x] 群聊中显示群成员（双击打开聊天窗口/发送好友请求）

# 安装说明
Python版本: 3.x

#第三方依赖库
- [x] pymysql
- [x] pycrypto
```
pip install pymysql
```

```
pip install pycrypto # 用于加密
```


# 运行方法
```
python run_client.py
python run_server.py
```
（一次只能运行一个server，但可以运行多个client）
# 配置好
第一次运行前，先运行
先手动配置数据库信息

```
server/setting.py 
```
```
创建5个用户["admin", "xiaomi", "robbin", "pony", "jackma"] # 密码都是123
```
```
install_pymysql_pycrypto.py # 自动检测模块是否安装
```

```
first_time_run_server_create_database.py 1 # 创建数据库，数据库信息自己填写
```
可以快速创建数据库，（需要有参数1）；
参数为2创建几条数据，方便使用（前提创建好数据库）；
参数为3，删除数据库。如果
运行报错，多半是因为使用了新版的MySQL。修改密码的认证方式即可(注pymsyql密码认证方式为mysql_native_password)。终端登陆mysql，输入
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '密码';
```


# 文件目录
```
├─README.md
├─first_time_run_server_create_database.py
├─run_client.py
├─run_server.py
│
├─client
│   __init__.py
|
│   chat_form.py
│   contact_form.py
│   login.py
│   register.py
│   memory.py
|
│   client_socket.py
|   common_socket.py
|   security.py
|
└─server
    __init__.py
    
    DB_Handler.py 
    server_windows.py
    common_handler.py
    server_socket.py
    memory.py
    
    register.py
    login.py
    mamage_friend.py
    manage_group.py
    chat_msg.py
```

# 界面预览图
![1](../MyQQ/简易版QQ/image/1.png)
![2](../MyQQ/简易版QQ/image/2.png)
![3](../MyQQ/简易版QQ/image/3.png)
![4](../MyQQ/简易版QQ/image/4.png)
![5](../MyQQ/简易版QQ/image/5.png)
![5](../MyQQ/简易版QQ/image/6.png)


# 用MySQL存储用户信息、消息记录等各种数据
数据库结构如下：

```
create table userinfo(
    -> id int primary key auto_increment,
    -> username varchar(50) unique not null,
    -> password varchar(254) not null,
    -> nickname varchar(50) not null,
    -> reg_time timestamp not null,
    -> isActive boolean not null)default charset=utf8;

create table chatmsg(
    -> id int primary key auto_increment,
    -> user_id int not null,
    -> send_time timestamp not null,
    -> target_id int not null,
    -> isRead boolean not null,
    -> msg_type tinyint not null,
    -> msg varchar(4096) not null,
    -> isActive boolean not null)default charset=utf8;

create table userfriend(
    -> id int primary key auto_increment,
    -> user_id int not null,
    -> friend_id int not null,
    -> add_time timestamp not null,
    -> isActive boolean not null)default charset=utf8;

create table chatroom(
    -> id int primary key auto_increment,
    -> chatroom_name varchar(30) unique not null,
    -> create_time timestamp not null,
    -> isActive boolean not null)default charset=utf8;

create table chatroom_user(
    -> id int primary key auto_increment,
    -> chatroom_id int not null,
    -> user_id int not null,
    -> create_time timestamp not null,
    -> isActive boolean not null)default charset=utf8;
```

所有数据没有delete选项，只有逻辑删除，默认isActive都为1，如果不需要了，改为0即可达到删除效果。

```chatmsg```表可以保存不同类型数据，用msg_type保存数字即可，默认聊天数据为1，系统消息为2，添加好友信息为3，群聊信息为4，这样可以方便不同类型消息的扩展；保存消息时先判断用户是否在线，如果在线，直接发送给用户并在保存数据时将isRead项保存为0，否则保存为1，当用户上线时读取该用户isRead项为1的所有消息。

