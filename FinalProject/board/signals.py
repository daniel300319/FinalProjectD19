from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from FinalProject.board.models import Comment


@receiver(post_save, sender=Comment)
def send_mail(sender, instance, created, **kwargs):

    if created:
        user = instance.post.author

        html = render_to_string(
            'board/messages/new_comment.html',
            {
                'user': user,
                'comment': instance,
             },
        )

        msg = EmailMultiAlternatives(
                subject=f'У вас новый отклик!',
                from_email='d.agur@yandex.ru',
                to=[user.email]
            )

        msg.attach_alternative(html, 'text/html')
        msg.send()
    else:
        user = instance.author

        html = render_to_string(
            'board/messages/update_comment.html',
            {
                'user': user,
                'comment': instance,
             },
        )

        msg = EmailMultiAlternatives(
                subject=f'Статус вашего отклика изменился!',
                from_email='d.agur@yandex.ru',
                to=[user.email]
            )

        msg.attach_alternative(html, 'text/html')
        msg.send()