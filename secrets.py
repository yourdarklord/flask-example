from os import environ

#Retrieve SOME_SECRET from .env file and assign it to a variable of the same name
SOME_SECRET = environ.get("SOME_SECRET")

#NOTE: It seems that flask doesn't like you naming these variables differently from their .env counterparts, so try to remain consistent