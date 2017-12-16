Processo e Sviluppo del Software - Labeling Immagini
======================================================

Assignment progettuale del corso di Processo e Sviluppo del Software.


Prerequisiti
------------

Per avviare il progetto è necessario avere installato python (versione 3.6.3).

### Windows:

Per installare Python su Windows e' possibile utilizzare l'installer ottenibile a [questo indirizzo](https://www.python.org/downloads/).

**NB:** Installare anche `pip` in quanto sara' necessario per installare le dipendenze del progetto.


### macOS - Linux:

Si consiglia l'uso di `pyenv` per installare una versione pulita ed evitare conflitti con altre versioni installate e/o librerie.

##### Pyenv su macOS:

```
$ brew install pyenv
```

##### Github way:

```
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
$ pyenv update
```

Ulteriori informazioni sull'installazione di pyenv [qui](https://github.com/pyenv/pyenv-installer).

##### Installazione python 3.6.3:

Dopo aver installato pyenv, installare python 3.6.3

```
$ pyenv install 3.6.3
```

Nel repository del progetto dovrebbe essere già presente il file `.python-version` che permettere di utilizzare la versione di python corretta. Qualore non fosse presente utilizzare il comando `pyenv local 3.6.3`.

Installazione
-------------

Installare tutte le dipendenze del progetto:
```
$ pip install -r requirements.txt
```

Creare il database:

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Avviare il server:
```
$ ./manage.py runserver
```

Authors
-------

   * Matteo Colella - 794028
   * Matteo Costantini - 795125
   * Gerosa Dario 793636

