from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse((
        'https',
        'api.vk.com',
        '/method/users.get',
        None,
        urlencode(OrderedDict(
            fields=','.join(('bdate', 'sex', 'about')),
            access_token=response['access_token'],
            v='5.92')),
        None
    ))

    vk_response = requests.get(api_url)

    if vk_response.status_code != 200:
        return

    data = vk_response.json()['response'][0]
    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    if data['bdate']:
        birth_date = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        today = timezone.now().date()

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18 or age > 100:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.userprofile.birth_date = birth_date

    user.save()
