#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import datetime
import logging

logger = logging.getLogger('gateendringer')
hdlr = logging.FileHandler('./gateendringer.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

endringer = []
slettinger = []

url = "https://www.vegvesen.no/nvdb/api/v2/vegobjekter/538/endringer?type={}&etter={}"

today_dtm = datetime.datetime.today() - datetime.timedelta(days=1)
today_str = today_dtm.strftime('%Y-%m-%m')


def behandle(nvdb_objekt):
    gate = {}
    gate['_id'] = nvdb_objekt.get('id', None)
    gate['versjon'] = nvdb_objekt['metadata']['versjon']
    gate['kommuner'] = nvdb_objekt['lokasjon'].get('kommuner', [])
    gate['fylker'] = nvdb_objekt['lokasjon'].get('fylker', [])
    for e in nvdb_objekt['egenskaper']:
        if e['navn'] == 'Gatekode':
            gate['kode'] = e['verdi']
        if e['navn'] == 'Gatenavn':
            gate['navn'] = e['verdi'].strip()
    endringer.append(nvdb_objekt)


def hent(url, op):
    print "henter:", url
    data = requests.get(url).json()
    for o in data.get('objekter', []):
        if op == "ENDRET":
            behandle(o.get('vegobjekt', {}))
        elif op == "SLETTET":
            slettinger.append(o.get('vegobjekt', ''))
        else:
            logger.warn("Ukjent operasjon: {}".format(op))
    return data.get('metadata', {}).get('neste', {}).get('href', '')


def hent_alle(url, op):
    start = url
    neste = ''
    while start != neste:
        neste = start
        start = hent(neste, op)
        print len(endringer)

def hent_endringer():
    start = url.format('endret', today_str)
    hent_alle(start,'ENDRET')

def hent_slettinger():
    start = url.format('slettet', today_str)
    hent_alle(start, 'SLETTET')

if __name__ =