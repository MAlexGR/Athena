.. _tex.mainpage:

.. highlight:: latex



LaTeX
##########



http://latex.silmaril.ie/formattinginformation/


.. rubric:: Πηγές πληροφόρησης

https://texfaq.org/

https://www.tug.org/begin.html


.. toctree::
   :maxdepth: 1
      
   help
   01Preamble/tex.Preamble
   01Preamble/tex.Conventions
   02FirstSteps/index
   03Introduction/index
   04Basics/index
   Fonts/tex.Fonts
   commands/tex.Commands
   
   

.. raw:: latex
   
   \begin{appendices}
   
   \begin{comment}
   η ακόλουθη εντολή είναι για την επαναρίθμηση του πίνακα
   περιεχομένων, μόνο για τα παραρτήματα. Πιθανώς δε χρειάζεται
   reset γιατί τα παραρτήματα είναι στο τέλος του βιβλίου. Το
   βρήκα στο https://tex.stackexchange.com/questions/172496/adding-appendix-chapters-without-sections-in-table-of-contents

   \end{comment}
   
   \addtocontents{toc}{\protect\setcounter{tocdepth}{0}}


.. toctree::
   :maxdepth: 1
   :caption: Παραρτήματα

   99Appendices/tex.HowItWorks
   99Appendices/tex.CommandList


.. raw:: latex
   
   \end{appendices}

