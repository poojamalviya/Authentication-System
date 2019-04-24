# Token based authentication
____

Django framework used to create a authentication middleware.
_MongoDb_ used as backend data base and RedisDb for cashing database

## /authenticate
Once the user is Signed In and tries to log in with Email id and password, the authicate function validates the credential against
object stored in mongoDb and if the credentials are matching then it creates and returns a bearer token which is saved in RedisDb
for 30 mins.


## /validate
Each time user tries to move to next page the saved bearer token in cookie is validated with the token saved in RedisDb.
