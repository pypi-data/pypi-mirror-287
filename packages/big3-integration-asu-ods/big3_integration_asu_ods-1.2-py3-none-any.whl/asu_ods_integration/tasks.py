import logging

from big3_data_main_app.celery import app


TASK_IS_START_TEXT = "Фоновая задача начала выполнение."


@app.task
def asu_ods_import_containers_task(date_from, date_to):
    log = logging.getLogger("ods_integration")
    log.info(TASK_IS_START_TEXT)
    from django.core import management
    try:
        management.call_command('asu_ods_import_containers', start_date=date_from, end_date=date_to)
    except Exception as e:
        log.error("", exc_info=True)
        raise e


@app.task
def asu_ods_save_raw_data_on_waste_site_task(date_from, date_to):
    log = logging.getLogger("ods_integration")
    log.info(TASK_IS_START_TEXT)
    from django.core import management
    try:
        management.call_command('save_raw_data_on_waste_site', start_date=date_from, end_date=date_to)
    except Exception as e:
        log.error("", exc_info=True)
        raise e


@app.task
def asu_ods_delete_all_import():
    log = logging.getLogger("ods_integration")
    log.info(TASK_IS_START_TEXT)
    from django.core import management
    management.call_command('asu_ods_delete_all_import')


@app.task
def asu_ods_import_contracts():
    log = logging.getLogger("ods_integration")
    log.info(TASK_IS_START_TEXT)
    from django.core import management
    management.call_command('asu_ods_import_contracts')
