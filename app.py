from flask import Flask, render_template

app = Flask(__name__)

# Set the view engine to EJS (Jinja2)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Serve static files from the 'public' directory
app.static_folder = 'public'

# Render the separate pages (also allowing for absolute urls)
@app.route('/')
def index():
    return render_template('pages/index.jade')

@app.route('/CurrencySorter')
def currency_sorter():
    return render_template('pages/CurrencySorter.jade')

@app.route('/courses')
def courses():
    return render_template('pages/courses.jade')

@app.route('/scam')
def scam():
    return render_template('pages/scam.jade')

@app.route('/FinancialTool')
def financial_tool():
    return render_template('pages/FinancialTool.jade')

@app.route('/donate')
def donate():
    return render_template('pages/donate.jade')

@app.route('/stock')
def stock():
    return render_template('pages/stock.jade')

# Initiate the server on port 8080
if __name__ == '__main__':
    app.run(port=8080)
