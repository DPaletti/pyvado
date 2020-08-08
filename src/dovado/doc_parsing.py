#!/usr/bin/env python3
import re
import dovado.vivado_interaction as vivado


def get_directives_paragraph(command):

    if command not in {"synthesis", "place", "route"}:
        raise ValueError(
            "get_directives_paragraph called with " + str(command)
        )
    if command == "synthesis":
        help = vivado.get_help("synth_design").strip()
    elif command == "place":
        help = vivado.get_help("place_design").strip()
    else:
        help = vivado.get_help("route_design").strip()

    help = re.split("(\r\n?|\n)+", help)
    directive_index = help.index(
        [
            i
            for i in [i for i in help if re.search("-directive", i)]
            if re.search("-directive <arg> -", i)
        ][0]
    )
    help_slice_from_directive = help[directive_index + 1 :]
    next_field_occurrences = [
        i
        for i in [
            i
            for i in help_slice_from_directive
            if re.search("-[a-zA-Z_]+[ \t]*(<arg>)?[ \t]*-[ \t]*", i)
        ]
        if i.strip()[0] == "-"
    ]
    return "".join(
        help[directive_index : help.index(next_field_occurrences[0])]
    ).strip()


def get_directives(directives_paragraph):
    return [
        re.sub(r"\*|-| ", "", item)
        for sublist in [
            re.findall(r"\* .* -", i.strip())
            for i in re.split("(\r\n?|\n)+", directives_paragraph)
            if re.match(r"\*.*", i.strip())
        ]
        for item in sublist
    ]


def get_note(par):
    return par[re.search("[ \t]*Note:[ \t]*", par).start() :]


def get_incremental_directives(directives_paragraph):
    note = get_note(directives_paragraph)
    or_regexp = ""
    for i in get_directives(directives_paragraph):
        or_regexp += i + "|"
    or_regexp = or_regexp[0 : len(or_regexp) - 1]
    return re.findall(or_regexp, note)
