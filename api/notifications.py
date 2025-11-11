import threading
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

def send_user_created_email(user):
    def _send_email():
        subject = 'Nuevo usuario creado'
        message = f'Se ha creado un nuevo usuario:\n\nNombre: {user.nombre}\nEmail: {user.email}\nTeléfono: {user.telefono}'
        recipient_list = [settings.ADMIN_EMAIL]
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            print("Correo enviado correctamente.")
        except BadHeaderError:
            print("Error: encabezado inválido")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
    threading.Thread(target=_send_email).start()
