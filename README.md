<!--
 * @Author: HYIUYOU 821219285@qq.com
 * @Date: 2023-12-09 13:57:25
 * @LastEditors: HYIUYOU 821219285@qq.com
 * @LastEditTime: 2023-12-09 15:47:38
 * @FilePath: \ULSA\README.md
-->
# ULSA 

## How to Use

### 1.运行WSL中部署的模型

``` shell
$ cd Path/to/ChatGLM2-6B
$ pip install -r requirements
$ pip install transformers==4.33.0
$ python api.py

```

### 2.发送请求

- 并行发送请求
```shell
$ python apirequest.py
```
- 命令行使用

```shell
$ curl -X POST "http://127.0.0.1:8000" \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "你好", "history": []}'
```

### 3.运行模型

```shell
$ cd Path/to/ULSA
$ g++ -o ULSA ULSA.cpp
$ ./ULSA 
```