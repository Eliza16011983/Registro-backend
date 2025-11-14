import requests
import threading

def send_user_created_email(user):
    def _send_notification():
        url = "http://notificaciones-service:8000/send-email/"
        payload = {
            "to": user.email,
            "subject": "Registro exitoso",
            "body": f"Hola {user.username}, gracias por registrarte."
        }
        try:
            response = requests.post(url, json=payload, timeout=3)
            response.raise_for_status()
            print("📤 Notificación enviada:", response.text)
        except requests.exceptions.RequestException as e:
            print("⚠️ Error al enviar notificación:", str(e))

    threading.Thread(target=_send_notification).start()
