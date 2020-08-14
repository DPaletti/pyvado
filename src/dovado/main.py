import dovado.user_input as user_input
import dovado.tcl_parsing as tcl
import dovado.report_parsing as report
import dovado.vivado_interaction as vivado
import yaml
from pathlib import Path


def main():
    # Starting Vivado in the background
    vivado.start()

    CONFIG = yaml.safe_load(Path("config.yaml").open())

    SRC_FOLDER = user_input.ask_code_dir()
    TOP_MODULE, TOP_SRC = user_input.ask_top_module(SRC_FOLDER)

    SYNTHESIS_PART = user_input.ask_part()

    # STOP_STEP can take the following values:
    #  "synthesis", "implementation"
    STOP_STEP = user_input.ask_stop_step()

    # Clock and out are needed for boxing the component
    # to avoid overflowing pins
    if STOP_STEP == "implementation":
        CLOCK_PORT, OUT_PORT = user_input.ask_identifiers(TOP_SRC, TOP_MODULE)

    # INCREMENTAL_MODE has the following structure:
    # {"is synthesis incremental" : boolean,
    #  "is implementation incremental" : boolean}
    # if STOP_STEP == "synthesis" the second key is absent
    INCREMENTAL_MODE = user_input.ask_incremental_mode(STOP_STEP)

    # Directives to give to the -directive switch in
    # synth_design and eventually in place_design and route_design
    # some directives are forbidden in incremental mode
    # for place_design and route_design
    (
        SYNTHESIS_DIRECTIVES,
        PLACE_DIRECTIVES,
        ROUTE_DIRECTIVES,
    ) = user_input.ask_directives(STOP_STEP, INCREMENTAL_MODE)

    CLOCK = user_input.ask_clock()

    # Swapping out placeholder in constraint file
    tcl.fill_frame(
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT_FRAME"],
        [str(1000 / CLOCK)],
        CONFIG["PLACEHOLDER"],
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
    )

    # Swapping out placeholders in TCL scripts
    tcl.fill_frame(
        CONFIG["TCL_DIR"] + CONFIG[STOP_STEP.upper() + "_FRAME"],
        [
            CONFIG["VIVADO_OUTPUT_DIR"],
            SRC_FOLDER,
            CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
            TOP_MODULE,
            SYNTHESIS_PART,
            CONFIG[STOP_STEP.upper() + "_TIMING"],
            CONFIG[STOP_STEP.upper() + "_UTILISATION"],
        ],
        CONFIG["PLACEHOLDER"],
        CONFIG[STOP_STEP.upper()],
    )

    # Calling vivado to evaluate the script
    vivado.execute_command("source " + CONFIG[STOP_STEP.upper()])

    utilization_metrics = {
        i: report.get_utilisation(
            CONFIG["UTILIZATION METRICS"],
            CONFIG["UTILIZATION_SECTION_TITLES"],
            CONFIG["VIVADO_OUTPUT_DIR"]
            + CONFIG[STOP_STEP.upper() + "UTILISATION"],
            "Util%",
            i,
        )
        for i in user_input.ask_utilization_metrics()
    }

    max_frequency = report.get_wns(
        CONFIG["VIVADO_OUTPUT_DIR"] + CONFIG["VIVADO_TIMING_SETUP_REPORT_NAME"]
    )
    print("Utilization metrics: " + str(utilization_metrics))
    print("Max frequency: " + str(max_frequency))
