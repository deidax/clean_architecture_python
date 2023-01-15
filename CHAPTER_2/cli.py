#!../venv/bin/python3

from rentomatic.repository import memrepo as mr
from rentomatic.use_case import room_list_use_case as uc

repo = mr.MemRepo([])
use_case = uc.RoomListUseCase(repo=repo)
result = use_case.execute()

print(result)