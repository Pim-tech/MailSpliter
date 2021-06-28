#!/usr/bin/env python3
#This script tries to order mailboxes

"""
A non interractive  mail splitter/Organizer

Usage: splitmail.py OPTIONS [-k|--keep <directory>] [-u|--unknown_dir <directory>] [-e|--exclude_file <pattern>] [-j '<operation1>,[<operation2],...]'

Options:
    -h
    --help
        Print this message and exit.

    -i <directory>
    --input-dir=directory
        Specifies the input directory from were are the emails to filter are, see -R option

    -R 
    --Recurse
        when -i is given the input directory is parse including all its sub-directories and so on.
        Note: be carefull to not re...parse an ouput data, you will write into a file into with you are
        actualy reading, and this will probably not stop until a disk full error.
    -f
    -file
        Instead of reading all the files into a given directory, reads only one file content.
        This option can replace -i option

    -o <directory>
    --output-dir directory
        Specifies the output directory were the filtered mail will be stored
    -m
    --move
        Moves mail for one dir to another : input dir and output dir MUST not be the same 
        This is the behavior needed if you need to parse again an old repository and firter it again
    
    -r
    --roll
        This is the behavior for rolling mail : input-dir and output dir should be the same directories
        Emails Older than compress_histo_days will be appended and compressed into .gz files 
        and email's contents older than retaindays will be written to new .mail.new files
        and mail contents youger than retaindays (recents mails) will be kept (into keepdir).
        finally, .mail.new files are renamed to .mail files thus rotating
        -i and -o should specify the same directory with this option.
        it is used to put the too old datas from .mail files into compressed .mail.gz and then
        reduce the .mail files.
    
    -k <directory>
    --keep <directory>
        Directory where to put recent mail: it must not be the input_dir because the files cannot be red
        and writen at the same time.
        splitmail considers that the last rotation must be done manualy,

    -u <directory>
    --unknown-dir <directory>
        Directory where we put mail that we could not filter according the given rules
    
    -e <file(s) pattern>
    --exclude-files
       Files to exclude when input_dir is given.
       Must be given as a regex (re) pattern

    -j <filter[,...]> 
    --jump <filter[,...]>
       Do not process the indicaded filter.
       Actualy filters are:
        - date
        - mail
       if you jump filter date the ouput will not be split in timestamped files.
       if you jump filter mail the output box will be just be split for date
       You must leave at least one or more filters.
       note that other filters can (will) be added later.

    -O <output-prefix>
    --Output-prefix <output-prefix>
       When we do not filter mail we must know the prefix that will be choose.
       it defaults to the output-dir if not given
    

"""

import sys
import getopt
import os
import gzip
import re
from time import *
from os.path import isfile, exists, basename, dirname
from lib import mails

h_parse = None

test = 0

parse =       None
file2parse =  None
input_dir  =  None 
output_prefix =  None
output_dir   = None
keepdir= './new_mail'
unknown_dir = './unknown_mail'
log_dir = "./log/"
tstamp=strftime("_%d_%m_%Y-%H%M")
log_file = log_dir + '/' + "splitmail" + tstamp + ".log"

exclude_files = None

try:
    if not os.path.exists(log_dir):
        print("Creating directory: '" + log_dir + "'\n")
        os.makedirs(log_dir , 0o777)

    print("Writing log file '" + log_file + "'\n")
    logd = open(log_file,'a',encoding = 'LATIN-1')
except OSError as msg:
    msg = "Error : '" + dirn + "' : '" + msg
    logd.write(msg)
    print(msg)
    sys.exit(1)


jump       = {}
filters = None

message_break = 'From '
messagebreak_pattern = re.compile('^From .+? \d{2}:\d{2}:\d{2} \d{4}')

