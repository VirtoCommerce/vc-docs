# Чеклист для тестирования версионированной документации

## ⚠️ Важно: перед тестированием

Убедитесь, что у вас есть версионированный контент в `gh-pages` ветке!

### Проверка наличия версий

```bash
cd /Users/symbot/DEV/vc-docs
git checkout gh-pages
ls -la marketplace/developer-guide/
```

Вы должны увидеть:
- `1.0/` (или другую версию)
- `versions.json`
- `index.html` (редирект на версию по умолчанию)

Если этих файлов нет - сначала задеплойте версию!

## Шаг 1: Деплой версии 1.0 (если еще не сделано)

```bash
# Вернитесь на рабочую ветку
git checkout feat/custom_versioning

# Запустите version manager
python3 version-manager.py

# Выберите опцию 1 (Deploy version to ALL subsites)
# Введите версию: 1.0
# Set as 'latest'? y
# Set as default version? y
# Push to GitHub immediately? y
```

Это создаст версию 1.0 для всех подсайтов и запушит в `gh-pages`.

## Шаг 2: Проверка деплоя

```bash
# Переключитесь на gh-pages
git checkout gh-pages

# Проверьте структуру
ls -la marketplace/developer-guide/
ls -la platform/developer-guide/
```

Вы должны увидеть:
```
marketplace/developer-guide/
├── 1.0/
│   ├── index.html
│   ├── assets/
│   └── ...
├── versions.json
└── index.html
```

## Шаг 3: Локальное тестирование

Теперь можете тестировать:

### Вариант А: Простой тест (без Docker)

```bash
git checkout feat/custom_versioning
python3 simple-test.py
```

Откройте http://localhost:8000/platform/developer-guide/1.0/

### Вариант Б: Docker тест

```bash
git checkout feat/custom_versioning
python3 quick-test.py
```

Откройте http://localhost:8080/platform/developer-guide/1.0/

## Что тестировать

✅ **Версионированные URL работают:**
- http://localhost:8000/platform/developer-guide/1.0/
- http://localhost:8000/marketplace/developer-guide/1.0/

✅ **Version selector отображается** в навигации

✅ **Редирект на default версию:**
- http://localhost:8000/platform/developer-guide/ → 1.0

✅ **Latest alias работает:**
- http://localhost:8000/platform/developer-guide/latest/

✅ **Root и intermediate сайты работают:**
- http://localhost:8000/ (root)
- http://localhost:8000/platform/ (intermediate)

✅ **Навигация НЕ перемешивается** между подсайтами

## Возможные проблемы

### Проблема: 404 на всех ссылках

**Причина:** В `gh-pages` ветке нет версионированного контента

**Решение:** Задеплойте версию 1.0 (см. Шаг 1)

### Проблема: Version selector не отображается

**Причина:** Отсутствует `versions.json`

**Решение:**
```bash
git checkout gh-pages
cat marketplace/developer-guide/versions.json
```
Если файла нет - пересоздайте деплой через version-manager

### Проблема: Навигация перемешивается

**Причина:** Root `mkdocs.yml` включает все подсайты

**Решение:** Уже исправлено в `action.yml` - используется временный `mkdocs-temp-root.yml` без подсайтов

### Проблема: Nginx infinite redirect

**Причина:** Nginx конфигурация была неправильной

**Решение:** Уже исправлено в `nginx.versioned.conf` - заменен `try_files $uri $uri/ /index.html` на `try_files $uri $uri/ $uri/index.html =404`

## CI/CD деплой

После успешного локального тестирования можете запустить workflow:

1. Перейдите в GitHub Actions
2. Запустите `virtocommerce.com docs versioned`
3. Укажите версию (например, `1.0`)
4. Включите `setAsLatest` и/или `setAsDefault`

Workflow:
1. Задеплоит версию для всех подсайтов
2. Скопирует контент из gh-pages
3. Соберет root и intermediate сайты
4. Создаст Docker image
5. Задеплоит на production

