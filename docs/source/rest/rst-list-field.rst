.. _rest-field-list-ref:

Λίστες Πεδίων (Field Lists)
-----------------------------------

Οι *λίστες ορισμών* χρησιμοποιούνται όταν τα αντικείμενα που θέλουμε να αναδείξουμε είναι κάποιες διευκρινήσεις ή οι ορισμοί κάποιων όρων. Παραδείγματα είναι όταν θέλουμε να περιγράψουμε τα βήματα μίας διαδικασίας ή να δημιουργήσουμε ένα επεξηγηματικό λεξικό όρων.

Ένα αντικείμενο μίας λίστας ορισμών αποτελείται από έναν όρο και έναν ορισμό. Πρώτα γράφουμε τον όρο (χωρίς καμία εσοχή ως προς το τρέχον κείμενο) και στην επόμενη γραμμή ή μετά από μία κενή γραμμή (προαιρετικά), τον ορισμό. Σε κάθε περίπτωση ο ορισμός πρέπει να ξεκινάει με ένα **τουλάχιστο** κενό εσοχή, σε σχέση με τον όρο (δες το παράδειγμα που ακολουθεί).

Μετά τον όρο μπορούμε (προαιρετικά) να εισάγουμε και επιπλέον *ταξινομητές* (identifiers), αν θέλουμε να προσθέσουμε και επιπλέον όρους. Αυτό γίνεται εισάγωντας το σύμβολο ``:`` μετά τον όρο. Συγκεκριμένα ακολουθθούμε τη σύνταξη: *όρος*, *κενό*, *άνω κάτω τελεία*, *κενό* *ταξινομητής*. Με τον ίδιο τρόπο μπορούμε να εισάγουμε και επιπλέον ταξινομητές (δες το παράδειγμα που ακολουθεί).

Κενές γραμμές πριν και μετά τη λίστα, είναι υποχρεωτικές. Δεν είναι υποχρεωτικές μεταξύ των αντικειμένων της λίστας.

Ένα αντικείμενο της λίστας μπορεί να εκτείνεται σε περισσότερες από μία παραγράφους ή/και να περιλαμβάνει και άλλες λίστες. Οι μόνοι περιορισμοί είναι η τήρηση των εσοχών και οι κανόνες εισαγωγής της αντίστοιχης λίστας. Το σημείο στο οποίο ξεκινάει το περιεχόμενο του πρώτου αντικειμένου, καθορίζει τις μετέπειτα στοιχίσεις.

Ακολουθεί ένα παράδειγμα::

  Πρώτος όρος
    Παράγραφος με την επεξήγηση του όρου.

  Δεύτερος όρος
    Παράγραφος με την επεξήγηση του όρου.

    Η επεξήγηση μπορεί να επεκτείνεται και σε άλλες παραγράφους.

  Ερμηνεία : *Γραμματική*
    Λεκτική σημασία, το τι σημαίνει μία λέξη. Προσωπική εκτίμηση
    γεγονότων, υποκειμενική ανάγνωση δεδομένων και εξαγωγή
    συμπερασμάτων

  Ερμηνεία : *Γενικά* : *Τέχνες*
    Καλλιτεχνική απόδοση.

-----

*Αποτέλεσμα*:

Πρώτος όρος
  Παράγραφος με την επεξήγηση του όρου.

Δεύτερος όρος
  Παράγραφος με την επεξήγηση του όρου.

  Η επεξήγηση μπορεί να επεκτείνεται και σε άλλες παραγράφους.

Ερμηνεία : *Γραμματική*
  Λεκτική σημασία, το τι σημαίνει μία λέξη. Προσωπική εκτίμηση
  γεγονότων, υποκειμενική ανάγνωση δεδομένων και εξαγωγή συμπερασμάτων

Ερμηνεία : *Γενικά* : *Τέχνες*
  Καλλιτεχνική απόδοση.

-----





Παραδείγματα
--------------

Στη συνέχεια ακολουθεί ένα αναλυτικό και σύνθετο παράδειγμα λίστας. Μπορείτε να αντιγράψετε τον κώδικα και να τον επεξεργαστείτε μόνοι σας.

