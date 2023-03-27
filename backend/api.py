from flask import Flask, request, jsonify
from flask_cors import CORS
from dnsresolver import EmailServer

app = Flask(__name__)
CORS(app)
@app.route('/mx_records/<domain>', methods=['GET'])
def main_api(domain):
    email_server = EmailServer(domain=domain)
    try: 
        print(email_server.valid_mail_server)
        return jsonify({'mx_records': email_server.valid_mail_server})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
