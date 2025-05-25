import sentry_sdk
from fastapi import HTTPException
import logging

from app.utils.messages import ERRO_GENERICO

logger = logging.getLogger(__name__)


class HandleExceptionMixin:
    def handle_exception(self, exc: Exception, mensagem_usuario: str):
        sentry_sdk.capture_exception(exc)

        logger.error(f"[ERRO] {exc}")

        mensagem_usuario = ERRO_GENERICO % mensagem_usuario

        raise HTTPException(status_code=500, detail=mensagem_usuario)