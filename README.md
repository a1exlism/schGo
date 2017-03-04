**sgo server**

built with flask + pymongo


# Deploy

## redis

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

## Docker

