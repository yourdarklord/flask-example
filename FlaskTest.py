from flask import Flask, abort

def start():
  #Create a new flask app and give it a name
  app = Flask("FlaskTest")

  #Load config from the specified python file
  app.config.from_pyfile("secrets.py")

  #Decorator to define route and method
  @app.route("/", methods=["GET"])
  def retrieve():
    #This will be logged to the console only when debugging is enabled
    app.logger.debug("Debug value")

    #Build response as a key-value dictionary, will be treated as json
    returnval = dict()
    returnval["response"] = "In flask"
    returnval["secret"] = app.config.get("SOME_SECRET") #Retrieve secret with given name form config

    return returnval

  @app.route("/error", methods=["POST"])
  def error():
    app.logger.error("An error has occurred")
    
    #Return error with the specified
    return abort(404)
  
  return app


# These should really be in a separate file where Flask would start instead, but i'm lazy
app = start()
app.run()