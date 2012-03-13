import subprocess

class Git:
    '''Helper class for running many of the systems Git commands
       with the subprocess module'''
    
    def __init__(self):
        pass
    
    def run(self, command):
        'runs a command with the subprocess module'
        process = subprocess.Popen(
            command, shell=False, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        
        # wait for our process to complete
        returncode = process.wait()
        message = process.communicate()
        
        # Git will return a status code of 0 on successful execution
        if returncode > 0:
            raise Exception(message[1])
        else:
            return (returncode, message)
    
    def init(self):
        'initialize a empty Git repository'
        command = ['git', 'init']
        results = self.run(command)
        return results
    
    def add_remote(self, name, remote):
        'add a remote to an existing repository'
        command = ['git', 'remote', 'add', name, remote]
        results = self.run(command)
        return results
    
    def clone(self, remote):
        'clone a remote repository to your working directory'
        command = ['git', 'clone', remote]
        results = self.run(command)
        return results
        
    def pull(self, remote, branch):
        'pull from a remote git repository'
        command = ['git', 'pull', remote, branch]
        results = self.run(command)
        return results
    
    def add(self, filepattern):
        'add files to the current repository index'
        command = ['git', 'add', filepattern]
        results = self.run(command)
        return results
    
    def commit(self, message):
        'commit your added changes with the following message'
        command = ['git', 'commit', '-m', message]
        results = self.run(command)
        return results
    
    def push(self, name, branch, force=False):
        'push changes to a remote branch'
        if force:
            command = ['git', 'push', '-f', name, branch]
        else:
            command = ['git', 'push', name, branch]
        results = self.run(command)
        return results
            
        