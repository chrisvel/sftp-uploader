import paramiko
import shutil
import glob
import config
from logalert import logalert

#create a new LogAlert object
logalert = logalert.LogAlert()

class SftpFilesUploader(object):
    """ Uploads files from locally to the Remote Sftp location """
    sftpURL = config.SFTP_URL
    localDIR = config.LOCAL_DIR
    localBackupDIR = config.LOCAL_BACKUP_DIR
    remoteDIR = config.REMOTE_DIR
    timeOut = config.TIMEOUT

    def __init__(self):
        self.sftpURL = config.SFTP_URL
        self.localDIR = config.LOCAL_DIR
        self.localBackupDIR = config.LOCAL_BACKUP_DIR
        self.remoteDIR = config.REMOTE_DIR
        self.timeOut = config.TIMEOUT
        self.ssh = None
        self.sftp = None
        self.filesToUpload = []

    def connecttosftp(self, username, password):
        """ Opens a connection to sftp site """
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.sftpURL, username=username, password=password, timeout=self.timeOut)
            self.sftp = self.ssh.open_sftp()

            logalert.lognalertaction("Successful connection to Sftp made.",'info')
        except Exception as e:
            logalert.lognalertaction(e,'warn')

    def getremotesftpfilesstatus(self):
        """ Gets remote Sftp site files' status """
        try:
            logalert.lognalertaction("Checking for files in remote Sftp folder.",'info')
            logalert.lognalertaction( str(self.sftp.listdir(self.remoteDIR)),'info')
            sftpFdlFiles = self.sftp.listdir(self.remoteDIR)
            if (len(sftpFdlFiles) == 0):
                logalert.lognalertaction("No files found in remote Sftp folder",'info')
            else:
                logalert.lognalertaction( "(" + str(len(sftpFdlFiles)) + ") files found in remote Sftp folder",'info')
        except IOError as e:
            logalert.lognalertaction(e,'warn')

    def getlocalfilesstatus(self):
        """ Gets local files """
        try:
            # check for files in local folder
            logalert.lognalertaction("Checking for files in local directory",'info')
            logalert.lognalertaction(str(glob.glob1(self.localDIR, "OR*.txt")),'info')
            for localFile in glob.glob1(self.localDIR, "OR*.txt"):
                self.filesToUpload.append(localFile)
                # print the amount of files that wait to be uploaded
            logalert.lognalertaction("(" + str(len(self.filesToUpload)) + ") file(s) to upload",'info')
        except IOError as e:
            logalert.lognalertaction("IOError",'warn')
        except EOFError as e:
            logalert.lognalertaction("EOFError",'warn')

    def uploadfiles(self):
        """ Uploads files to the Remote sftp site"""
        if len(self.filesToUpload) > 0 :
            logalert.lognalertaction("Uploading files to remote Sftp site",'info')
            for file in self.filesToUpload:
                logalert.lognalertaction("[" + file + "]",'info')
                try:
                   self.sftp.put (self.localDIR + file, self.remoteDIR + file)
                   shutil.move (self.localDIR + file, self.localBackupDIR + file)
                except paramiko.SSHException as e:
                   logalert.lognalertaction(e,'warn')
                except IOError as e:
                    logalert.lognalertaction("IOError",'warn')
                except EOFError as e:
                    logalert.lognalertaction("EOFError",'warn')
                logalert.lognalertaction("File uploaded successfully",'info')
            self.sftp.close()
        else:
            pass