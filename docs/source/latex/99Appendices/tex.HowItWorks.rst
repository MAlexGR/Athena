


Πως Λειτουργεί η LaTeX
========================

Ίσως είναι λίγο ριψοκίνδυνο να https://tex.stackexchange.com/questions/104023/what-is-a-token

Strictly speaking, LaTeX is a set of macros built on top of the TeX program originally developed by Donald Knuth [Knu86, Knu84] in the early 1980’s. TeX is undoubtedly one of the most robust computer programs to date.

Leslie Lamport says that most TeX commands can be used with LaTeX and lists those that cannot be used [Lam94, Appendix E]. Apart from this he says nothing about any TeX commands. I have used some TeX macros in the code examples and so I need to talk a little bit about these.

I like to think of the commands and macros as falling into one of several groups.

\begin{description}\tightlist
    \item[TeX primitives] Είναι οι βασικές, θεμελιώδεις κατασκευές που αναγνωρίζονται από το πρόγραμμα \TeX. Δεν είναι εντολές με την κοινή έννοια αλλά κατασκευές με τις οποίες δημιουργούνται εντολές.
  
    \item[TeX commands or macros] Οι εντολές του \TeX\ είναι κατασκευές που βασίζονται σε \TeX\ primitives. Οι μακροεντολές του \TeX\ είναι κατασκευές που βασίζονται είτε σε εντολές, είτε σε primitives του \TeX, είτε και στα δύο.
 
    \item[LaTeX kernel commands or macros] Είναι νέες εντολές που εισήγαγε η \LaTeX\ που βασίζονται σε primitives και εντολές του \TeX. Αυτές ορίζονται στον πυρήνα (kernel) της \LaTeX. Κάποιες από αυτές στην ουσία επαναπροσδιορίζουν τις εντολές του \TeX. Οι μακροεντολές τώρα είναι συνδυασμοί εντολών ώστε να παράγουν πιο σύνθετα αποτελέσματα. Αυτές είναι κατά βάση οι εντολές και μακροεντολές που μας ενδιαφέρουν.
  
    \item[Class command] Είναι νέες εντολές που ορίζονται σε μία κλάση εγγράφου. Τις εντολές αυτές προσδιόρισε με μοναδικό τρόπο, ο συγγραφέας της κλάσης. Οι  και οι οποίες βασίζονται, κυρίως, σε εντολές και μακροεντολές της \LaTeX\ και πιθανώς σε εντολές \TeX.
  
  \item[Package commands] Ισχύει ότι και παραπάνω και επιπλέον είναι σπάνιο να περιλαμβάνουν εντολές \TeX\ (βασίζονται εξολοκλήρου στη \LaTeX).
  
  \item[User commands] Typically these are limited to the commands provided by the class and any packages that might be called for, but more experienced users will employ some kernel commands, like newcommand, to make their authoring more efficient.
  
\end{description}

• TeX primitives. These are the basic constructs of the TeX language.
• TeX commands or macros. These are part of the plain TeX system and are constructed
from the TeX primitives.
• LaTeX kernel commands or macros. These are defined in the LaTeX kernel and
are based on plain TeX primitives or commands. In turn, some higher level kernel macros are constructed from more basic aspects of the kernel. The kernel does
redefine some of the plain TeX commands.
• Class command. These are mainly built up on the kernel commands but may use
some basic TeX.
• Package commands. These are similar to the class commands but are less likely to
directly use TeX macros.
• User commands. Typically these are limited to the commands provided by the class and any packages that might be called for, but more experienced users will employ some kernel commands, like \verb|\newcommand|, to make their authoring more efficient.

Although TeX is designed as a language for typesetting it is also a ‘Turing complete’ language which means that it can perform any function that can be programmed in any familiar programming language. For example, an interpreter for the BASIC language has been written in TeX, but writing this kind of program using TeX is something that only an expert1 might consider.

Nevertheless, you may have to, or wish to, write a typesetting function of your own. This chapter presents a few of the programming aspects that you may need for this, such as performing some simple arithmetic or comparing two lengths. For anything else you will have to read one or more of the TeX books or tutorials.

In England witnesses at a trial have to swear to ‘Tell the truth, the whole truth, and nothing but the truth’. I will try and tell the truth about TeX but, to misquote Hamlet

There are more things in heaven and TeX, Horatio,
Than are dreamt of in your philosophy

\section{THE TEX PROCESS}
As we are delving deeper than normal and because at the bottom it is the TeX language that does all the work, it is useful to have an idea of how TeX processes a source file to produce a dvi file. It is all explained in detail by Knuth [Knu84] and also perhaps more accessibly by Eijkhout [Eij92]; the following is a simplified description. Basically there are four processes involved and the output from one process is the input to the following one.

