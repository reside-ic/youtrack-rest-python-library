import json
import urllib.parse
import httplib2 as httplib2

from enum import Enum, auto


class RequestType(Enum):
    POST = auto()


class YTClient(object):
    def __init__(self, url, proxy_info=None, token=None):
        if proxy_info:
            self.http_client = httplib2.Http(disable_ssl_certificate_validation=True)
        else:
            self.http_client = httplib2.Http(disable_ssl_certificate_validation=True, proxy_info=proxy_info)

        self.baseUrl = url.rstrip('/')
        self.apiUrl = self.url + '/api'
        self.headers = dict()
        self.__last_credentials = None

        self.set_auth_token(token)

        self.headers['Accept'] = 'application/json'
        self.headers['Content-Type'] = 'application/json'

    def set_auth_token(self, token):
        if token:
            self.headers = {'Authorization': 'Bearer {}'.format(token)}

    def create_issue(self, project, summary, description, **additional_fields):
        return_fields = None

        issue_info = {'project': project,
                      'summary': summary,
                      'description': description}

        self.headers['Cache-Control'] = 'no-cache'

        for key, value in additional_fields.items():
            if key == 'return':
                return_fields = value
                continue

            issue_info[key] = value

        self.__request(RequestType.POST, '/issues', return_fields, issue_info)

    def __request(self, request_type, resource, request_prams=None, request_body=None):
        if resource.startswith('http'):
            request_url = resource
        else:
            request_url = self.apiUrl + resource

        if request_prams:
            request_url += urllib.parse.urlencode(request_prams)

        body_json = None
        if request_body:
            body_json = json.dumps(request_body)

        return RequestEngine.send_request(self.http_client, request_type, request_url, self.headers, body_json)


class RequestEngine(object):
    @staticmethod
    def send_request(http_client, request_type, url, headers, body):
        request_handlers = {RequestType.POST: RequestEngine.post_request}

        return request_handlers[request_type](http_client, url, headers, body)

    @staticmethod
    def post_request(http_client: httplib2.Http, url, headers, body):
        return http_client.request(url.encode('utf-8'),
                                   'POST',
                                   body,
                                   headers)
