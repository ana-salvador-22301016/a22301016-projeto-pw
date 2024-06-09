from django.shortcuts import render
import requests

d_lisboa = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
clima_descricao = 'https://api.ipma.pt/open-data/weather-type-classe.json'


# Create your views here.
def meteo_view(request):
    caminho = "w_ic_d_"
    request_d = requests.get(d_lisboa)
    request_c = requests.get(clima_descricao)
    d = {}
    c = {}

    if request_d.status_code == 200:
        d = request_d.json()

    if request_c.status_code == 200:
        c = request_c.json()

    list_desc = []

    for c_info in c['data']:
        if c_info ['idWeatherType'] >= 0:

            list_desc.append(c_info['descWeatherTypePT'])

    list_dic = []

    for d_info in d['data']:
        dic = {}
        dic['dataAtual'] = d_info['forecastDate']
        dic['tmpMin'] = d_info['tMin']
        dic['tmpMax'] = d_info['tMax']
        dic['desTmp'] = list_desc[d_info['idWeatherType']]

        dic['svg'] = caminho + (str(d_info['idWeatherType']) if d_info['idWeatherType'] > 9 else "0" + str(d_info['idWeatherType'])) + "anim.svg"

        list_dic.append(dic)

        context = {
            'climaDetalhes' : list_dic
            }


    return render(request, "meteo/home.html", context)
