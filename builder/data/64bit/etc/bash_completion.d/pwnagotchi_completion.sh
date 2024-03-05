_show_complete()
{
    local cur opts node_names all_options opt_line
    all_options="
bananagotchi -h --help -C --config -U --user-config --manual --skip-session --clear --debug --version --print-config --check-update --donate {plugins,google}
bananagotchi plugins -h --help {list,install,enable,disable,uninstall,update,upgrade}
bananagotchi plugins list -i --installed -h --help
bananagotchi plugins install -h --help
bananagotchi plugins uninstall -h --help
bananagotchi plugins enable -h --help
bananagotchi plugins disable -h --help
bananagotchi plugins update -h --help
bananagotchi plugins upgrade -h --help
bananagotchi google -h --help {login,refresh}
bananagotchi google login -h --help
bananagotchi google refresh -h --help
"
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    # shellcheck disable=SC2124
    cmd="${COMP_WORDS[@]:0:${#COMP_WORDS[@]}-1}"
    opt_line="$(grep -m1 "$cmd" <<<"$all_options")"
    if [[ ${cur} == -* ]] ; then
        opts="$(echo "$opt_line" | tr ' ' '\n' | awk '/^ *-/{gsub("[^a-zA-Z0-9-]","",$1);print $1}')"
        # shellcheck disable=SC2207
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
    fi

    # shellcheck disable=SC2086
    opts="$(echo $opt_line | grep -Po '{\K[^}]+' | tr ',' '\n')"
    # shellcheck disable=SC2207
    COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
}

complete -F _show_complete bananagotchi
