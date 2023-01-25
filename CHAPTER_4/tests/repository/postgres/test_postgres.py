import pytest
from rentomatic.repository.postgresrepo import PostgresRepo
from rentomatic.services.room_list_service import RoomListService

pytestmark = pytest.mark.integration

def test_repository_list_without_parameters(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list()
    assert set([r.code for r in repo_rooms]) ==\
        set([r['code'] for r in pg_data])

def test_repository_list_with_code_equal_filter(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list(
        filters={'code__iq': 'f853578c-fc0f-4e65-81b8-566c5dffa35a'}
    )
    
    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == 'f853578c-fc0f-4e65-81b8-566c5dffa35a'

def test_repository_list_with_price_equal_filter(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list(
        filters={'price__iq': '160'}
    )
    
    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == '913694c6-435a-4366-ba0d-da5334a611b2'

def test_repository_list_with_price_less_than_filter(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list(
        filters={'price__lt': '60'}
    )
    
    assert set([r.code for r in repo_rooms]) ==\
        {
            'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'eed76e77-55c1-41ce-985d-ca49bf6c0585'
        }

def test_repository_list_with_price_greater_than_filter(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list(
        filters={'price__gt': '66'}
    )
    
    assert set([r.code for r in repo_rooms]) ==\
        {
            '913694c6-435a-4366-ba0d-da5334a611b2'
        }

def test_repository_list_with_price_between_filter(pg_env,pg_data,pg_session):
    repo = PostgresRepo(pg_env['postgres'])
    
    repo_rooms = repo.list(
        filters={
            'price__lt': 160,
            'price__gt': 48
        }
    )
    
    assert len(repo_rooms) == 1
    assert set([r.code for r in repo_rooms]) ==\
        {
            'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a'
        }

def test_with_room_service(pg_env,pg_data,pg_session):
    
    pg_service = RoomListService(
                PostgresRepo(pg_env['postgres'])
            )

    result = pg_service.list_with_filters()
    
    assert set([r.code for r in result.response_value]) ==\
        set([r['code'] for r in pg_data])