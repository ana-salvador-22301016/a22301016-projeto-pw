from curso.models import Curso
from curso.models import Area_cientifica
from curso.models import Disciplina
from curso.models import Projeto
from curso.models import Linguagem
from curso.models import Docente

import json

# Limpa os dados existentes antes de carregar os novos
Curso.objects.all().delete()
Disciplina.objects.all().delete()
Projeto.objects.all().delete()
Area_cientifica.objects.all().delete()
Linguagem.objects.all().delete()
Docente.objects.all().delete()


with open('curso/ficheiro_json/lei.json') as f:
    data = json.load(f)

    # Carrega os detalhes do curso
    course_detail_data = data.get('courseDetail', {})
    course_detail = Curso.objects.create(
        courseCode=course_detail_data.get('courseCode'),
        institutionCode=course_detail_data.get('institutionCode'),
        A3ESDeliberation=course_detail_data.get('A3ESDeliberation'),
        accessContidions=course_detail_data.get('accessContidions'),
        careerOportunities=course_detail_data.get('careerOportunities'),
        competences=course_detail_data.get('competences'),
        conferedDegree=course_detail_data.get('conferedDegree'),
        creditationStatus=course_detail_data.get('creditationStatus'),
        creditationStatusCode=course_detail_data.get('creditationStatusCode'),
        directionContact=course_detail_data.get('directionContact'),
        directionEmail=course_detail_data.get('directionEmail'),
        courseECTS=course_detail_data.get('courseECTS'),
        courseName=course_detail_data.get('courseName'),
        courseSecretariatContact=course_detail_data.get('courseSecretariatContact'),
        courseSecretariatEmail=course_detail_data.get('courseSecretariatEmail'),
        curricularPlanCode=course_detail_data.get('curricularPlanCode'),
        curricularPlanName=course_detail_data.get('curricularPlanName'),
        degree=course_detail_data.get('degree'),
        departement=course_detail_data.get('departement'),
        futureStudies=course_detail_data.get('futureStudies'),
        hasBranches=course_detail_data.get('hasBranches'),
        infrastructure=course_detail_data.get('infrastructure'),
        objectives=course_detail_data.get('objectives'),
        presentation=course_detail_data.get('presentation'),
        publicationDate=course_detail_data.get('publicationDate'),
        scientificArea=course_detail_data.get('scientificArea'),
        scientificAreaCNAEFCode=course_detail_data.get('scientificAreaCNAEFCode'),
        scientificAreaCode=course_detail_data.get('scientificAreaCode'),
        semesters=course_detail_data.get('semesters'),
        areaScientificMkt=course_detail_data.get('areaScientificMkt'),
        idAreaScientificMkt=course_detail_data.get('idAreaScientificMkt'),
        directorLogin=course_detail_data.get('directorLogin'),
        secretariatCurseId=course_detail_data.get('secretariatCurseId'),
        phoneExtension=course_detail_data.get('phoneExtension'),
        attendanceLocation=course_detail_data.get('attendanceLocation'),
        registration=course_detail_data.get('registration'),
        modEstudo=course_detail_data.get('modEstudo'),
        scheduleAttendee=course_detail_data.get('scheduleAttendee'),
        recipients=course_detail_data.get('recipients'),
        telephoneNumber=course_detail_data.get('telephoneNumber'),
        guestTeachers=course_detail_data.get('guestTeachers'),
        cientific2=course_detail_data.get('cientific2'),
        recordId=course_detail_data.get('recordId'),
        coorCursoContacto=course_detail_data.get('coorCursoContacto'),
        coorCursoEmail=course_detail_data.get('coorCursoEmail')
    )

       # Carrega as unidades curriculares
    curricular_units = data.get('curricularUnits', [])
    for curricular_unit_data in curricular_units:
        curricular_unit = Disciplina.objects.create(
            curricularBranchName=curricular_unit_data.get('curricularUnitName'),
            curricularBranchCode=curricular_unit_data.get('curricularBranchCode'),
            curricularUnitGroupCode=curricular_unit_data.get('curricularUnitGroupCode'),
            curricularYear=curricular_unit_data.get('curricularYear'),
            semester=curricular_unit_data.get('semester'),
            semesterCode=curricular_unit_data.get('semesterCode'),
            curricularIUnitReadableCode=curricular_unit_data.get('curricularIUnitReadableCode'),
            curricularUnitCode=curricular_unit_data.get('curricularUnitCode'),
            ects=curricular_unit_data.get('ects'),
            curricularUnitName=curricular_unit_data.get('curricularUnitName'),
            optionCode=curricular_unit_data.get('optionCode'),
            option=curricular_unit_data.get('option'),
            pubMobIncoming=curricular_unit_data.get('pubMobIncoming'),
            pubMobOutgoing=curricular_unit_data.get('pubMobOutgoing'),
            hrTotalContacto=curricular_unit_data.get('hrTotalContacto'),
            hrTotalContactoInt=curricular_unit_data.get('hrTotalContactoInt')
        )
        curricular_unit.course_detail = course_detail
        curricular_unit.save()
