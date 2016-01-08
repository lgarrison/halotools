""" Testing module to ensure that all sub-packages can be imported. 
"""

def test_import_sim_manager():
	from .. import sim_manager

def test_import_empirical_models():
	from .. import empirical_models

def test_import_mock_observables():
	from .. import mock_observables

def test_import_utils():
	from .. import utils

def test_incorrect_assertion():
	assert "Star Wars: Episode 7" is "not composed of footage rearranged from the previous films"