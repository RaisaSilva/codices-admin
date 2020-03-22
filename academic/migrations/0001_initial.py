# Generated by Django 2.2.8 on 2020-03-15 21:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_comment', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email_comment', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('message_comment', models.TextField(validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Mensaje')),
                ('ip_comment', models.CharField(blank=True, max_length=40, null=True, verbose_name='IP')),
                ('country_name_comment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pais')),
                ('country_code_comment', models.CharField(blank=True, max_length=4, null=True, verbose_name='Código de Pais')),
            ],
            options={
                'verbose_name_plural': 'M. Comentarios Enviados al Site',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acronym_conference', models.CharField(max_length=50, verbose_name='Sigla de la Conferencia')),
                ('name_conference', models.CharField(max_length=200, verbose_name='Nombre')),
                ('place_conference', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lugar')),
                ('start_conference', models.DateField(blank=True, null=True, verbose_name='Inicia')),
                ('end_conference', models.DateField(blank=True, null=True, verbose_name='Termina')),
                ('deadline_conference', models.DateField(blank=True, null=True, verbose_name='Deadline')),
                ('site_conference', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Web Site')),
                ('qualis_cc', models.CharField(blank=True, max_length=2, null=True, verbose_name='Calificación')),
                ('discontinued_conference', models.BooleanField(default=False, verbose_name='Conferencia descontinuada')),
            ],
            options={
                'verbose_name_plural': 'K. Eventos Relacionadas al Instituto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del formulario o documento')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha de subida')),
                ('document', models.FileField(help_text='Este campo acepta diversos formatos (doc, docx, pdf, xls, ppt, pptx, etc.)', upload_to='documentos/')),
                ('hidden', models.BooleanField(default=False, help_text='Ocultar formulario o documento.')),
            ],
            options={
                'verbose_name_plural': 'M. Formularios y Documentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_meeting', models.CharField(max_length=150, verbose_name='Nombre del evento')),
                ('description_meeting', models.TextField(validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción')),
                ('date_meeting', models.DateField(verbose_name='Fecha')),
                ('site_meeting', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Web Site')),
                ('document_meeting', models.FileField(blank=True, help_text='Documento del evento.', null=True, upload_to='eventos/')),
                ('image_meeting', models.ImageField(blank=True, default='images/logo.png', help_text='Publicidad del evento (jpg, gif, png).', null=True, upload_to='eventos/')),
                ('past_event', models.BooleanField(default=False, verbose_name='Excluir noticia')),
            ],
            options={
                'verbose_name_plural': 'J. Noticias del Instituto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Usa tu nombre completo e.g. Juan José Perez.', max_length=150, verbose_name='Nombre')),
                ('join_date', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso al instituto')),
                ('author_name', models.CharField(help_text='Use su nombre de autor como en publicaciones e.g. JJ Perez', max_length=50, verbose_name='Nombre de Autor')),
                ('technical_committee', models.BooleanField(default=False, help_text='Pertenece al Consejo/Comité Técnico', verbose_name='Comité/Consejo Técnico')),
                ('executive_committee', models.BooleanField(default=False, help_text='Pertenece al Consejo/Comité Ejecutivo', verbose_name='Comité/Consejo Ejecutivo')),
                ('editor_committee', models.BooleanField(default=False, help_text='Pertenece al Consejo/Comité Editorial', verbose_name='Consejo/Comité Editor')),
                ('scholarship_committee', models.BooleanField(default=False, help_text='Pertenece al Consejo/Comité de Becas', verbose_name='Consejo/Comité de Becas')),
                ('email', models.EmailField(help_text='De preferencia un email institucional.', max_length=100, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono(s)')),
                ('personal_web', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Web personal')),
                ('cv_web', models.URLField(blank=True, help_text='Linkdin o otro sitio web donde actualiza constantemente su CV, dirección completa https://', max_length=250, null=True, verbose_name='Web de su CV')),
                ('curriculo_vitae', models.FileField(blank=True, help_text='Curriculo vitae del miembro del instituto de investigación.', null=True, upload_to='curriculos_vitae/')),
                ('image', models.ImageField(default='images/logo.png', help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.', upload_to='images/')),
                ('past_member', models.BooleanField(default=False, verbose_name='Ex miembro del instituto')),
                ('hidden_member', models.BooleanField(default=False, verbose_name='Ocultar al miembro de reportes y la página Personal')),
            ],
            options={
                'verbose_name_plural': 'E. Personal del Instituto de Investigación',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_position', models.CharField(max_length=150, verbose_name='Nombre del Cargo')),
                ('position_description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción del cargo')),
                ('document', models.FileField(blank=True, help_text='Descripción del cargo.', null=True, upload_to='cargos/', verbose_name='Documento del Cargo')),
            ],
            options={
                'verbose_name_plural': 'D. Cargos/Puestos del Instituto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.PositiveIntegerField(help_text='Escribe el año del reporte.', validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Año')),
                ('hidden', models.BooleanField(default=False, help_text='Ocultar informe año de vista principal.')),
            ],
            options={
                'verbose_name_plural': 'L. Reportes por año',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ResearchArea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Área de investigación')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha de creación')),
                ('area_description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción del área')),
                ('area_document', models.FileField(blank=True, help_text='Documento describiendo la investigación informativa del Área.', null=True, upload_to='areas_investigacion/', verbose_name='Documento descripción del área')),
                ('area_discontinued', models.BooleanField(default=False, verbose_name='Descontinuada')),
            ],
            options={
                'verbose_name_plural': 'B. Areas de Investigación',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ResearchTopics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Línea de investigación')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha de creación')),
                ('topic_description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción de la linea de investigación')),
                ('topic_document', models.FileField(blank=True, help_text='Documento definiendo la línea de investigación.', null=True, upload_to='lineas_investigacion/', verbose_name='Descripción de la línea')),
                ('topic_discontinued', models.BooleanField(default=False, verbose_name='Descontinuada')),
                ('index_description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(140)], verbose_name='Descripción del index')),
                ('index_image', models.ImageField(default='images/logo.png', help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.', upload_to='lineas_investigacion/')),
                ('index_button', models.CharField(default='Investigación', max_length=30, verbose_name='Nombre del botón del index')),
                ('area', models.ForeignKey(help_text='Seleccione o adicione el Área de Investigación de la Línea de Investigación.', on_delete=django.db.models.deletion.PROTECT, to='academic.ResearchArea')),
            ],
            options={
                'verbose_name_plural': 'C. Lineas de Investigación',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_services', models.CharField(max_length=150, verbose_name='Nombre del servicio')),
                ('description_service', models.TextField(validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción del servicio')),
                ('web_service', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Sitio web del servicio')),
                ('service_triptych', models.FileField(blank=True, help_text='Documento definiendo la línea de investigación.', null=True, upload_to='services/', verbose_name='Tríptico del Servicio')),
                ('image_service', models.ImageField(default='images/logo.png', help_text='Suba imágenes (jpg, gif, png) de igual tamaño en alto y ancho.', upload_to='services/')),
                ('past_service', models.BooleanField(default=False, verbose_name='Descontinuado')),
                ('research_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rt_service', to='academic.ResearchTopics')),
            ],
            options={
                'verbose_name_plural': 'G. Servicios Ofrecidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acronym', models.CharField(max_length=20, verbose_name='Sigla del Proyecto')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del Proyecto')),
                ('website', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Web Site del Proyecto')),
                ('project_document', models.FileField(blank=True, help_text='Documento del proyecto.', null=True, upload_to='proyectos/', verbose_name='Documento del proyecto')),
                ('description', models.TextField(blank=True, help_text='Describir información acerca del proyecto y sus patrocinadores.', null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción')),
                ('impact', models.TextField(blank=True, help_text='Describir los resultados esperados del proyecto', null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Impacto')),
                ('objective', models.TextField(blank=True, help_text='Describir los objetivos del proyecto', null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Objetivo(s)')),
                ('start', models.DateField(blank=True, null=True, verbose_name='Inicio del Proyecto')),
                ('end', models.DateField(blank=True, null=True, verbose_name='Fin del Proyecto')),
                ('proponent', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidad Proponente')),
                ('counterpart_unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidad Contraparte')),
                ('co_executing_unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidad(es) Co-Ejecutoras')),
                ('responsible_unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidad Responsable')),
                ('monitor_project', models.CharField(blank=True, help_text='Lista de monitores separados por coma.', max_length=100, null=True, verbose_name='Monitor(es)')),
                ('chair', models.ForeignKey(help_text='Seleccione al coordinador del Proyecto.', on_delete=django.db.models.deletion.PROTECT, to='academic.People')),
                ('co_chair', models.ManyToManyField(blank=True, help_text='Lista de co-coordinadores del proyecto.', related_name='co_chair_project', to='academic.People')),
                ('collaborator', models.ManyToManyField(blank=True, help_text='Lista de colaboradores del proyecto.', related_name='collaborator_project', to='academic.People')),
                ('member', models.ManyToManyField(blank=True, help_text='Lista de miembros del proyecto.', related_name='member_project', to='academic.People')),
                ('topic', models.ForeignKey(help_text='Seleccione la Línea de Investigación al cual pertenece.', on_delete=django.db.models.deletion.PROTECT, to='academic.ResearchTopics')),
            ],
            options={
                'verbose_name_plural': 'F. Proyectos de Investigación',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='people',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='position', to='academic.Position'),
        ),
        migrations.AddField(
            model_name='people',
            name='research_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rt_people', to='academic.ResearchTopics'),
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Insituto de Investigación ', max_length=150, verbose_name='Nombre del instituto')),
                ('acronym', models.CharField(default='II', max_length=10, verbose_name='Sigla del instituto')),
                ('inauguration', models.DateField(blank=True, null=True, verbose_name='Fecha de inauguración')),
                ('resolution', models.CharField(blank=True, max_length=20, null=True, verbose_name='Resolución')),
                ('faculty', models.CharField(blank=True, default='Facultad de Ciencias Puras y Naturales', max_length=100, null=True, verbose_name='Facultad')),
                ('career', models.CharField(blank=True, default='Carrera de ', max_length=100, null=True, verbose_name='Carrera')),
                ('address', models.TextField(help_text='Describa de forma exacta la dirección del Instituto de Investigación.', validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Dirección')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teléfono(s)')),
                ('fax', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax')),
                ('pob', models.CharField(blank=True, max_length=100, null=True, verbose_name='Casilla Postal')),
                ('website', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Sitio Web del Instituto')),
                ('email', models.EmailField(help_text='De preferencia email institucional @fcpn.edu.bo.', max_length=100, verbose_name='Email del Instituto')),
                ('research_area', models.ManyToManyField(help_text='Seleccione las áreas de investigación del Instituto.', to='academic.ResearchArea')),
            ],
            options={
                'verbose_name_plural': 'A. Instituto de Investigación',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code_course', models.CharField(max_length=10, verbose_name='Código')),
                ('name_course', models.CharField(max_length=100, verbose_name='Curso')),
                ('website_course', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Web Site')),
                ('description_course', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción')),
                ('prerequisites_course', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Pre-requisitos')),
                ('course_document', models.FileField(blank=True, help_text='Documento describiendo el contenido del curso/publicidad.', null=True, upload_to='cursos/', verbose_name='Documento del curso')),
                ('past_course', models.BooleanField(default=False, verbose_name='Descontinuado')),
                ('professor_course', models.ForeignKey(blank=True, help_text='Docente del Curso', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='professor_course', to='academic.People')),
            ],
            options={
                'verbose_name_plural': 'I. Cursos del Instituto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('award', models.CharField(help_text='Nombre completo del premio o reconocimiento.', max_length=200, verbose_name='Premio')),
                ('web_award', models.URLField(blank=True, help_text='Escriba la dirección completa incluido http:// o https://', max_length=250, null=True, verbose_name='Sitio web del premio')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha de la ceremonia de la premiación')),
                ('description_award', models.TextField(validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción')),
                ('awarded', models.ManyToManyField(blank=True, help_text='Seleccione a los miembros premiados del Instituto.', related_name='awarded_award', to='academic.People')),
            ],
            options={
                'verbose_name_plural': 'H. Premios del Instituto',
                'ordering': ['id'],
            },
        ),
    ]