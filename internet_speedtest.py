import speedtest
from collections import OrderedDict
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def print_results(d):
    dict = {
        'Speed': {
            'Download': '{} Mb/s'.format(d['download'] / (1024 * 1024)),
            'Upload': '{} Mb/s'.format(d['upload'] / (1024 * 1024)),
            'Data wasted for download speed test': '{} MB'.format(float(d['bytes_received']) / (1024 * 1024)),
            'Data wasted for upload speed test': '{} MB'.format(float(d['bytes_sent']) / (1024 * 1024)),
        },
        'ISP': {
            'name': d['client']['isp'],
            'Rating': d['client']['isprating']
        },
        'Target Server': {
            'Sponsor': d['server']['sponsor'],
            'host': d['server']['host'],
            'url': d['server']['url'],
            'Latency': d['server']['latency']
        },
        'IP Address': d['client']['ip'],
    }
    print '\nSpeed test results :::::\n{}\n\n'.format(dict)


def download_upload_speed():
    servers = []
    threads = None

    s = speedtest.Speedtest()
    s.get_servers()
    print '\nour speed test host sponsor details :::::\n{}\n\n'.format(s.get_best_server())
    s.download(threads=threads)
    s.upload(threads=threads)

    print_results(s.results.dict())


download_upload_speed()

