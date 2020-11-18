from subprocess import Popen, STDOUT, PIPE

def system (command, err=STDOUT, out=PIPE):
    p = Popen(command, shell=True, stderr=err, stdout=out)
    output = p.communicate()[0]
    return output.decode('utf-8') 

output = system('ls /')
print(output)
