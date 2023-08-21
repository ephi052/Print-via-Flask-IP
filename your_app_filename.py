from flask import Flask, request, render_template
import cups

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_and_print():
    if request.method == 'POST':
        # Get uploaded file and printer credentials
        uploaded_file = request.files['file']
        printer_ip = request.form['printer_ip']
        username = request.form['username']
        password = request.form['password']

        # Upload the file
        file_path = f"uploads/{uploaded_file.filename}"
        uploaded_file.save(file_path)

        # Connect to the printer
        conn = cups.Connection()
        conn.authenticate(username, password)

        # Print the file
        conn.printFile(printer_ip, file_path, "Print Job", {})
        
        return "File uploaded and sent for printing!"
    
    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run(debug=True)
