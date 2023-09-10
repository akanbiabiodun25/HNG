#!flask/bin/python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return "Welcome! kindly use th api service at /api"

@app.route('/api', methods=['GET'])
def get_item():
  """Retrieves all data of the item with the slack_name and track param"""
  slack_name = request.args.get('slack_name')
  current_day = datetime.now().strftime('%A')
  utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
  track = request.args.get('track')
  github_file_url = 'https://github.com/akanbiabiodun25/HNG/blob/main/api/app.py'
  github_repo_url = "https://github.com/akanbiabiodun25/HNG"

  res = {
     "slack_name": slack_name,
     "current_day": current_day,
     "utc_time": utc_time,
     "track": track,
     "github_file_url": github_file_url,
     "github_repo_url": github_repo_url,
     "status_code": 200,
  }
  return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)

