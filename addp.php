<?php

$hostname = "localhost";
$username = "root";
$password = "team11";
$db = "password_storage";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

if(isset($_POST['submit'])) {
  $clientname=$_POST['clientname'];
  $clientpassword=$_POST['clientpassword'];
  

  $query = "INSERT INTO user_password (clientname, clientpassword)
  VALUES ('$clientname', '$clientpassword')";

    if (!mysqli_query($dbconnect, $query)) {
        die('Sorry, we were unable to add your password... Please try again!');
    } else {
      echo "Password has been updated.";
    }

}
?>
