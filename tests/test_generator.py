import unittest

from buzz import generator


def test_get_maven_artifacts():
    results = generator.get_maven_artifacts(l)
    assert len(results) > 0


def test_get_file_stats_for_artifacts():
    file_stats = generator.get_file_stats_for_artifacts()
    assert len(file_stats) > 0
