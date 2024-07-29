import datetime
from django import forms


def get_ears_list(start_year=None) -> "tuple":
    if not start_year:
        start_year = 2021
    current_year = datetime.datetime.now().date().year
    years_list = tuple(range(start_year, current_year + 1))
    return years_list


class DateInputForm(forms.Form):
    date_from = forms.DateField(widget=forms.SelectDateWidget(years=get_ears_list()),
                                label="Начало периода")
    date_to = forms.DateField(widget=forms.SelectDateWidget(years=get_ears_list()),
                              label="Конец периода")
