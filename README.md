# 開発メモ

参考 URL:  
https://docs.docker.jp/compose/django.html  
https://qiita.com/sey323/items/a4875408a67cea6a8c52  
https://gotohayato.com/content/533/

```bash
docker-compose run web django-admin startproject config .
```

# devcontainer の設定

https://zenn.dev/saboyutaka/articles/9cffc8d14c6684

# localhost では繋がらない

http://127.0.0.1:8000/

# envファイルの作成時の参考
https://maku77.github.io/python/env/dotenv.html

# blackの導入
```bash
black --check .
black .
```

# celery　の導入
https://zats-firm.com/2022/02/05/django_cerery_redis%e3%81%ab%e3%82%88%e3%82%8b%e9%9d%9e%e5%90%8c%e6%9c%9f%e5%87%a6%e7%90%86%e3%81%ae%e5%ae%9f%e8%a3%85/
```bash
pip install celery django-celery-results django-redis
```
```bash
celery -A config worker -l info

```

# Start

- clone
- dev container を開く
- python manage.py migrate
- python manage.py runserver