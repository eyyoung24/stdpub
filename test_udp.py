from pub import Publisher, DEFAULT_ENV_ROOT

import os

os.environ[DEFAULT_ENV_ROOT + 'BACKEND'] = 'udp'

pub = Publisher()
for i in range(10000):
    pub.publish({'test': [1,2]})
    pub.log('Everything is good.')

