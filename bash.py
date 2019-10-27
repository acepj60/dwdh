#codec by dw
import os, sys, fileinput, time
black = '\x1b[0;30m'
blue = '\x1b[0;34m'
ijo = '\x1b[0;32m'
bm = '\x1b[0;36m'
red = '\x1b[0;31m'
purple = '\x1b[0;35m'
brown = '\x1b[0;33m'
abu = '\x1b[0;37m'
gr = '\x1b[1;32m'
Kuning = '\x1b[1;33m'
putih = '\x1b[1;37m'
N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[0;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print '\x1b[0;34m           888 88e   888'Y88   e88'Y88   888'Y88 Y88b Y88   e88'Y88'
print '\x1b[0;34m           888 888b  888 ,'Y  d888  'Y   888 ,'Y  Y88b Y8  d888  'Y'
print '\x1b[0;34m           888 8888D 888C8   C8888       888C8   b Y88b Y C8888'
print '\x1b[0;34m           888 888P  888 ",d  Y888  ,d   888 ",d 8b Y88b   Y888,'
print '\x1b[0;34m           888 88"   888,d88   "88,d88   888,d88 88b Y88b   "88,d88'
print '\x1b[0;32m' + bm + '[' + gr + '+' + bm + ']' + red + '______________________________________________________' + bm + '[' + gr + '+' + bm + ']'
print '\x1b[0;35m     Tools Decrypt dan Encrypt | MADE BY DW SQUAD | JANGAN DEC SC GW ASW'
print '\x1b[0;35m' + bm + '[' + gr + '+' + bm + ']' + red + '______________________________________________________' + bm + '[' + gr + '+' + bm + ']'
print '\x1b[0;35m[' + ijo + '01' + putih + ']' + abu + 'Encript File '
print '\x1b[0;35m[' + purple + '02' + putih + ']' + abu + 'Decrypt File'
print '\x1b[0;35m[' + red + '00' + putih + ']' + abu + 'Exit '

def dekrip():
    try:
        sc = raw_input(ask + W + 'Input Your File ' + G + '|> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Output Your File' + G + ' |> ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch tes.sh')
        os.system('bash ' + out + ' > tes.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'File Berhasil di Decrypt..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Ditemukan!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Input Alamat File /sdcard ' + G + '> ' + W)
        output = raw_input(ask + W + 'Alamat Output File /sdcard ' + G + '> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'File Berhasil Di Encript.'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File tidak ditemukan!'


takok = raw_input(W + 'Input Pilihan' + G + ' |> ')
if takok == '1' or takok == '01':
    enkrip()
elif takok == '2' or takok == '02':
    dekrip()
else:
    print eror + ' Input salah'
