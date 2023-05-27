<?php
session_start();
if(isset($_SESSION['mail'])) {
	header("location:https://www.mediafire.com/file/5ecg4tiugiy3wmj/projet_fac_exe_dl.rar/file");
}	
else {
	header("location:connexion.php");
}
?>