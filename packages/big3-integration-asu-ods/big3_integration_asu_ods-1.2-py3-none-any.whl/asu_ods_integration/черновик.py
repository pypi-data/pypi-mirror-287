import datetime

d = {
    'contractDate': datetime.datetime(2021, 6, 11, 0, 0),
    'contractNumber': '48-ЮС/44-21 Южное Бутово/3',
    'contractObj': 'ПРОС',
    'contractSum': 0.0,
    'custPerson': {
        'inn': '7727846180',
        'kpp': '772701001',
        'name': 'Государственное бюджетное учреждение города Москвы «Жилищник района Южное Бутово»',
        'ogrn': '5147746230253',
        'shortName': 'Жилищник Южное Бутово'
    },
    'dateFrom': datetime.datetime(2021, 12, 18, 0, 0),
    'dateTo': datetime.datetime(2023, 12, 31, 0, 0),
    'distanceAvg': None,
    'execPerson': {
        'inn': '7734690939',
        'kpp': '771501001',
        'name': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ «ЭкоЛайн»',
        'ogrn': '1127747172002',
        'shortName': 'ООО «ЭкоЛайн»'
    },
    'files': [],
    'finName': 'Коммерческий',
    'kindName': 'Вывоз отходов',
    'peopleCnt': None,
    'singleCustomerContract': False
}


d2 = {
    'area': 216.44,
    'parent': [
        {'root_id': 763694726,
         'end_date': '3000-01-01',
         'object_id': 763694726,
         'start_date': '2021-09-08',
         'ogh_object_type_id':
             {'ogh_object_type': 'yard'}}
    ],
    'in_yard': 1,
    'no_calc': 0,
    'root_id': 763694728,
    'end_date': '3000-01-01',
    'geometry':
        {'type': 'MultiPolygon',
         'coordinates':
             [
                 [
                     [
                         [17777.182467, 769.604963], [17760.601501, 770.893814], [17759.496093, 762.6083],
                         [17777.550918, 758.741724], [17777.182467, 769.604963]
                     ]
                 ],
                 [
                     [
                         [17740.151606, 775.496879], [17733.519209, 774.944519], [17732.966505, 769.052602],
                         [17740.520057, 767.395495], [17740.151606, 775.496879]
                     ]
                 ]
             ]
         },
    'object_id': 763694728,
    'start_date': '2021-09-08',
    'address_list': [{'unad': {'bti_object': '1'}, 'unom': {'bti_object': '440773'}}],
    'coating_type_id': {'coating_type': 'asphalt_concrete'},
    'coating_group_id': {'coating_group': 'advanced'},
    'container_type_id': {'container_type': 'container_area'},
    'ogh_object_type_id': {'ogh_object_type': 'container'},
    'is_diff_height_mark': 0, 'is_separate_garbage_collection': 1}

l = [
    [[[17777.182467, 769.604963], [17760.601501, 770.893814]]],[[[17740.151606, 775.496879], [17733.519209, 774.944519]]]
]
