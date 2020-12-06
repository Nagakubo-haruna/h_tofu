from flask import Flask, render_template #追加
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    with open('room_data.json') as f:
    	df = json.load(f)
    #return name
    return render_template('hello.html', title='flask test', name=name, df=df['members']) #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)