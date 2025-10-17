FROM nginx:alpine

RUN rm /usr/share/nginx/html/index.html \
    && mkdir -p /usr/share/nginx/html \
    && apk update && apk add -u gettext

# Copy versioned documentation (from gh-pages + root/intermediate sites)
COPY ./vc-docs/site /usr/share/nginx/html

# Copy nginx configuration for versioned setup
COPY ./nginx.versioned.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

