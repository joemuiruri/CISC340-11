	CISC340-11
	CISC 340 Group Project
	Team Project - Team 11
	Minicom set up:
I.	Set up in CMD:
i.	pi@team11: $ sudo apt-get install minicom
ii.	pi@team11: $ sudo minicom -b 115200 -D /dev/ttyUSB0
iii.	pi@team11: $ minicom -s
iv.	pi@team11: $ minicom -s -c on
v.	pi@team11: $ export MINICOM=”-m -c on”
vi.	pi@team11: $ minicom

	Software set up:
I.	Apache2
1.	pi@team11: $ sudo apt-get update
2.	 pi@team11: $ sudo apt-get upgrade
3.	pi@team11: $ sudo apt install apache2 -y
II.	MariaDB (followed Maria repository guide and sourced below)
1.	pi@team11: $ sudo apt-get install software-properties-common dirmngr
2.	pi@team11: $ sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
3.	pi@team11: $ sudo add-apt-repository 'deb [arch=amd64,i386] https://mirror.herrbischoff.com/mariadb/repo/10.4/debian sid main'
4.	pi@team11: $ sudo apt-get update
5.	pi@team11: $ sudo apt-get install mariadb-server
III.	PHP and MySQL
1.	pi@team11: $ sudo mysql_secure_installation
2.	pi@team11: $ sudo apt install php7.3 php7.3-mbstring php7.3-mysql php7.3-curl php7.3-gd php7.3-curl php7.3-zip -y
IV.	GitHub set up 
1.	pi@team11: $ sudo apt-get install git
2.	pi@team11: $ git config --global user.name "user_name"
3.	pi@team11: $ git config --global user.email "email_id"
4.	pi@team11: $ git remote add origin git@github.com:joemuiruri/CISC340-11.git
V.	Change Permission of folders to enable read/write
1.	pi@team11: $ sudo usermod -a -G www-data pi
2.	pi@team11: $ sudo chown -R -f www-data:www-data /var/www/html
    
	Web Server set up (Assuming Raspberry pi is connected to Laptop):
I.	add "RewriteEngine on" onto new file then save and exit.
1.	pi@team11: $ sudo nano /var/www/html/.htaccess 
	Connect to our Raspbery Pi using PUTTY
o	password: team11
o	ssh pi@team11.local
	Database set up
o	Follow DatabaseReadME in order:
	URL for each Web Page: 
o	Pre-Requirements
1.	Raspberry Pi connected to a Power Supply or USB (MICRO USB to USB connection)
2.	ssh and get a connection with APACHE (APACHE2)
o	URLs
1.	http://team11.local/showuser.php
2.	http://team11.local/addp.php
3.	http://team11.local/newpage.html
	Github General (Assuming you've added the files into your local repository)
I.	ssh (use command below to copy a new file into /var/www/html/CISC340-11)
1.	pi@team11 $ cp -R /var/www/html/NEWFILE /var/www/html/CISC340-11/NEWFILE
II.	Run Commands in this order:
1.	git pull
2.	git add NEWFILE
3.	git commit NEWFILE - m 'Comment'
4.	git push
	Additional Software
I.	sudo apt-get install ufw
II.	sudo systemctl status apache2
III.	sudo apache2ctl configtest 
    
	Raspberry Pi (Power Supply) & Monitor & MICRO HDMI & Keyboard are Connected: 
o	Add on Software to support wireless devices (keyboard, mouse)
	pi@team11: $ sudo add-apt-repository ppa:daniel.pavel/solaar
	pi@team11: $ sudo apt-get update
	Sources:
  1. https://downloads.mariadb.org/mariadb/repositories/#distro=Debian&distro_release=sid--sid&mirror=herrbischoff&version=10.4
  2. https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md
  3. https://pimylifeup.com/raspberry-pi-apache/
  4. https://www.ionos.com/community/hosting/php/use-php-to-insert-information-into-a-mysqlmariadb-database-from-an-html-form/
  5. https://www.tutorialspoint.com/mariadb/mariadb_connection.htm
  6. https://stackoverflow.com/questions/20270879/whats-the-default-password-of-mariadb-on-fedora
  7. https://mariadb.com/kb/en/library/connecting-to-mariadb/
  8. https://help.ubuntu.com/lts/serverguide/httpd.html
  9. https://websiteforstudents.com/setup-apache2-http-https-and-domain-redirects-on-ubuntu-16-04-lts-servers/
  10. https://www.digitalocean.com/community/tutorials/how-to-rewrite-urls-with-mod_rewrite-for-apache-on-ubuntu-16-04
  11. https://httpd.apache.org/docs/2.4/urlmapping.html
  12. https://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/
  13. https://launchpad.net/~daniel.pavel/+archive/ubuntu/solaar
  14. https://linuxhint.com/debian_network_interface_setup/
  15. https://linuxize.com/post/how-to-install-wordpress-with-apache-on-ubuntu-18-04/
  16. https://startingelectronics.org/articles/raspberry-PI/serial-port-connecting-linux/
  17. https://scribles.net/setting-up-serial-communication-between-raspberry-pi-and-pc/
