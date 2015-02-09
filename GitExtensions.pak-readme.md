GitExtensions openSUSE package
==============================

Upstream source
---------------
- https://github.com/gitextensions/gitextensions/
- There you can see they use their own build service
=> we use the prebuilt zip-package for now (LATER: it would be nice to build GitExt from scratch)


Build from scratch
------------------
1) checkout source
`git clone https://github.com/gitextensions/gitextensions.git`

2) update submodules
`git submodule update --init --recursive`

2) ./Build/build.mono.debug.sh:
-xbuild /p:TargetFrameworkProfile="" $MONOSOLUTION
+xbuild /p:TargetFrameworkProfile="" /p:Configuration=Release $MONOSOLUTION

3) run: `./Build/build.mono.debug.sh`
```
       8 Warning(s)
         30 Error(s)
```

todo


openSUSE build service
----------------------
https://build.opensuse.org/package/show/home:codeminister/gitextensions



Source information
------------------
* GitExtensions-2.48.03-Mono.zip
    - the original assemblies downloaded from
    http://sourceforge.net/projects/gitextensions/files/Git%20Extensions/Version%202.48.03/

* GitExtensions.png
    - converted from source file git-extensions-logo-final-256.ico to 64x64 png image

* GitExtensions.desktop
    - TODO


Build service info
==================
osc usage:
```
# local build
osc build openSUSE_13.2 x86_64
# intermediate results see: /var/tmp/build-root/openSUSE_13.2-x86_64/home/abuild/rpmbuild/

# one-time checkout of empty project (does not exist anymore)
osc co home:codeminister/freefilesync-6.13 -o .

# add all files
osc add *

# commit to server
osc commit
```

for current time in freefilesync.changes
`date --utc`


Build information
=================
home:codeminister/FreeFileSync> osc buildhist
Valid arguments for this package are:

openSUSE_Factory  i586
openSUSE_Factory  x86_64
openSUSE_13.1     i586
openSUSE_13.1     x86_64
openSUSE_12.3     i586
openSUSE_12.3     x86_64
openSUSE_12.2     i586
openSUSE_12.2     x86_64
Missing arguments

Build specific platform
-----------------------
osc build openSUSE_13.1 x86_64
osc build openSUSE_13.1 i586
