# CoronaBrasil services

CoronaBrasil services is a Django API running for the project [https://coronabrasil.org](https://coronabrasil.org) to help brazilian people to find information about availability of public and private services separated by regions of Brazil.



## Installation
We use [Python 3.7](https://www.python.org/downloads/) and [Postgresql](https://www.postgresql.org/download/).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install our dependencies.

```bash
mkdir cbrasil
cd cbrasil
virtualenv venv
source venv/bin/activate
git clone https://github.com/coronaaqui/website.git
cd services
pip install -r requirements.txt
```



## Running

```bash
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata bootstrap_dump.json (optional - some basic data)
./manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Stay connected in our Slack channel: [CoronaBrasil Slack](https://join.slack.com/t/voluntariostech/shared_invite/zt-cy3297ao-Wh70mOR0BBKT8N4BykgI0A).

## License
[MIT](https://choosealicense.com/licenses/mit/)
