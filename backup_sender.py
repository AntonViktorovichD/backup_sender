#!/usr/bin/python3

import os

for item in os.listdir('/home/User/web/backup'):
    if item.find('20230215') != -1:
        os.system('sudo rsync -av /home/User/web/backup/' + item + ' **********@**********:/home/grand/web/grandgold.jewelry/public_html/bitrix/backup/')
        print(item)
