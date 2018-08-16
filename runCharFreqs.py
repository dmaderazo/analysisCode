import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n','--numGroups', type = int)
parser.add_argument("-i", "--input", help="Coded alignment", type = str)
parser.add_argument("-t", "--threshold", help="Threshold", type = float)
# parser.add_argument("-gpfile", "--groupfile", help="group profile", type = str)

foo = parser.parse_args()
for ix in range(foo.numGroups):
    # print('python file{}.py'.format(ix))
    gpFile = '{}.{}grps.p{}'.format(foo.input,foo.numGroups,ix)
    subprocess.call('python ~/bin/getCharFreqs.py -i {} -t {} -gpfile {} -o blah'.format(foo.input, foo.threshold,gpFile),shell=True)

    # subprocess.call(['python','~/bin/getCharFreqs.py','-i','{}'.format(foo.input),'-t','{}'.format(foo.threshold),'-gpfile', gpFile])

    #subprocess.run('python file{}.py'.format(ix), shell=True)