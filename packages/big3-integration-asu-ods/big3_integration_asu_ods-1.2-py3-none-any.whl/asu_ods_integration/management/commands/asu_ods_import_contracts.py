from django.core.management.base import BaseCommand

from asu_ods_integration import constants
from asu_ods_integration.external.asu_ods import AsuOds
from asu_ods_integration.import_contracts import AsuOdsEavCreator
from asu_ods_integration.models import AsuOdsExport
from data_exchange_with_external_systems.logging_of_tasks import LogManager
from workflow.models import DocType, DocItem


class Command(BaseCommand):
    def handle(self, fn=None, **options):
        log_manager = LogManager("ods_integration")
        try:
            obj = AsuOdsExport.objects.create(
                command_name="import_contracts"
            )
            log_manager.set_obj(obj)
            log_manager.log.info("Начинается импорт документов из АСУ ОДС")
            log_manager.save_log()
            try:
                doc_type = DocType.objects.get(code=constants.CONTRACT_DOCTYPE_CODE)
                DocItem.objects.filter(doc_type=doc_type).delete()
            except DocType.DoesNotExist:
                pass

            log_manager.log.info('Выполняется запрос договоров')
            log_manager.save_log()
            contracts = AsuOds.get_contracts()
            log_manager.log.info(f"Из АСУ ОДС было получено {len(contracts)} договоров.")
            log_manager.save_log()

            contracts_list = []
            for contract in contracts:
                contract_dict = {
                    "contractDate": contract.contractDate,
                    "contractNumber": contract.contractNumber,
                    "contractObj": contract.contractObj,
                    "contractSum": contract.contractSum,
                    "custPerson": contract.custPerson,
                    "dateFrom": contract.dateFrom,
                    "dateTo": contract.dateTo,
                    "distanceAvg": contract.distanceAvg,
                    "execPerson": contract.execPerson,
                    "files": contract.files,
                    "finName": contract.finName,
                    "kindName": contract.kindName,
                    "peopleCnt": contract.peopleCnt,
                }
                contracts_list.append(contract_dict)

            log_manager.log.info("Сохранение полученных договоров в системе.")
            eav_creator = AsuOdsEavCreator(
                constants.CONTRACT_DOCTYPE_NAME,
                constants.CONTRACT_DOCTYPE_CODE,
                contracts_list,
                log_manager
            )
            eav_creator.set_data_example(contracts_list[0])
            eav_creator.create_eav()
            log_manager.log.info(f"Выполнение программы успешно завершено")
            log_manager.save_log()
        except Exception as e:
            log_manager.log.error("", exc_info=True)
            log_manager.save_log()
            raise e

