import json

from flask import request
from flask import Blueprint, Response

from rentomatic.repository import memrepo as mr
from rentomatic.use_case import room_list_use_case as uc
from rentomatic.request_object.room_list_request_object import RoomListRequestObject
from rentomatic.serializers.requests.http_flask_request_ser import HttpFlaskRequestSer

blueprint = Blueprint('room', __name__)

room1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': -0.09998975,
    'latitude': 51.75436293,
}
room2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': 0.18228006,
    'latitude': 51.74640997,
}
room3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}
room4 = {
    'code': 'k13694c4-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 160,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}

@blueprint.route('/rooms', methods=['GET'])
def room():
    repo = mr.MemRepo([room1,room2,room3,room4])
    """Serialize the filters args"""
    filters = HttpFlaskRequestSer().filters(flask_request_args=request.args.items())
    """Inject the filters in the rooms list request"""
    room_list_request = RoomListRequestObject.from_dict(dict_f=filters)
    """Create a use case repo"""
    use_case = uc.RoomListUseCase(repo)
    
    response_object = use_case.execute(room_list_request)

    
    
    return Response(response_object.json_ser(), mimetype='application/json', status=response_object.status_code)
