This will work as long as the user has created a key and run ssh-copy-id on the remote host
which could probably set up in paramiko but let's not worry about it.

    ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect('hostname')
        except paramiko.AuthenticationException:
            sys.exit("Authentication failed - is your SSH key set up?   \
                      ssh-copy-id hostname")
        return(ssh)


