import os

import yaml
from kestrel_interface_opensearch.config import (PROFILE_PATH_ENV_VAR,
                                                 Connection, load_config)


def test_load_config(tmp_path):
    config = {
        "connections": {
            "localhost": {
                "url": "https://localhost:9200",
                "verify_certs": False,
                "auth": {
                    "username": "admin",
                    "password": "admin",
                }
            },
            "some-cloud-thing": {
                "url": "https://www.example.com:9200",
                "verify_certs": True,
                "auth": {
                    "username": "hunter",
                    "password": "super_secret",
                }
            }
        },
        "datasources": {
            "some_ds": {
                "connection": "some-cloud-thing",
                "index_pattern": "logs-*",
                "timestamp": "@timestamp",
                "timestamp_format": "%Y-%m-%d %H:%M:%S.%f",
                "data_model_map": "mapping.yaml"
            }
        }
    }
    map_file = tmp_path / "mapping.yaml"
    with open(map_file, 'w') as fp:
        fp.write("some.field: other.field\n")
    config_file = tmp_path / "opensearch.yaml"
    with open(config_file, 'w') as fp:
        yaml.dump(config, fp)
    os.environ[PROFILE_PATH_ENV_VAR] = str(config_file)
    read_config = load_config()
    conn: Connection = read_config.connections["localhost"]
    assert conn.url == config["connections"]["localhost"]["url"]
    assert read_config.connections["localhost"].url == config["connections"]["localhost"]["url"]
    assert read_config.datasources["some_ds"].index_pattern == config["datasources"]["some_ds"]["index_pattern"]
    assert read_config.datasources["some_ds"].data_model_map["some.field"] == "other.field"
