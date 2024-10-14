# pip install google-cloud-storage
# pip install flask
from flask import Flask, request, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'service-account-file.json'

# Initialize the Google Cloud Storage client with the service account file
storage_client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)

# Define the bucket name
BUCKET_NAME = 'myimage-store'

@app.route('/update_airport_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    try:
        # Create a new blob and upload the file's content
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)

        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
