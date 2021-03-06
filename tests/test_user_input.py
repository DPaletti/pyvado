import dovado.user_input as test
import io
import tests.vivado_2019_2_mock_data as version_dependent
from pathlib import Path
from unittest.mock import patch
import pytest
from dovado.src_parsing import StopStep, IsIncremental, ImplementationStep


@pytest.mark.skip("To Fix")
def test_ask_code_dir():
    for dir in [x for x in Path("examples").iterdir() if x.is_dir()]:
        with patch("sys.stdin", io.StringIO(str(dir))):
            assert test.ask_code_dir() == str(dir)

    with patch("sys.stdin", io.StringIO("\n")):
        assert test.ask_code_dir() == "./"

    with patch("sys.stdin", io.StringIO("invalid_path\n\n")):
        assert test.ask_code_dir() == "./"


def test_top_module_exists():
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "fifo_mem")
        == "examples/vhdl_fifo_memory/fifo.vhd"
        or test.top_module_exists("examples/vhdl_fifo_memory", "fifo_mem")
        == "examples/vhdl_fifo_memory/dovado_work_file.vhd"
    )
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "memory_array")
        == "examples/vhdl_fifo_memory/fifo.vhd"
        or test.top_module_exists("examples/vhdl_fifo_memory", "memory_array")
        == "examples/vhdl_fifo_memory/dovado_work_file.vhd"
    )
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "invalid") == None
    )
    assert test.top_module_exists("invalid", "") == None
    assert test.top_module_exists("invalid", "fifo_mem") == None
    # Verilog 2001
    assert (
        test.top_module_exists(
            "examples/verilog_unsigned_adder", "krnl_vadd_rtl_adder"
        )
        == "examples/verilog_unsigned_adder/unsigned_adder.sv"
    )


def test_default_top_module():
    assert test.default_top_module("examples/verilog_unsigned_adder") == (
        "krnl_vadd_rtl_adder",
        "examples/verilog_unsigned_adder/unsigned_adder.sv",
    ) or ("box", "examples/verilog_unsigned_adder/box.sv",)
    with pytest.raises(ValueError):
        test.default_top_module("invalid")


def test_ask_top_module():
    src_folder = "examples/vhdl_fifo_memory"
    module = "fifo_mem"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module),
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "krnl_vadd_rtl_adder"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module),
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == test.default_top_module(
            src_folder
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "invalid\n\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == test.default_top_module(
            src_folder
        )


def test_ask_part():
    for answer in version_dependent.parts:
        with patch(
            "dovado.vivado_interaction.get_parts",
            lambda: version_dependent.parts,
        ):
            with patch(
                "dovado.vivado_interaction.get_parts",
                lambda: version_dependent.parts,
            ):
                with patch(
                    "sys.stdin", io.StringIO("wrong part\n?\n" + answer + "\n")
                ):
                    assert test.ask_part() == answer


def test_ask_stop_step():
    for answer in {"synthesis\n", "implementation\n", "\n"}:
        with patch(
            "sys.stdin", io.StringIO("wrong stop step\n" + answer),
        ):
            assert (
                test.ask_stop_step() == StopStep.SYNTHESIS
                if answer.strip() == "synthesis"
                else StopStep.IMPLEMENTATION
                if answer != "\n"
                else test.ask_stop_step() == StopStep.SYNTHESIS
            )


def test_ask_incremental_mode():
    for stop_step in StopStep:
        for answers in {
            ("yes\n", "yes\n"),
            ("no\n", "no\n"),
            ("yes\n", "no\n"),
            ("no\n", "yes\n"),
            ("\n", "\n"),
        }:
            if stop_step is StopStep.SYNTHESIS:
                with patch(
                    "sys.stdin",
                    io.StringIO("wrong stop step\n" + answers[0] + ""),
                ):
                    assert test.ask_incremental_mode(
                        stop_step
                    ) == IsIncremental(
                        True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False
                    )
            elif stop_step is StopStep.IMPLEMENTATION:
                with patch(
                    "sys.stdin",
                    io.StringIO(
                        "wrong stop step\n" + answers[0] + answers[1] + ""
                    ),
                ):
                    assert test.ask_incremental_mode(
                        stop_step
                    ) == IsIncremental(
                        True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False,
                        True
                        if answers[1].strip() == "yes" or answers[1] == "\n"
                        else False,
                    )


def test_parse_comma_separated_list():
    assert test.parse_comma_separated_list(
        "[1-9]|1[0-1]", "1, 2, 3, 4, 11"
    ) == ["1", "2", "3", "4", "11"]
    assert not test.parse_comma_separated_list(
        "[1-9]|1[0-1]", "1, 2, 3, 4, 12"
    )


def mock_get_directives_paragraph(param):
    if param == "place":
        return version_dependent.place_directives_paragraph
    elif param == "route":
        return version_dependent.route_directives_paragraph
    elif param == "read checkpoint":
        return version_dependent.read_checkpoint_directives_paragraph


