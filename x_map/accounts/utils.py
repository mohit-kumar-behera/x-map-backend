def create_response_obj(status, success, message):
  return {
    'success': success,
    'message': message
  }, status