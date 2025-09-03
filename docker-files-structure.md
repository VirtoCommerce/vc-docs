# Docker Files Structure for Your Action

Для того чтобы `.github-actions-versioned.yml` работал с вашим существующим Dockerfile, 
структура файлов в вашем action должна быть:

```
your-action/
├── action.yml (или .github-actions-versioned.yml)
└── docker/
    ├── Dockerfile
    └── nginx.default.conf
```

## Dockerfile (docker/Dockerfile):
```dockerfile
FROM nginx:alpine

RUN rm /usr/share/nginx/html/index.html \
    && mkdir -p /usr/share/nginx/html/2.0 \
    && apk update && apk add -u gettext

COPY ./vc-docs/site /usr/share/nginx/html
COPY ./nginx.default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

## nginx.default.conf (docker/nginx.default.conf):
Ваш существующий nginx конфиг, но с поддержкой версионирования mike:

```nginx
server {
    listen 80;
    server_name _;
    root /usr/share/nginx/html;
    index index.html;

    # Handle mike version routing
    location / {
        try_files $uri $uri/ $uri/index.html =404;
    }
    
    # Handle version selector and assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        try_files $uri =404;
    }
    
    # Optional: Redirect root to latest version if needed
    # location = / {
    #     return 301 /latest/;
    # }
}
```

## Как это работает:

1. **`./build.ps1`** → создает `vc-docs/site` (обычная сборка)
2. **Mike deployment** → создает версионированный контент в gh-pages branch
3. **Prepare step** → заменяет `vc-docs/site` версионированным контентом
4. **Docker build** → использует ваш существующий Dockerfile с версионированным контентом
5. **Результат** → Docker образ содержит все версии сразу

## Ключевые изменения:

- ✅ **Dockerfile остается тот же** - копирует из `./vc-docs/site`
- ✅ **nginx.conf остается похожий** - но с поддержкой маршрутизации версий mike
- 🆕 **`vc-docs/site` теперь содержит** все версии вместо одной
- 🆕 **Docker tag** теперь версионированный: `3.800-123` вместо просто `123`