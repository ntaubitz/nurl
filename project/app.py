from flask import Flask, request
from project.lib.nurl_repository import NUrlRepository

app = Flask(__name__)


@app.route('/health')
def get_health():
    return 'OK'


@app.route('/shorten')
def get_shorten():
    return NUrlRepository.get_instance().get_or_create(request.args.get('url')).short_url


@app.route('/redirect')
def get_redirect():
    return NUrlRepository.get_instance().get_by_original(request.args.get('nurl')).original_url


if __name__ == '__main__':
    app.run()
