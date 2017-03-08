**sgo server**

built with flask + pymongo


# Deploy

## Docker

### 0x01  speed up

[阿里云加速](http://warjiang.github.io/devcat/2016/11/28/%E4%BD%BF%E7%94%A8%E9%98%BF%E9%87%8C%E4%BA%91Docker%E9%95%9C%E5%83%8F%E5%8A%A0%E9%80%9F/)

### 0x02  install docker compose


[install docker compose](https://docs.docker.com/compose/install/#alternative-install-options)

1. install docker-ce
2. install docker-compose
    use pip to install, recommend for virtualenv
    
### 0x03 build and run

`docker-compose up`

### 0x04 info

* app/

    the code
    
* data/
    
    mongodb folder (shared with Mongo's Container) (暂时没什么用)
    
* Dockerfiles/
    - flask
    
        requirements.txt: a copy of sgo_python/requirements.txt
        
    - mongod
        
* docker-compose.yml/

## redis (暂时用不上)

`sudo apt install redis-server`

### configure

/etc/redis/redis.conf

```
#绑定主机IP，默认值为127.0.0.1

#bind 127.0.0.1

#Redis默认监听端口

port 6379
```

`sudo service redis-server restart`