.. code-block:: none

  Αυτή είναι μία συνηθισμένη παράγραφος που τη γράφουμε εδώ για 
  λόγους παρουσίασης. Αμέσως μετά ακολουθεί μία σύνθετη λίστα.

  #. Η βασική λίστα ακολουθεί αυτόματη αρίθμηση (με το σύμβολο ``#.``)

  #. Αυτό είναι το δεύτερο αντικείμενο της λίστας. Περιλαμβάνει μία
     ενσωματωμένη λίστα με κουκίδες.

     + Ένα

     + Δύο

     + Τρία

  #. Αυτό είναι το τρίτο αντικείμενο της αρχικής λίστας.
     Αναπτύσσεται σε τρεις παραγράφους από τις οπόιες η δεύτερη
     περιέχει και μία λίστα ορισμών.

     Αυτή είναι η δεύτερη παράγραφος του τρίτου αντικειμένου. Εδώ
     θα ενσωματώσουμε και μία λίστα ορισμών

     Όρος πρώτος
      Η επεξήγηση του πρώτου όρου.

     Όρος δεύτερος : με έναν προσδιοριστή
      Η επεξήγηση του δεύτερου όρου.

     Όρος τρίτος : με έναν προσδιοριστή : και έναν ακόμη
      Η επεξήγηση του τρίτου όρου.

    Αυτή είναι η τρίτη παράγραφος του τρίτου αντικειμένου.

  #. Αυτό είναι το τέταρτο αντικείμενο της αρχικής λίστας.
     Περιλαμβάνει τρεις ενσωματωμένες (nested) λίστες. Παρατηρήστε
     τη διάρθρωση στον κώδικα, παράλληλα με το αποτέλεσμα (φαίνεται
     στη συνέχεια).

     * Ένα.

     * Δύο. Εδώ εισάγουμε μία ακόμη αριθμητική λίστα.

       (I) One.

       (II) Two. Εδώ εισάγουμε και μία λίστα ορισμών

            Όρος πρώτος
             Η επεξήγηση του πρώτου όρου.

            Όρος δεύτερος : με έναν προσδιοριστή
             Η επεξήγηση του δεύτερου όρου. Εδώ θα εισάγουμε
             επιπλέον και έναν πίνακα.

              =====  =====  ======
                 Inputs     Output
              ------------  ------
                A      B    A or B
              =====  =====  ======
              False  False  False
              True   False  True
              False  True   True
              True   True   True
              =====  =====  ======

            Όρος τρίτος : με έναν προσδιοριστή : και έναν ακόμη
             Η επεξήγηση του τρίτου όρου.

       (III) Three.

     * Τρία.

   #. Αυτό είναι το πέμπτο και τελευταίο αντικείμενο της αρχικής
      λίστας. Ελπίζουμε να καταλάβατε το πως προσθέτουμε αυθαίρετα
      υλικό. Πάντα να προσέχετε τις στοιχίσεις.

   Αυτή είναι μία συνηθισμένη παράγραφος που τη γράφουμε εδώ για να
   δείξουμε πως συνεχίζεται το τρέχον κείμενο μετά από μία λίστα.

-------

*Αποτέλεσμα*:

Αυτή είναι μία συνηθισμένη παράγραφος που τη γράφουμε εδώ για λόγους παρουσίασης. Αμέσως μετά ακολουθεί μία σύνθετη λίστα.

#. Η βασική λίστα ακολουθεί αυτόματη αρίθμηση (με το σύμβολο ``#.``)

#. Αυτό είναι το δεύτερο αντικείμενο της λίστας. Περιλαμβάνει μία ενσωματωμένη λίστα με
   κουκίδες.

   + Ένα

   + Δύο

   + Τρία

#. Αυτό είναι το τρίτο αντικείμενο της αρχικής λίστας. Αναπτύσσεται σε τρεις παραγράφους από
   τις οπόιες η δεύτερη περιέχει και μία λίστα ορισμών.

   Αυτή είναι η δεύτερη παράγραφος του τρίτου αντικειμένου. Εδώ θα ενσωματώσουμε και μία λίστα ορισμών

   Όρος πρώτος
     Η επεξήγηση του πρώτου όρου.

   Όρος δεύτερος : με έναν προσδιοριστή
     Η επεξήγηση του δεύτερου όρου.

   Όρος τρίτος : με έναν προσδιοριστή : και έναν ακόμη
     Η επεξήγηση του τρίτου όρου.

   Αυτή είναι η τρίτη παράγραφος του τρίτου αντικειμένου.

#. Αυτό είναι το τέταρτο αντικείμενο της αρχικής λίστας. Περιλαμβάνει τρεις ενσωματωμένες (nested)
   λίστες. Παρατηρήστε τη διάρθρωση στον κώδικα, παράλληλα με το αποτέλεσμα (φαίνεται στη συνέχεια).
   
   * Ένα.

   * Δύο. Εδώ εισάγουμε μία ακόμη αριθμητική λίστα.
     
     (I) One.
     
     (II) Two. Εδώ εισάγουμε και μία λίστα ορισμών
         
          Όρος πρώτος
            Η επεξήγηση του πρώτου όρου.

          Όρος δεύτερος : με έναν προσδιοριστή
            Η επεξήγηση του δεύτερου όρου. Εδώ θα εισάγουμε επιπλέον και έναν πίνακα.

            =====  =====  ======
               Inputs     Output
            ------------  ------
              A      B    A or B
            =====  =====  ======
            False  False  False
            True   False  True
            False  True   True
            True   True   True
            =====  =====  ======

          Όρος τρίτος : με έναν προσδιοριστή : και έναν ακόμη
            Η επεξήγηση του τρίτου όρου.

     (III) Three.

   * Τρία.
     
#. Αυτό είναι το πέμπτο και τελευταίο αντικείμενο της αρχικής λίστας. Ελπίζουμε να καταλάβατε 
   το πως προσθέτουμε αυθαίρετα υλικό. Πάντα να προσέχετε τις στοιχίσεις.

Αυτή είναι μία συνηθισμένη παράγραφος που τη γράφουμε εδώ για να δείξουμε πως συνεχίζεται το τρέχον κείμενο μετά από μία λίστα.

-------

.. important::
  Αν αντιμετωπίσετε προβλήματα στην επεξεργασία ή τα αποτελέσματα δεν είναι τα αναμενόμενα, ελέγξτε καταρχάς τις στοιχίσεις (εσοχές). Ακόμη και ένα space να έχετε κάνει λάθος, λάθος αποτέλεσμα θα πάρετε. Αν συνεχίζετε να έχετε πρόβλημα, προσπαθήστε να αφήνετε ή όχι κενές γραμμές μεταξύ των αντικειμένων. Αν και πάλι έχετε πρόβλημα, αντιγράψτε τον κώδικα μίας λειτουργικής λίστας (όπως η παραπάνω), ελέγξτε ότι λειτουργεί και σε εσάς και στη συνέχεια προσαρμόστε τη στις ανάγκες σας. Το επόμενο βήμα (αποτυχίας) σημαίνει να ψάξετε για σχετική βοήθεια στο δίκτυο.

