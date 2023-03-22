from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input text from the form
        text = request.form['text']


        # Generate the plot
        x = np.arange(0, 10, 0.1)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title(text)

        # Save the plot to a file
        filename = 'plot.png'
        plt.savefig(filename)

        # Serve the file over HTTP
        return send_file(filename, mimetype='image/png')

    # Render the input form
    return '''
        <form method="post">
            <label for="text">Enter text:</label>
            <input type="text" name="text" id="text">
            <button type="submit">Submit</button>
        </form>
    '''
    
def returntext():
    return request.form['text']


if __name__ == '__main__':
    app.run()