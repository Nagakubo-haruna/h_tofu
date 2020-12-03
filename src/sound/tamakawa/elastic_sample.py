# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self):
        es = Elasticsearch("http://localhost:9200")
        self.es = es


    def create_index(self, mapping):
        self.es.indices.create(index='sound', body=mapping)


    def delete_index(self, name):
        self.es.indices.delete(index=name)


    def index_cat(self):
        # インデックス一覧の取得
        indices = self.es.cat.indices(index='*', h='index').splitlines()
        # インデックスの表示
        for index in indices:
            print(index)


    def insert_data(self, name, data):
        # 登録したいドキュメント
        student = {
            "name": "Taro",
            "age": 36,
            "email": "taro@example.com"
        }

        # ドキュメントの登録
        self.es.create(index='students', id=1, body=student)


    def close(self):
        # 内部接続を閉じる
        self.es.close()



if __name__ == '__main__':
    mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "text"},
                "data": {"type": "int"},
                "timestamp": {"type": "date"}
            }
        }
    }


    elastic = Elastic()
    elastic.create_index(mapping)
    elastic.close()




