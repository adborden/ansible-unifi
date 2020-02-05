# unifi

Installs the Ubiquiti UniFi contorller on [Ubuntu 16.04](https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-and-Update-via-APT-on-Debian-or-Ubuntu).

_Note: Ubuntu 18.04 is currently not supported. UniFi controller depends on
MongoDB 3.4 or older, but MongoDB only provides 4.x for Ubuntu 18.04._

## Usage

    $ vagrant up


## Keystore

    $ sudo keytool -genkey -keyalg RSA -alias selfsigned -keystore /usr/lib/unifi/data/keystore -storepass aircontrolenterprise -validity 365 -keysize 2048 -destalias unifi
