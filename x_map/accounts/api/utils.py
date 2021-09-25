# create response object
def create_response_obj(success, data=None, error=None):
    return {
        'success': success,
        'data': data,
        'error': error
    }


# create http status response (200)
def create_200_response(data):
    return create_response_obj(True, data, None)

# create http status response (400)
def create_400_response(data=None, message='Bad Request. Sorry there are some invalid syntax'):
    return create_response_obj(False, data, {'code': 400, 'message': message})

# create http status response (404)
def create_404_response(data=None, message='Sorry! Couldn\'t find anything related to your search'):
    return create_response_obj(False, data, {'code': 404, 'message': message})