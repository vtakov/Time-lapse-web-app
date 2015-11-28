from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time-lapse/<options>')
def timeLapse(options):
    print('hm......................')
    return render_template('time-lapse.html', options = options)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