header_pattern     = re.compile('^Lines:\s\d+$',re.MULTILINE)
header_pattern_2   = re.compile('\n\n')
rcpdat_pattern = re.compile('^From\s+.+?\s+(\w+)\s+(\w+)\s+(\d+)\s+(\d{2}):(\d{2}):(\d{2})\s+(\d{4})')
mail_clause_pattern = re.compile('^([A-Z][a-zA-Z-]+|from|reply-to|to|subject|CC): ',re.MULTILINE|re.DOTALL)
mail_grouping       = re.compile('([\w\-_\.\d]+(@[\w\-_\.\d]+))',re.MULTILINE)
file_regex = None

retaindays = 100;
compress_histo_days = retaindays + 60; 

h_grp_adr = { }
h_grp_dom = { }

h_parse_rolling = {
           'exclude' : ['.mail.gz' ],
           'output'   : '.mail.new',
           'output_Z' : '.mail.gz',
           'rename'  : ( '.mail.new', '.mail')
          }

h_parse_first = {
           'output'  : '.mail',
           'output_Z': '.mail.gz'
           }


hday = {
        'Mon' : 0,
        'Tue' : 1,
        'Wed' : 2,
        'Thu' : 3,
        'Fri' : 4,
        'Sat' : 5,
        'Sun' : 6
        }
hmon = {
        'Jan' : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9,
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12
        }



def compile_r(dic):
    " Compiling regex "
    for a, b in dic:
        if b == 'm':
            kw = re.compile(a,re.MULTILINE|re.DOTALL)  
            dic[(a,b)] = (dic[(a,b)],kw) 

def subject_def(s,flg):
    if s.find('[SPAM]') != -1:
        flg['Subject']='spam'
    elif s.find('[LL-DISC]') != -1: 
        flg['Subject'] = 'attac'
    else:
        flg['Subject']='ok'
    return
        

def to_def(s,flg):
    #print("To : '" + s + "'")
    to_from_reply('To',mails.my_addr,s,flg)

def from_def(s,flg):
     
    to_from_reply('From',mails.ext_addr,s,flg)

def reply_to(s,flg): 
    to_from_reply('Reply-To',mails.my_addr,s,flg)

def delivered_to(s,flg):
    to_from_reply('Delivered-To',mails.my_addr,s,flg)

def Cc_ref(s,flg):
    to_from_reply('Cc',mails.my_addr,s,flg)


def to_from_reply(to_from,dic,s,fl):
    s = s.lower()
    
    tout  = mail_grouping.finditer(s)
    for found in tout:
            a = found.groups()
            g0,g1 = a[0],a[1]
            if not g0 in h_grp_adr: h_grp_adr[g0] = 1
            else:  h_grp_adr[g0] = h_grp_adr[g0] + 1 
            if not g1 in h_grp_dom: h_grp_dom[g1] = 1
            else:  h_grp_dom[g1] = h_grp_dom[g1] + 1 


    for kw,t in dic:
        if t == 's':
            if s.find(kw) != -1:
                #print(s,to_from,"=>",dic[(kw,'s')])
                fl[to_from] = dic[(kw,'s')]
                break
        elif t == 'm':
            if dic[(kw,t)][1].search(s) is not None:
                #print(s,to_from,"=>",dic[(kw,'m')][0])
                fl[to_from] = dic[(kw,'m')][0]
                break
    if not to_from in fl:
        fl[to_from + '_' + 'unknown'] = s

def creation_date(s,fl):
    s = s.replace("\n","")
    #print("'" + s + "'")
    return

def rcpt_date(s):
    s = s.replace("\n","")
    found = rcpdat_pattern.match(s)
    if found is None:
        print("No match: '" +s+ "'")
        return
    jr,month,dday,h,m,s,year = found.groups()
    j = hday[jr]
    mth = hmon[month]
    rcpt = int(year),mth,int(dday),int(h),int(m),int(s),j,0,-1
    tim = mktime(rcpt) 
    diff = int(time()) - int(tim)
    aged = int(diff/86400)
    return (tim,rcpt,aged)

def lines_def(s,fl):
    #print("Lines : '" + s + "'")
    return

