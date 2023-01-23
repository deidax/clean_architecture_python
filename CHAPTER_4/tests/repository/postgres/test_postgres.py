import pytest
from rentomatic.repository.postgresrepo import PostgresRepo

pytestmark = pytest.mark.integration

def test_repository_list_without_parameters(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list
    
    assert set([r.code for r in repo_rooms]) ==\
        set([r['code'] for r in pg_data])