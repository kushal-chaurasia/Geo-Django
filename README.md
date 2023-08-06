# Setup of PostgreSQL for GeoDjango

This guide provides step-by-step instructions for setting up PostgreSQL with GeoDjango on Ubuntu.

## PostgreSQL Installation

1. Add the PostgreSQL repository to your system's sources list:
   
    ```bash
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    ```

2. Import the repository signing key:

    ```bash
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    ```

3. Update the package lists:

    ```bash
    sudo apt-get update
    ```

4. Install PostgreSQL and PostGIS:

    ```bash
    sudo apt-get -y install postgresql
    sudo apt install postgis postgresql-15-postgis-3
    ```

5. Install GDAL bin:

    ```bash
    sudo apt install gdal-bin
    ```

6. Create a PostgreSQL database:

    ```bash
    sudo -u postgres createdb challenge
    ```

7. Access the PostgreSQL shell:

    ```bash
    sudo -u postgres psql
    ```

8. In the PostgreSQL shell, run the following commands to enable PostGIS and create a user with appropriate privileges:

    ```sql
    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;

    CREATE USER proj_user WITH PASSWORD 'ABCDEFGHIJK';
    ALTER USER proj_user WITH SUPERUSER;
    ALTER ROLE proj_user SET client_encoding TO 'utf8';
    ALTER ROLE proj_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE proj_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE challenge TO proj_user;
    \q
    ```

## Cloning repo

```bash
    git clone https://github.com/kushal-chaurasia/Geo-Django.git

```

## Python Setup

1. Add the DeadSnakes PPA for Python 3.9:

    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    ```

2. Install Python 3.9 virtual environment:

    ```bash
    sudo apt install python3.9-venv
    ```

3. Create and activate a virtual environment:

    ```bash
    python3.9 -m venv venvmyenv
    source venvmyenv/bin/activate
    ```

4. Install required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Activate the virtual environment before working on your project:

    ```bash
    source venvmyenv/bin/activate
    ```

2. Deactivate the virtual environment when you're done:

    ```bash
    deactivate
    ```


