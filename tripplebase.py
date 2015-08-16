from flask import Flask
from twilio.rest import TwilioRestClient
from twilio import twiml

# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT = "AC65041c9af6c305c4dadbb58f1279daf2"
TOKEN  = "31da0ac861bc350fc86c9accd8f5547e"
client = TwilioRestClient(ACCOUNT, TOKEN)

# conn = TwilioRestClient()

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


# ########################################

# @app.route('/sms', methods=['POST'])

#     def add_entry():
# some sample code for interacting with the database:



        # if not session.get('logged_in'):
        #     abort(401)
        # g.db.execute('insert into entries (title, text) values (?, ?)',
        #              [request.form['title'], request.form['text']])
        # g.db.commit()
        # flash('New entry was successfully posted')
        # return
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
@app.route('/sms')
# request TwiML


# @app.route('/sms_callback', methods=['POST'])
# respond to inbound message
# action="http://tripledog.me/sms_callback"
def respond():
    response = twiml.Response()
    message = response.message("Vote received; checkout @tripledogme on Twitter for more action!", sender="+14153199984")
    print "responded"
    return message


# SMS callback method; retrieve message SID and parameters
@app.route('/sms_callback')

def get_message():


    return None




# TWILIO stuff ###########################



# STRETCH GOALS:

# USERS ========
# twitter oath for user accounts, dare tracking

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

# todo:
# install twitter wrapper:
#


# inbound SMS
# /message resources
# twitter API (consumer key: G2lHCk80bZzuIL2pf6d9AUsli)
#
