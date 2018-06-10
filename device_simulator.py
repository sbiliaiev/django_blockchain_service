import random
import time
import uuid

import requests
import yarl


DJANGO_URL = 'http://localhost:8080/api/'
BLOCKCHAIN_URL = 'http://localhost:5000/'


def generate_string(size):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(alphabet) for _ in range(size))


class AbstractDeviceEmulator:

    def __init__(self, base_url, *args, **kwargs):
        self._base_url = yarl.URL(base_url)
        self._transport = requests.Session()
        self._transport.headers.update({
            'Content-Type': 'application/json',
        })

    def send_data(self):
        raise NotImplemented()

    def generate_data(self):
        return {
            'rvc_as': generate_string(10),
            'ctx_era': generate_string(5),
            'cnt': random.uniform(1.6, 52.3),
            'mix_stp': random.randint(0, 100),
            'mux_delta_vp': random.uniform(0.9, 23.3),
            'coef_ttx': random.uniform(0.02, 0.9),
            'active': True
        }


class DjangoDeviceEmulator(AbstractDeviceEmulator):
    def __init__(self, base_url, *args, **kwargs):
        super(DjangoDeviceEmulator, self).__init__(base_url, *args, **kwargs)
        # Device registration
        rv = self._transport.post(self._base_url / 'devices/', json={
            'deviceId': generate_string(5)
        }, timeout=None)

        if rv.status_code != 201:
            raise Exception

        self._id = rv.json()['id']

    def send_data(self):
        payload = super(DjangoDeviceEmulator, self).generate_data()
        payload.update({'device': self._id})
        print('Sending {}'.format(payload))
        rv = self._transport.post(self._base_url / 'data/', json=payload,
                                  timeout=None)
        if rv.status_code != 201:
            raise Exception


class BlockchainDeviceEmulator(AbstractDeviceEmulator):
    
    def __init__(self, base_url, *args, **kwargs):
        super(BlockchainDeviceEmulator, self).__init__(base_url, *args, **kwargs)

        self._author = str(uuid.uuid4())

    def send_data(self):
        payload = {
            'author': self._author,
            'content': super(BlockchainDeviceEmulator, self).generate_data()
        }
        print('Sending {}'.format(payload))
        rv = self._transport.post(self._base_url / 'new_transaction', json=payload,
                                  timeout=None)
        if rv.status_code != 201:
            raise Exception


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise RuntimeError

    cls = sys.argv[1]
    cnt = int(sys.argv[2])
    map = {
        'd': (DjangoDeviceEmulator, DJANGO_URL),
        'b': (BlockchainDeviceEmulator, BLOCKCHAIN_URL)
    }
    devices = [ map[cls][0](map[cls][1]) for _ in range(cnt) ]
    while True:
        try:
            random.choice(devices).send_data()
        except Exception:
            pass
        except KeyboardInterrupt:
            break