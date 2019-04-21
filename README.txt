(1)Cloneする
(2)本番環境の場合は
・mysite/local_settings.pyを削除または名前変更
・mysite/settings.pyのALLOWED_HOSTSを設定
(3)Djangoの設定
python manage.py collectstatic (本番環境の場合)
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
(4)実行
python manage.py runserver
gunicorn --bind=0.0.0.0:8000 mysite.wsgi:application (本番環境の場合)
ブラウザからアクセス
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/

実行環境 (Windows)
python 3.6.8
Django 2.1.7 / 2.2
whitenoise 3.3.1 / 4.1.2 (本番環境の場合) バージョンによってソース一部非互換
