data = "ERROR connection ERROR failed access"
data = data.replace("ERROR","ALERT")
#я до конца не понял какие предупреждения надо посчитать,но в своем кода я посчитаю количество "ALERT",так как в переводе с английского он идет как "тревога" или же "предупреждение"
count_alerts = data.count("ALERT")
print(data)
print(count_alerts)