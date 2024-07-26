import os
from pathlib import Path

from icreports.config import Config

def get_test_data_dir():
    return Path(__file__).parent / "data"

def test_config():

    config_file = get_test_data_dir() / "mock_document/_config.yml"

    config = Config()
    config.load(config_file)

    config_out = Path(os.getcwd()) / "config_out.yml"
    config.write(config_out)

    config1 = Config()
    config1.load(config_out)

    assert config.project_name == config1.project_name

    config_out.unlink()
