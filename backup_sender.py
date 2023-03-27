#!/usr/bin/python3

import os
import concurrent.futures
from functools import partial

def backup_rsync(item, source_dir, target_dir, ssh_port):
    if '20230321' in item:
        try:
            os.system(f'sudo rsync -av {source_dir}/{item} -e "ssh -p {ssh_port}" root@185.154.52.238:{target_dir}/{item}')
            print(item)
        except Exception as e:
            print(f"Ошибка при выполнении rsync для элемента {item}: {e}")

def main():
    source_dir = '/home/User/web/backup'
    target_dir = '/home/grand/web/grand.gold/public_html/bitrix/backup'
    ssh_port = 63450

    with concurrent.futures.ThreadPoolExecutor() as executor:
        backup_func = partial(backup_rsync, source_dir=source_dir, target_dir=target_dir, ssh_port=ssh_port)
        executor.map(backup_func, os.listdir(source_dir))

if __name__ == "__main__":
    main()
