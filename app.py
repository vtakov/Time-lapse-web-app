from flask import Flask, render_template
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time-lapse', methods=['GET', 'POST'])
def timeLapse():
    bashCommand = ""
    
    if request.method == 'POST':
        if request.form['submit'] == 'Capture':
            bashCommand = 'gphoto2 --capture-image'
        elif request.form['submit'] == 'Capture 2':
            bashCommand = 'gphoto2 --capture-image -F 2 -I 1'
            
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)
        
    return render_template('time-lapse.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
