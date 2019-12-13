import unittest

from buzz import generator


def test_get_maven_artifacts():
    results = generator.get_maven_artifacts()
    assert len(results) > 0


def test_get_file_stats_for_artifacts():
    download_list = generator.get_file_stats_for_artifacts()
    assert len(download_list) > 0
