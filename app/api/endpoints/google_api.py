# Понадобится для того, чтобы задать временные интервалы
from datetime import datetime
# Класс «обёртки»
from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import CharityProjectDB
from app.services.google_api import (
    set_user_permissions, spreadsheets_create, spreadsheets_update_value
)

FORMAT = "%Y/%m/%d %H:%M:%S"

# Создаём экземпляр класса APIRouter
router = APIRouter()


@router.post(
    '/',
    # Тип возвращаемого эндпоинтом ответа
    response_model=list[CharityProjectDB],
    # Определяем зависимости
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        # «Обёртка»
        wrapper_services: Aiogoogle = Depends(get_service)

):
    """Только для суперюзеров."""
    project = await charity_project_crud.get_complete_project(
        session
    )
    now_time = datetime.now().strftime(FORMAT)
    spreadsheetid = await spreadsheets_create(
        wrapper_services, now_time
    )
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    project,
                                    wrapper_services,
                                    now_time)
    return project
