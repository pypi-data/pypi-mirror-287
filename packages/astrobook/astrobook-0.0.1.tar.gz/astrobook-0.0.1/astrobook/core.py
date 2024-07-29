import pandas as pd
from requests import request
from io import StringIO

SIMBAD_API = 'https://simbad.u-strasbg.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&query='
IRSA_API = 'https://irsa.ipac.caltech.edu/TAP/sync?QUERY='


def sql2df(script, api):
    if api.lower()=='simbad':
        api = SIMBAD_API
    elif api.lower()=='irsa':
        api = IRSA_API
    script = ' '.join(script.strip().split('\n'))
    url = api + script.replace(' ', '%20') + '&format=csv'
    res = request('GET', url).content.decode('utf-8')
    return pd.read_csv(StringIO(res))