def mock_get_directives(param):
    if param == version_dependent.place_directives_paragraph:
        return version_dependent.place_directives
    if param == version_dependent.route_directives_paragraph:
        return version_dependent.route_directives
    if param == version_dependent.read_checkpoint_directives_paragraph:
        return version_dependent.read_checkpoint_directives


@patch(
    "dovado.doc_parsing.get_directives_paragraph",
    new=mock_get_directives_paragraph,
)
@patch("dovado.doc_parsing.get_directives", new=mock_get_directives)
def test__ask_implementation_directives():
    for to_ask in ImplementationStep:
        if to_ask is ImplementationStep.PLACE:
            directives = version_dependent.place_directives
        if to_ask is ImplementationStep.ROUTE:
            directives = version_dependent.route_directives
        incremental_directives = version_dependent.read_checkpoint_directives
        for incremental_mode in [
            IsIncremental(True, True),
            IsIncremental(True, False),
        ]:
            for answer in (
                incremental_directives
                if incremental_mode.implementation
                else directives
            ):
                with patch(
                    "sys.stdin", io.StringIO("?\n" + str(answer)),
                ):
                    assert (
                        test._ask_implementation_directives(
                            to_ask, incremental_mode
                        )
                        == answer
                    )
    with pytest.raises(ValueError):
        test._ask_implementation_directives("invalid", "ignored")


@patch(
    "dovado.doc_parsing.get_directives_paragraph",
    lambda x: version_dependent.synth_directives_paragraph,
)
@patch(
    "dovado.doc_parsing.get_directives",
    lambda x: version_dependent.synth_directives,
)
@patch(
    "dovado.user_input._ask_implementation_directives", lambda x, y: "default",
)
def test_ask_directives():
    with patch("sys.stdin", io.StringIO("runtimeoptimized")):
        assert test.ask_directives(
            StopStep.SYNTHESIS, IsIncremental(None, None)
        ) == ("runtimeoptimized", None, None,)
    with patch("sys.stdin", io.StringIO("invalid\n\n")):
        assert test.ask_directives(
            StopStep.SYNTHESIS, IsIncremental(None, None)
        ) == ("default", None, None,)
    with patch("sys.stdin", io.StringIO("invalid\n?\n\n")):
        incremental_mode = IsIncremental(True, True)
        assert test.ask_directives(
            StopStep.IMPLEMENTATION, incremental_mode
        ) == (
            "default",
            test._ask_implementation_directives("place", incremental_mode),
            test._ask_implementation_directives("route", incremental_mode),
        )


def test_ask_clock():
    with patch("sys.stdin", io.StringIO("40.0\n\n")):
        assert test.ask_clock() == 250

    with patch("sys.stdin", io.StringIO("400\n")):
        assert test.ask_clock() == 400


def test_get_default_clock_identifier():
    assert test.get_default_clock_identifier(
        "./examples/vhdl_fifo_memory/fifo.vhd", "fifo_mem"
    ) == ["clk"]


def test_is_valid_clock():
    assert test.is_valid_clock(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
        "rbs",
        "invalid port",
    ) == (None, None, None)

    assert set(("IN", "std_logic",)).issubset(
        set(
            test.is_valid_clock(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
                "rbs",
                "binN",
            )
        )
    )
    assert test.is_valid_clock(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs", "diffN",
    ) == (None, "OUT", "std_logic_vector")


def test_ask_identifiers():
    with patch("sys.stdin", io.StringIO("invalid\nbinN\ninvalid\ndiffN\n")):
        test_call = test.ask_identifiers(
            "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs"
        )
        assert str(test_call.name) == "binN"
    with patch("sys.stdin", io.StringIO("invalid\naclk\ninvalid\nm_tdata\n")):
        test_call = test.ask_identifiers(
            "./examples/verilog_unsigned_adder/unsigned_adder.sv",
            "krnl_vadd_rtl_adder",
        )
        assert str(test_call.name) == "aclk"


def test_ask_utilization_metrics():
    with patch("sys.stdin", io.StringIO("1, 2, 3, 3, 1")):
        assert set(
            test.ask_utilization_metrics(version_dependent.utilization_metrics)
        ) == set(
            [
                ("Slice Logic", "Slice LUTs*"),
                ("Slice Logic", "LUT as Memory"),
                ("Slice Logic", "LUT as Logic"),
            ]
        )

    with patch("sys.stdin", io.StringIO("1, 12")):
        assert set(
            test.ask_utilization_metrics(version_dependent.utilization_metrics)
        ) == set([("Slice Logic", "Slice LUTs*"), ("Memory", "RAMB36/FIFO*")])


def test_ask_parameters():
    with patch(
        "sys.stdin",
        io.StringIO("invalid\nMalformed,,List\nNbit_rbs\n fake\n"),
    ):
        assert test.ask_parameters(
            "examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs"
        ) == ["Nbit_rbs"]
