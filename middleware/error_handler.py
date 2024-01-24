from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    def __int__(self, app: FastAPI) -> None:
        super().__int__(app)

    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
