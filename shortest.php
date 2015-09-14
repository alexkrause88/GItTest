<?php 
error_reporting(E_ALL); 
ini_set('display_errors', '1');
$routes = array(
	'Elevator'=>array('3050'=>10, '3020'=>10),
	'3050'=>array('3100'=>10, 'Elevator'=>10, '3070'=>15),
	'3070'=>array('3050'=>10, '3075'=>10),
	'3075'=>array('3070'=>10, '3080'=>10),
	'3080'=>array('3075'=>10, '3090'=>10),
	'3090'=>array('3080'=>10, '3100'=>10),
	'3100'=>array('3090'=>10, '3005'=>10, '3050'=>15),
	'3005'=>array('3100'=>10, '3010'=>10),
	'3010'=>array('3005'=>10, '3015'=>10),
	'3015'=>array('3010'=>10, '3020'=>10),
	'3020'=>array('Elevator'=>10, '3015'=>10),
);
$shortest = 1000000000000000000000000000; $shortestTemp = 0; $shortestRoute = array(); $shortestTempRoute = array(); 
$currentIteration = 0; $beginning = ''; 
$anotherTemp = array(); $anotherArray = array();
$keys = array();
function shortest($start, $finish, $array){
	global $currentIteration;
	global $anotherArray;
	global $shortestTempRoute;
	global $shortestRoute;
	global $shortestTemp;
	global $shortest;
	global $routes;
	global $anotherTemp;
	global $beginning;
	global $keys;
	$anotherTemp[$start] = $routes[$start];
	$keys[] = $start;
	$now = 1;
	if($currentIteration == 0){
		$beginning = $start;
		$shortestTempRoute[] = $beginning;
	}
	$thisTotal = 0;
	foreach($array as $key => $value){
		$currentIteration++;
		$thisTotal = $thisTotal + $value;
		if($key == $finish || $key == $beginning){
			$keys[] = $key;
			$shortestTempRoute[] = $key;
			$shortestTemp = $shortestTemp+$value;
			if($shortestTemp < $shortest){
				$shortest = $shortestTemp;
				$shortestRoute[] = $shortestTempRoute;
			}
			unset($shortestTempRoute[$key]);
		} else {
			$shortestTemp = $shortestTemp + $value;
			$shortestTempRoute[] = $key;
			$currentArray = $routes[$key];
			unset($currentArray[$start]);
			if((in_array($beginning, $currentArray) || in_array($finish, $currentArray)) && count($currentArray) == 1){
				unset($shortestTempRoute[$key]);
			}
			shortest($key, $finish, $currentArray);
		}
	}
	$shortestTemp = $shortestTemp - $thisTotal;
}
shortest('3020', '3090', $routes['3020']);
print_r($shortest);
print_r($shortestRoute);
