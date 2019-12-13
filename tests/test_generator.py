import unittest

from popular_artifacts import popular_artifact_generator


def test_get_maven_artifacts():
    results = popular_artifact_generator.get_maven_artifacts()
    assert len(results) > 0


def test_get_file_stats_for_artifacts():
    download_list = popular_artifact_generator.get_file_stats_for_artifacts()
    assert len(download_list) > 0
