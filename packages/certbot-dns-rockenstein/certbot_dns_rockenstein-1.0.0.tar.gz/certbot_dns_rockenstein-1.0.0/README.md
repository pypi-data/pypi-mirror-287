certbot-dns-rockenstein
=======================

rockenstein DNS Authenticator plugin für Certbot

Dieses Plugin hilft bei der Automatisierung der Erstellung und Verlängerung von Let's Encrypt-Zertifikaten in Verbindung mit Certbot.

Im Rahmen des ``dns-01`` Verfahrens werden automatisch TXT-Records der entsprechenden Domain hinzugefügt und entfernt.

Installation
------------

    pip install certbot-dns-rockenstein

Named Arguments
---------------

Um den Certbot in Verbindung mit der RoxApi der rockenstein AG zu verwenden, fügen Sie folgende Argumente Ihrem Certbot-Aufruf hinzu:



**Required**
```
--authenticator dns-rockenstein
```

Legt fest, dass dieses Plugin verwendet werden soll.

**Required**
```
--dns-rockenstein-credentials <credentials-ini-file>
```

Dieser Parameter gibt an, in welcher Datei die Credentials zur Authentifizierung zu finden sind.

Der Inhalt der Datei muss dann wie folgt aussehen:
```
dns_rockenstein_token=<token>
dns_rockenstein_url=https://api.rox.net
```

Der Token kann im Service-Portal der rockenstein AG generiert werden.

Die Zeile mit der **dns_rockenstein_url** ist **optional**. Bei Angabe überschreibt sie die URL der rockenstein-API.

Bei Fragen hierzu wenden Sie sich bitte an unseren Support.

**Optional**
```
--certbot-dns-rockenstein-url <url>
```

Legt eine alternative URL der rockenstein RoxApi fest. Im Normalfall muss hier nichts angegeben werden.

**Optional**
```
--certbot-dns-rockenstein-ignore-ssl
```
Deaktiviert die Überprüfung des SSL-Zertifikats der rockenstein RoxApi. Dies dient nur zum Einsatz in Verbindung mit einer lokalen API-Entwicklungsumgebung und ist für den normalen Einsatz nicht relevant.

**Optional**
```
--dns-rockenstein-propagation-seconds
```

Überschreibt den Standard-Wert von 120 Sekunden. Das ist die Zeit, die nach dem DNS-Eintrag und der Überprüfung dessen abgewartet wird.

Beispiele
---------

Ein typischer Aufruf zum Erstellen von einem neuen SSL-Zertifkat ist:

```
certbot certonly --authenticator dns-rockenstein --dns-rockenstein-credentials <path to credentials ini file> -m <admin-email-adresse> --agree-tos --non-interactive -d <fully-qualified-domain-name>
```

