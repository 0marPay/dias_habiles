from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from flask import Flask, request, redirect

# Credenciales de Twilio (reemplaza con tus propias credenciales)
account_sid = 'AC2144e18f10b06f172bc23c0672bce1fa'
auth_token = '5b4907c33ebebc0a8356750a0ca206d9'
client = Client(account_sid, auth_token)

# Configuración del servidor Flask
app = Flask(__name__)

# Ruta para manejar mensajes entrantes
@app.route('/incoming', methods=['POST'])
def incoming(body):
    print(body)
    response = MessagingResponse()
    response.message("¡Hola! Soy tu bot de WhatsApp. ¿En qué puedo ayudarte?")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)


# from twilio.rest import Client

# account_sid = 'AC2144e18f10b06f172bc23c0672bce1fa'
# auth_token = '5b4907c33ebebc0a8356750a0ca206d9'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Holi',
#   to='whatsapp:+5217225515918'
# )

# print(message.sid)