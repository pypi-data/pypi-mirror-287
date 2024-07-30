NAME

::

    NIXT - you have been nixt


SYNOPSIS

::

    nixt <cmd> [key=val] [key==val]
    nixtc
    nixtd


DESCRIPTION

::

    NIXT is python3 code to program objects in a functional way. It
    provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    NIXT allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    NIXT has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

INSTALL

::

    $ pipx install nixt
    $ pipx ensurepath
    $ nixt skl
    $ nixt srv > nixt.service
    $ sudo mv nixt.service /etc/systemd/system/
    $ systemctl enable nixt --now


COMMANDS

::

    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    exp - export opml (stdout)
    imp - import opml
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    res - restore deleted objects
    rss - add a feed
    syn - sync rss feeds


CONFIGURATION

::

    irc

    $ nixt cfg server=<server>
    $ nixt cfg channel=<channel>
    $ nixt cfg nick=<nick>

    sasl
 
    $ nixt pwd <nsvnick> <nspass>
    $ nixt cfg password=<frompwd>

    rss

    $ nixt rss <url>
    $ nixt dpl <url> <item1,item2>
    $ nixt rem <url>
    $ nixt res <url>
    $ nixt nme <url> <name>

    opml

    $ nixt exp
    $ nixt imp <filename>


SYSTEMD

::

    save the following it in /etc/systemd/system/rssbot.service and
    replace "<user>" with the user running pipx


    [Unit]
    Description=you have been nixt!
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.nixt
    ExecStart=/home/<user>/.local/bin/nixtd
    ExitType=cgroup
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

    then run this

    $ mkdir ~/.nixt
    $ sudo systemctl enable nixt --now

    default channel/server is #nixt on localhost


FILES

::

    ~/.nixt
    ~/.local/bin/nixt
    ~/.local/bin/nixtc
    ~/.local/bin/nixtd
    ~/.local/pipx/venvs/nixt/


AUTHOR

::

    xobejctz <objx@proton.me>


COPYRIGHT

::

    NIXT is Public Domain.
