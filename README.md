# FlaskScaffold - Flask开发脚手架

```
├── common                      # 存放公用模块目录
│   ├── libs                        # 存放一些公用类与函数
│   └──  models                     # 存放数据库模型
│        └── __init__.py            # 改写SQLAlchemy, 数据模型基类
│   
├── config                      # 配置文件目录
│   ├── baseSetting.py              # 基础配置
│   ├── development.py              # 开发环境配置
│   └── production.py               # 生产环境配置
│   
├── web                         # 网站相关内容目录
│   ├── controllers                 # 控制器目录
│   └── httpCode                    # http返回
│        ├── __init__.py                # 改写APIResponse, 统一数据返回
│        └── code.py                    # 常用的http返回代码
│   ├── interceptors            # 拦截器目录
│   ├── static                  # 静态资源目录
│   └── templates               # 模板目录
│        └── index.html             # html单页面入口
│   └── validators              # 表单验证目录
│        └── __init__.py             # 表单验证基类
│   
├── application.py              # app工厂
├── secret.ini                  # 敏感信息秘钥
├── manager.py                  # 入口文件
└── www.py                      # 路由蓝图
```
