from bandas.models import *
import json
from datetime import timedelta

Banda.objects.all().delete()


with open('bandas/json/bandas_rock.json') as f:
    bandas_de_rock = json.load(f)

    for banda in bandas_de_rock:

        Banda.objects.create(
            nome = banda["nome"],
            nacionalidade=banda["nacionalidade"],
            ano_de_criacao=banda["ano_de_criacao"]
        )

with open('bandas/json/disco_de_rock.json') as f:
    bandas = json.load(f)

    for banda in bandas:
        discos = banda['discos']
        b = Banda.objects.get(nome=banda['banda'])


        for disco in discos:

            album = Album.objects.create(titulo = disco['titulo'],
            banda = b, ano_lancamento = disco['ano_lancamento'])

            for musica_data in disco['musicas']:

                duracao_parts = musica_data['duracao'].split(':')
                duracao = timedelta(minutes=int(duracao_parts[0]), seconds=int(duracao_parts[1]))

                Musica.objects.create(
                    titulo = musica_data["titulo"],
                    album= album,
                    duracao=duracao
                    )

    Banda.objects.order_by('nome')