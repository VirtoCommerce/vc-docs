# GitHub Actions для Версионированной Документации

## Обзор

Создана новая GitHub Action конфигурация для деплоя версионированной документации с использованием Mike.

## Расположение

- **Репозиторий**: `VirtoCommerce/vc-github-actions`
- **Папка**: `update-virtocommerce-docs-versioned/`
- **Action**: `VirtoCommerce/vc-github-actions/update-virtocommerce-docs-versioned@main`

## Структура

```
vc-github-actions/
├── update-virtocommerce-docs/          # Старая конфигурация (без версионирования)
│   ├── action.yml
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── nginx.default.conf
│   └── README.md
│
└── update-virtocommerce-docs-versioned/ # Новая конфигурация (с версионированием)
    ├── action.yml
    ├── docker/
    │   ├── Dockerfile
    │   └── nginx.versioned.conf
    ├── .github/workflows/
    │   └── deploy-versioned-docs.yml.example
    └── README.md
```

## Ключевые Отличия

### 1. Неверсионированная Конфигурация (`update-virtocommerce-docs`)

**Характеристики:**
- Простая сборка всех сайтов
- URL: `/marketplace/developer-guide/`
- Нет версионирования
- Нет селектора версий
- Nginx: `nginx.default.conf`
- Docker image: `docs`

**Использование:**
```yaml
- uses: VirtoCommerce/vc-github-actions/update-virtocommerce-docs@main
  with:
    azureSubscriptionId: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    # ... другие параметры
```

### 2. Версионированная Конфигурация (`update-virtocommerce-docs-versioned`)

**Характеристики:**
- Независимое версионирование каждого подсайта
- URL: `/marketplace/developer-guide/1.0/`
- Mike интеграция
- Селектор версий
- Nginx: `nginx.versioned.conf`
- Docker image: `docs-versioned`

**Использование:**
```yaml
- uses: VirtoCommerce/vc-github-actions/update-virtocommerce-docs-versioned@main
  with:
    version: '3.2025-S13'
    setAsLatest: 'true'
    setAsDefault: 'false'
    azureSubscriptionId: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    # ... другие параметры
```

## Параметры Action

### Обязательные

| Параметр | Описание | Пример |
|----------|----------|--------|
| `version` | Версия для развертывания | `3.2025-S13`, `1.0` |
| `azureSubscriptionId` | Azure Subscription ID | `${{ secrets.AZURE_SUBSCRIPTION_ID }}` |
| `azureResourceGroupName` | Azure Resource Group | `${{ secrets.AZURE_RESOURCE_GROUP }}` |
| `azureWebAppName` | Azure WebApp Name | `${{ secrets.AZURE_WEBAPP_NAME }}` |
| `azureTenantId` | Azure Tenant ID | `${{ secrets.AZURE_TENANT_ID }}` |
| `azureApiKey` | Azure API Key | `${{ secrets.AZURE_API_KEY }}` |
| `azureAppId` | Azure App ID | `${{ secrets.AZURE_APP_ID }}` |
| `dockerRegistry` | Docker Registry URL | `${{ secrets.DOCKER_REGISTRY }}` |
| `dockerUsr` | Docker Username | `${{ secrets.DOCKER_USERNAME }}` |
| `dockerPwd` | Docker Password | `${{ secrets.DOCKER_PASSWORD }}` |

### Опциональные

| Параметр | Default | Описание |
|----------|---------|----------|
| `setAsLatest` | `true` | Установить как 'latest' алиас |
| `setAsDefault` | `false` | Установить как default версию |

## Процесс Работы Action

### Шаги Выполнения

1. **Checkout vc-docs** - Клонирование репозитория с полной историей
2. **Setup Python** - Установка Python 3.x
3. **Install MkDocs and Mike** - Установка всех зависимостей:
   - mkdocs-material
   - mike
   - все необходимые плагины
4. **Configure Git** - Настройка git для github-actions bot
5. **Build and deploy versioned documentation** - Запуск `build-versioned.sh`:
   - Развертывание версий для всех 7 подсайтов
   - Обновление gh-pages ветки
6. **Export from gh-pages** - Экспорт версионированного контента из gh-pages
7. **Build non-versioned sites** - Сборка root и промежуточных сайтов
8. **Prepare Docker context** - Подготовка файлов для Docker
9. **Build and Push Docker** - Сборка и отправка Docker image

### Структура Деплоя

После выполнения action создается следующая структура:

```
site/
├── index.html                           # Root site (non-versioned)
├── marketplace/                         # Intermediate site
│   ├── index.html
│   ├── developer-guide/                 # Versioned subsite
│   │   ├── 1.0/                        # Version 1.0
│   │   ├── 1.1/                        # Version 1.1
│   │   ├── latest/                     # Alias to latest version
│   │   ├── index.html                  # Redirect to default
│   │   └── versions.json               # Version metadata
│   └── user-guide/                      # Versioned subsite
│       ├── 1.0/
│       └── versions.json
├── platform/
│   ├── index.html
│   ├── developer-guide/
│   │   ├── 3.2025-S13/
│   │   ├── latest/
│   │   └── versions.json
│   ├── user-guide/
│   │   └── versions.json
│   └── deployment-on-cloud/
│       └── versions.json
└── storefront/
    ├── index.html
    ├── developer-guide/
    │   └── versions.json
    └── user-guide/
        └── versions.json
```

## Настройка Workflow в vc-docs

### 1. Создать Workflow Файл

Создайте файл `.github/workflows/deploy-versioned-docs.yml` в репозитории `vc-docs`:

