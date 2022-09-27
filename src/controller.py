from datetime import datetime

from flask import request, Blueprint, Response, json, render_template
from flask import current_app

import src.service as service


app = Blueprint('app', __name__, url_prefix='/')


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/oembed', methods=['GET'])
def main():
    url = request.args.get('url')

    if valid_necessary_token_url(url):
        return Response(json.dumps({"msg" : "해당 사이트가 접근 권한을 막았습니다."}), status=403, mimetype='application/json')

    result = service.get_oEmbed_from_url(url)
    return Response(json.dumps(result), status=200, mimetype='application/json')


def valid_necessary_token_url(url: str):
    necessary_token_site_list = ["instagram"]
    for site in necessary_token_site_list:
        if site in url:
            return True