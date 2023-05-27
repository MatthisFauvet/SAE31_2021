<?php
	session_start();
	if(isset($_SESSION['mail']))
	{
		header("location:profilconnect.php");
	}

	else {
		header("location:connexion.php");
	}
	
?>