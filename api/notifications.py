import requests
import threading

def send_user_created_email(user):
    def _send_notification():
        url = "http://notification-service:5000/notify"
        payload = {
            "asunto": "Nuevo registro de usuario",
            "mensaje": f"Se ha creado un nuevo usuario:\nNombre: {user.nombre}\nCorreo: {user.email}",
            "nombre": user.nombre,
            "correo": user.email
        }
        try:
            response = requests.post(url, json=payload, timeout=3)
            response.raise_for_status()
            print("📤 Notificación enviada:", response.text)
        except requests.exceptions.RequestException as e:
            print("⚠️ Error al enviar notificación:", str(e))

    threading.Thread(target=_send_notification).start()
