from flask import Flask, make_response, request, send_from_directory,send_file

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>Transform a file demo</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/transform', methods=["POST"])
def transform_view():
    

    f = request.files["data_file"]
    
    
    
    return send_file(f, mimetype='image/png')

@app.route('/return-files', methods=['GET'])
def return_file():
    return send_from_directory(directory='uploads', filename='3.png', as_attachment=True)

if __name__ == "__main__":
    app.run()