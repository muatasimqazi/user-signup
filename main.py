from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = False

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>User Signup</title>
        </head>
        <body>

        <h1>Signup</h1>

          <form method="POST">

          <div>
              <label for="rot">Username </label>
              <input type="text" name="username">
          </div>

          <div>
              <label for="rot">Username </label>
              <input type="text" name="username">
          </div>

          <div>
              <label for="rot">Username </label>
              <input type="text" name="username">
          </div>

          <div>
              <label for="rot">Username </label>
              <input type="text" name="username">
          </div>

          <input type="submit">
          </form>
        </body>
    </html>
"""

@app.route('/', methods=['POST'])
def encrypt():
    str_1 = request.form['rot']
    str_2 = request.form['text']
    encrypted_str = rotate_string(str_2,int(str_1))

    return form.format(encrypted_str)

@app.route("/")
def index():
    return form.format('')

app.run()
