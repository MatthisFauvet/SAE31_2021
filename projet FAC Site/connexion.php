<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
    <head>
        
        <meta http-equiv="content-type" content="text/html"; charset="utf-8" />
        <title>Connexion a votre compte</title>
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
                <li><a href="profil.php">Profil</a></li>
            </ul>
        </nav>

    	<h2 class="titre" align="center">Connectez vous, ou créer votre Espace Personel</h2>
        
        <fieldset class="fieldset-inscr-content">
            <form action="verification.php" method="POST">
                <fieldset class="inscr-box1">
                    <legend>Connexion a mon compte</legend>
                    <h2 class="compte">
                        Adresse E-mail :<br /><input type="text" name="mail" class="cases" placeholder="Entrer le mail" required/><br/>
                        Mot de passe :<br /><input type="password" name="pwd" class="cases" placeholder="Entrer le mot de passe" required/><br/>
                    </h2>

                    <input type="submit" id="submit" name="valider" value="Je me connecte" class="test" size="20px" />

                    <?php
                    if(isset($_GET['erreur'])){
                        $err = $_GET['erreur'];
                        if($err==1 || $err==2) 
                        {
                            echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
                        }
                    }   
                    ?>

                </fieldset>
            </form>


            <form action="inscription.php" method="POST">
                <fieldset>
                    <legend> Je ne possède pas de compte :</legend>
                    <input type="submit" value="J'en creer un !" class="pas_compte" size="20px"/>
                </fieldset>
            </form>
        </fieldset>
    </body>
</html>