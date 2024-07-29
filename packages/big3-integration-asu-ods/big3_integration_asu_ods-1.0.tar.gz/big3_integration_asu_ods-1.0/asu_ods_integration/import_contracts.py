import logging

from typing import List

from integrations.doctype_creator.core import EAVCreator


class AsuOdsEavCreator(EAVCreator):

    def _prepare_data(self, raw_data) -> "List[dict]":
        log = logging.getLogger("ods_integration")
        log.info("Начался этап подготовки данных")
        prepared_data = []
        for d in raw_data:
            document_data = {}
            for k, v in d.items():
                if isinstance(v, dict):
                    for k2, v2 in v.items():
                        field_name = str(k) + "__" + str(k2)
                        value = v2
                        document_data[field_name] = value
                elif isinstance(v, list):
                    # Списки пропускаются
                    continue
                else:
                    field_name = str(k)
                    value = v
                    document_data[field_name] = value
            prepared_data.append(document_data)
        return prepared_data
