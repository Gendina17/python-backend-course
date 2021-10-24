from datetime import datetime
import json

def app(environ, start_response):
	data = {'time': str(datetime.now().time()), 'url': environ["HTTP_HOST"]}
	data = json.dumps(data).encode('utf-8')
	start_response("200 OK", [
		("Content-Type", "application/json"),
		("Content-Length", str(len(data)))
	])
	return iter([data])
