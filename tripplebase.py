from flask import Flask
from twilio.rest import TwilioRestClient

conn = TwilioRestClient()
app = Flask(__name__)


@app.route('/')
<<<<<<< HEAD
# load most popular dares
# -> twitter feed panel + internal tracking of votes

def greeting():
    return 'Hello World!'
    return 'IamN00B!woot'
=======
# def greeting():
#     return 'Hello World!'
>>>>>>> df2d1d3fd072f6a1d5e94c8668285207016a8a0c

# load most popular dares
# -> twitter feed panel + internal tracking of votes

# ########################################
# STAVROS, this is your section here:
# database stuff, happening in here in root route

def load_tweets(arg):
    pass


def load_dares(arg):
    pass


# ########################################

# @app.route('/sms', methods=['POST'])

<<<<<<< HEAD
#     def add_entry():



        # if not session.get('logged_in'):
        #     abort(401)
        # g.db.execute('insert into entries (title, text) values (?, ?)',
        #              [request.form['title'], request.form['text']])
        # g.db.commit()
        # flash('New entry was successfully posted')
        # return
=======
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



>>>>>>> df2d1d3fd072f6a1d5e94c8668285207016a8a0c

# @app.route('/sms_callback', methods=['POST'])

    # SMS callback method, possibly a response


# @app.route('/sms_callback', methods=['POST'])







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
# install twitter wrapper:
#


# inbound SMS
# /message resources
# twitter API (consumer key: G2lHCk80bZzuIL2pf6d9AUsli)
#
