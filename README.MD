Для запуска необходимо установить необходимые пакеты
pip install -r requirements.txt
активировать виртуальное окружение
source your_venv_name/bin/activate
применить миграции и создать бд sqlite
python manage.py makemigrations
python manage.py migrate
запустить как стандартное джанго приложение
python manage.py runserver 8000

в приложение 2 эндпоинта
/links/create/
принимает следующие параметры
original_link строка в формате url обязательный
lifetime  datetime формат с таймзоной опциональный(до какого времени url будет активным)

при успешном ответе возвращает 

original_link строка в формате url обязательный
lifetime  datetime формат с таймзоной опциональный
short_link строка

/<str: short_link>

редиректит на оригинальный url
 если время жизни меньше чем сейчас отдает 404