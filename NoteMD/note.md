# FLASK 基本概念
from flask import Flask
## 1. 实例化与路由
使用 `name = Flask(__name__)` 来实例化 flask。
使用 `name.route(path)` 来为网页添加路由。
其中：
- name 是任意字符串，用来作为实例化的变量;
- path 是一个路径，相对于 path root 。

