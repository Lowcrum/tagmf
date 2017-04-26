# tagmf
Tag amazon resources in mass

### Overview

### Installation

1. Install nginx
```  
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / { try_files $uri @boto3_flask; }
        location @boto3_flask {
          include uwsgi_params;
          uwsgi_pass unix:///tmp/boto3_flask_uwsgi.sock;
        }

}
```

2. install uwsgi and the python uwsgi plugin
3. Pull down the tagmf code
4. run the following in a screen `uwsgi --ini /home/ubuntu/tagmf/boto3_flask_uwsgi.ini`

### Use

### Further Documentatoin and Links
