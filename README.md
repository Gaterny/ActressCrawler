### JavBus--Crawler Based On Scrapy

---

#### 注意：针对JavBus的演员信息进行抓取，并将演员姓名，演员参演作品，作品番号以及上映时间存入数据库。仅供学习交流使用，勿作他用。



#### 下载

```
git clone git@github.com:Gaterny/ActressCrawler.git
```



#### Requirement

```
python3
scrapy
mysql
```



#### 数据库配置

```
# 创建数据库
CREATE DATABASE fuli;

# 创建表
DROP TABLE IF EXISTS `actress`;
CREATE TABLE `actress` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `film` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=268223 DEFAULT CHARSET=utf8;
```



#### 运行

```
scrapy crawl actress_spider
```



#### 结果说明

```
name: 演员名字
film: 演员作品
tag: 作品番号
date: 上映时间
```

