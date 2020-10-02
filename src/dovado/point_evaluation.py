import yaml
from functools import lru_cache
from pathlib import Path
from dataclasses import dataclass
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.src_parsing as src
import numpy as np
import dovado.global_user_selections as gus
from typing import Tuple, Dict

CONFIG = yaml.safe_load(Path("config.yaml").open())


@dataclass
class EvaluationSetup:
    stop_step: src.StopStep
    top_lang: src.RTL
    is_boxed: bool
    top_module: str
    src_folder: str
    top_src: str
    target_clock: float


@dataclass
class DesignValue:
    utilisation: Dict[Tuple[str, str], float]
    negative_max_frequency: float


evaluation_setup = None
is_evaluation_setup = False


def setup_evaluation(
    stop_step, top_lang, to_box, top_module, src_folder, target_clock
):
    global is_evaluation_setup
    if is_evaluation_setup:
        return
    global evaluation_setup
    evaluation_setup = EvaluationSetup(
        stop_step, top_lang, to_box, top_module, src_folder, target_clock
    )
    is_evaluation_setup = True


@lru_cache
def evaluate(design_point: Tuple[int]) -> DesignValue:
    if not evaluation_setup.is_boxed:
        for parameter, value in zip(gus.FREE_PARAMETERS, design_point):
            src.set_parameter(
                Path.joinpath(
                    Path(evaluation_setup.src_folder), CONFIG["VHDL_LOCAL_SRC"]
                ),
                evaluation_setup.top_module,
                src.get_parameter_on_name(
                    Path.joinpath(
                        Path(evaluation_setup.src_folder),
                        evaluation_setup.top_src,
                    ),
                    evaluation_setup.top_module,
                    parameter,
                ),
                value,
            )
    else:
        for parameter, value in zip(gus.FREE_PARAMETERS, design_point):
            src.map_parameter(
                Path(CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"])
                if evaluation_setup.top_lang is src.RTL.VHDL
                else Path(CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"]),
                evaluation_setup.top_module,
                src.get_parameter_on_name(
                    Path.joinpath(
                        Path(evaluation_setup.src_folder),
                        evaluation_setup.top_src,
                    ),
                    evaluation_setup.top_module,
                    parameter,
                ),
                value,
            )
    vivado_out, success = vivado.source(
        CONFIG["TCL_DIR"] + CONFIG[evaluation_setup.stop_step.name]
    )
    print(vivado_out)
    return (
        DesignValue(np.inf, np.inf)
        if not success
        else DesignValue(
            utilisation={
                i: report.get_utilisation(
                    CONFIG["VIVADO_OUTPUT_DIR"]
                    + CONFIG[evaluation_setup.stop_step.name + "_UTILISATION"],
                    i[0],
                    i[1],
                )
                for i in gus.METRICS
            },
            negative_max_frequency=-float(
                get_max_frequency(
                    report.get_wns(
                        CONFIG["VIVADO_OUTPUT_DIR"]
                        + CONFIG[evaluation_setup.stop_step.name + "_TIMING"]
                    )
                )
            ),
        )
    )


def get_max_frequency(wns):

    return 1000 / ((1 / 1000 * evaluation_setup.target_clock) - wns)


def get_metric(design_value, metric):
    if metric == "max_frequency":
        return design_value.negative_max_frequency
    else:
        try:
            return design_value.utilisation[metric]
        except Exception:
            raise Exception(
                "Invalid metric passed to the fitness function: " + str(metric)
            )
