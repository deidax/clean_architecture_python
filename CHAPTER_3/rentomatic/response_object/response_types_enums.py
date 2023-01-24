class ResponseTypesEnums:
    SUCCESS = { 'label': 'Success', 'value': True, 'status_code': 200}
    FAILURE = { 'label': 'ResponseError', 'value': False}
    SYSTEM_ERROR = { 'label': 'SystemError', 'value': False, 'status_code': 500}
    PARAMETERS_ERROR = { 'label': 'ParametersError', 'value': False, 'status_code': 400}
    RESOURCE_ERROR = { 'label': 'SourceError', 'value': False, 'status_code': 404}
    
    
