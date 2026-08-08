from rich.console import Console
from rich import print as rprint
from time import sleep

con = Console()

comm = None
hlp = False
hlpc = False
hcom = None

print('Python 4.1.3 (main, Mar 29 2026, 21:17:38) [GCC 15.2.0] on linux')
print('Type "help", "copyright", "credits" or "license" for more information.')

def main():
    global hlp, hlpc, hcom
    while True:
        
        if hlp:
            if hlpc:
                hcomm = hcom
            else:
                hcomm = con.input("[magenta]help> ")
            
            modules = 'pygame-ce#2.5.8.dev1#(SDL#2.30.0,#Python#3.13.14)#Crypto#_xxtestfuzz#importlib#re#Cryptodome#_yaml#importlib_metadata#readlin#OpenSSL#_yappi#inspect#referencing#PySide6#_zoneinfo#io#reprlib#Xlib#abc#ipaddress#requests#__future__#ada92cb5d92a588d1b93__mypyc#iso8601#resource#__hello__#aifc#itertools#rfc3986#__phello__#alembic#itsdangerous#rlcompleter#_abc#amqp#jinja2#routes#_aix_support#aniso8601#json#rpds#_android_support#antigravity#jsonschema#runpy#_apple_support#argparse#jsonschema_specifications#saml2#_ast#array#jwt#saml2test#_asyncio#ast#keystone#sched#_bisect#asyncio#keystoneauth1#secrets#_blake2#atexit#keystoneclient#select#_bz2#attr#keystonemiddleware#selectors#_cffi_backend#attrs#keyword#serial#_codecs#audioop#kombu#setuptools#_codecs_cn#autocommand#linecache#shelve#_codecs_hk#backports#locale#shiboken6#_codecs_iso2022#base64#logging#shlex#_codecs_jp#bcrypt#lzma#shutil#_codecs_kr#bdb#mailbox#signal#_codecs_tw#binascii#mako#site#_collections#bisect#markupsafe#six#_collections_abc#blinker#marshal#smtplib#_colorize#builtins#math#socket#_compat_pickle#bz2#mccabe#socketserver#_compression#cProfile#mfusepy#speech_recognition#_contextvars#cachetools#mimetypes#sqlalchemy#_csv#calendar#mmap#sqlite3#_ctypes#capstone#modulefinder#sre_compile#_ctypes_test#certifi#more_itertools#sre_constants#_curses#cffi#mouseinfo#sre_parse#_curses_panel#cgi#msgpack#ssl#_datetime#cgitb#mtkclient#stat#_decimal#charset_normalizer#multiprocessing#statistics#_distutils_hack#chunk#netaddr#statsd#_elementtree#click#netrc#stevedore#_functools#cmath#ntpath#string#_hashlib#cmd#nturl2path#stringprep#_heapq#code#numbers#struct#_imp#codecs#oauthlib#subprocess#_interpchannels#codeop#opcode#symtable#_interpqueues#collections#operator#sys#_interpreters#colorama#optparse#sysconfig#_io#colorsys#os#syslog#_ios_support#compileall#os_service_types#tabnanny#_json#concurrent#oslo_cache#tarfile#_locale#configparser#oslo_concurrency#tempfile#_lsprof#contextlib#oslo_config#termios#_lzma#contextvars#oslo_context#test#_markupbase#copy#oslo_db#testresources#_md5#copyreg#oslo_i18n#testscenarios#_multibytecodec#cryptography#oslo_log#textwrap#_multiprocessing#csv#oslo_messaging#this#_opcode#ctypes#oslo_metrics#threading#_opcode_metadata#curses#oslo_middleware#time#_operator#dataclasses#oslo_policy#timeit#_osx_support#datetime#oslo_serialization#tkinter#_pickle#dateutil#oslo_service#token#_posixshmem#dbm#oslo_upgradecheck#tokenize#_posixsubprocess#debtcollector#oslo_utils#tomli#_py_abc#decimal#osprofiler#tomllib#_pydatetime#decorator#packaging#trace#_pydecimal#defusedxml#pathlib#traceback#_pyio#difflib#pbr#tracemalloc#_pylong#dis#pdb#tty#_pyrepl#dns#pickle#turtle#_queue#doctest#pickletools#turtledemo#_random#dogpile#pip#types#_sha1#elementpath#pkgutil#typing#_sha2#email#platform#typing_extensions#_sha3#encodings#platformdirs#tzdata#_signal#ensurepip#plistlib#unicodedata#_sitebuiltins#enum#poplib#unicorn#_socket#errno#posix#unittest#_sqlite3#eventlet#posixpath#urllib#_sre#fasteners#pprint#urllib3#_ssl#faulthandler#prettytable#usb#_stat#fcntl#profile#uuid#_statistics#filecmp#prometheus_client#venv#_string#fileinput#pstats#vine#_strptime#flake8#psutil#warnings#_struct#flask#pty#wave#_suggestions#flask_restful#pwd#wcwidth#_symtable#fnmatch#py_compile#weakref#_sysconfig#fractions#pyaudio#webbrowser#_sysconfigdata__linux_x86_64-linux-gnu#ftplib#pyautogui#webob#_testbuffer#functools#pycadf#werkzeug#_testcapi#futurist#pyclbr#wheel#_testclinic#gc#pycodestyle#wrapt#_testclinic_limited#genericpath#pycparser#wsgiref#_testexternalinspection#getopt#pydoc#xml#_testimportmultiple#getpass#pydoc_data#xmlrpc#_testinternalcapi#gettext#pyexpat#xmlschema#_testlimitedcapi#glob#pyflakes#xxlimited#_testmultiphase#graphlib#pygame#xxlimited_35#_testsinglephase#greenlet#pygetwindow#xxsubtype#_thread#grp#pymsgbox#yaml#_threading_local#gzip#pyparsing#yappi#_tkinter#hashlib#pyperclip#zipapp#_tokenize#heapq#pyrect#zipfile#_tracemalloc#hmac#pyscreeze#zipimport#_typing#html#pytweening#zipp#_uuid#http#pytz#zlib#_warnings#idlelib#queue#zoneinfo#_weakref#idna#quopri#_weakrefset#imaplib#random'
            modules = modules.split('#')
            keywords = 'False#class#from#or#None#continue#global#pass#True#def#if#raise#and#del#import#return#as#elif#in#try#assert#else#is#while#async#except#lambda#with#await#finally#nonlocal#yield#break#for#not'
            keywords = keywords.split('#')
            symbols = '!=#+#<<=#_#"#+=#<=#__#"""#,#<>#`#%#-#==#b"#%=#-=#>b\'#&#.#>=#f"&=#...#>>#f\'#\'#/#>>=#j#\'\'\'#//#@r"#(#//=#Jr\'#)#/=#[u"#*#:#\\#u\'#**#:=#]#|#**=#<#^#|=#*=#<<#^=#~'
            symbols = symbols.split('#')
            topics = 'ASSERTION#EXCEPTIONS#PACKAGES#ASSIGNMENT#EXECUTION#POWER#ASSIGNMENTEXPRESSIONS#EXPRESSIONS#PRECEDENCE#ATTRIBUTEMETHODS#FLOAT#PRIVATENAMES#ATTRIBUTES#FORMATTING#RETURNING#AUGMENTEDASSIGNMENT#FRAMEOBJECTS#SCOPING#BASICMETHODS#FRAMES#SEQUENCEMETHODS#BINARY#FUNCTIONS#SEQUENCES#BITWISE#IDENTIFIERS#SHIFTING#BOOLEAN#IMPORTING#SLICINGS#CALLABLEMETHODS#INTEGER#SPECIALATTRIBUTES#CALLS#LISTLITERALS#SPECIALIDENTIFIERS#CLASSES#LISTS#SPECIALMETHODS#CODEOBJECTS#LITERALS#STRINGMETHODS#COMPARISON#LOOPING#STRINGS#COMPLEX#MAPPINGMETHODS#SUBSCRIPTS#CONDITIONAL#MAPPINGS#TRACEBACKS#CONTEXTMANAGERS#METHODS#TRUTHVALUE#CONVERSIONS#MODULES#TUPLELITERALS#DEBUGGING#NAMESPACES#TUPLES#DELETION#NONE#TYPEOBJECTS#DICTIONARIES#NUMBERMETHODS#TYPES#DICTIONARYLITERALS#NUMBERS#UNARY#DYNAMICFEATURES#OBJECTS#UNICODE#ELLIPSIS#OPERATORS'
            topics = topics.split('#')

            if hcomm == "modules":
                print("Please wait a moment while I gather a list of all available modules\n")
                sleep(1)
                print('pygame-ce 2.5.8.dev1 (SDL 2.30.0, Python 3.13.14)')
                print('Crypto              _xxtestfuzz         importlib           re')
                print('Cryptodome          _yaml               importlib_metadata  readline')            
                print('OpenSSL             _yappi              inspect             referencing')
                print('PySide6             _zoneinfo           io                  reprlib')
                print('Xlib                abc                 ipaddress           requests')
                print('__future__          ada92cb5d92a588d1b93__mypyc iso8601             resource')
                print('__hello__           aifc                itertools           rfc3986')
                print('__phello__          alembic             itsdangerous        rlcompleter')
                print('_abc                amqp                jinja2              routes')
                print('_aix_support        aniso8601           json                rpds')
                print('_android_support    antigravity         jsonschema          runpy')
                print('_apple_support      argparse            jsonschema_specifications saml2')
                print('_ast                array               jwt                 saml2test')
                print('_asyncio            ast                 keystone            sched')
                print('_bisect             asyncio             keystoneauth1       secrets')
                print('_blake2             atexit              keystoneclient      select')
                print('_bz2                attr                keystonemiddleware  selectors')
                print('_cffi_backend       attrs               keyword             serial')
                print('_codecs             audioop             kombu               setuptools')
                print('_codecs_cn          autocommand         linecache           shelve')
                print('_codecs_hk          backports           locale              shiboken6')
                print('_codecs_iso2022     base64              logging             shlex')
                print('_codecs_jp          bcrypt              lzma                shutil')
                print('_codecs_kr          bdb                 mailbox             signal')
                print('_codecs_tw          binascii            mako                site')
                print('_collections        bisect              markupsafe          six')
                print('_collections_abc    blinker             marshal             smtplib')
                print('_colorize           builtins            math                socket')
                print('_compat_pickle      bz2                 mccabe              socketserver')
                print('_compression        cProfile            mfusepy             speech_recognition')
                print('_contextvars        cachetools          mimetypes           sqlalchemy')
                print('_csv                calendar            mmap                sqlite3')
                print('_ctypes             capstone            modulefinder        sre_compile')
                print('ctypes_test        certifi             more_itertools      sre_constants')
                print('_curses             cffi                mouseinfo           sre_parse')
                print('_curses_panel       cgi                 msgpack             ssl')
                print('_datetime           cgitb               mtkclient           stat')
                print('_decimal            charset_normalizer  multiprocessing     statistics')
                print('_distutils_hack     chunk               netaddr             statsd')
                print('_elementtree        click               netrc               stevedore')
                print('_functools          cmath               ntpath              string')
                print('_hashlib            cmd                 nturl2path          stringprep')
                print('_heapq              code                numbers             struct')
                print('_imp                codecs              oauthlib            subprocess')
                print('_interpchannels     codeop              opcode              symtable')
                print('_interpqueues       collections         operator            sys')
                print('_interpreters       colorama            optparse            sysconfig')
                print('_io                 colorsys            os                  syslog')
                print('_ios_support        compileall          os_service_types    tabnanny')
                print('_json               concurrent          oslo_cache          tarfile')
                print('_locale             configparser        oslo_concurrency    tempfile')
                print('_lsprof             contextlib          oslo_config         termios')
                print('_lzma               contextvars         oslo_context        test')
                print('_markupbase         copy                oslo_db             testresources')
                print('_md5                copyreg             oslo_i18n           testscenarios')
                print('_multibytecodec     cryptography        oslo_log            textwrap')
                print('_multiprocessing    csv                 oslo_messaging      this')
                print('_opcode             ctypes              oslo_metrics        threading')
                print('_opcode_metadata    curses              oslo_middleware     time')
                print('_operator           dataclasses         oslo_policy         timeit')
                print('_osx_support        datetime            oslo_serialization  tkinter')
                print('_pickle             dateutil            oslo_service        token')
                print('_posixshmem         dbm                 oslo_upgradecheck   tokenize')
                print('_posixsubprocess    debtcollector       oslo_utils          tomli')
                print('_py_abc             decimal             osprofiler          tomllib')
                print('_pydatetime         decorator           packaging           trace')
                print('_pydecimal          defusedxml          pathlib             traceback')
                print('_pyio               difflib             pbr                 tracemalloc')
                print('_pylong             dis                 pdb                 tty')
                print('_pyrepl             dns                 pickle              turtle')
                print('_queue              doctest             pickletools         turtledemo')
                print('_random             dogpile             pip                 types')
                print('_sha1               elementpath         pkgutil             typing')
                print('_sha2               email               platform            typing_extensions')
                print('_sha3               encodings           platformdirs        tzdata')
                print('_signal             ensurepip           plistlib            unicodedata')
                print('_sitebuiltins       enum                poplib              unicorn')
                print('_socket             errno               posix               unittest')
                print('_sqlite3            eventlet            posixpath           urllib')
                print('_sre                fasteners           pprint              urllib3')
                print('_ssl                faulthandler        prettytable         usb')
                print('_stat               fcntl               profile             uuid')
                print('_statistics         filecmp             prometheus_client   venv')
                print('_string             fileinput           pstats              vine')
                print('_strptime           flake8              psutil              warnings')
                print('_struct             flask               pty                 wave')
                print('_suggestions        flask_restful       pwd                 wcwidth')
                print('_symtable           fnmatch             py_compile          weakref')
                print('_sysconfig          fractions           pyaudio             webbrowser')
                print('_sysconfigdata__linux_x86_64-linux-gnu ftplib              pyautogui           webob')
                print('_testbuffer         functools           pycadf              werkzeug')
                print('_testcapi           futurist            pyclbr              wheel')
                print('_testclinic         gc                  pycodestyle         wrapt')
                print('_testclinic_limited genericpath         pycparser           wsgiref')
                print('_testexternalinspection getopt              pydoc               xml')
                print('_testimportmultiple getpass             pydoc_data          xmlrpc')
                print('_testinternalcapi   gettext             pyexpat             xmlschema')
                print('_testlimitedcapi    glob                pyflakes            xxlimited')
                print('_testmultiphase     graphlib            pygame              xxlimited_35')
                print('_testsinglephase    greenlet            pygetwindow         xxsubtype')
                print('_thread             grp                 pymsgbox            yaml')
                print('_threading_local    gzip                pyparsing           yappi')
                print('_tkinter            hashlib             pyperclip           zipapp')
                print('_tokenize           heapq               pyrect              zipfile')
                print('_tracemalloc        hmac                pyscreeze           zipimport')
                print('_typing             html                pytweening          zipp')
                print('_uuid               http                pytz                zlib')
                print('_warnings           idlelib             queue               zoneinfo')
                print('_weakref            idna                quopri                      ')
                print('_weakrefset         imaplib             random                      ')
                print()
                print('Enter any module name to get more help.  Or, type "modules spam" to search')
                print('for modules whose name or summary contain the string "spam".')
            elif hcomm in modules:
                rprint(f"[magenta]help.modules.{hcomm}.data could not be loaded")
            elif hcomm == "keywords":
                print("\nHere is a list of the Python keywords.  Enter any keyword to get more help.\n")
                print('False               class               from                or')
                print('None                continue            global              pass')
                print('True                def                 if                  raise')
                print('and                 del                 import              return')
                print('as                  elif                in                  try')
                print('assert              else                is                  while')
                print('async               except              lambda              with')
                print('await               finally             nonlocal            yield')
                print('break               for                 not              \n')
            elif hcomm in keywords:
                rprint(f"[magenta]help.keywords.{hcomm}.data could not be loaded")
            elif hcomm == "symbols":
                print("\nHere is a list of the punctuation symbols which Python assigns special meaning")
                print("to. Enter any symbol to get more help.\n")
                print('!=                  +                   <<=                 _')
                print("                   +=                  <=                  __")
                print('"""                 ,                   <>                  `')
                print('%                   -                   ==                  b"')
                print("%=                  -=                  >                   b'")
                print('&                   .                   >=                  f"')
                print("&=                  ...                 >>                  f'")
                print("'                   /                   >>=                 j")
                print("'''     " + '            //                  @                   r"')
                print("(                   //=                 J                   r'")
                print(')                   /=                  [                   u"')
                print("*                   :                   \\                   u'")
                print("**                  :=                  ]                   |")
                print("**=                 <                   ^                   |=")
                print("*=                  <<                  ^=                  ~\n")

            elif hcomm in symbols:
                rprint(f"[magenta]help.symbols.{hcomm}.data could not be loaded")
            elif hcomm == "topics":
                print("\nHere is a list of available topics.  Enter any topic name to get more help.\n")
                print("ASSERTION                 EXCEPTIONS                PACKAGES\n\
ASSIGNMENT                EXECUTION                 POWER\n\
ASSIGNMENTEXPRESSIONS     EXPRESSIONS               PRECEDENCE\n\
ATTRIBUTEMETHODS          FLOAT                     PRIVATENAMES\n\
ATTRIBUTES                FORMATTING                RETURNING\n\
AUGMENTEDASSIGNMENT       FRAMEOBJECTS              SCOPING\n\
BASICMETHODS              FRAMES                    SEQUENCEMETHODS\n\
BINARY                    FUNCTIONS                 SEQUENCES\n\
BITWISE                   IDENTIFIERS               SHIFTING\n\
BOOLEAN                   IMPORTING                 SLICINGS\n\
CALLABLEMETHODS           INTEGER                   SPECIALATTRIBUTES\n\
CALLS                     LISTLITERALS              SPECIALIDENTIFIERS\n\
CLASSES                   LISTS                     SPECIALMETHODS\n\
CODEOBJECTS               LITERALS                  STRINGMETHODS\n\
COMPARISON                LOOPING                   STRINGS\n\
COMPLEX                   MAPPINGMETHODS            SUBSCRIPTS\n\
CONDITIONAL               MAPPINGS                  TRACEBACKS\n\
CONTEXTMANAGERS           METHODS                   TRUTHVALUE\n\
CONVERSIONS               MODULES                   TUPLELITERALS\n\
DEBUGGING                 NAMESPACES                TUPLES\n\
DELETION                  NONE                      TYPEOBJECTS\n\
DICTIONARIES              NUMBERMETHODS             TYPES\n\
DICTIONARYLITERALS        NUMBERS                   UNARY\n\
DYNAMICFEATURES           OBJECTS                   UNICODE\n\
ELLIPSIS                  OPERATORS          \n")
            elif hcomm in topics:
                rprint(f"[magenta]help.topics.{hcomm}.data could not be loaded")
            elif hcomm == "modules spam":
                print("\nHere is a list of modules whose name or summary contains 'spam'.\n\
                If there are any, enter a module name to get more help.\n\n\
                __phello__.spam \n")
            elif hcomm == "q" or hcomm == "quit" or hcomm == "exit":
                print("\nYou are now leaving help and returning to the Python interpreter.\n\
                If you want to ask for help on a particular object directly from the\n\
                interpreter, you can type" + ' "help(object)". ' + ' Executing "help' + "('string')" + '"\n\
                has the same effect as typing a particular string at the help> prompt.\n\
                ')
                hlp = False
                hlpc = False
            else:
                print(f"No Python documentation found for '{hcomm}'.\n\
                Use help() to get the interactive help utility.\n\
                Use help(str) for help on the str class.\n\
                \n")
        if not hlp:
            comm = con.input("[magenta]>>> ")
            comm = comm.replace(';', '')
        if comm == "quit" or comm == "exit":
            break
        elif comm == "help" and not hlp:
            print("Welcome to Python 4.1.3's help utility! " + 'If this is your first time using')
            print('Python, you should definitely check out the tutorial at')
            print('https://docs.python.org/4.1.3/tutorial/.\n')
            print('Enter the name of any module, keyword, or topic to get help on writing')
            print('Python programs and using Python modules.  To get a list of available\n')
            print('modules, keywords, symbols, or topics, enter "modules", "keywords",')
            print('"symbols", or "topics".\n')
            print('Each module also comes with a one-line summary of what it does; to list')
            print('the modules whose name or summary contain a given string such as "spam",')
            print('enter "modules spam".\n')
            print('To quit this help utility and return to the interpreter,')
            print('enter "q", "quit" or "exit".')
            hlp = True
        elif comm.startswith("help(") and comm.endswith(")"):
            hcom = comm[len("help("):-1]
            hlpc = True
            print("HELP(    )")
        else:
            try:
                exec(comm)
            except Exception as e:
                rprint(f"[magenta]{e}")

if __name__ == '__main__':
    main()