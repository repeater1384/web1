import json
import datetime


def get_result_data_with_json_file(JSON_FILE_LOCATION, month):
    with open(JSON_FILE_LOCATION, encoding='UTF8') as json_file:
        data = json.load(json_file)

    _result_data = {}

    YEAR = 2020
    MONTH = month
    DATE = 1

    idx = 0
    while True:
        try:
            cur_date = datetime.datetime(year=YEAR, month=MONTH, day=DATE).strftime('%Y-%m-%d')
            if data['DATA'][idx]['dates'] == cur_date:
                for i in range(6):
                    _result_data[cur_date + str(i)] = data['DATA'][idx + i]
                DATE += 1
                idx = 0
        except ValueError:
            break
        idx += 1

    return _result_data


def get_all_food_of_date(_result_data, _date):  # 해당 날짜의 아침/점심/저녁을 리턴함
    all_food = []
    for _idx in range(6):
        all_food.append(_result_data[_date + str(_idx)])
    return all_food


def after_treatment_all_food(_all_food, _type=None):  # 아침/점심/저녁에서 _type만 리턴함
    if _type is None:
        return

    return [temp[_type] for temp in _all_food if temp[_type]]


def get_inner_html_data():
    all_result = {}
    for _date in range(1, 32):
        for when in ['brst', 'lunc', 'dinr']:
            cur_date = datetime.datetime(2020, 12, _date).strftime('%Y-%m-%d')
            all_result[cur_date + ' ' + when] = after_treatment_all_food(
                get_all_food_of_date(_result_data=result_data, _date=cur_date), _type=when)

    print('{', end='')
    for key in all_result.keys():
        print(f"'{key}' : {all_result[key]},",end='')
    print('\b}', end='')


input_month = int(input('검색할 달 : '))
result_data = get_result_data_with_json_file('제3389부대 식단 정보_월별.json', month=input_month)
get_inner_html_data()

# 아침 = brst / 점심 = lunc / 저녁 = dinr