def content_length(s,fl):
    #print("Length : '" + s + "'")
    return
     
def dkim(s,fl):
    #print("Dkim: '" + s + "'")
    return

def msgid_def(s,fl):
    return


dic_action = {
    'To'           : to_def,
    'to'           : to_def,
    'From'         : from_def,
    'from'         : from_def,
    'CC'           : Cc_ref,
    'Cc'           : Cc_ref,
    'Date'         : creation_date,
    'Subject'      : subject_def,
    'subject'      : subject_def,
    'Message-ID'   : msgid_def,
    'Reply-To'     : reply_to,
    'reply-to'     : reply_to,
    'Delivered-To' : delivered_to,
    'Lines'          :  lines_def,
    'Content-Length' : content_length,
    'DKIM-Signature' : dkim
    }


def list_to_tuples(lst):
    i = 0
    ltup = [] 
    while  i < len(lst):
        if (i%2):
            ltup.append((lst[i-1],lst[i]))
        i = i + 1
    return ltup


def treat_message(message,name,firstline):

    """
    Treat ONE message and only one at a time
    """

    destination = ''
    status = None
    ml = header_pattern.search(message)
    if ml is None:
        ml = header_pattern_2.search(message)
    if ml is None:
        status = 'no_end_header'
    else:
        if not 'mail' in jump:
            re.purge() #purge rejexp memory
            header = message[:ml.end()] #extract header
            mcl = mail_clause_pattern.split(header) #We loop on each clause
            if (mcl is None):
                msg="ALERT : Header has none clause !!!"
                print(msg)
                logd.write(msg + "\n")
                logd.write(message)
                return
            del(mcl[0])
    
            lt = list_to_tuples(mcl) 
            flag = {}
            for clause, result in lt:
                if not clause in dic_action:
                    continue
                dic_action[clause](result,flag)
            
    
            if not 'From' in flag:
                if 'To' in flag:
                    if flag['To'] == 'Ceisame/ceisame':
                        if 'Subject' in flag:
                            if flag['Subject'] == 'spam':
                                destination = 'Ceisame/spam'
                            else:
                                destination = 'Ceisame/ceisame'
                        else:
                            destination = 'Ceisame/ceisame'
                    else:
                        destination = flag['To'] 
                elif 'Reply-To' in flag:
                    destination = flag['Reply-To']
                elif 'Cc' in flag:
                    destination = flag['Cc']
                elif 'Delivered-To' in flag:
                    if flag['Delivered-To'] == 'Ceisame/ceisame':
                        if 'Subject' in flag:
                            if flag['Subject'] == 'spam':
                                destination = 'Ceisame/spam'
                            else:
                                destination = 'Ceisame/ceisame'
                        else:
                            destination = 'Ceisame/ceisame'
                    else:
                        status = 'unknown'
                elif 'Subject' in flag:
                    if flag['Subject'] == 'attac':
                        destination='ml/attac'
                    else:
                        status = 'unknown'
                else:
                    status = 'unknown'
            else:
                destination = flag['From']

        else:
            destination=output_prefix

    t,st,days = rcpt_date(firstline)
     
    fname = None
    if status == 'no_end_header':
        fname=unknown_dir + '/' + name + '_no_end_header'
    elif status == 'unknown':
        fname=unknown_dir + '/' + 'unknown.mail'
    elif not 'date' in jump and  days > retaindays:
        if  destination.find('/') == -1:
            destdir = ''
            if os.path.isfile(output_dir + '/' + destination):
                destdir = destination + '_' 
            else:
                destdir = destination
            destination = destdir + '/' + destination

        destination += '_' + strftime("%B_%Y",st)
        if ( days <= compress_histo_days):
            fname = output_dir + '/' + destination + h_parse['output'] 
        else:
            fname = output_dir + '/' + destination + h_parse['output_Z']
    else:
        start =  destination.rfind('/')
        if start != -1:
            destination=destination[start+1:]

        fname =  keepdir + '/' + destination

    #Creation des repertoires et sous repertoires
    #print ("fname : " + fname)
    dirn=dirname(fname)
    if not dirn == output_dir:
        if not exists(dirn): 
            try:
               logd.write("Creating directory: '" + dirn + "'\n")
               os.makedirs(dirn , 0o777)
            except OSError as msg:
               msg = "Could not create directory: '" + dirn + "' : '" + msg
               logd.write(msg)
               print(msg)
               sys.exit(1)
    #MARK
    msg = "writing to: '" + fname + "'\n"
    logd.write(msg)
    fw=None
    #Ouverture du fichier en append
    #print("fname : " + fname + "\n");
    try: 
        if days > compress_histo_days and not status:
            #On append dans le .gz
            fw = gzip.open(fname,'ab')
            #On transforme en bytes
            message=bytes(message,encoding = 'LATIN-1')
        else:
            #On ouvre le fichier texte en append
            fw = open(fname,"a", encoding = 'LATIN-1')
    except IOError as msg:
        print("Cannot open the file : " + fname + ' :',msg)

    fw.write(message)
    fw.close()


