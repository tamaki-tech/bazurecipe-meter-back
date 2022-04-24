# BAZURECIPE_METER_BACK

## set up

```bash

# build image
$ docker-compose build --no-cache

# up container
$ docker-compose up -d

# access
http://localhost:8000/docs#/
```

## deply

```bash

$ heroku login

# for the first time only
$ heroku git:remote -a bazurecipe-meter-back

# push to heroku repo
$ git push heroku master

```