\begin{description}
    \item[Input] The input process, which Knuth terms the ‘eyes’, reads the source file and converts what it sees into tokens. There are essentially two kinds of token. A token is either a single character such as a letter or a digit or a punctuation mark, or a token is a control sequence. A control sequence consists of a backslash and either all the alphabetic characters immediately following it, or the single non-alphabetic following it. Control sequence is the general term for what I have been calling a macro or a command.
    
    \item[Expansion] The expansion processor is what Knuth calls ‘TeX’s mouth’. In this process some of the tokens from the input processor are expanded. Expansion replaces a token by other tokens or sometimes by no token. The expandible tokens include macros, conditionals, and a number of TeX primitives.
    
    \item[Execution] The execution process is TeX’s ‘stomach’. This handles all the tokens output by the expansion processor. Control sequences that are not expandible are termed executable, and the execution processor executes the executable tokens. Character tokens are neither expandible nor executable. It handles any macro defintions and also builds horizontal, vertical and mathematical lists.
    
    \item[Layout] The layout processor (TeX’s ‘bowels’) breaks horizontal lists into paragraphs, mathematical lists into formulae, and vertical lists into pages. The final output is the dvi file.
\end{description}
 
 
 
 
In spite of the sequential nature implied by this description the overall process includes some feedback from a later process to an earlier one which may affect what that does.

It is probably the expansion processor that needs to be best understood. Its input is a sequence of tokens from the input processor and its output is a sequence of different tokens. In outline, the expansion processor takes each input token in turn and sees if it is expandible; if it is not it simply passes it on to the output. If the token is expandible then it is replaced by its expansion. The most common expandible tokens are control sequences that have been defined as macros. If the macro takes no arguments then the macro’s name is replaced by its definition. If the macro takes arguments, sufficient tokens are collected
to get the values of the arguments, and then the macro name is replaced by the definition. The expansion processor then looks at the first token in the replacement, and if that is expandible it expands that, and so on.

Nominally, the eventual output from the expansion processor is a stream of nonexpandible tokens. There are ways, however of controlling whether or not the expansion processor will actually expand an expandible token, and to control the order in which things get expanded, but that is where things get rapidly complicated.

The layout processor works something like this. Ignoring maths, TeX stores what you type in two kinds of lists, vertical and horizontal. As it reads your words it puts them one after another in a horizontal list. At the end of a paragraph it stops the horizontal list and adds it to the vertical list. At the beginning of the next paragraph it starts a new horizontal list and adds the paragraph’s words to it. And so on. This results in a vertical list of horizontal lists of words, where each horizontal list contains the words of a paragraph. It then goes through each horizontal list in turn, breaking it up into shorter horizontal lists, one for each line in the paragraph. These are put into another vertical list, so conceptually there is a vertical list of paragraphs, and each paragraph is a vertical list of lines, and each line is a horizontal list of words, or alternatively one vertical list of lines. Lastly it chops up the vertical list of lines into page sized chunks and outputs them a page at a
time.

TeX is designed to handle arbitrary sized inserts, like those for maths, tables, sectional divisions and so forth, in an elegant manner. It does this by allowing vertical spaces on a page to stretch and shrink a little so that the actual height of the typeblock is constant. If a page consists only of text with no widow or orphan then the vertical spacing is regular, otherwise it is likely to vary to some extent. Generally speaking, TeX is not designed to typeset on a fixed grid, but against this other systems are not designed to produce high quality typeset mathematics. Attempts have been made to tweak LaTeX to typeset on a fixed grid but as far as I know nobody has been completely successful.

TeX works somewhat more efficiently than I have described. Instead of reading the whole document before breaking paragraphs into lines, it does the line breaking at the end of each paragraph. After each paragraph it checks to see if it has enough material for a page, and outputs a page whenever it is full. However, TeX is also a bit lazy. Once it has broken a paragraph into lines it never looks at the paragraph again, except perhaps to split it at a page break. If you want to change, say, the width of the typeblock on a particular page, any paragraph that spills over from a previous page will not be reset to match the new measure. This asynchronous page breaking also has an unfortunate effect if you are trying to put a note in say, the outside margin, as the outside is unknown until after the paragraph has been set, and so the note may end up in the wrong margin.

\section{LATEX FILES}

The aux file is the way LaTeX transfers information from one run to the next and the process works roughly like this.

\begin{itemize}
    \item The aux file is read at the start of the document environment. If \verb|\nofiles| has not been specified a new empty aux file is then created which has the side effect of destroying the original aux file.

    \item Within the document environment there may be macros that write information to the aux file, such as the sectioning or captioning commands. However, these macros will not write their information if \verb|\nofiles| has been specified.
    
    \item At the end of the document environment the contents of the aux file are read.
\end{itemize}

Under normal circumstances new output files are produced each time LaTeX is run, but when \verb|\nofiles| is specified only the dvi and log files will be new — any other files are unchanged.

In the case of the sectioning commands these write macros into the aux file that in turn write information into a toc file, and the \verb|\tableofcontents| command reads the toc file which contains the information for the Table of Contents. To make this a bit more concrete, as LaTeX processes a new document through the first two runs, the following events occur

