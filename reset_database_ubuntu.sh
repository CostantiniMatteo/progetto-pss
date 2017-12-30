sudo -u postgres psql -c '\c postgres' \
    -c 'drop database mitalian;' \
    -c 'create database mitalian with owner admin;' && \
./manage.py migrate && \
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" \
    | python manage.py shell
rm media/*.jpg
