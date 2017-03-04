
class BadRequest(HTTPException): 400


- - -
### draft
```

user_id: 5 - 16

/users
    GET     查询用户
    POST    用户注册, 用户连接
    
/users/me
    GET     根据 session_token 查询用户
    
/users/<user_id>
    GET     获取用户
    PUT     更新用户, 用户连接
    
/users/<user_id>/refresh_session_token
    PUT
    
/users/<user_id>/update_pw
    PUT

/tasks
    GET     查询任务
    POST    发布任务

/tasks/<task_id>
    GET     获取任务
    PUT     更新任务

/products/<product_id>
    GET
    PUT
    
/products
    GET
    POST


/rtm/messages
    POST

/media/
    
/lbs


```
- - -
# sgo

tips:

if success, flag = '1' is in response

if not success, key 'flag' is omitted

## Users [/user]

### get user info [GET]

+ Request(application/json)
        