# database

**mongo guide**

[atomic operations](http://docs.mongoing.com/manual-zh/tutorial/model-data-for-atomic-operations.html)



```python

# TODO: Money should be a accurate type
ID = "An Object ID"
TIME = "a datetime type"

USER = {
    "name": "",
    "school": "",
    "phone": "",
    "wechat": "",
    "weibo": "",
    "qq": "",
    "bio": "",
    "balance": 0,
    "credit": 0,
    "params": {
        "pic_url": "",
    },
}

TASK = {
    "place": "",
    "publisher": {
        "id": ID,
        "name": "",
        "url": "",
    },
    "receiver_id": ID,
    "description": "",
    "reward": 0,
    "pub_time": TIME,
    "from": {
        "detail": "",
        "landmark": "",
        "campus": "",
        "school": "",
    },
    "to": {
        "detail": "",
        "landmark": "",
        "campus": "",
        "school": "",
    },
}

LOCATIONS = {

}

USER_TASKS = {
    "task_id": ID,
}

FOLLOWERS = {
    "idol_id": ID,
    "fans_id": ID,
}

PRODUCT = {
    "publisher_id": ID,
    "pub_time": TIME,
    "description": "",
    "views": 0,
    "likes": 0,
    "from": "",  # the school of publisher
    "params": {
        "pic_url": "",
        "video_url": "",
    },
    "tags": ["tag1", "tag2"],
    "comments": [
        {
            "floor": 0,
            "author": "",
            "author_id": ID,
            "date": TIME,
            "comments": "",
            "likes": 0,
        },
        {
            "floor": 0,
            "author": "",
            "author_id": ID,
            "date": TIME,
            "comments": "",
            "likes": 0,
        },
    ]
}

# 优惠
PREFERENTIAL = {

}
```
