# Статус Развертывания Версий

## Выполненные Команды

Все 7 подсайтов развернуты с версией **1.0**:

### ✅ Развернутые Подсайты

1. **marketplace/developer-guide**
   - Версия: 1.0 (latest, default)
   - Удалена версия: 1.1
   - Команда: `mike deploy + mike set-default + mike delete 1.1`

2. **marketplace/user-guide**
   - Версия: 1.0 (latest, default)
   - Команда: `mike deploy + mike set-default`

3. **platform/developer-guide**
   - Версия: 1.0 (latest, default)
   - Статус: Уже был развернут ранее

4. **platform/user-guide**
   - Версия: 1.0 (latest, default)
   - Команда: `mike deploy + mike set-default`

5. **platform/deployment-on-cloud**
   - Версия: 1.0 (latest, default)
   - Команда: `mike deploy + mike set-default`

6. **storefront/developer-guide**
   - Версия: 1.0 (latest, default)
   - Команда: `mike deploy + mike set-default`

7. **storefront/user-guide**
   - Версия: 1.0 (latest, default)
   - Команда: `mike deploy + mike set-default`

## Проверка Результатов

### Через HTTP Сервер

Запустите HTTP сервер на gh-pages ветке:

```bash
cd /Users/symbot/DEV/vc-docs
git checkout gh-pages
python3 -m http.server 8000
```

Затем откройте в браузере:

- http://localhost:8000/marketplace/developer-guide/
- http://localhost:8000/marketplace/user-guide/
- http://localhost:8000/platform/developer-guide/
- http://localhost:8000/platform/user-guide/
- http://localhost:8000/platform/deployment-on-cloud/
- http://localhost:8000/storefront/developer-guide/
- http://localhost:8000/storefront/user-guide/

### Через Mike List

Проверьте версии каждого подсайта:

```bash
cd /Users/symbot/DEV/vc-docs
git checkout feat/custom_versioning

# Marketplace
mike list -F marketplace/developer-guide/mkdocs.yml --deploy-prefix marketplace/developer-guide
mike list -F marketplace/user-guide/mkdocs.yml --deploy-prefix marketplace/user-guide

# Platform
mike list -F platform/developer-guide/mkdocs.yml --deploy-prefix platform/developer-guide
mike list -F platform/user-guide/mkdocs.yml --deploy-prefix platform/user-guide
mike list -F platform/deployment-on-cloud/mkdocs.yml --deploy-prefix platform/deployment-on-cloud

# Storefront
mike list -F storefront/developer-guide/mkdocs.yml --deploy-prefix storefront/developer-guide
mike list -F storefront/user-guide/mkdocs.yml --deploy-prefix storefront/user-guide
```

### Проверка Структуры gh-pages

```bash
git checkout gh-pages
ls -la marketplace/developer-guide/
ls -la marketplace/user-guide/
ls -la platform/developer-guide/
ls -la platform/user-guide/
ls -la platform/deployment-on-cloud/
ls -la storefront/developer-guide/
ls -la storefront/user-guide/
```

Каждая директория должна содержать:
- `1.0/` - папка с версией 1.0
- `latest/` - симлинк или папка на latest
- `index.html` - редирект на default версию
- `versions.json` - метаданные версий

## Ожидаемые Результаты

### versions.json

Каждый подсайт должен иметь такой файл:

```json
[
  {
    "version": "1.0",
    "title": "1.0",
    "aliases": [
      "latest"
    ]
  }
]
```

### Version Selector

В каждом подсайте должен появиться version selector в правом верхнем углу с единственной версией "1.0".

### URL Структура

- `/marketplace/developer-guide/` → редирект на `/marketplace/developer-guide/1.0/`
- `/marketplace/developer-guide/1.0/` → контент версии 1.0
- `/marketplace/developer-guide/latest/` → алиас на версию 1.0

## Следующие Шаги

1. **Проверить результаты** через HTTP сервер
2. **Закоммитить изменения** в feat/custom_versioning ветке
3. **Пушнуть gh-pages** ветку (если нужно)
4. **Обновить TODO** списки

## Быстрая Проверка

```bash
# Проверить что все версии на месте
cd /Users/symbot/DEV/vc-docs
git checkout gh-pages

# Найти все versions.json файлы
find . -name "versions.json" -type f | sort

# Должны быть:
# ./marketplace/developer-guide/versions.json
# ./marketplace/user-guide/versions.json
# ./platform/deployment-on-cloud/versions.json
# ./platform/developer-guide/versions.json
# ./platform/user-guide/versions.json
# ./storefront/developer-guide/versions.json
# ./storefront/user-guide/versions.json
```

---

**Дата**: 2025-10-15
**Статус**: ✅ Все 7 подсайтов развернуты с версией 1.0