```yaml
name: Deploy Versioned Documentation

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to deploy'
        required: true
        type: string
      setAsLatest:
        description: 'Set as latest'
        required: false
        type: boolean
        default: true
      setAsDefault:
        description: 'Set as default'
        required: false
        type: boolean
        default: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Extract version
        id: version
        run: |
          if [ "${{ github.event_name }}" == "workflow_dispatch" ]; then
            echo "VERSION=${{ github.event.inputs.version }}" >> $GITHUB_OUTPUT
          else
            VERSION="${GITHUB_REF#refs/tags/v}"
            echo "VERSION=$VERSION" >> $GITHUB_OUTPUT
          fi

      - name: Deploy Versioned Docs
        uses: VirtoCommerce/vc-github-actions/update-virtocommerce-docs-versioned@main
        with:
          version: ${{ steps.version.outputs.VERSION }}
          setAsLatest: 'true'
          setAsDefault: 'false'
          # Add all required secrets
```

### 2. Настроить Secrets

В Settings → Secrets and variables → Actions добавьте:

- `AZURE_SUBSCRIPTION_ID`
- `AZURE_RESOURCE_GROUP`
- `AZURE_WEBAPP_NAME`
- `AZURE_TENANT_ID`
- `AZURE_API_KEY`
- `AZURE_APP_ID`
- `DOCKER_REGISTRY`
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

## Использование

### Автоматический Деплой при Создании Tag

```bash
# Создать и отправить tag
git tag v3.2025-S13
git push origin v3.2025-S13

# Workflow запустится автоматически
```

### Ручной Деплой через UI

1. Перейти в Actions → Deploy Versioned Documentation
2. Нажать "Run workflow"
3. Ввести параметры:
   - Version: `3.2025-S13`
   - Set as latest: ✓
   - Set as default: ☐
4. Нажать "Run workflow"

### Через GitHub CLI

```bash
gh workflow run deploy-versioned-docs.yml \
  -f version=3.2025-S13 \
  -f setAsLatest=true \
  -f setAsDefault=false
```

## Nginx Конфигурация

### Версионированная Конфигурация (`nginx.versioned.conf`)

**Основные правила:**

1. **Version selector JSON**:
   ```nginx
   location ~ ^/(marketplace|platform|storefront)/(developer-guide|user-guide|deployment-on-cloud)/versions\.json$ {
       add_header Content-Type application/json;
       add_header Access-Control-Allow-Origin *;
   }
   ```

2. **Version aliases** (latest, stable):
   ```nginx
   location ~ ^/(marketplace|platform|storefront)/(developer-guide|user-guide|deployment-on-cloud)/(latest|stable)/?$ {
       try_files $uri $uri/ $uri/index.html =404;
   }
   ```

3. **Versioned content**:
   ```nginx
   location ~ ^/(marketplace|platform|storefront)/(developer-guide|user-guide|deployment-on-cloud)/([0-9]+\.[0-9]+|[0-9]+\.[0-9]+-S[0-9]+|latest|stable)/ {
       try_files $uri $uri/ =404;
   }
   ```

4. **Legacy redirects**:
   ```nginx
   rewrite ^/new/user_docs/(.*)$ /platform/user-guide/latest/$1 permanent;
   ```

## Тестирование

### Локальное Тестирование Docker Image

```bash
# Собрать локально
docker build -t docs-versioned:test .

# Запустить
docker run -p 8080:80 docs-versioned:test

# Проверить
open http://localhost:8080/marketplace/developer-guide/1.0/
```

### Проверка Версий

После деплоя проверьте:

1. **Version selector появляется**:
   ```bash
   curl https://docs.virtocommerce.org/marketplace/developer-guide/versions.json
   ```

2. **Latest alias работает**:
   ```bash
   curl -I https://docs.virtocommerce.org/marketplace/developer-guide/latest/
   ```

3. **Конкретная версия доступна**:
   ```bash
   curl -I https://docs.virtocommerce.org/marketplace/developer-guide/1.0/
   ```

## Миграция

### От Неверсионированной к Версионированной

1. **Текущая ситуация**:
   - URL: `https://docs.virtocommerce.org/platform/developer-guide/`
   - Нет версий

2. **После миграции**:
   - URL: `https://docs.virtocommerce.org/platform/developer-guide/1.0/`
   - Version selector доступен
   - Legacy URL редиректят на `/latest/`

3. **Шаги миграции**:
   ```bash
   # 1. Развернуть первую версию
   gh workflow run deploy-versioned-docs.yml -f version=1.0 -f setAsDefault=true

   # 2. Обновить DNS/CDN (если необходимо)

   # 3. Переключить workflow на версионированный action
   ```

## Troubleshooting

### Version Selector Не Появляется

**Проблема**: Селектор версий не отображается.

**Решение**:
1. Проверить `versions.json`:
   ```bash
   curl https://docs.virtocommerce.org/marketplace/developer-guide/versions.json
   ```
2. Проверить nginx конфигурацию
3. Очистить кэш CDN/браузера

### Ошибка "Failed to deploy"

**Проблема**: Action падает с ошибкой.

**Решение**:
1. Проверить logs в GitHub Actions
2. Проверить, что все secrets настроены
3. Проверить права доступа к gh-pages ветке

### Версия Не Обновляется

**Проблема**: Новая версия не появляется после деплоя.

**Решение**:
1. Проверить gh-pages ветку:
   ```bash
   git checkout gh-pages
   ls marketplace/developer-guide/
   ```
2. Проверить versions.json
3. Пересобрать Docker image

## Поддержка

Для вопросов и проблем:

1. Проверьте [VERSIONING.md](VERSIONING.md)
2. Проверьте логи GitHub Actions
3. Проверьте nginx logs в Azure
4. Контакт DevOps команды

## Дополнительные Ресурсы

- [Mike Documentation](https://github.com/jimporter/mike)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [vc-docs VERSIONING.md](VERSIONING.md)

