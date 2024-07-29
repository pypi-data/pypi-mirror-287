import datetime
import os
import shutil
import zipfile
import json
import requests
import zeep as zeep
from requests.auth import HTTPBasicAuth
from time import sleep
import tempfile
from requests_toolbelt.utils import dump

from ..exceptions import RequestError
from ..models import AsuOdsExport, StatusesOfCompletions

ASU_ODS_HOST_DEV = 'https://test-reestr-ogh.tech.mos.ru'
ASU_ODS_HOST_PROD = 'https://reestr-ogh.mos.ru/'
ASU_ODS_USERNAME = 'tsoo'
ASU_ODS_PASSWORD = 'admin'


class GetTokenError(Exception):
    pass


class AsuOds:

    @classmethod
    def get_token(cls):
        # выполняем запрос за токеном
        response = requests.post(f'{ASU_ODS_HOST_DEV}/sso/auth/signin', verify=True, data={
            'username': ASU_ODS_USERNAME,
            'password': ASU_ODS_PASSWORD,
        })
        if response.status_code != 200:
            raise GetTokenError('Ошибка получения токена')
        return response.json()['data']['accessToken']

    @classmethod
    def request_ogh(cls, ogh_type, start_dt: "datetime.datetime", end_dt: "datetime.datetime") -> "AsuOdsExport":
        # Регулярка на сервере, не предусматривает нормального указания часового пояса o_O
        # там только положительные значения. Поэтому на данный момент буду считать, что
        # время только в формате UTC
        # r = r"^([1-3][0-9]{3}-(((0[1-9]|1[012])-(0[1-9]|[12][0-9]))|((0[469]|11)-30)|(
        #       (0[13578]|1[02])-3[01])))T(([0-1][0-9])|(2[0-3])):[0-5][0-9]:[0-5][0-9]\\.[0-9]*Z$"
        # 'startDate': start_dt.strftime("%Y-%m-%dT%H:%M:%S.0"),
        # 'endDate': end_dt.strftime("%Y-%m-%dT%H:%M:%S.0"),
        #
        param = {'ogh_object_type_id': {'ogh_object_type': ogh_type, },
                 'startDate': start_dt.strftime("%Y-%m-%dT%H:%M:%S.0Z"),
                 'endDate': end_dt.strftime("%Y-%m-%dT%H:%M:%S.0Z"),
                 }
        response = requests.post(
            f'{ASU_ODS_HOST_DEV}/tsoo/ods/ogh/export',
            verify=True,
            headers={'accessToken': cls.get_token(), },
            json=param,
        )
        # заводим хранимый объект интеграции
        export = AsuOdsExport.objects.create(
            request_raw=dump.dump_all(response).decode('utf-8'),
        )
        if response.status_code != 200:
            export.request_error = (f'Ошибка отправки запроса. Код ответа: {response.status_code}. '
                                    f'Ответ: {response.content}')
            export.save()
            raise RequestError(export.request_error)

        export.request_id = response.json()['request_id']
        export.save()
        return export

    @classmethod
    def create_empty_export_obj(cls, command_name: str, status: "StatusesOfCompletions") -> "AsuOdsExport":
        export = AsuOdsExport.objects.create(
            request_raw="",
            command_name=command_name,
            status_of_completion=status.name,
        )
        return export

    @classmethod
    def response_set(cls, request_id, data):
        export = AsuOdsExport.objects.filter(request_id=request_id).first()
        if not export:
            raise Exception('Данные экспорта не обнаружены')
        export.response_url = data.get('url')
        export.response_raw = data
        export.save()

    @classmethod
    def request_wait(cls, request_id, timeout=1):
        # активное ожидание
        while AsuOdsExport.objects.filter(request_id=request_id, response_raw=None).exists():
            sleep(timeout)
        # объект экспорта
        export = AsuOdsExport.objects.get(request_id=request_id)
        if export.response_error:
            raise Exception(export.response_error)

    @classmethod
    def iter_parse_ogh(cls, request_id):
        # объект экспорта
        export = AsuOdsExport.objects.get(request_id=request_id)
        if not export.response_url:
            raise Exception('URL экспорта не обнаружен')

        # выгружаем файл экспорта
        response = requests.get(export.response_url, verify=True, stream=True)
        if response.status_code != 200:
            export.parse_error = f'{response.status_code}'
            export.save()
            raise Exception(export.parse_error)

        with tempfile.TemporaryDirectory() as tmpdir:
            fn_zip = os.path.join(tmpdir, 'ogh.zip')
            folder = os.path.join(tmpdir, 'ogh')
            # пишем данные в файл
            with open(fn_zip, 'wb') as fp:
                shutil.copyfileobj(response.raw, fp)
            # распаковываем архив
            with zipfile.ZipFile(fn_zip, 'r') as zip_ref:
                zip_ref.extractall(folder)
            # читаем первый файл из целевой папки
            fn_json = os.path.join(folder, os.listdir(folder)[0])
            # парсим json
            with open(fn_json, 'rb') as fp:
                for line in fp:
                    yield json.loads(line)

    @classmethod
    def get_contracts(cls):
        session = requests.Session()
        session.auth = HTTPBasicAuth('WST_TSOO', '0fKGPJTa')

        client = zeep.Client(
            wsdl='https://ods.mos.ru/garbageRoute/garbageInformationWebService?wsdl',
            transport=zeep.transports.Transport(session=session),
        )
        return client.service.getContractList(date='2021-12-20')
