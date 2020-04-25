import http.client

conn = http.client.HTTPConnection("httpbin.org")

payload = "{\"arg1\": \"value1\"}"

headers = {'x-my-name': "anshul"}

conn.request("POST", "/post", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
