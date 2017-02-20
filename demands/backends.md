FORMAT: 1A
HOST: http://polls.apiblueprint.org/

# SchGo

Backends API file.

## Users [/user]

### Get user info [GET]

+ Request (application/json)
    + Headers

            Location: /user/2

    + Body
            {
              "userid": "1",
              "username": "Bob"
            }

+ Response 201 (application/json)

    + Body
            {
              "infos": "infos"
            }


### Create a new user [POST]
+ backends
  will add a special `token` for validation

+ Request (application/json)
        {
            "username": "Bob",
            "password": "Encrypted",
            "phone": "18805716666",
            "avatar_url": "http://www.google.com/xxx.jpg",
            "school": "HDU"
        }

+ Response 201 (application/json)

    + Body
      + success
            {
              "status": "1"
            }
      + fail
            {
              "status": "0"
            }

### Login [/user/login] [GET]

+ Request (application/json)
        {
            "username": "Bob",
            "password": "Encrypted"
        }

+ Response 201 (application/json)

    + Body
      + success
            {
              "status": "1"
            }
      + fail
            {
              "status": "0"
            }

## 0x2. Orders/Task [/order]

### Get orders [GET]
+ Request (application/json)
        {
          "user": "user's token"
        }

+ Response 201 (application/json)

    + Body
      + success
            {
              "status": "1",
              "details": {
                "announcer_name": "user1's name",
                "announcer_phone": "12200003333",
                "rewards": "$5",
                "description": "user1 do sth for user2 at price of $5",
                "location": "HDU",
                "date": "Task release time."
              }
            }
      + fail
            {
              "status": "0"
            }

### Post an order [POST]
`Here Can't understand use the user name or user token to user`
+ Request (application/json)
        {
            "announcer": "user1",
            "order_type": "delivery",
            "rewards": "$5",
            "description": "user1 do sth for user2 at price of $5",
            "item_type": "fragile",
            "location": "HDU",
            "date": "Task release time.",
            "recipient": "user2"
        }

+ Response 201 (application/json)

    + Body
      + success
            {
              "status": "1"
            }
      + fail
            {
              "status": "0",
              "message": "error 1"
            }



## 0x3. Pay? [/pay]
