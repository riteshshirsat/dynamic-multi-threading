<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);

echo "start inserting....</br>";
sleep(3);

echo "start multi-threading....</br>";


$id="123";
$data_city='mumbai';
$threadProcess = shell_exec("python3.9 billprocess.py $id $data_city");

print_r($threadProcess);

$result = json_decode($threadProcess, true);
echo "errorcode:".$result['errorcode']."</br>";
echo "errorcode:".$result['status']."</br>";

if($result['errorcode'] == 0 and $result['status'] == "success"){
    echo "start further process";
}else{
    echo "fail";
}
