import argparse
import re
from models import ArgsModel


class CLI:
    def __init__(self, default_period: int, default_debug: bool):
        parser = argparse.ArgumentParser()
        parser.add_argument("--period", type=int, default=default_period, help="Period of updating currency rates")
        parser.add_argument("--debug", type=str, default=str(default_debug).lower(), help="On|Off debug mode")
        known_args, unknown_args = parser.parse_known_args()

        debug = known_args.debug.lower() in ["1", "true", "y", "yes"]

        self.__args = ArgsModel(period=known_args.period, debug=debug, currencies={})

        for arg_id in range(len(unknown_args) - 1):
            if re.search("-{2}[a-zA-Z]{3}", unknown_args[arg_id]) and \
               unknown_args[arg_id + 1].replace('.', '', 1).isdigit():
                self.__args.currencies[unknown_args[arg_id][2:].lower()] = float(unknown_args[arg_id + 1])

    
    def get_args(self) -> ArgsModel:
        return self.__args
