<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
    <head>
        
        <meta http-equiv="content-type" content="text/html"; charset="utf-8" />
        <title>Formulaire de saisie utilisateur</title>
    <link href="style.css" rel="stylesheet" media="all" type="text/css">
    </head>
    <body>
        <div>
            <img src="images/FAC-CorpLOGO.png">
        </div>
        <nav>
            <ul>
	            <li><a href="index.php">Accueil</a></li>
	            <li><a href="Actualite.html">Acutalité</a></li>
	            <li><a href="nos_jeux.php">Nos Jeux</a></li>
	            <li><a href="resultat.php">Resultats / Scores</a></li>
	            <li><a href="Profil.php">Profil</a></li>
            </ul>
        </nav>

		<h2 class="titre_inscr"><u>Voici le formulaire d'inscription suite à votre demande de création</u></h2>

		<br>
		
		<form name="inscription" method="post" action="inscription.php">

			<fieldset class="fieldset-inscr-content">
				<fieldset class="inscr-box1">
					<legend> Vos Cordonees </legend>
					Nom : <br> <input type="text" name="nom" class="cases"> <br>
					Prenom : <br> <input type="text" name="prenom" class="cases"><br>
					Mail : <br> <input type="texte" name="mail" class="cases"><br>
					Mot de passe : <br> <input type="text" name="mdp1" class="cases"><br>
					Mot de passe - Vérif : <br> <input type="text" name="mdp2" class="cases"><br>
					Pays : <br> <input type="text" name="pays" class="cases"><br>
					Ville : <br> <input type="text" name="ville" class="cases"><br>
				</fieldset>
				<fieldset class="inscr-box3">
					<fieldset class="inscr-box2">	
						<legend> Votre Visibilitée : </legend>
						Pseudo : <br> <input type="text" name="pseudo"  class="cases"/><br>
					</fieldset>
					<input type="submit" name="valider" value="Inscription" class="pas_compte2" />
				</fieldset>
			</fieldset>
		</form>

		<?php
		$base = new mysqli('localhost', 'root', 'root','projet_fac');

		if (isset ($_POST['valider'])) {
			//on récupère les valeurs entrées par l'utilisateur
			$nom=$_POST['nom'];
			$prenom=$_POST['prenom'];
			$mail=$_POST['mail'];
			$mdp=$_POST['mdp1'];
			$mdp2=$_POST['mdp2'];
			$pays=$_POST['pays'];
			$ville=$_POST['ville'];
			$pseudo=$_POST['pseudo'];

			if ($_POST['mdp1'] != $_POST['mdp2']) // On test les mdp pour voir si ils sont différent
			{ 
				$erreur = "les deux mots de passes sont différents ! ";
				echo $erreur; exit();
			}

			//commandes SQL d'insertion, valeur 0 pour auto incrémentation
			$sql = 'INSERT INTO compte VALUES("'.utf8_encode($mail).'","'.utf8_encode($nom).'","'.utf8_encode($prenom).'","'.utf8_encode($pays).'","'.utf8_encode($ville).'","'.utf8_encode($pseudo).'","'.utf8_encode($mdp).'")';
			// On lance la requête (mysql_query) 
	        $req = $base->query($sql); // la flèche fonctionne comme le point en python en POO
			if (!$req)   // si la requete a envoyé une erreur
			{echo '<p>Erreur SQL !<br />'.$base->error.'</p>';}

			header('location:index.php');
        }

		//on ferme la connexion à la base
        mysqli_close ($base);

		?>	
    </body>
</html>