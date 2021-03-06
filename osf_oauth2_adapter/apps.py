import os

from django.apps import AppConfig


class OsfOauth2AdapterConfig(AppConfig):
    name = 'osf_oauth2_adapter'
    # staging by default so people don't have to run OSF to use this.
    osf_api_url = os.environ.get('OSF_API_URL', 'https://api.staging.osf.io').rstrip('/') + '/'
    osf_accounts_url = os.environ.get('OSF_ACCOUNTS_URL', 'https://accounts.staging.osf.io').rstrip('/') + '/'
    default_scopes = ['osf.users.profile_read', ]
    humans_group_name = 'OSF_USERS'
