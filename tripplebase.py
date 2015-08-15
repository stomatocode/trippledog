from flask import Flask
app = Flask(__name__)


@app.route('/')
# load most popular dares
# -> twitter feed panel + internal tracking of votes
# def greeting():
#     return 'Hello World!'


@app.route('/sms', methods=['POST'])

    def add_entry():



        # if not session.get('logged_in'):
        #     abort(401)
        # g.db.execute('insert into entries (title, text) values (?, ?)',
        #              [request.form['title'], request.form['text']])
        # g.db.commit()
        # flash('New entry was successfully posted')
        return

@app.route('/sms_callback', methods=['POST'])

    # SMS callback method, possibly a response






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