\begin{enumerate}
    \item Initially there is neither an aux nor a toc file. At the start of the document environment a new empty aux file is created.
    
    \item During the first run the \verb|\tableofcontents| typesets the Contents heading and creates a new empty toc file.
    
    During the run sectional commands write information into the new aux file. At the end of the document environment the aux file is read. Contents information in the aux file is written to the toc file. Lastly all the output files are closed.
    
    \item For the second run the aux file from the previous run is read at the start of the document environment; no information can be written to a toc file because the toc file is only made available by the \verb|\tableofcontents| command. The aux file from the previous run is closed and the new one for this run is created.
    
    This time the \verb|\tableofcontents| reads toc file that was created during the previous run which contains the typesetting instructions for the contents, and then starts a new toc file.
    
    And so the process repeats itself.
\end{enumerate}

The aux file mechanism means that, except for the simplest of documents, LaTeX has to be run at least twice in order to have all the information to hand for typesetting. If sections are added or deleted, two runs are necessary afterwards to ensure that everything is up to date. Sometimes three, or even more, runs are necessary to guarantee that things are settled.

\section{SYNTAX}

The LaTeX syntax that you normally see is pretty regular. Mandatory arguments are enclosed in curly braces and optional arguments are enclosed in square brackets. One exception to this rule is in the picture environment where coordinate and direction pairs are enclosed in parentheses.

The TeX syntax is not regular in the above sense. For example, if in LaTeX you said 

\begin{verbatim}
\newcommand*{\cmd}[2]{#1 is no. #2 of}
\cmd{M}{13} the alphabet. % prints: M is no. 13 of the alphabet
\end{verbatim}

Then in TeX you would say

\begin{verbatim}
\def\cmd#1#2{#1 is no. #2 of}
\end{verbatim}

and you could then use either of the following calls:

\begin{verbatim}
\cmd M{13} the alphabet. % prints: M is no. 13 of the alphabet
\cmd{M}{13} the alphabet. % prints: M is no. 13 of the alphabet
\end{verbatim}

A simplistic explanation of the first TeX call of \cmd is as follows. A control sequence starts with a backslash, followed by either a single character, or one or more of what TeX thinks of as letters (normally the 52 lower- and upper-case alphabetic characters); a space or any non-letter, therefore, ends a multiletter control sequence. TeX and LaTeX discard any spaces after a macro name. If the macro takes any arguments, and \verb|\cmd| takes two, TeX will then start looking for the first argument. An argument is either something enclosed in braces or a single token. In the example the first token is the character ‘M’, so that is the value of the first argument. TeX then looks for the second argument, which is the ‘13’ enclosed in the braces. In the second example, both arguments are enclosed in braces. Here are some TeX variations.

\begin{verbatim}
\cmd B{2} the alphabet. % prints: B is no. 2 of the alphabet.
\cmd B2 the alphabet. % prints: B is no. 2 of the alphabet.
\cmd N14 the alphabet. % prints: N is no. 1 of4 the alphabet.
\end{verbatim}

The result of \verb|\cmd B{2}| is as expected. The results of \verb|\cmd B2| and \verb|\cmd N14| should also be expected, and if not take a moment to ponder why. The ‘B’ and ’N’ are the first arguments to \verb|\cmd| in the two cases because a single character is a token. Having found the first argument TeX looks for the second one, which again will be a token as there are no braces. It will find ‘2’ and ‘1’ as the second arguments and will then expand the \verb|\cmd| macro. In the case of \verb|\cmd B2| this gives a reasonable result. In the case of \verb|\cmd N14|, TeX expands \verb|\cmd N1| to produce ‘N is in position 1 of’, then continues printing the rest of the text, which is ‘4 the alphabet’, hence the odd looking result.

\section{(LA)TEX COMMANDS}

I have used some TeX commands in the example code and it is now time to describe these. Only enough explanation is given to cover my use of them. Full explanations would require a doubling in the size of the book and a concomitant increase in the price, so for full details consult the TeXbook which is the definitive source, or one of the TeX manuals listed in the Bibliography. I find TeX by Topic particularly helpful.

I have also used LaTeX commands that are not mentioned by Lamport. LaTeX uses a convention for command names; any name that includes the @ character is an ‘internal’ command and may be subject to change, or even deletion. Normal commands are meant to be stable — the code implementing them may change but their effect will remain unaltered. In the LaTeX kernel, and in class and package files the character @ is automatically treated as a letter so it may be used as part of a command name. Anywhere else you have to use \verb|\makeatletter| to make @ be treated as a letter and \verb|\makeatother| to make @ revert to its other meaning. So, if you are defining or modifying or directly using any command that includes an @ sign then this must be done in either a ``.sty'' file or if in the document itself it must be surrounded by \verb|\makeatletter| and \verb|\makeatother|.

The implication is ‘don’t use internal commands as they may be dangerous’. Climbing rocks is also dangerous but there are rock climbers; the live ones though don’t try climbing Half Dome in Yosemite or the North Face of the Eiger without having first gained experience on friendlier rocks.

The LaTeX kernel is full of internal commands and a few are mentioned in Lamport. There is no place where you can go to get explanations of all the LaTeX commands, but if you run LaTeX on the source2e.tex file which is in the standard LaTeX distribution you will get the commented kernel code. The index of the commands runs to about 40 double column pages. Each class and package introduce new commands over and above those in the kernel. LaTeX includes \verb|\newcommand|, \verb|\providecommand| and \verb|\renewcommand| as means of (re-)defining a command, but TeX provides only one method.




