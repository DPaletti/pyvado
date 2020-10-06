import yaml
import sys
from functools import lru_cache
from pathlib import Path
from dataclasses import dataclass
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.src_parsing as src
import dovado.global_user_selections as gus
import numpy as np
from dovado.frame_handling import setup_incremental
from dovado.src_parsing import IsIncremental
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
    is_incremental: IsIncremental


@dataclass
class DesignValue:
    utilisation: Dict[Tuple[str, str], float]
    negative_max_frequency: float


evaluation_setup = None
is_evaluation_setup = False


def setup_evaluation(
    stop_step,
    top_lang,
    to_box,
    top_module,
    src_folder,
    top_src,
    target_clock,
    is_incremental,
):
    global is_evaluation_setup
    if is_evaluation_setup:
        return
    global evaluation_setup
    evaluation_setup = EvaluationSetup(
        stop_step,
        top_lang,
        to_box,
        top_module,
        src_folder,
        top_src,
        target_clock,
        is_incremental,
    )
    is_evaluation_setup = True
    print("Evaluation Setup: " + str(evaluation_setup))


is_first_evaluation = True


@lru_cache
def evaluate(design_point: Tuple[int]) -> DesignValue:
    global is_first_evaluation
    if not evaluation_setup.is_boxed:
        for parameter, value in zip(gus.FREE_PARAMETERS, design_point):
            src.set_parameter(
                Path.joinpath(
                    Path(evaluation_setup.src_folder), CONFIG["VHDL_LOCAL_SRC"]
                ),
                evaluation_setup.top_module,
                parameter,
                value,
            )
    else:
        for parameter, value in zip(gus.FREE_PARAMETERS, design_point):
            src.map_parameter(
                Path(CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"])
                if evaluation_setup.top_lang is src.RTL.VHDL
                else Path(CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"]),
                "box",
                parameter,
                value,
            )
    vivado_out, success = vivado.source(
        CONFIG["TCL_DIR"] + CONFIG[evaluation_setup.stop_step.name]
    )
    print(vivado_out)
    if is_first_evaluation:
        is_first_evaluation = False
        setup_incremental(evaluation_setup.is_incremental)

    return (
        DesignValue(
            utilisation={i: np.inf for i in gus.METRICS},
            negative_max_frequency=np.inf,
        )
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
        except Exception as e:
            raise Exception(
                "Invalid metric passed to the fitness function: "
                + str(metric)
                + "\n"
                + str(e)
            )
