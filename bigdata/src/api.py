from requests import get, HTTPError
from sodapy import Socrata
import os

API_BASE = 'data.cityofnewyork.us'
END_POINT = 'nc67-uf89'
APP_KEY = os.environ.get('APP_KEY')

def get_data(page_size: int, num_pages = None, output_fn = None):
   
    if num_pages is None:
        total = get_size(API_BASE,END_POINT,APP_KEY )
        num_pages = (total // page_size) + 1

    try:
        client = Socrata(API_BASE, APP_KEY)
    except HTTPError as e:
        print(f'Check URL: {e}')
        raise
    except Exception as e:
        print(f'Something Went Wrong: {e}')
        raise

    try:
        if output_fn is None:
            for i in range(num_pages):
                r = client.get(END_POINT, limit = page_size, offset = i*page_size)
                print(r)
        else:
            with open(output_fn, 'a') as fw:
                for i in range(page_size):
                    for r in range(i):
                        r = client.get(END_POINT, limit = page_size, offset = i*page_size)
                        fw.write( str(r)+'\n')
    except HTTPError as e:
        print(f'Something Went Wrong: {e}')
        raise


        def get_size(API_BASE, END_POINT, APP_KEY ):
   
            try:
                client = Socrata(API_BASE, APP_KEY)
                return int(client.get(END_POINT, select = 'count(*)')[0]['count'])
            except HTTPError as e:
                print(f'Check Your API TOKEN: {e}')
                raise
            except Exception as e:
                print(f'Something Went Wrong: {e}')
                raise