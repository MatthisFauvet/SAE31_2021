<!DOCTYPE html>
<html>
	<head>
	<title>Resultats</title>
        <meta http-equiv="content-type" content="text/html"; charset="utf-8" />
		<link href="style.css" rel="stylesheet" media="all" type="text/css">
	</head>
	<body> 
        </div>
		<div>
			<img src="images/FAC-CorpLOGO.png">
		</div>
		<nav>
	        <ul>
	            <li><a href="index.php">Accueil</a></li>
	            <li><a href="Actualite.html">Acutalité</a></li>
	            <li><a href="nos_jeux.php">Nos Jeux</a></li>
	            <li><a href="resultat.php">Resultats / Scores</a></li>
	            <li><a href="profil.php">Profil</a></li>
	        </ul>
 		</nav>
 		<h2>
 			Ici sont présent, les résultats de tous les joueurs
 		</h2>

 		<?php
		// on se connecte à la base
		$base = new mysqli('localhost', 'root', 'root','projet_fac');
		//commandes SQL d'insertion, valeur 0 pour auto incrémentation

		$sql = 'SELECT id_score, pseudo, score FROM compte JOIN resultats ON compte.mail = resultats.mail_joueur ORDER BY score DESC';	
		// On lance la requête (mysql_query) 
        $req = $base->query($sql); // la flèche fonctionne comme le point en python en POO
		if ($req)  // si la requete passe
		{ 
			echo '<table>
					<tr> 
						<th>id_score</th>
						<th>Pseudo</th>
						<th>Score </th>
					</tr> ';

			while ($data = mysqli_fetch_array($req)) {
				//on scanne les lignes de la liste obtenue
				//avec la requete, chaque colonne est
				//repérée par le nom de la colonne dans la BDD
				echo 
					'<tr>
						<td>'.utf8_encode($data["id_score"]).'</td>
						<td>'.utf8_encode($data["pseudo"]).'</td>
						<td>'.utf8_encode($data["score"]).'</td>
					</tr>'; 
			}
		echo '</table>';
		}
		else //si erreur 
		{
			echo '<p>Erreur SQL !<br />'.$base->error.'</p>';
		} 
		//on ferme la connexion à la base
        mysqli_close ($base);
		
		?>	
 	</body>
</html>