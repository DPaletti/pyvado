import dovado.doc_parsing as d
import pytest
from hypothesis import given, example
from hypothesis.strategies import text
import tests.vivado_2019_2_mock_data as version_dependent


# Care in this test \n is assumed as newline
@given(command=text())
@example(command="synthesis")
@example(command="place")
@example(command="route")
# ignoring a false positive HypothesisDeprecationWarning
# other warnings may be shadowed too
@pytest.mark.filterwarnings("ignore:tests/test_doc_parsing.py")
def test_get_directives_paragraph(command, monkeypatch):
    with monkeypatch.context() as m:
        if command not in {"synthesis", "place", "route"}:
            pytest.raises(ValueError, d.get_directives_paragraph, command)
            return
        if command == "synthesis":
            m.setattr(
                "dovado.vivado_interaction.get_help",
                lambda x: version_dependent.help_synth_design,
            )
            assert d.get_directives_paragraph(
                command
            ) in version_dependent.synth_directives_paragraph.replace(
                "\n\n", "\n"
            )
        elif command == "place":
            m.setattr(
                "dovado.vivado_interaction.get_help",
                lambda x: version_dependent.help_place_design,
            )
            assert d.get_directives_paragraph(
                command
            ) in version_dependent.place_directives_paragraph.strip().replace(
                "\n\n", "\n"
            )
        elif command == "route":
            m.setattr(
                "dovado.vivado_interaction.get_help",
                lambda x: version_dependent.help_route_design,
            )
            assert d.get_directives_paragraph(
                command
            ) in version_dependent.route_directives_paragraph.strip().replace(
                "\n\n", "\n"
            )


def test_get_directives():
    assert (
        d.get_directives(version_dependent.route_directives_paragraph)
        == version_dependent.route_directives
    )
    assert (
        d.get_directives(version_dependent.place_directives_paragraph)
        == version_dependent.place_directives
    )
    assert (
        d.get_directives(version_dependent.synth_directives_paragraph)
        == version_dependent.synth_directives
    )


def test_get_note():
    assert (
        d.get_note(version_dependent.route_directives_paragraph)
        in version_dependent.route_note
    )

    assert (
        d.get_note(version_dependent.place_directives_paragraph)
        in version_dependent.place_note
    )


def test_get_incremental_directives():
    assert (
        d.get_incremental_directives(
            version_dependent.route_directives_paragraph
        )
        == version_dependent.incremental_route_directives
    )

    assert (
        d.get_incremental_directives(
            version_dependent.place_directives_paragraph
        )
        == version_dependent.incremental_place_directives
    )
