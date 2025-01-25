# What is it?

This project plots the distribution of outputs from LeetCode problem [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)

![](https://github.com/lantenak/last_stone_weight/blob/main/images/stone_head.jpg)

# What technologies are being used?

* Python
* Kafka
* InfluxDB
* Grafana

# Resolving dependencies

| name | version |
| --- | --- |
| Python | 3.13.0 |
| kafka-python | 2.0.3.dev0 |
| influxdb-client | 1.48.0 |

# How to run it?

1. Run `docker-compose up -d`;

2. Run `python producer.py`;
3. Run `python consumer.py`;
4. Open Grafana and build a dashboard

# Dashboard example

![](https://github.com/lantenak/last_stone_weight/blob/main/images/last_stone_weight.png)
