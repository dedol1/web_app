from flask import Flask, render_template
#
app = Flask(__name__)
@app.route('/')
def index():
        return render_template('index.html')
        
        
        

@app.route('/about.html')

def about():
        return render_template('about.html')



@app.route('/products.html')

def product():
        return render_template('products.html')


@app.route('/store.html')

def store():
        return render_template('store.html')
        
@app.route('/index.html')

def home():
        return render_template('index.html')
        

        
        
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

