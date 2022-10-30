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

# Start

- clone
- dev container を開く
- python manage.py migrate
- python manage.py runserver