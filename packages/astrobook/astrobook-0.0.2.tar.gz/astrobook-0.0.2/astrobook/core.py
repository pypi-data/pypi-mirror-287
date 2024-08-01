import pandas as pd
from requests import request
from io import StringIO

APIs = {
    'simbad': 'https://simbad.u-strasbg.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&query=',
    'vizier': 'http://tapvizier.u-strasbg.fr/TAPVizieR/tap/sync?request=doQuery&lang=adql&query=',
    'gaia': 'https://gea.esac.esa.int/tap-server/tap/sync?request=doQuery&lang=adql&query=',
    'irsa': 'https://irsa.ipac.caltech.edu/TAP/sync?QUERY=',
    }


def sql2df(script, api):
    if api.lower() in APIs.keys():
        api = APIs[api]
    script = ' '.join(script.strip().split('\n'))
    url = api + script.replace(' ', '%20') + '&format=csv'
    res = request('GET', url).content.decode('utf-8')
    return pd.read_csv(StringIO(res))
