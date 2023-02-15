import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

meine_adresse = ''
mein_passwort = 'Passwort'
host_adresse = 'smtp-mail.'
email_port = 
#Pfad zu Dateien im Anhang
pfad=""

class Email:
    #Vornamen und Email-Adressen einlesen
    def getContacts(self, filename):
        namen = []
        emails = []
        self.filename = filename
        with open(file=self.filename, mode="r", encoding="utf-8") as contacsFile:
            for contact in contacsFile:
                namen.append(contact.split()[0])
                emails.append(contact.split()[1])
        return namen, emails

    def getTemplate(self, filename):
        self.filename = filename
        with open(self.filename, mode="r", encoding="utf-8") as templateFile:
            templateFileNachricht = templateFile.read()
        return templateFileNachricht
      
    
    def sendMail(self):
        msg = MIMEMultipart()       # Erstelle Nachricht
        # Vorname in die Nachricht einfügen
        message = self.getTemplate('nachricht.txt')

        # Parameters der Nachricht vorbereiten
        msg['From'] = meine_adresse
        msg['To']= ", ".join(emails)
        msg['CC']= meine_adresse
        msg['Subject'] = "Fehlermeldung"

        # Nachricht hinzufügen
        msg.attach(MIMEText(message))

        #Dateien in Anhang hinzufügen
        dateien=os.listdir(pfad)
        for datei in dateien:
            dateiname=pfad+datei
            msg.attach(MIMEText(open(dateiname).read()))

        # Nachricht über den eingerichteten SMTP-Server abschicken
        s.send_message(msg)

        del msg 
     
s = smtplib.SMTP(host=str(host_adresse), port=email_port)
s.starttls()
s.login(meine_adresse, mein_passwort)
print("SMTP-Verbindung erfolgreich!")
objekt1 = Email()
namen, emails = objekt1.getContacts('kontakte.txt')
print("Namen:" + str(namen))
print("Emails:" + str(emails))
#versendet Mail an alle Kontakte
objekt1.sendMail()
s.quit()