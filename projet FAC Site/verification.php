<?php
session_start();
if(isset($_POST['mail']) and isset($_POST['pwd']))
{
    // connexion à la base de données
    $base = new mysqli('localhost', 'root', 'root','projet_fac');
    
    // on applique les deux fonctions mysqli_real_escape_string et htmlspecialchars
    // pour éliminer toute attaque de type injection SQL et XSS
    $mail = mysqli_real_escape_string($base,htmlspecialchars($_POST['mail'])); 
    $pwd = mysqli_real_escape_string($base,htmlspecialchars($_POST['pwd']));

    // Si les deux infos de sont pas vides 
    if($mail !== "" && $pwd !== "")
    {
        $requete = "SELECT count(*) FROM compte WHERE mail = '".$mail."' and mdp = '".$pwd."' ";
        $exec_requete = mysqli_query($base,$requete);
        $reponse      = mysqli_fetch_array($exec_requete);
        $count = $reponse['count(*)'];
        if($count!=0) // nom d'utilisateur et mot de passe correctes
        {
            $_SESSION['mail'] = $mail;
            header('Location: profilconnect.php');
        }
        else
        {
           header('Location: profil.php'); // utilisateur ou mot de passe incorrect
           echo "Mail ou mot de passe invalide";
        }
    }
    else
    {
       header('Location: profil.php'); // utilisateur ou mot de passe vide
       echo "Une case n'a pas été complété";
    }
}
else
{
   header('Location:profil.php');
}
mysqli_close($base); // fermer la connexion
?>