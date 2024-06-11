import json
import pandas
import pathlib

config_path = pathlib.Path.cwd() / "shared" / "config.json"
config_file = json.load(open(config_path))
load_file = pathlib.Path(config_file["stock_analysis"]["load_file"])

data = pandas.read_csv(load_file)