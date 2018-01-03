Processo e Sviluppo del Software - Labelling Immagini
====================================================

Assignment progettuale del corso di Processo e Sviluppo del Software.

Indice
------
  * [Prerequisiti](#prerequisiti)
     * [Python:](#python)
     * [PostgreSQL:](#postgresql)
  * [Installazione e Avvio](#installazione-e-avvio)
  * [Studenti](#studenti)

Prerequisiti
------------

Per avviare il progetto è necessario avere installato Python (versione 3.6.3) e PostgreSQL 10.

### Python:

#### Windows:

Per installare Python su Windows è possibile utilizzare l'installer ottenibile a [questo indirizzo](https://www.python.org/downloads/).

**NB:** Installare anche `pip` in quanto sarà necessario per installare le dipendenze del progetto.


#### macOS - Linux:

Si consiglia l'uso di `pyenv` per installare una versione pulita ed evitare conflitti con altre versioni installate e/o librerie.

##### macOS:

```
$ brew install pyenv
```

##### Linux:

```
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

In `~/.bashrc` aggiungere:

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Infine:

```
$ pyenv update
```

Ulteriori informazioni sull'installazione di pyenv [qui](https://github.com/pyenv/pyenv-installer).

##### Installazione Python 3.6.3:

Dopo aver installato pyenv, installare python 3.6.3
```
$ pyenv install 3.6.3
```
Nel repository del progetto dovrebbe essere già presente il file `.python-version` che permettere di utilizzare la versione di python corretta. Qualore non fosse presente, utilizzare il comando `pyenv local 3.6.3`.


### PostgreSQL:
[Scaricare](https://www.postgresql.org/download/) ed installare PostgreSQL-10 e creare un utente con nome `admin` e password `admin`. Per creare l'utente:

##### macOS:
Scaricare la versione Postgres.app

##### Linux:

Su Ubuntu 16.04 è stato installato nel seguente modo:

In `/etc/apt/sources.list.d/pgdg.list` aggiungere:
```
deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main
```

Poi copia-incollare nel terminale:
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  sudo apt-key add -
sudo apt-get update
```

Installare PostgreSQL:
```
$ sudo apt-get install postgresql-10
```


```
$ sudo -u postgres createuser admin

$ sudo -u postgres psql

psql=# alter user admin with encrypted password 'admin';
```

##### Windows:
Dopo aver installato Postgres utilizzando l'installer:
```
$ psql -U postgres

postgres=# create user admin with password 'admin';
```

##### Creare il database (indipendentemente dal sistema operativo):

```
$ psql         # oppure: sudo -u postgres psql
               # oppure ancora: psql -U postgres
psql=# create database mitalian with owner admin;
```

Installazione e Avvio
-------------

Installare tutte le dipendenze del progetto (potrebbero essere necessari i privilegi di amministratore):
```
$ pip install -r requirements.txt
```


##### Migrazioni:

Creare ed applicare le migrazioni:
```
$ ./manage.py makemigrations        # oppure: python manage.py makemigrations
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
   * Dario Gerosa 793636
