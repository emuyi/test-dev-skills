import json
import yaml
import os

from projects.test_requests.test_wework.settings import Settings as ST


def formatter(content):
    """json response formatter"""
    print(json.dumps(content, indent=2, ensure_ascii=False))


def load_yaml(yaml_name):
    """
    yaml_name:
        {testcase_name}.data.yml  for data ddt
        {testcase_name}.step.yml   for step ddt
    """
    for root, dirs, files in os.walk(ST.DDT_PATH):
        for file in files:
            if yaml_name in file:
                with open(os.path.join(root, file), encoding='utf-8') as f:
                    return yaml.safe_load(f)
