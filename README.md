# 山东大学青岛校区山大V卡通2.0版本电量查询接口

曾经的电量查询脚本 [SDUQD-Electricity-Inquiry](https://github.com/SkywalkerWei/SDUQD-Electricity-Inquiry) 停止维护，本人抓包研究后重新编写了一款新的查询脚本。

## 功能简介

- 无需进入山大 V 卡通即可查询宿舍当前电费余量
- 可与 QQ bot 或短信发送平台结合，制作定时电费提醒（电费预警）
- 支持使用 GitHub Actions 进行电量提醒
- 当前可查询区域：`S1 S2 S5 S6 S7 S8 S9 S10 S11 B1 B2 B5 B9 B10`

## 认证说明

- 当前测试结果表明 `Synjones-Auth` 字段不会过期，可长期使用
- `Synjones-Auth` 字段获取方法有两种：网页端抓包和手机端抓包
- 网页端抓包较为简单，手机端抓包较为复杂，且两种方式抓取的字段内容不同
- 网页端重新登录后原字段会失效，手机端同样如此
- 网页端登录会经常性过期，重新登录后需要修改项目配置；手机端一般不需要
- 推荐使用网页端抓包，并尽量一次抓包后不再登录网页版 V 卡通

## 教程链接

- [网页版 Synjones-Auth 字段获取教程](guide/网页端抓包教程.md)
- [手机版 Synjones-Auth 字段获取教程](guide/burpsuite手机抓包教程.md)

## 依赖安装

- `pip install -r requirements.txt`
- Python 版本：3.12.7

## 使用方法

1. 在 `config.yaml` 中填入抓包获得的 `Synjones-Auth` 字段信息。
2. 在其他 Python 文件中调用 `query` 函数即可。
3. 若要启动网页查询页面，运行：

~~~
streamlit run webUI.py
~~~

## 隐私声明

所有服务均在本地运行，不会保存或上传任何用户数据。可能会在同级目录生成缓存文件，清理后不影响使用。

## 未来计划

- ~~加入手机抓包教程~~
- ~~制作可视化页面~~

> 目前都已完成