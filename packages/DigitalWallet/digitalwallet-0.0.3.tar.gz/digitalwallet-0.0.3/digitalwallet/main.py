from utils import CLI, configure_logging
from models import Wallet
from service import API, Fetcher

cli = CLI(1, False)
args = cli.get_args()
configure_logging(args.debug)

wallet = Wallet()
fetcher = Fetcher(args.period, args.currencies, wallet)
app = API(wallet, fetcher).app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")