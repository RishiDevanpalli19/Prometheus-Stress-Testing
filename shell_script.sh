#Start the prometheus server - localhost:9090

ssh -i ~/.ssh/key_id  root@192.168.43.55 "systemctl stop firewalld" &
ssh -i ~/.ssh/key_id  root@192.168.43.55 "cd /root/prometheus-2.52.0.linux-amd64  && ./prometheus --config.file=prometheus.yml" &


# Start the node_exporter server - datanode1:9100

ssh -i ~/.ssh/key_id  root@192.168.43.109 "systemctl stop firewalld" &
ssh -i ~/.ssh/key_id  root@192.168.43.109 "cd /root/node_exporter-1.8.1.linux-amd64 && ./node_exporter" &

# Start the alertmanager server - alertmanager1:9093

ssh -i ~/.ssh/key_id  root@192.168.43.123  "systemctl stop firewalld" &
ssh -i ~/.ssh/key_id  root@192.168.43.123  "cd /root/alertmanager-0.27.0.linux-amd64 && ./alertmanager" &

# Start the mysql_exporter server - mysqlnode1:9104

ssh -i ~/.ssh/key_id  root@192.168.43.219  "systemctl stop firewalld" &
ssh -i ~/.ssh/key_id  root@192.168.43.219  "cd /root/mysqld_exporter-0.15.1.linux-amd64 && ./mysqld_exporter --config.my-cnf=/etc/mysqld_exporter/.my.cnf" &

# Start the grafana server - localhost:3000

ssh -i ~/.ssh/key_id  root@192.168.43.212 "systemctl stop firewalld" &
ssh -i ~/.ssh/key_id  root@192.168.43.212 "systemctl start grafana-server"


echo https://localhost:9090/ -- prometheus 🖥️
echo https://localhost:3000/ -- grafana 📊
echo https://192.168.43.109:9100/ -- node_exporter datanode 💻
echo https://192.168.43.219:9104/ -- mysql_exporter mysqlnode 💻
echo https://192.168.43.123:9093/ -- alertmanager alertmanager1 ⚠️
