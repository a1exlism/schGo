# database

**mongo guide**

[atomic operations](http://docs.mongoing.com/manual-zh/tutorial/model-data-for-atomic-operations.html)




## user
- _id
- name[重复 或 不重复?]
- school
- phone
- wechat
- weibo
- qq
- bio
- balance
- credit [信用等级]
- params
    - pic_url

- (感觉Android 端的那个 UI 有点问题, IM 部分没凸显出来)
- (好多都没凸显出来, 原型还得再做...)

## task

- _id
- place
- publisher
    - publisher_id
    - publisher_name
    - avatar_url
- receiver_id
- description
- reward
- pub_time
- from
    - detai
    - landmark
    - campus[校区]
    - school
- to
    - ...
    - school

## locations [为了弥补地图服务的不足]


## user_tasks 

- _id
- 


## followers

- _id
- user_id
- following_id

## product

- _id
- publisher_id
- pub_time
- description
- popularity
- likes
- from [the school of publisher]
- params
    - pic_url...
    - video_url...
- tags
- comment
    - comments
    - date
    - author
    - likes


## preferential [优惠]