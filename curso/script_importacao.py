from curso.models import *
import json

def importar_curso(ficheiro_json):
    
    Curso.objects.all().delete()
    Area_cientifica.objects.all().delete()
    Disciplina.objects.all().delete()
    Docente.objects.all().delete()

    
    with open(ficheiro_json) as f:
        dados_curso = json.load(f)

    
    reasons = dados_curso['reasons']
    scientific_area_name = dados_curso['courseDetail']['scientificArea']

   
    area_cientifica_obj, created = Area_cientifica.objects.get_or_create(nome=scientific_area_name)

    
    curso_obj = Curso.objects.create(
        nome="Lei",
        apresentacao=reasons[0]['reason'],
        objetivo=reasons[1]['reason'],
        competencia=reasons[2]['reason'],
        area_cientifica=area_cientifica_obj
    )

   
    course_flat_plan = dados_curso['courseFlatPlan']

   
    for disciplina_data in course_flat_plan:
        nome = disciplina_data['curricularBranchName']
        ano = disciplina_data['curricularYear']
        semestre = disciplina_data['semester']
        ects = disciplina_data['ects']
        curricularIUnitReadableCode = disciplina_data['curricularIUnitReadableCode']

       
        disciplina_obj = Disciplina.objects.create(
            nome=nome,
            ano=ano,
            semestre=semestre,
            ects=ects,
            curricularIUnitReadableCode=curricularIUnitReadableCode,
            areaCientifica=area_cientifica_obj 
        )

        
        curso_obj.disciplinas.add(disciplina_obj)

        
        docente_nome = disciplina_data.get('docente', None)
        if docente_nome:
            docente_obj, _ = Docente.objects.get_or_create(nome=docente_nome)
            disciplina_obj.docentes.add(docente_obj)

   
    curso_obj.save()
