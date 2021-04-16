# version: '3'

# services:
#  class-offering:
#   image: php:7.2-apache
#   volumes:
#    - ./classes:/var/www/html
#   ports:
#    - 5001:80
#  website:
#   image: php:7.2-apache
#   volumes:
#    - ./website:/var/www/html
#   ports:
#    - 5000:80
#   depends_on:
#    - class-offering

########################################################
            
# version: '3.3'

# services:
#     db:
#         image: mysql:5.7
#         volumes:
#           - db_data:/var/lib/mysql
#         restart: always
#         environment:
#             MYSQL_ROOT_PASSWORD: somewordpress
#             MYSQL_DATABASE: wordpress
#             MYSQL_USER: wordpress
#             MYSQL_PASSWORD: wordpress

#     wordpress:
#         depends_on:
#           - db
#         image: wordpress:latest
#         ports:
#           - "8000:80"
#         restart: always
#         environment:
#           WORDPRESS_DB_HOST: db:3306
#           WORDPRESS_DB_USER: wordpress
#           WORDPRESS_DB_PASSWORD: wordpress
#           WORDPRESS_DB_NAME: wordpress
# volumes:
#     db_data: {}

# <div style="display : flex">
#   <form >
#     <input placeholder="이름을 입력해주세요">
#     <button>클릭</button>
#   </form> 
# </div>