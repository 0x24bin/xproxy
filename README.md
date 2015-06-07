# xproxy
一个动态更新代理接口类，遵循proxychain的代理保存方式
通过scrapy抓取代理接口，并通过开启抓取线程，确保proxies代理池内数量

安装&使用
=================================== 
1. 依赖python scrapy，使用前请确保安装
2. 内置两个scrapy爬取web接口的例子，可参考这两个例子编写，确保爬去结果符合proxychain的格式，并将结果保存在proxies.txt内
3. XProsy类的具体使用可参考demo.py

说明
=================================== 
现在仅支持http/https，待修改
