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
https://build.opensuse.org/package/show/home:codeminister/GitExtensions

copied some spec file stuff from: https://build.opensuse.org/package/show/home:Warhammer40k:stuff/GitExtensions



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

```
[   22s] RPMLINT report:
[   22s] ===============
[   28s] GitExtensions.noarch: W: suse-filelist-forbidden-opt /opt/GitExtensions is not allowed for official SUSE packages
[   28s] /opt may not be used by a SUSE.                       It is reserved for 3rd
[   28s] party packagers
[   28s]
[   28s] GitExtensions.src: W: strange-permission GitExtensions.desktop 0744L
[   28s] GitExtensions.src: W: strange-permission GitExtensions-2.48.03-Mono.zip 0400L
[   28s] A file that you listed to include in your package has strange permissions.
[   28s] Usually, a file should have 0644 permissions.
[   28s]
[   28s] GitExtensions.noarch: W: non-executable-script /usr/share/applications/GitExtensions.desktop 0644L /usr/bin/env
[   28s] This text file contains a shebang or is located in a path dedicated for
[   28s] executables, but lacks the executable bits and cannot thus be executed.  If
[   28s] the file is meant to be an executable script, add the executable bits,
[   28s] otherwise remove the shebang or move the file elsewhere.
[   28s]
[   28s] GitExtensions.noarch: W: no-manual-page-for-binary gitext
[   28s] Each executable in standard binary directories should have a man page.
[   28s]
[   28s] GitExtensions.noarch: W: incorrect-fsf-address /opt/GitExtensions/Diff-Scripts/TortoiseSVN License.txt
[   28s] The Free Software Foundation address in this file seems to be outdated or
[   28s] misspelled.  Ask upstream to update the address, or if this is a license file,
[   28s] possibly the entire file with a new copy available from the FSF.
[   28s]
[   28s] 2 packages and 0 specfiles checked; 0 errors, 6 warnings.
```
todo: fix these issues


# one-time checkout of empty project (does not exist anymore)
osc co home:codeminister/GitExtensions -o .

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
