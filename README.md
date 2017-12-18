Processo e Sviluppo del Software - Labeling Immagini
======================================================

Assignment progettuale del corso di Processo e Sviluppo del Software.


Prerequisiti
------------

Per avviare il progetto è necessario avere installato python (versione 3.6.3).

### Windows:

Per installare Python su Windows è possibile utilizzare l'installer ottenibile a [questo indirizzo](https://www.python.org/downloads/).

**NB:** Installare anche `pip` in quanto sarà necessario per installare le dipendenze del progetto.


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

In `~/.bashrc` aggiungere:

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Ulteriori informazioni sull'installazione di pyenv [qui](https://github.com/pyenv/pyenv-installer).

##### Installazione python 3.6.3:

Dopo aver installato pyenv, installare python 3.6.3
```
$ pyenv install 3.6.3
```
Nel repository del progetto dovrebbe essere già presente il file `.python-version` che permettere di utilizzare la versione di python corretta. Qualore non fosse presente, utilizzare il comando `pyenv local 3.6.3`.

Installazione
-------------

Installare tutte le dipendenze del progetto (potrebbero essere necessari i privilegi di amministratore):
```
$ pip install -r requirements.txt
```


##### Installare PostgreSQL (DA RIVEDERE):
Scaricare ed installare PostgreSQL a [questo indirizzo](https://www.postgresql.org/download/) e creare un utente con nome `admin` e password `admin`. Per creare l'utente:
```
$ sudo -u postgres createuser <username>

$ sudo -u postgres psql
psql=# alter user <username> with encrypted password '<password>';
```

##### Creare il database (DA RIVEDERE):

```
$ psql
psql=# create database mitalian with owner admin;
```

##### Migrazioni:

Creare ed applicare le migrazioni:
```
$ ./manage.py makemigrations
$ ./manage.py migrate

# In alternativa python manage.py
```

Per creare un utente amministratore:
```
$ ./manage.py createsuperuser
```
Il pannello di amministrazione è raggiungibile alla pagina `/admin`.

##### Avvio:

Avviare il server (raggiungibile a `localhost:8000`):
```
$ ./manage.py runserver
```

Studenti
--------

   * Matteo Colella - 794028
   * Matteo Costantini - 795125
   * Gerosa Dario 793636
