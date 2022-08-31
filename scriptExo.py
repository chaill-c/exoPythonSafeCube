import json 

tracks = json.loads('''[
    {"data": {"mac1": "E8:BE:81:A1:44:70", "mac2": "D8:07:B6:7F:05:FF", "type": "Wifi", "geoloc": false}, "radius": 97, "is_done": true, "latitude": 48.8112438, "longitude": 2.400947182, "date_reached": "2021-01-20 18:42"}, 
    {"data": {"mac1": "E4:9E:12:77:FB:EB", "mac2": "84:A1:D1:3B:AA:F0", "type": "Wifi", "geoloc": false}, "radius": 6500, "is_done": true, "latitude": 48.81595567993225, "longitude": 2.4114014759409463, "date_reached": "2021-01-20 18:42"}, 
    {"data": {"mac1": "E8:BE:81:A1:44:70", "mac2": "34:27:92:D8:34:B0", "type": "Wifi", "geoloc": false}, "radius": 56, "is_done": true, "latitude": 48.8111453, "longitude": 2.400685438, "date_reached": "2021-01-20 18:45"}, 
    {"data": {"mac1": "E4:9E:12:0F:B4:B5", "mac2": "E4:9E:12:0F:B4:B7", "type": "Wifi", "geoloc": false}, "radius": 62, "is_done": true, "latitude": 48.8110864, "longitude": 2.400727272, "date_reached": "2021-01-20 18:46"}, 
    {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": false}, "radius": 250, "is_done": true, "latitude": 48.8111542, "longitude": 2.400504064, "date_reached": "2021-01-20 19:02"}, 
    {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "84:8A:8D:F4:F8:78", "type": "Wifi", "geoloc": false}, "radius": 61, "is_done": true, "latitude": 48.8120502, "longitude": 2.399715718, "date_reached": "2021-01-20 19:02"}, 
    {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": false}, "radius": 123, "is_done": true, "latitude": 48.8112391, "longitude": 2.400305793, "date_reached": "2021-01-20 19:07"}, 
    {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": false}, "radius": 127, "is_done": true, "latitude": 48.8113913, "longitude": 2.399820891, "date_reached": "2021-01-20 19:08"}, 
    {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": false}, "radius": 126, "is_done": true, "latitude": 48.8113828, "longitude": 2.399827458, "date_reached": "2021-01-20 21:10"}, 
    {"data": {"mac1": "00:1F:C9:FC:F2:50", "mac2": "84:8A:8D:F4:F8:78", "type": "Wifi", "geoloc": false}, "radius": 70, "is_done": true, "latitude": 48.8123243, "longitude": 2.399805473, "date_reached": "2021-01-20 21:10"}, 
    {"data": {"mac1": "00:26:0A:EF:8B:80", "mac2": "00:3A:9A:3F:6F:50", "type": "Wifi", "geoloc": false}, "radius": 48, "is_done": true, "latitude": 48.8127258, "longitude": 2.399676978, "date_reached": "2021-01-20 21:18"}, 
    {"data": {"mac1": "70:01:B5:31:5D:18", "mac2": "64:7C:34:F2:4B:6C", "type": "Wifi", "geoloc": false}, "radius": 49, "is_done": true, "latitude": 48.8127092, "longitude": 2.399718476, "date_reached": "2021-01-20 21:18"}, 
    {"data": {"mac1": "70:01:B5:31:5D:18", "mac2": "00:26:0A:EF:8B:80", "type": "Wifi", "geoloc": false}, "radius": 45, "is_done": true, "latitude": 48.8125931, "longitude": 2.399841137, "date_reached": "2021-01-21 06:09"}, 
    {"data": {"mac1": "00:3A:9A:3F:6F:50", "mac2": "EC:8E:B5:AC:79:8C", "type": "Wifi", "geoloc": false}, "radius": 55, "is_done": true, "latitude": 48.8125821, "longitude": 2.399738258, "date_reached": "2021-01-21 06:09"}, 
    {"data": {"mac1": "34:27:92:47:77:69", "mac2": "34:27:92:47:77:6B", "type": "Wifi", "geoloc": false}, "radius": 72, "is_done": true, "latitude": 48.8129672, "longitude": 2.39961969, "date_reached": "2021-01-21 06:19"}, 
    {"data": {"mac1": "34:27:92:47:77:6A", "mac2": "44:CE:7D:D3:26:56", "type": "Wifi", "geoloc": false}, "radius": 62, "is_done": true, "latitude": 48.8129618, "longitude": 2.400074506, "date_reached": "2021-01-21 06:19"}, 
    {"data": {"mac1": "34:27:92:47:77:6B", "mac2": "34:27:92:47:77:6A", "type": "Wifi", "geoloc": false}, "radius": 69, "is_done": true, "latitude": 48.8129651, "longitude": 2.399579219, "date_reached": "2021-01-21 06:21"}, 
    {"data": {"mac1": "34:27:92:47:77:69", "mac2": "44:CE:7D:D3:26:56", "type": "Wifi", "geoloc": false}, "radius": 61, "is_done": true, "latitude": 48.8129533, "longitude": 2.400144078, "date_reached": "2021-01-21 06:21"}, 
    {"data": {"mac1": "00:3A:9A:1A:C5:D0", "mac2": "68:A3:78:0D:39:BC", "type": "Wifi", "geoloc": false}, "radius": 65, "is_done": true, "latitude": 48.8130416, "longitude": 2.399362081, "date_reached": "2021-01-21 06:41"}, 
    {"data": {"mac1": "94:10:3E:A7:D9:7C", "mac2": "68:A3:78:0D:39:BA", "type": "Wifi", "geoloc": false}, "radius": 82, "is_done": true, "latitude": 48.8131206, "longitude": 2.399266009, "date_reached": "2021-01-21 06:41"}, 
    {"data": {"mac1": "68:A3:78:0D:39:BC", "mac2": "68:A3:78:0D:39:BA", "type": "Wifi", "geoloc": false}, "radius": 70, "is_done": true, "latitude": 48.8131257, "longitude": 2.39933306, "date_reached": "2021-01-21 06:46"}, 
    {"data": {"mac1": "00:3A:9A:1A:C5:D0", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": false}, "radius": 553, "is_done": true, "latitude": 48.812571, "longitude": 2.405984, "date_reached": "2021-01-21 06:46"}, 
    {"data": {"mac1": "34:27:92:42:CB:A3", "mac2": "70:FC:8F:52:25:18", "type": "Wifi", "geoloc": false}, "radius": 60, "is_done": true, "latitude": 48.8124271, "longitude": 2.397505111, "date_reached": "2021-01-21 07:01"}
]''')

