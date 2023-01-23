import pytest
from rentomatic.repository.postgres_object import Room

pytestmark = pytest.mark.integration

def test_dummy(pg_session):
    assert len(pg_session.query(Room).all()) == 4


"""
def test_repository_list_without_parameters(pg_env,pg_data,pg_session):
    repo = Room(pg_env['postgres'])
    
    repo_rooms = repo.list
    
    assert set([r.code for r in repo_rooms]) ==\
        set([r['code'] for r in pg_data])
"""