def parse_file(directory,filename,gzipped=0):
    path = directory + '/' + filename
    if (file_regex):
        if file_regex.search(filename):
            print("file : '" + path + "' is rejected")
            return
    try:
        if gzipped:
            fr=gzip.open(path,'rb') #Opening read only in binary mode
        else:
            fr = open(path,'r',encoding = 'Latin-1') #Opening read only
    except IOError as msg:
        print("Cannot open file : " + filename + ' :',msg)
        return
    firstline = fr.readline() #Reading first line
    if gzipped:
        firstline = firstline.decode('Latin-1')
    if not messagebreak_pattern.match(firstline): #firstline.startswith(message_break):
        logd.write("file "+ path + " is not in mail format.\n")
        return
    message = firstline
    while (True):
        line=fr.readline()
        if not line:
            break
        if gzipped:
            line=line.decode('Latin-1')
        if messagebreak_pattern.match(line): #line.startswith(message_break):
            treat_message(message,filename,firstline)
            message = line
            firstline = line
        else:
            message += line
    fr.close()
    treat_message(message,filename,firstline)

def parse_dir(directory):
    """
        Parses a directory containing mail boxes, open each files,
        split each message of each files and sends them to trad message function

        Note: We kept line flow so we use readline for a more comprehensive behavior
    """
    try:
        names=os.listdir(directory) #Try to read directory
    except OSError:
        print("Cannot open directory",repr(directory))
        sys.exit(1)

    for filename in names:
        path = directory + '/' + filename
        if not isfile(path):
            continue
        if filename.endswith('.gz'):
            parse_file(directory,filename,1)
        else:
            parse_file(directory,filename)
    return


def parse_dir_archives(directory):
    """
        We parse all <directory> (parameter) tree by recurse
        we call parse_file for each .mail file
        and parse_gzipped_file for compressed files .mail.gz
    """
    for root,dirs,files in os.walk(directory):
        if len(files) > 0:
            for f in files:
                cont=0
                if 'exclude' in h_parse:
                    for ext in h_parse['exclude']:
                        if f.endswith(ext):
                            cont=1
                            break
                if cont: continue
                if f.endswith('.gz'):
                    parse_file(root,f,1)
                else:
                    parse_file(root,f)

def delete_pmail(directory,to_del):
    for root,dirs,files in os.walk(directory):
        if len(files)>0:
            for f in files:
                st = f.find(to_del)
                if st != -1 and f[st:] == to_del:
                    delf = root + '/' + f  
                    try:
                        os.unlink(delf)
                        msg = "deleted :'" + delf + "'"
                        logd.write(msg + "\n")
                    except OSError as msg:
                        print("Could not delete '" + delf +  "' :",msg)

   

