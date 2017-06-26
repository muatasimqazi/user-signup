from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = False

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>User Signup</title>
            <style>
            #sign-up {{
                width: 300px;
                padding: 5px;
            }}
            label {{
                float: left;
                clear: left;
            }}
            input {{
                float: right;
                display: inline-block;
            }}
            #sign-up input, #sign-up label {{
                margin-bottom: 5px;
            }}
            div #submit {{
                float: left;
                clear: left;
            }}
            </style>
        </head>
        <body>

        <h1>Signup</h1>
          <div id="sign-up">
              <form method="POST">

              <div>
                  <label for="rot">Username </label>
                  <input type="text" name="username">
              </div>

              <div>
                  <label for="rot">Password </label>
                  <input type="password" name="password">
              </div>

              <div>
                  <label for="rot">Verify Password </label>
                  <input type="password" name="password">
              </div>

              <div>
                  <label for="rot">Email (optional) </label>
                  <input type="text" name="email">
              </div>

              <br>
              <div id="submit">
              <input type="submit">
              </div>
              </form>

          </div>
        </body>
    </html>
"""

@app.route('/', methods=['POST'])
def signup():
    encrypted_str = rotate_string(str_2,int(str_1))

    return form.format(encrypted_str)

@app.route("/")
def index():
    return form.format('')

app.run()
