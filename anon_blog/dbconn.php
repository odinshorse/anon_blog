

<?php
$dbhost = 'localhost';
$dbuser = 'pabstsmear';
$dbpass = 'Silverrocket1';

$conn = mysql_connect($dbhost, $dbuser, $dbpass) or die('Error connecting to mysql');

$dbname = 'anonblog';
mysql_select_db($dbname);
?>

