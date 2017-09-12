from flask import Flask
app = Flask(__name__)

html = """
<html>
<body>
<img src="http://i.imgur.com/jrtNP6s.jpg" width="600px; border-bottom: solid 1px black; padding-bottom: 10px; margin-bottom: 10px; clear: right;" />
</body>
</html>
"""

@app.route('/')
def moe():
    return html

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
