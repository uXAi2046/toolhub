# 使用 Nginx 作为 Web 服务器
FROM nginx:alpine

# 将所有 HTML 文件和资源复制到 Nginx 默认目录
COPY *.html /usr/share/nginx/html/

# 暴露 80 端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
