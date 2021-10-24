from datetime import datetime
import json

def app(environ, start_response):
	data = {'time': datetime.now().strftime("%H:%M:%S"),
			'url': environ["HTTP_HOST"] + environ["RAW_URI"]}
	data = json.dumps(data).encode('utf-8')
	start_response("200 OK", [
		("Content-Type", "application/json"),
		("Content-Length", str(len(data)))
	])
	return [data]
