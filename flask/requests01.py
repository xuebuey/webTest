import urllib.request
from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    url = "https://space.bilibili.com/245658064/favlist"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('utf-8')
    return data

    print(type(response))
    print(response.geturl())
    print(response.info())
    print(response.getcode())
if __name__ == '__main__':
    app.run(debug=True)