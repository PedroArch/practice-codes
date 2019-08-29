from flask import Flask

app = Flask(__name__)

# End of File
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)