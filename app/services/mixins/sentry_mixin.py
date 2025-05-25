from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import ForeignKeyViolation, UniqueViolation
import sentry_sdk
import logging

logger = logging.getLogger(__name__)


class HandleExceptionMixin:
    def handle_exception(self, exc: Exception, mensagem_usuario: str = "Ocorreu um erro inesperado. Já estamos verificando."):
        if isinstance(exc, IntegrityError) or isinstance(exc, ValueError):
            return HTTPException(status_code=400, detail=str(exc.args[0]))

        sentry_sdk.capture_exception(exc)
        logger.error(f"[ERRO] {exc}")

        raise HTTPException(status_code=500, detail=mensagem_usuario)
