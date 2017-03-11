
class BadRequest(HTTPException): 400


- - -
# API draft

## assume

仅用于演示

## intro

* about id

    5 - 16 位, 英文 数字  部分特殊符号
    
* about token auth
    
    Authorization: sgo_token <your token>
    
    tips:   
    
    Authorization in Request Header
   
    value field begin with 'sgo_token', 
    then separate with a space, then the token
    
    the expire time is set to 100 years for the first edition

* about the response

    if your request success, there MUST be a `flag` key in the returned json
    
    else there may be nothing
    
    only part of the failed response with `flag` set to integer 1,
    and a hint `msg` with string


- /auth/login
    - POST    登录

- /users  
    - GET     查询用户
    - POST    用户注册, 用户连接
    
- /users/me 
    - GET     根据 session_token 查询用户
    
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
        