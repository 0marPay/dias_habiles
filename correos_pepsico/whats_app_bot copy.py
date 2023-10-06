from twilio.rest import Client

account_sid = 'AC2144e18f10b06f172bc23c0672bce1fa'
auth_token = '5b4907c33ebebc0a8356750a0ca206d9'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='d',
  to='whatsapp:+5217225515918'
)

print(message.sid)