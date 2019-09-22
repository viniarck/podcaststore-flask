#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import requests


def base_url() -> str:
    """get base URL."""
    return "http://localhost:5000/v1/"


@pytest.fixture()
def db_setup():
    from podcaststore.app import db

    # TODO segregate the DB locally
    db.create_all()
    yield db
    db.drop_all()


class TestPodcast:

    """Podcast test suite."""

    def test_get_empty(self, db_setup) -> None:
        res = requests.get(f"{base_url()}podcast")
        assert res.status_code == 200
        assert res.json() == []

    def test_post_get_list(self, db_setup) -> None:
        url = f"{base_url()}podcast"
        data = {"name": "pod1", "title": "super pod1"}
        res = requests.post(
            url, json=data, headers={"Content-Type": "application/json"}
        )
        assert res.status_code == 201
        res = requests.get(url)
        assert res.status_code == 200
        res_data = res.json()[0]
        for k, v in data.items():
            assert res_data[k] == v
