from django.core.mail import send_mail
from lead.models import Lead



def enviar_campana(campana):

    if campana.estado != "Activa":
        return

    leads = Lead.objects.filter(
        categoria_fav__iexact=campana.publico_obj
    )

    for lead in leads:

        if lead.correo:

            # 🔥 MENSAJE PERSONALIZADO
            mensaje = f"""
Hola {lead.nombre} 👋

Esperamos que te encuentres muy bien 😊

Tenemos nuevas ofertas para ti:

{campana.mensaje}

¡No te lo pierdas! 🔥
"""

            send_mail(
                subject=f"🔥 {campana.nombre}",
                message=mensaje,
                from_email='tucorreo@gmail.com',
                recipient_list=[lead.correo],
                fail_silently=False,
            )