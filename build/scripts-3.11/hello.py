#!python
from dev_aberto import hello

import os
from datetime import date, datetime
from babel.dates import format_date
import gettext

locale_env = os.environ.get('LANGUAGE', 'en_US.UTF-8').split('.')[0] 

try:
    t = gettext.translation('cli', localedir='locale', languages=[locale_env])
    t.install()
    _ = t.gettext
except FileNotFoundError:
    # Fallback to default English strings
    _ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()

    dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    formated_dt = format_date(dt, format='full', locale=locale_env)
    
    print(_('Last commit made on:'), formated_dt, _('by'), name)
