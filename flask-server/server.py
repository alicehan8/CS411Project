from flask import Flask, render_template, redirect, request, session, make_response,session,redirect
import spotipy
import spotipy.util as util#
from dotenv import load_dotenv
import os
#from credentz import * # stores credential information such as SSK, CLIENT_SESSION, CLIENT_ID
import time
import json

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# app.secret_key = os.getenv('CLIENT_SECRET')

# API_BASE = 'https://accounts.spotify.com'

# # Make sure you add this to Redirect URIs in the setting of the application dashboard
# REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

# SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# # Set this to True for testing but you probaly want it set to False in production.
# # SHOW_DIALOG = True


# # authorization-code-flow Step 1. Have your application request authorization; 
# # the user logs in and authorizes access
# @app.route("/")
# def verify():
#     # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#     sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id =process.env, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#     auth_url = sp_oauth.get_authorize_url()
#     print(auth_url)
#     return redirect(auth_url)

# @app.route("/index")
# def index():
#     return render_template("index.html")

# # authorization-code-flow Step 2.
# # Have your application request refresh and access tokens;
# # Spotify returns access and refresh tokens
# @app.route("/api_callback")
# def api_callback():
#     # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#     sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#     session.clear()
#     code = request.args.get('code')
#     token_info = sp_oauth.get_access_token(code)

#     # Saving the access token along with all other token related info
#     session["token_info"] = token_info


#     return redirect("index")

# # authorization-code-flow Step 3.
# # Use the access token to access the Spotify Web API;
# # Spotify returns requested data
# @app.route("/go", methods=['POST'])
# def go():
#     session['token_info'], authorized = get_token(session)
#     session.modified = True
#     if not authorized:
#         return redirect('/')
#     data = request.form
#     sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
#     response = sp.current_user_top_tracks(limit=data['num_tracks'], time_range=data['time_range'])

#     # print(json.dumps(response))

#     return render_template("results.html", data=data)

# # Checks to see if token is valid and gets a new token if not
# def get_token(session):
#     token_valid = False
#     token_info = session.get("token_info", {})

#     # Checking if the session already has a token stored
#     if not (session.get('token_info', False)):
#         token_valid = False
#         return token_info, token_valid

#     # Checking if token has expired
#     now = int(time.time())
#     is_token_expired = session.get('token_info').get('expires_at') - now < 60

#     # Refreshing token if it has expired
#     if (is_token_expired):
#         # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#         sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#         token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

#     token_valid = True
#     return token_info, token_valid

# if __name__ == "__main__":
#     app.run(debug=True)




####################################
### basics to get things running ###

# from flask import Flask

# app = Flask(__name__)

# Members API Route
# verify it on localhost:5000/members
@app.route("/members")
def members():
  return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
  app.run(debug=True) #debug = true since we're in dev mode

### Important notes:
# run by typing this in terminal: python3 server.py
# runs on port 5000 by default --> go to http://127.0.0.1:5000/members in my case
# start virtual environment with: source venv/bin/activate
# use command shift p if you flask isnt' installing and then go to "Python: select interpreter"
# in the client/package.json file you may need to change the proxy to the start of your link (everything preceding /members above) so we can use relative paths
# following this video: https://www.youtube.com/watch?v=7LNl2JlZKHA&ab_channel=ArpanNeupane
# everyone will need to go into the package.json file and change the proxy to their local tunnel