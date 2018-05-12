#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import json
import pexpect
import pytest
import requests
import sh

INPUT_TEXT = "Although they didn't like it, they accepted the offer."
EXPECTED_OUTPUT = """{"scored_rst_trees": [{"tree": "(ROOT (satellite:contrast (text 0)) (nucleus:span (text 1)))", "score": -0.9662282971887425}], "edu_tokens": [["Although", "they", "did", "n't", "like", "it", ","], ["they", "accepted", "the", "offer", "."]]}
"""


@pytest.fixture(scope="session", autouse=True)
def start_api():
    print("starting API...")
    child = pexpect.spawn('hug -f hs2015_hug_api.py')
    yield child.expect('(?i)Serving on :8000') # provide the fixture value
    print("stopping API...")
    child.close()


def test_api_plaintext():
    """The heilman-sagae-2015-service API produces the expected plaintext parse output."""
    res = requests.post(
        'http://localhost:8000/parse',
        files={'input': INPUT_TEXT},
        data={'output_format': 'output'})
    
    result_str = res.content.decode('utf-8')
    json_produced = json.loads(result_str)
    
    json_expected = json.loads(EXPECTED_OUTPUT)
    
    # the scores might not be indentical but the parse results should
    assert json_produced['edu_tokens'] == json_expected['edu_tokens']
    assert json_produced['scored_rst_trees'][0]['tree'] == json_expected['scored_rst_trees'][0]['tree']

