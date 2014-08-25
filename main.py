from sftpupload import sftpupload
import datetime, time
import config
import getpass
import os

start_time = datetime.time(config.START_HOUR, config.START_MIN)
end_time = datetime.time(config.END_HOUR,config.END_MIN)
now_is = datetime.datetime.now().time()
current_time = datetime.time(now_is.hour, now_is.minute, now_is.second)
sleepFlag = True

try:
    os.system('cls')
    print("-"*70)
    print("**** Welcome to sftp Uploader v1.2 ****")
    print("-"*70)
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    print("The application is setup to run from {} to {}.".format(start_time, end_time))
    print("The time now is {}.".format(current_time))
    while True:
        now_is = datetime.datetime.now().time()
        current_time = datetime.time(now_is.hour, now_is.minute, now_is.second)
        if start_time < current_time < end_time:
            print ("-"*70)
            if sleepFlag == False:
                sleepFlag = True
                print("Running...")
            sftpUp = sftpupload.SftpFilesUploader()
            sftpUp.connecttosftp(username,password)
            sftpUp.getremotesftpfilesstatus()
            sftpUp.getlocalfilesstatus()
            sftpUp.uploadfiles()
            print("Operation completed successfully.")
            print("Running again in {} minute(s).".format(config.INTERVAL//60))
            time.sleep(config.INTERVAL)
        else:
            if sleepFlag == True:
                print ("-"*70)
                print("Sleeping...")
                sleepFlag = False
            else:
                pass

except KeyboardInterrupt:
    print('You cancelled the operation. Goodbye.')





