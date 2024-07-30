import datetime
import json
import logging
import os
import time

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from big3_data_main_app.custom_admin import custom_admin_site
from asu_ods_integration import constants
from asu_ods_integration.management.commands import save_raw_data_on_waste_site, asu_ods_import_containers
from tasks.tasks import asu_ods_import_containers_task, asu_ods_delete_all_import, asu_ods_import_contracts, \
    asu_ods_save_raw_data_on_waste_site_task
from asu_ods_integration.models import AsuOdsExport
from asu_ods_integration.forms import DateInputForm
from workflow.models import DocItem, DocType


class AsuOdsCallbackView(APIView):
    serializer_class = None
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response({})

    def post(self, request, *args, **kwargs):
        time.sleep(5)  # заглушка. Иногда ответ приходит раньше, чем создаётся объект запроса в бд.
        print('AsuOdsCallbackView:', request.query_params, request.data)
        logger = logging.getLogger("ods_integration")
        logger.info("----------Начало сеанса для представления AsuOdsCallbackView------------")
        logger.info(f"Данные запроса {request.data}. Тип данных в запросе {type(request.data)}")
        try:
            request_id = request.data['request_id']
            try:
                export = AsuOdsExport.objects.filter(request_id=request_id).latest("datetime_create")
                export.response_raw = json.dumps(request.data, ensure_ascii=False)
                export.save()
                response = Response("Success", status=status.HTTP_200_OK)
                logger.info(f" был найден объект с request_id {request_id}, данные успешно сохранены.")
            except AsuOdsExport.DoesNotExist:
                logger.error(f"Произошла ошибка. Объект с request_id {request_id} не найден.")
                response = Response(f"Error: object with request_id-{request_id} not found.",
                                    status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            logger.error(f"Произошла ошибка. Ключа request_id не было в запросе.")
            response = Response("Error: key 'request_id' not found.", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Произошла непредвиденная ошибка.", exc_info=True)
            logger.info("----------Конец сеанса для представления AsuOdsCallbackView------------")
            raise e
        logger.info("----------Конец сеанса для представления AsuOdsCallbackView------------")
        return response


def superuser_required(view):
    def f(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Доступ разрешён только суперпользователю.")
        response = view(request, *args, **kwargs)
        return response
    return f


@superuser_required
@login_required
def menu_of_commands(request):
    context: "dict" = custom_admin_site.each_context(request)
    response = render(request, template_name="menu_of_commands.html", context=context)
    return response


class CommandsNames:
    IMPORT_CONTAINERS = os.path.splitext(os.path.basename(asu_ods_import_containers.__file__))[0]
    IMPORT_RAW_DATA = os.path.splitext(os.path.basename(save_raw_data_on_waste_site.__file__))[0]


@superuser_required
@login_required
def import_containers_page(request, command_name):

    log = logging.getLogger("ods_integration")
    log.info("Представление выполнилось")
    if command_name not in (CommandsNames.IMPORT_CONTAINERS, CommandsNames.IMPORT_RAW_DATA):
        raise PermissionDenied("Команда <<{}>> не разрешена".format(command_name))
    context: "dict" = custom_admin_site.each_context(request)
    if request.method == "POST":
        form = DateInputForm(request.POST)
        if form.is_valid():
            date_from = form.cleaned_data["date_from"]
            date_to = form.cleaned_data["date_to"]
            log.info("Запуск фоновой задачи")
            if isinstance(date_from, datetime.date):
                date_from = date_from.isoformat()
            if isinstance(date_to, datetime.date):
                date_to = date_to.isoformat()
                if command_name == CommandsNames.IMPORT_CONTAINERS:
                    asu_ods_import_containers_task.delay(date_from, date_to)
                elif command_name == CommandsNames.IMPORT_RAW_DATA:
                    asu_ods_save_raw_data_on_waste_site_task.delay(date_from, date_to)
                else:
                    raise RuntimeError()
            log.info(f"Поступили даты: {date_from}, {date_to}")
            log.info("Фоновая задача была запущена")
            log.info("Перенаправление на лог выполнения")
            response = redirect("admin:asu_ods_integration_asuodsexport_changelist")
        else:
            context.update({"form": form})
            if command_name == CommandsNames.IMPORT_CONTAINERS:
                response = render(request, template_name="import_containers.html", context=context)
            elif command_name == CommandsNames.IMPORT_RAW_DATA:
                response = render(request, template_name="import_raw_data.html", context=context)
            else:
                raise RuntimeError()
    elif request.method == "GET":
        form = DateInputForm()
        context.update({"form": form})
        if command_name == CommandsNames.IMPORT_CONTAINERS:
            response = render(request, template_name="import_containers.html", context=context)
        elif command_name == CommandsNames.IMPORT_RAW_DATA:
            response = render(request, template_name="import_raw_data.html", context=context)
        else:
            raise RuntimeError()
    else:
        raise RuntimeError()
    return response


@superuser_required
@login_required
def delete_all_containers_page(request):
    response = render(request, template_name="delete_containers.html")
    return response


@superuser_required
@login_required
def delete_containers_start(request):
    asu_ods_delete_all_import.delay()
    response = redirect("admin:asu_ods_integration_asuodsexport_changelist")
    return response


@superuser_required
@login_required
def import_contracts_page(request):
    contracts_count = DocItem.objects.filter(doc_type__code=constants.CONTRACT_DOCTYPE_CODE).count()
    try:
        doc_type = DocType.objects.get(code=constants.CONTRACT_DOCTYPE_CODE)
        link_to_doctype = reverse("admin:workflow_doctype_change", args=[doc_type.id, ])
    except DocType.DoesNotExist:
        link_to_doctype = ""
    context = {"contracts_count": contracts_count, "link_to_doctype": link_to_doctype}
    response = render(request, template_name="import_contracts.html", context=context)
    return response


@superuser_required
@login_required
def import_contracts_start(request):
    asu_ods_import_contracts.delay()
    response = redirect("admin:asu_ods_integration_asuodsexport_changelist")
    return response
