FROM nginx:alpine

#Remove default nginx welcome page
RUN rm -rf /usr/share/nginx/html/*

#Copy site files into container
COPY site/ /usr/share/nginx/html/

EXPOSE 80