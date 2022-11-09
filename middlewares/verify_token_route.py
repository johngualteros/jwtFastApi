from fastapi import Request
from functions_jwt import validate_token
from fastapi.routing import APIRoute


class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request: Request):
            token = request.headers["Authorization"].split(" ")[1]

            validation_response = validate_token(token)

            if validate_token == None:
                return await original_route(request)
            return validate_token
