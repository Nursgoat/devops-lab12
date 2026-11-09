Зертханалық жұмыс №12
Тақырыбы
Мониторинг және логтау жүйелері (Prometheus, ELK Stack)

Жұмыстың мақсаты
Prometheus жүйесін үйрену
ELK Stack жұмысын түсіну
Docker арқылы контейнерлерді іске қосу
Grafana арқылы метрикаларды көрсету
Kibana арқылы логтарды іздеу

Қолданылған технологиялар
Docker
Prometheus
Node Exporter
Grafana
Elasticsearch
Logstash
Kibana
Python

Prometheus іске қосу
docker compose up -d


Prometheus:
http://localhost:9090/

Grafana:
http://localhost:3000/

Node Exporter:
http://localhost:9100/metrics

Grafana логин: admin
Пароль: admin

Grafana метрикалары
CPU:
100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])))


RAM:
100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)


Disk:
100 * (1 - node_filesystem_avail_bytes{mountpoint="/",fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{mountpoint="/",fstype!~"tmpfs|overlay"})


ELK Stack іске қосу
docker compose -f docker-compose-elk.yml up -d


Kibana:
http://localhost:5601/

Elasticsearch:
http://localhost:9200/

Логтарды тексеру
INFO App started
WARNING Low memory
ERROR App crashed


Kibana-да logstash-* индексін құрып, Discover бөлімінде error сөзі арқылы іздеу жасау.

Python логтау
python app.py


Қорытынды
Зертханалық жұмыста Prometheus және Grafana арқылы жүйе метрикаларын бақылауды үйрендім. ELK Stack көмегімен логтарды жинау, сақтау және іздеу тәсілдерін қарастырдым. Docker арқылы қажетті контейнерлерді іске қосу жолдарын меңгердім.
