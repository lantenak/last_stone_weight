# What is it?

This project plots the distribution of outputs from LeetCode problem [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)

![](https://github.com/lantenak/last_stone_weight/blob/main/images/stone_head.jpg)

# What technologies are being used?

* Python
* Kafka
* InfluxDB
* Grafana

# How to run it?

1. Run `docker-compose up -d`;

2. Run `python producer.py`;
3. Run `python consumer.py`;
4. Open Grafana and build a dashboard

# Dashboard example

![](https://github.com/lantenak/last_stone_weight/blob/main/images/last_stone_weight.png)
