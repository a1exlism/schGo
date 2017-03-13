
class BadRequest(HTTPException): 400


- - -
# API draft

## assume

仅用于演示

## intro

* about id

    5 - 16 位, 英文大小写 数字 下划线

* about token auth

    Authorization: sgo_token <your token>

    tips:   

    Authorization in Request Header

    value field begin with 'sgo_token',
    then separate with a space, then the token

    the expire time is set to 100 years for the first edition

* about security

    客户端进行字符串过滤
    服务端检查字符串合法性, 不进行过滤

* about the response

    if your request success, there MUST be a `flag` key in the returned json

    else there may be nothing

    only part of the failed response with `flag` set to integer 1,
    and a hint `msg` with string

* about datetime
    in utc time, regardless of timezone
    in seconds

* about tags of tasks and products
    all should be lower case if English

- /auth/login
    - POST    登录

- /users  
    - GET     查询用户
    - POST    用户注册, 用户连接

- /users/me
    - GET     根据 token 查询用户

- /users/<user_id>    
    - GET     获取用户
    - PUT     更新用户, 用户连接
        request should contain most of the fields

- /users/<user_id>/refresh_session_token  
    - PUT

    <building>

- /users/<user_id>/update_pw             
    - PUT

- /tasks                                
    - GET     查询任务
    - POST    发布任务

- /tasks/<task_id>                     
    - GET     获取任务
    - PUT     更新任务

- /products/<product_id>              
    - GET
    - PUT

- /products                          
    - GET
    - POST


- /rtm/messages                     
    - POST

- /media/                            

- /lbs                              

- - -
# sgo

## Users [/user]

### get user info [GET]

+ Request(application/json)

# Models

in `sgo/user/models.py` and `sgo/store/models.py`

# Apis

in `sgo/user/views.py` and `sgo/store/views.py`

# Auth

in `sgo/auth/views.py`

if deploy, please comment `@token_auth.verify_token`

on `def verify_token_dev(token):`

and uncomment this

on `def verify_token(token):`
