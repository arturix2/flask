from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/par_mums')
def par_mums():
    return render_template('par_mums.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/aiziet', methods=['POST'])
def aiziet():
    lietotajs = request.form['lietotajvards']
    return f"Paldies, {lietotajs}! Jūsu pieteikums ir saņemts"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
