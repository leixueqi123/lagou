## po封装

第一层
 1、搭建架子，构建 PO模型，构造相关的类和方法 
 2、编写测试用例，编写业务逻辑代码

page/ page 页 app.py 负责 app的启动，重启，关闭，进入主页等操作 
main_page.py 主页 ...其它page 

testcase/ 存放测试用例 test_contact.py

log/ 日志 report/ 报告 data/ 数据 util/ 公共方法 .....


## po封装

第二层 1、填充内容 。 2、在每个page页面中 ，接收上个页面传递过来的 driver


## po封装

第三层改造优化

优化框架，封装模板代码
1、优化 driver 创建base_page.py 基本的方法 
包括 ：初始化driver find, click, swipe_find ,send_keys

每一个 page都去继承 将每一个PAGE页面，都继承 BasePage 类

2、优化 find 方法 3、添加日志

## po封装

第四层 复用driver

1、BasePage driver 设置一个初始值为None 
2、在app.py 文件App类继承 BasePage - start() 方法中，判断 driver 是否为None - 如果为None： 则创建一个新的driver -
如果不为None：复用这个driver


第五层 日志
添加日志：
1、创建conftest.py定义日志的文件名和级别
2、pytest.ini配置 pytest日志相关项


第六层 多设备执行，多appium server
端口号间隔2 

appium -p 4723 --session-override
appium -p 4725 --session-override
udid  测试多设备唯一标示


执行命令 shell
mac/linux电脑： 
第一台设备：
udid='123456' port = 4723  回车
pytest test_contact.py

第二台设备：
udid='654321' port = 4725  回车
pytest test_contact.py



代码里调用时：
udid = os.getenv("udid")
port = os.getenv("port")



windows电脑：
第一台设备：
set udid='123456' port = 4723  回车
pytest test_contact.py

第二台设备：
set udid='654321' port = 4725  回车
pytest test_contact.py


代码里调用时：
udid = os.getenv("udid")
port = os.getenv("port")

----------------------

执行命令 shell
mac/linux电脑/windows： 
python -m pytest test_contact.py --udid='123456' --port=4725

代码里调用时：
udid = sys.argv[1]
port = sys.argv[2]


第七层  run.py调用执行脚本
调用方法：python run.py emulator-5554 4723
