###1) Количество строк

```bash
    cat access.log | wc -l
```
   
  	225133
   
###2) Общее количество запросов по типу

```bash
   awk 'BEGIN {req[1] = "GET"; req[2] = "POST"; req[3] = "PUT"; req[4] = "PATCH"; req[5] = "HEAD"; req[6] = "DELETE"; req[7] = "TRACE"; ans[1] = 0; ans[2] = 0; ans[3] = 0; ans[4] = 0; ans[5] = 0; ans[6] = 0; ans[7] = 0} {for (i = 1; i < 8; i++) {if (index($6, req[i]) != 0) ans[i]+=1}} END{for (i = 1; i < 8; i++) {print req[i] " : " ans[i]}}' access.log
```
Я очень долго разбирался с этими массивами, циклами и писал первый вариант, но через пять минут я придумал тупую и короткую версию
Мне жалко удалять первый, поэтому я оставлю оба)
```bash
    awk '{print $6}' access.log| sort |uniq -c
```

Первый вариант

	GET : 122096
    POST : 102504
    PUT : 6
    PATCH : 0
    HEAD : 528
    DELETE : 0
    TRACE : 0
    
Второй вариант

    1 "g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET
    122095 "GET
    528 "HEAD
    102503 "POST
    6 "PUT
  
###3) Топ 10 самых частых запросов

```bash
   awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -10
```

	103932 /administrator/index.php
	26336 /apache-log/access.log
	6940 /
	4980 /templates/_system/css/general.css
	3199 /robots.txt
	2356 http://almhuette-raith.at/administrator/index.php
	2201 /favicon.ico
	1644 /wp-login.php
	1563 /administrator/
	1287 /templates/jp_hotel/css/template.css

###4) Топ самых больших по размеру запросов с кодом 4XX

```bash
   awk '{if (index($9, "4") == 1) print $7 " " $9 " " $10 " " $1}' access.log | sort -n -k3 -r | uniq -d | head -5
```

	/index.php?option=com_phocagallery&view=category&id=7806&Itemid=53 404 1417 189.217.45.73
    /index.php?option=com_phocagallery&view=category&id=4025&Itemid=53 404 1417 189.217.45.73
    /index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%289168%3D4696%29%20THEN%209168%20ELSE%209168%2A%28SELECT%209168%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53 404 1417 189.217.45.73
    /index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%281753%3D1753%29%20THEN%201753%20ELSE%201753%2A%28SELECT%201753%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53 404 1417 189.217.45.73
    /?view=videos&type=member&user_id=1%20and%201=0%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,concat%280x3c757365723e,username,0x3c757365723e3c706173733e,password,0x3c706173733e%29,14,15,16,17,18,19,20,21,22,23,24,25,26,27%20from+jos_users+where+gid=25+limit+0,1--&option=com_jomtube 404 1397 5.206.77.93

###5) Топ 5 пользователей по количеству запросов с кодом 5XX

```bash
   awk '{if (index($9, "5") == 1) print $1}' access.log  | uniq -c | sort -nr -k1  | awk '{print $2 " " $1}' | head -5
```

	189.217.45.73 225
	82.193.127.15 4
	91.210.145.36 3
	195.133.48.198 2
	194.87.237.6 2
