from django import forms    # formulários Django
from .models import Banda
from .models import Musica
from .models import Album


class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da banda', 'title': 'Insira o nome da banda.'}),
            'nacionalidade': forms.TextInput(attrs={'placeholder': 'Nacionalidade', 'title': 'Insira a nacionalidade da banda.'}),
            'ano_de_criacao': forms.NumberInput(attrs={'placeholder': 'Ano de Criação', 'title': 'Insira o ano de criação da banda.'}),
            'detalhe': forms.TextInput(attrs={'placeholder': 'Detalhe', 'title': 'Insira algum detalhe adicional sobre a banda.'}),
            'biografia': forms.Textarea(attrs={'placeholder': 'Biografia', 'title': 'Insira uma breve biografia da banda.'}),
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título da Música', 'title': 'Insira o título da música.'}),
            'data': forms.DateInput(attrs={'placeholder': 'Data de Lançamento', 'title': 'Insira a data de lançamento da música.'}),
            'spotify_link': forms.URLInput(attrs={'placeholder': 'Link do Spotify', 'title': 'Insira o link do Spotify da música (se disponível).'}),
            'duracao': forms.TextInput(attrs={'placeholder': 'Duração', 'title': 'Insira a duração da música.'}),
            'letra': forms.Textarea(attrs={'placeholder': 'Letra', 'title': 'Insira a letra da música (se disponível).'}),
            'biografia': forms.Textarea(attrs={'placeholder': 'Biografia Relacionada', 'title': 'Insira uma breve biografia relacionada à música (se disponível).'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do Álbum', 'title': 'Insira o título do álbum.'}),
            'ano_lancamento': forms.NumberInput(attrs={'placeholder': 'Ano de Lançamento', 'title': 'Insira o ano de lançamento do álbum.'}),
        }
