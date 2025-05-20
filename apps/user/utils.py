from rest_framework.response import Response
def custom_response(success, message, data=None):
    return Response({"success": success, "message": message, "data": data or []})