<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
    <head>
        
        <meta http-equiv="content-type" content="text/html"; charset="utf-8" />
        <title>Profil personnel</title>
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
                <li class="bouton_logout"><a href='profilconnect.php?deconnexion=true'><img src="./images/logout.png" class="bouton_logout"></a></li>
            </ul>
        </nav>
        <!-- tester si l'utilisateur est connecté -->
        <div>
        <?php
            session_start(); //On lance une session
            if(isset($_GET['deconnexion'])){ //Si il existe une variable $_GET['deconnxion'] et qu'elle est définie alors
                if($_GET['deconnexion']==true){  
                    session_unset(); //On ferme la session 
                    header("location:profil.php"); // On renvoie sur la page de conexion
                }
            }
            if($_SESSION['mail'] !== "")//si la variable $_SESSION['mail'] n'est pas null
            { 
                $user = $_SESSION['mail'];
                // afficher un message
                $base = new mysqli('localhost', 'root', 'root','projet_fac');
                $sql2 = 'SELECT prenom FROM compte WHERE mail = "'.$user.'"';
                $req2 = $base->query($sql2);
                if($req2)
                {
                    $data = mysqli_fetch_array($req2);
                    echo '<p>Bonjour '.utf8_encode($data['prenom']).', vous êtes désormais connecté!</p>'; 
                }
            }
            else {
                echo '<p>Erreur SQL !<br />'.$base->error.'</p>';
            }
            mysqli_close ($base);
        ?>   
        <div class="boutondl">
            <?php
            // on se connecte à la base
            $base = new mysqli('localhost', 'root', 'root','projet_fac');
            //commandes SQL d'insertion, valeur 0 pour auto incrémentation

            $sql = 'SELECT pseudo, score FROM compte JOIN resultats ON compte.mail = resultats.mail_joueur WHERE mail="'.utf8_encode($_SESSION["mail"]).'"'; 
            // On lance la requête (mysql_query) 
            $req = $base->query($sql); // la flèche fonctionne comme le point en python en POO
            if ($req)  // si la requete passe
            { 
                echo '<fieldset class="score_account"><legend>Score :</legend>';
                while ($data = mysqli_fetch_array($req)) {
                    //on scanne les lignes de la liste obtenue
                    //avec la requete, chaque colonne est
                    //repérée par le nom de la colonne dans la BDD
                    echo 'Bonjour '.utf8_encode($data["pseudo"]).' votre score est de : '.utf8_encode($data["score"]).'pts actuellement.'; 
                }
            echo '</fieldset>';
            }
            else //si erreur 
            {
                echo '<p>Erreur SQL !<br />'.$base->error.'</p>';
            } 
            //on ferme la connexion à la base
            mysqli_close ($base);
            
            ?>  
        </div>
    </body>
</html>