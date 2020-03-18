from src.api import get_data
from sys import argv
import argparse
import json

from datetime import datetime
from elasticsearch import Elasticsearch


def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    es.indices.put_mapping(
        index=index_name,
        doc_type=doc_type,
        body={
            doc_type: {
                "properties": {"issue_date_time": {"type": "date"},
                }
            }
        }
    )
    return es

def get_output_data(result_fn: str) ->list:
    
    with open(result_fn) as f_read:
        r = json.load(f_read)
        data_list = r["data_list"]
    return data_list

if __name__=='__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument("--page_size", type=int, default=None)
    ap.add_argument("--num_pages", type=int, default=None)
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    page_size, num_pages, output_fn = args.page_size, args.num_pages, args.output

    if page_size is None:
        print('Page size should be specified!')
        exit()

    get_data(page_size, num_pages, output_fn)

    es = create_and_update_index('violation-index', 'violation')
    j = get_output_data(output_fn)


    
    i = 0
    if output_fn != None:
        for j in j:
            try:
                
                j['issue_date_time'] = datetime.strptime(  j['issue_date'] + ' ' + j['violation_time']+'M',
                                                        '%m/%d/%Y %I:%M%p' )
            except Exception as e:
                j['issue_date_time'] = None

            res = es.index(index='violation-index', doc_type='violation', body=j,)
            print(res['result'] + f' at index: {i}')
            i+=1