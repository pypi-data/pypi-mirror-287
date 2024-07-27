## Digital Wallet

### Setup

```
git clone https://github.com/heliosgrounder/DigitalWallet.git
cd DigitalWallet
python -m venv venv
```

* Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```

* Unix:
```
./venv/bin/activate
```

```
pip install -r requirements.txt
```

### Run

You can choose all available currencies in [this](https://www.cbr-xml-daily.ru/daily_json.js).

```
cd digitalwallet
```

```
python -m main --period 10 --rub 10 --debug y
```

```
python -m main --rub 100 --eur 300 --usd 200
```

```
python -m main --aud 200 --rub 0
```

### Using

You can go to `localhost:8000/docs` and use FastApi interface.