import pytest
from pgbackup import cli

#  $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_partser_whithoud_driver(parser):
    """
    Whithout a specified driver parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parser will exit if it reiceves a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the drier name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destionation'])

def test_parser_with_know_driver(parser):
    """
    The parser will not exit if the driver name is know.
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])

def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destination
    """
    args = parser.parse_args([url, "--driver", "local", "/some/path"])

    assert args.url == url
    assert args.driver == "local"
    assert args.destination == '/some/path'

