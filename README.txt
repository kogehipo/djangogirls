(1)Cloneする
(2)Djangoの設定
python manage.py collectstatic (本番環境の場合)
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
(3)実行
python manage.py runserver
ブラウザからアクセス
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/

実行環境 (Windows)
python 3.6.8
Django 2.1.7
whitenoise 3.3.1 (本番環境の場合)
