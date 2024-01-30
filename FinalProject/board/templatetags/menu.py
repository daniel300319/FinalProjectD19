from django.template import Library

register = Library()


@register.simple_tag()
def get_items_for_menu(request):
    is_authenticated = request.user.is_authenticated
    blocks = [
        {'title': 'Новости', 'url_name': 'board:home'}
    ]

    if is_authenticated:
        blocks.append({'title': 'Мои отклики', 'url_name': 'board:my_comments'})
        blocks.append({'title': 'Добавить новость', 'url_name': 'board:create'})

    return blocks