def rename_files(directory,src_ext,dest_ext):
    for root,dirs,files in os.walk(directory):
        if len(files)>0:
            for f in files:
                st = f.find(src_ext)
                if st != -1 and f[st:] == src_ext:
                    prefix = f[0:st]
                    dest = root + '/' + prefix + dest_ext
                    src = root + '/' + f
                    try:
                        os.rename(src,dest)
                        msg="renamed '" + src + "' to '" + dest + "'"
                        logd.write(msg + "\n")
                        print(msg) 
                    except OSError as msg:
                        print("Could not rename '" + src + "' to '" + dest + "' : ",msg)



compile_r(mails.my_addr)        
compile_r(mails.ext_addr)        

parse = parse_dir

def usage(code, msg=''):
    print(__doc__, file=sys.stderr)
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(code)


try:
    opts, args = getopt.getopt(sys.argv[1:],'hmrRi:f:k:o:u:e:j:O:', 
    ['help','move','roll','Recurse','input-dir=','file=','keep=','output-dir=','unknown-dir=','exclude-files=','filters=','Ouput-prefix='])
except getopt.error as msg:
    usage(1,msg)

for opt,arg in opts:
    if opt in ('-h','--help'):
        usage(0) 
    elif opt in ('-m','--move'):
        h_parse = h_parse_first
    elif opt in ('-f','--file'):
        file2parse=arg 
    elif opt in ('-r','--roll'):
        h_parse = h_parse_rolling
    elif opt in ('-i','--input-dir'):
        input_dir = arg
    elif opt in ('-o','--output-dir'):
        output_dir= arg 
    elif opt in ('-k','--keep'):
        keepdir = arg
    elif opt in ('-u','--unknown-dir'):
        unknown_dir=arg
    elif opt in ('-e','--exclude-files'):
        file_regex = re.compile(arg)
    elif opt in ('-R','--Recurse'):
        parse = parse_dir_archives
    elif opt in ('-j','--jump'):
        filters = arg
    elif opt in ('-O','--Ouput-prefix'):
        output_prefix = arg
         

if not input_dir and not file2parse:
    usage(1,'No input_dir nor input_file -i or -f option given.')

if filters:
    for a in filters.split(','):
        jump[a] = 1

if not h_parse:
    usage(1,"You must chose move (-m) or roll (-r) method")

if file2parse:
    if not output_dir:
       usage(1,"No output dir given but file2parse:") 
    if  not output_prefix:
        output_prefix = basename(output_dir)
    directory = dirname(file2parse)
    filename =  basename(file2parse)
    for d in (keepdir, unknown_dir):
        if not exists(d): 
            try:
                os.makedirs(d, 0o777)
            except OSError as msg:
                print("Could not create",d,':',msg) 
                sys.exit(1)
    if filename.endswith('.gz'):
        parse_file(directory,filename,1)
    else:
        parse_file(directory,filename)

if input_dir:
    if not output_dir:
        usage(1,"You must give output_dir if you give an input_dir")
    if  not output_prefix:
        output_prefix = basename(output_dir)
    for d in (keepdir, unknown_dir):
        if not exists(d): 
            try:
                os.makedirs(d, 0o777)
            except OSError as msg:
                print("Could not create",d,':',msg) 
                sys.exit(1)
    parse(input_dir)

#We rotate
if 'rename' in h_parse:
    (src,dest) = h_parse['rename']
    if input_dir:
        delete_pmail(input_dir,dest)
        rename_files(input_dir,src,dest)
    if file2parse:
       od = dirname(file2parse)
       delete_pmail(od,dest)
       rename_files(od,src,dest)


def display(mh,fic):
    fwr = open(fic,'w')
    liste = []
    for a,b in mh.items():
        liste.append((b,a))
    for a,b in sorted(liste,reverse=True):
        fwr.write(b + ' => ' + str(a) + "\n")
    fwr.close()

#display(h_grp_adr,'sorted_emails.txt')
#display(h_grp_dom,'sorted_domains.txt')

