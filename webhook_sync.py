import hmac
import requests

request_body = b""
secret = b""
webhook_url = "https://prod.api.elementary-data.com/webhook/sync/"
signature = hmac.new(secret, request_body, "sha256").hexdigest()
requests.post(webhook_url, headers={"Authorization": signature}, data=request_body)
