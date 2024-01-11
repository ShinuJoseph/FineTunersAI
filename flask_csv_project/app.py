from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish')
def publish_data():
    file_path = '/../../data/output_R1.csv'
    try:
        data_frame = pd.read_csv(file_path)

        # Assuming the second column is 'title'
        sample_titles = data_frame.iloc[:, 1].sample(10)
        return render_template('display.html', titles=sample_titles)
    except Exception as e:
        print(e)
        return f"An error occurred: {e}"

@app.route('/content')
def show_content():
    title = request.args.get('title')
    file_path = '/../../data/output_R1.csv'
    try:
        data_frame = pd.read_csv(file_path)
        
        # Find the content for the given title
        content = data_frame[data_frame.iloc[:, 1] == title].iloc[0, 2]
        return render_template('content.html', title=title, content=content)
    except Exception as e:
        print(e)
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)