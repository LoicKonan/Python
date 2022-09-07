from datetime import date, timedelta
from elasticsearch import Elasticsearch

today = date.today()
d2 = today - timedelta(days=5)
d1 = today.strftime("%Y-%m-%d")
d2 = d2.strftime("%Y-%m-%d")

es = Elasticsearch('https://siem.cnap.dso.mil:9200')
es.options(request_timeout=30)

resp = es.search(index="panw.panos*", query={"exists": {"field": "source.ip.keyword"},
                                             "range": {"@timestamp": {"lt": f"{d1}T00:00:00.000-04:00",
                                                                      "gte": f"{d2}T00:00:00.000-04:00"}}})
print(resp)
