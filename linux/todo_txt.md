Download todo.txt

install to `/opt/todo/`
    chmod +x todo.sh
    sudo cp /opt/todo/todo.sh /usr/local/bin

add to bash.rc:
    alias t='/opt/todo/todo.sh -d /opt/todo/todo.cfg'
    source /opt/todo/todo_completion
    complete -F _todo t
    export TODOTXT_DEFAULT_ACTION=ls


    t add "my task"
    t ls
    t pri 3 A
    t ls keyword
    t add "my task +keyword @context"
    t ls keyword
    t ls content
    t do 3


