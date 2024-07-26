from os.path import isfile as isf
from os.path import isdir as isd
from os.path import basename
from os.path import join as j
from os import remove as rm
from os import rmdir
from os import mkdir
from os import listdir as ls
from shutil import run as r
from shutil import copytree as cpr

#need debug
#oh umm... U.U

o = open
w = lambda f : o(f, 'w')

def s(x, islog = True):
  ret = r(x, shell = True)
  if islog: print(ret)
  return ret

def wither(opener):
  def with_deco(func):
    def with_opener(fn):
      with opener(fn) as fp:
        return func(fp)
    return with_opener
  return with_deco

txtloader = wither(o)((lambda f : f.read()))
def txtdumper(f, x):
  return wither(w)((lambda f : f.write(x)))(f)

def popfile(f):
  ret = txtloader(f); rm(f)
  return ret

def NewRepoBuilder(ghusername, ghrepo, ghuseremail, pkg, login = False):
  repourl = f'https://github.com/{ghusrname}/{ghrepo}'
  s('git clone {repourl}.git')
  if login:
    s(f'git config --global user.name {ghusername}')
    s(f'git config --global user.email {ghuseremail}')
  assert isd(ghrepo), f"Can't load the ghrepo. [{repourl}]"
  cd(ghrepo)
  description = txtloader('README.md').split('\n')[1]
  pkgnames = basename(pkg)
  dirs = j('.', pkgnames)
  if not isd('.temp'): mkdir('.temp')
  cpr(pkgnames, j('.temp', pkgnames))
  txtdumper(j('.temp', pkgnames))
  cpr(pkg, dirs)
  cd(pkgnames)
  f = '__init__.py'
  cd('.temp')
  src = popfile('setup.py')
  ver = popfile('ver.txt')
  cd('..')
  rmdir('.temp')
  origin = list(filter((lambda x : x[-4:] == 'temp' and x[0] == '.' and x[1:-4].replace('A', '') == ''), ls()))
  for i, j in zip(origin, list(map((lambda x : x.replace('.Atemp', '.temp').replace('AA', 'A')), origin))): mv(i, j)
  txtdumper(f, "__version__ = '{}'\n{}".format(ver, txtloader(f)))
  cd('..')
  txtdumper('setup.py', src.replace('#setup(~)', f"name = '{pkgnames}', description = '{description}', version = {ver}, url = {repourl}, auther = '{ghusername}', auther_email = '{ghuseremail}', ").replace('#\\setup', '#setup').replace('\\\\', '\\'))
  s(f'git add .')
  s(f'git commit -m "mypkggener:{ver}PyPIPkgProjectRepoGen [AUTO]"')
  s(f'git push')

def deploys(ghusername, ghrepo, loginemail = None):
  repourl = f'https://github.com/{ghusrname}/{ghrepo}'
  if loginemail != None:
    s(f'git config --global user.name {ghusername}')
    s(f'git config --global user.email {loginemail}')
  s(f'git clone {repourl}.git')
  assert isd(ghrepo), f"Can't load the ghrepo. [{repourl}]"
  cd(ghrepo)
  s('python setup.py sdist bdist_wheel')
  s('python -m twine upload dist/*')
  s('git add .')
  s('git commit -m "mypkggener:PyPIUploaded [AUTO]"')
  s('git push .')
  cd('..')

def RepoUpdateBuildPre(ghusername, ghrepo, loginemail = None):
  repourl = f'https://github.com/{ghusrname}/{ghrepo}'
  if loginemail != None:
    s(f'git config --global user.name {ghusername}')
    s(f'git config --global user.email {loginemail}')
  s(f'git clone {repourl}.git')
  assert isd(ghrepo), f"Can't load the ghrepo. [{repourl}]"
  cd(ghrepo)
  fn = popfile(j('.temp', '.name.txt'))
  mv(j('.temp', fn), j('..', fn))
  iferr = '.temp{}'.format(hash(ls('..')))
  actually = '.temp' if '.temp' in ls('..') else iferr
  mv('.temp', j('..', actually))
  that = j('..', actually)
  thatthat = j(that, '.temp')
  for i in ls(thatthat):
    mv(j(thatthat, i), i)
  rmrs(fn)
  rmrs('build')
  rmrs('dist')
  s('git add .')
  s('git commit -m "mypkggener:PopLastUpdates [AUTO]"')
  s('git push .')
  cd('..')