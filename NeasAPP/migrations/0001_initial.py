# Generated by Django 4.2 on 2023-04-18 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('SEV', 'Sevilla'), ('CDZ', 'Cádiz'), ('GRA', 'Granada'), ('COR', 'Cordoba'), ('HLV', 'Huelva'), ('JN', 'Jaen'), ('ALM', 'Almeria'), ('MAL', 'Malaga'), ('CAC', 'Caceres'), ('BAD', 'Badajoz'), ('MUR', 'Murcia'), ('ALI', 'Alicante'), ('VAL', 'Valencia'), ('CAST', 'Castellon'), ('ISBL', 'Islas Baleares'), ('TNF', 'Tenerife'), ('LAPM', 'las Palmas'), ('ALB', 'Albacete'), ('CUEN', 'cuenca'), ('TOL', 'Toledo'), ('CDRL', 'Ciudad Real'), ('GUAL', 'Guadalajara'), ('MADR', 'Madrid'), ('TER', 'Teruel'), ('ZAR', 'Zaragoza'), ('H', 'Huesca'), ('TARR', 'Tarragona'), ('LER', 'lerida'), ('BAR', 'Barcelona'), ('GER', 'Gerona'), ('LARJ', 'La Rioja'), ('NAV', 'Navarra'), ('VZY', 'Vizcaya'), ('ALA', 'Alava'), ('CANT', 'Cantabria'), ('AST', 'Asturias'), ('LGO', 'Lugo'), ('ORS', 'Orense'), ('PNVD', 'Pontevedra'), ('LCÑA', 'La Coruña'), ('LN', 'León'), ('PL', 'Palencia'), ('BRG', 'burgos'), ('SOR', 'Soria'), ('VLLD', 'Valladolid'), ('SEG', 'Segovia'), ('AVLA', 'Avila'), ('SAL', 'Salamanca'), ('ZAM', 'Zamora')], max_length=100)),
                ('es_capital', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Operador_tur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cif', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=150)),
                ('fecha_fundacion_oper', models.DateField()),
                ('logo', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=50)),
                ('sitio_web', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=500)),
                ('hora_inicio', models.TimeField(default=None)),
                ('hora_fin', models.TimeField(default=None)),
                ('tematica', models.CharField(choices=[('Gastronómico', 'Gastronomico'), ('Cultural', 'Cultural'), ('Historico', 'Historico'), ('Ocio', 'Ocio'), ('Naturaleza', 'Naturaleza'), ('Religioso', 'Religioso')], max_length=100)),
                ('tramo_horario', models.CharField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=50)),
                ('transporte', models.CharField(choices=[('Turismo', 'Turismo'), ('Ciclomotor', 'Ciclomotor'), ('Motocicleta', 'Motocicleta'), ('Bicicleta', 'Bici'), ('A pie', 'Caminando')], max_length=100)),
                ('valoracion_media', models.FloatField(default=0.0, max_length=4)),
                ('operador_tur', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='NeasAPP.operador_tur')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('Apellidos', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('rol', models.CharField(choices=[('Admin', 'Admin'), ('Cliente', 'Cliente'), ('Operador', 'Operador')], default='Cliente', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Valoracion_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_estrellas', models.IntegerField()),
                ('rutas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeasAPP.ruta')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeasAPP.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_login',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ruta',
            name='usuarios',
            field=models.ManyToManyField(default=None, to='NeasAPP.usuario'),
        ),
        migrations.AddField(
            model_name='operador_tur',
            name='usuario_login',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Monumento_pi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('imagen', models.CharField(max_length=500)),
                ('horario_visita', models.TimeField()),
                ('latitud', models.PositiveIntegerField()),
                ('longitude', models.PositiveIntegerField()),
                ('ciudades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeasAPP.ciudad')),
                ('rutas', models.ManyToManyField(to='NeasAPP.ruta')),
                ('valoraciones', models.ManyToManyField(to='NeasAPP.valoracion_usuario')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='rutas',
            field=models.ManyToManyField(to='NeasAPP.ruta'),
        ),
    ]
