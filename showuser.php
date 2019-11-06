<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>
<?php

$hostname = "localhost";
$username = "root";
$password = "team11";
$db = "password_storage";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

?>

<table border="1" align="center">
<tr>
  <td>id</td>
  <td>Client Name</td>
  <td>Password</td>
</tr>

<?php

$query = mysqli_query($dbconnect, "SELECT *  FROM user_password")
   or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  echo
   "<tr>
    <td>{$row['id']}</td>
    <td>{$row['clientname']}</td>
    <td>{$row['clientpassword']}</td>
   </tr>\n";

}

?>
</table>
</body>
</html>
