# -*- coding: utf-8 -*-

def main():
    import os
    import json

    info = {'name': 'Tom',
            'age': '12',
            'job': 'work'}

    if os.path.exists(r'/airflow/xcom/'):
        pass
    else:
        os.makedirs(r'/airflow/xcom/')

    print('hello k8s pod')
    with open(r"/airflow/xcom/return.json", mode='w', encoding='utf-8') as ff:
        ff.write(json.dumps(info))


if __name__ == '__main__':
    main()
