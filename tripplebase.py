from flask import Flask
from twilio.rest import TwilioRestClient
from twilio import twiml

conn = TwilioRestClient()
app = Flask(__name__)


@app.route('/')
# def greeting():
#     return 'Hello World!'

# load most popular dares
# -> twitter feed panel + internal tracking of votes/dares

# STAVROS ########################################
# this is your section here:
# database stuff, happening in here in root route

def load_tweets(arg):
    pass


def load_dares(arg):
    pass

# some sample code for interacting with the database:

    # def add_entry():
    #
    #
    #
    #     # if not session.get('logged_in'):
    #     #     abort(401)
    #     # g.db.execute('insert into entries (title, text) values (?, ?)',
    #     #              [request.form['title'], request.form['text']])
    #     # g.db.commit()
    #     # flash('New entry was successfully posted')
    #     return
# STAVROS ########################################



# TWILIO stuff ###########################
# inbound sms and callback methods
#
@app.route('/sms', methods=['GET'])
# request TwiML

# respond to inbound message
def respond:

    response = twiml.Response()
# r.say("Hello")
# print str(r)
    message = response.message("Vote received; checkout @tripledogme on Twitter for more action!", sender="+14153199984")

    print "responded"



@app.route('/sms_callback', methods=['POST'])

    # SMS callback method; retrieve message SID and parameters




# TWILIO stuff ###########################



# STRETCH GOALS:

# USERS ========

# @app.route('/home')
# # authenticated users main area
# def hello_world():
#     return 'Hello World!'
#

#
# @app.route('/user/<username>')
# user profile
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# USERS ========







if __name__ == '__main__':
    app.run()

# (checkmark in osx: option + v)
# TODO:
# install twitter wrapper: √
#


# inbound SMS
# /message resources
# twitter API (consumer key: G2lHCk80bZzuIL2pf6d9AUsli)
#
