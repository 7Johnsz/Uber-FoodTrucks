from fastapi import Request, HTTPException, status
from functools import wraps
from dotenv import load_dotenv
import os
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()
expected_auth = os.getenv('AUTHORIZATION')

def AuthService(func):
    """
    A decorator to ensure that the request has the correct Authorization header.
    This decorator checks if the Authorization header in the request matches the expected value.
    If it does, it proceeds to execute the wrapped function. Otherwise, it raises an HTTPException with a status code of 401.

    Returns:
    Callable: The wrapped function with Authorization header check.

    Raises:
    HTTPException: If the Authorization header does not match the expected value.
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        # Verifica se o cabeçalho de autorização é o esperado
        auth_header = request.headers.get('Authorization')
        if auth_header != expected_auth:
            now = datetime.now().isoformat()
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "msg": "You don't have permission to access this page",
                    "timestamp": now
                }
            )
        return await func(request, *args, **kwargs)
    return wrapper
