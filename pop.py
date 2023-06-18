import requests
url = "https://mcv-pro.herokuapp.com/api/car-detail/2"

payload={'car_id': '2',
'car_speed': '110',
'car_rpm': '4',
'car_begin_distance': '187789',
'car_distance': '33',
'car_run_time': '50',
'car_tempreture': '30',
'car_fuel_level': '8',
'car_engine_load': '70'}
files=[

]
headers = {
  'Authorization': 'Token 6354124dffe47ee221e276d63481fcc6e7877fe5'
}

response = requests.request("PUT", url, headers=headers, data=payload, files=files)

print(response.text)



int x , y;
cout<<"enter x , y : ";
cin>> x >> y;

if(y == 0){
  cerr<<"Invalid Value";
}




