from flask import Flask, render_template    
import pandas as pd                         
app = Flask(__name__)                

@app.route('/')               
def index():                  
    # HTML to render the initial page with the Refresh button
    return '''
    <!doctype html>
    <html>
    <head><title>CSV Data Display</title></head>
    <body>
        <h1>10 News for You</h1>
        <form action="/publish" method="get">
            <button type="submit">Refresh</button>
        </form>
    </body>
    </html>
    '''

@app.route('/publish')
def publish_data():
    # Correct path for your CSV file location
    file_path = '../../flask_csv_project/output.csv'
    try:
        data_frame = pd.read_csv(file_path)
        sample_data = data_frame.sample(10)  # Select 10 random rows
        # Pass the sampled data to the display.html template
        return render_template('display.html', tables=[sample_data.to_html(classes='data', header="true")], titles=sample_data.columns.values)
    except Exception as e:
        # If there's an error, print it to the console and show it on the webpage
        print(e)
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
