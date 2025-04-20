## 项目概述

基于Django框架开发的图书管理系统，支持多角色用户访问，包含以下核心功能模块：

- **用户端**（学生/教职工）：图书检索、借阅记录查询、公告查看
    
- **管理端**（图书馆管理员）：图书数据管理、借阅审批、公告发布、用户权限管理  

---

## 运行环境依赖

### 基础环境

- 操作系统：`Windows 10/11 / macOS 13+ / Linux (Ubuntu 22.04+)`
    
- Python版本：`python 3.10+`
    
- 数据库：`MySQL 8.0.40`
    

### 依赖组件

`asgiref==3.8.1`
`async-timeout==5.0.1`
`certifi==2024.8.30`
`cffi==1.17.1`
`charset-normalizer==3.4.0`
`cryptography==43.0.3`
`Django==5.1.2`
`django-ranged-response==0.2.0`
`django-simple-captcha==0.6.0`
`django-simpleui==2025.1.13`
`et_xmlfile==2.0.0`
`idna==3.10`
`my_module==1.6.2`
`numpy==2.1.3`
`openpyxl==3.1.5`
`pillow==11.0.0`
`pip==25.0.1`
`pycparser==2.22`
`PyMySQL==1.1.1`
`PySocks==1.7.1`
`redis==5.2.0`
`requests==2.32.3`
`setuptools==75.8.0`
`sqlparse==0.5.1`
`typing_extensions==4.12.2`
`tzdata==2024.2`
`urllib3==2.2.3`
`wheel==0.45.1`

---

## 部署配置说明

### 数据库配置（需提前创建）

`DATABASES = {`  
    `'default': {`  
        `'ENGINE': 'django.db.backends.mysql',`     
        `'NAME': 'django_library',`   
        `'HOST': '127.0.0.1',`  
        `'PORT': 3306,`  
        `'USER': 'django_user',`   
        `'PASSWORD': 'SecurePass123!',`   
    `}`  
`}`

### 本地运行流程

1. 克隆仓库
    
    `git clone  https://github.com/kko7/myLibrary`
    `cd myLibrary`
    
2. 安装依赖
    
    `pip install -r requirements.txt`
    
3. 数据库迁移
    
    `python manage.py makemigrations`
    `python manage.py migrate`
    
4. 启动服务
    
    `python manage.py runserver`
    

---

## 系统访问信息

### 入口地址

- 本地运行：[http://localhost:8000](http://localhost:8000/)(用户端)

- 本地运行：[http://localhost:8000/admin](http://localhost:8000/admin)(管理端)


### 测试账号

| 角色    | 用户名    | 密码           | 访问权限         |
| ----- | ------ | ------------ | ------------ |
| 普通用户  | test2  | test12345678 | 图书检索、借书还书    |
| 图书管理员 | test3  | test12345678 | 管理读者/图书/借阅记录 |
| 系统管理员 | admin1 | admin1       | 全功能管理后台      |

---

## 数据初始化

1. 预置数据脚本
    
    `/datebase/`
    `├── django_library.sql  %% 完整数据库导出文件(含表结构+初始数据) %%`
    `├── django_library_base.sql %% 基础表结构，不含数据 %%`
    
2. 加载数据：
    
    `mysql -u django_user -p django_library < database/django_librarys.sql`
    

---

## 注意事项

1. **依赖安装**：建议使用虚拟环境
    
2. **数据库准备**：需手动创建`django_library`数据库并授权用户
    
3. **浏览器兼容**：推荐Chrome 115+ / Firefox 110+
    
4. **时区设置**：系统默认使用UTC时间

---

>最后更新：2025年4月20日