# Локальное тестирование версионированной документации

## Самый простой способ (рекомендуется)

Используйте Python скрипты для тестирования:

### Вариант 1: Простой тест

```bash
cd /Users/symbot/DEV/vc-docs
python3 simple-test.py
```

Откройте http://localhost:8000

**Что делает:**
- Экспортирует контент из gh-pages (версионированные подсайты)
- Билдит root сайт БЕЗ подсайтов (избегает конфликтов)
- Билдит intermediate сайты (marketplace/, platform/, storefront/)
- Мержит все вместе с приоритетом версионированному контенту
- Запускает Python HTTP сервер
- ✅ Не требует Docker

### Вариант 2: Быстрый Docker тест

```bash
cd /Users/symbot/DEV/vc-docs
python3 quick-test.py
```

Откройте http://localhost:8080

**Что делает:**
- Экспортирует контент из gh-pages (версионированные подсайты)
- Билдит root сайт БЕЗ подсайтов (избегает конфликтов)
- Билдит intermediate сайты (marketplace/, platform/, storefront/)
- Мержит все вместе с приоритетом версионированному контенту
- Билдит Docker image с nginx
- Запускает контейнер
- ✅ Полная эмуляция продакшна

### Вариант 3: Полный тест

```bash
cd /Users/symbot/DEV/vc-docs
python3 test-versioned-locally.py
```

Откройте http://localhost:8080

**Что делает:**
- Деплоит версию 1.0 для всех подсайтов
- Экспортирует контент из gh-pages
- Билдит root и intermediate сайты
- Билдит Docker image с nginx
- Запускает контейнер

## Альтернативный способ (с копированием)

Если не хотите переключать ветку:

```bash
# 1. Сохраните текущую ветку
CURRENT_BRANCH=$(git branch --show-current)

# 2. Переключитесь на gh-pages
git checkout gh-pages

# 3. Создайте временную папку с контентом
mkdir -p ../vc-docs-test
rsync -a --exclude='.git' ./ ../vc-docs-test/

# 4. Вернитесь на рабочую ветку
git checkout $CURRENT_BRANCH

# 5. Запустите сервер из временной папки
cd ../vc-docs-test
python3 -m http.server 8000

# 6. После тестирования удалите временную папку
cd ..
rm -rf vc-docs-test
```

## Полное тестирование с Docker

Если нужно протестировать полностью как в продакшне (с nginx):

```bash
# 1. Перейдите в директорию vc-docs
cd /Users/symbot/DEV/vc-docs

# 2. Экспортируйте gh-pages контент
git checkout gh-pages
mkdir -p site
rsync -a --exclude='.git' ./ site/
git checkout -

# 3. Билд root и intermediate сайтов
cat > mkdocs-temp-root.yml << 'EOF'
INHERIT: mkdocs.yml
nav:
    - Home: index.md
EOF

mkdocs build -f mkdocs-temp-root.yml -d site-root-temp
mkdocs build -f storefront/mkdocs.yml -d site-storefront-temp
mkdocs build -f platform/mkdocs.yml -d site-platform-temp
mkdocs build -f marketplace/mkdocs.yml -d site-marketplace-temp

rsync -a --ignore-existing site-root-temp/ site/
mkdir -p site/storefront site/platform site/marketplace
rsync -a --ignore-existing site-storefront-temp/ site/storefront/
rsync -a --ignore-existing site-platform-temp/ site/platform/
rsync -a --ignore-existing site-marketplace-temp/ site/marketplace/

# 4. Подготовка Docker
cp -r site vc-docs/
cp -r ../vc-github-actions/update-virtocommerce-docs-versioned/docker/* ./

# 5. Билд и запуск Docker
docker build -t vc-docs-versioned:local .
docker run --rm -p 8080:80 vc-docs-versioned:local

# Откройте http://localhost:8080
```

## Что тестировать

- ✅ **Навигация не перемешивается** между разными подсайтами
- ✅ **Version selector работает** в навигации
- ✅ **Ссылки работают** корректно
- ✅ **Root и intermediate сайты** загружаются
- ✅ **Версионированные URL** работают (например, `/platform/developer-guide/1.0/`)
- ✅ **Latest alias** редиректит на нужную версию

