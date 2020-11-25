from pathlib import Path
from typing import List, Tuple, Any, Union, Optional, Dict
from antlr4 import CommonTokenStream, FileStream
from dovado_rtl.antlr.generated.vhdl.vhdlLexer import vhdlLexer
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from dovado_rtl.antlr.VhdlEntityVisitor import VhdlEntityVisitor
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Parser import (
    Verilog2001Parser,
)
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Lexer import (
    Verilog2001Lexer,
)
from dovado_rtl.antlr.Verilog2001EntityVisitor import Verilog2001EntityVisitor
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLParser import (
    SysVerilogHDLParser,
)
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLLexer import (
    SysVerilogHDLLexer,
)
from dovado_rtl.antlr.SysVerilogHDLEntityVisitor import (
    SysVerilogHDLEntityVisitor,
)
from dovado_rtl.antlr.HdlRepresentation import (
    Entity,
    TopLevel,
    Parameter,
    Port,
)
from dovado_rtl.utility_classes import RTL


class SourceFile:
    def __init__(self, src_path: str, entity: Optional[str] = None):
        self.posix_path = Path(src_path)
        supported_extensions = [".vhd", ".vhdl", ".v", ".sv"]
        if self.posix_path.suffix not in supported_extensions:
            raise Exception(
                "Supported extensions are: "
                + str(supported_extensions)
                + ", input extension "
                + self.posix_path.suffix
                + " not supported"
            )
        self.__input_stream = FileStream(self.posix_path.read_text())
        self.__RTL = (
            RTL.VHDL
            if (
                self.posix_path.suffix == ".vhd"
                or self.posix_path.suffix == ".vhdl"
            )
            else RTL.VERILOG
            if self.posix_path.suffix == ".v"
            else RTL.SYSTEM_VERILOG
        )
        self.__entities, self.__top_level = self.parse()
        self.__selected_entity: Optional[Entity] = entity

    def parse(self) -> Tuple[List[Entity], Union[TopLevel, Any]]:
        if self.__RTL is RTL.VHDL:
            lexer = vhdlLexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = vhdlParser(token_stream)
            visitor = VhdlEntityVisitor()
        elif self.__RTL is RTL.VERILOG:
            lexer = Verilog2001Lexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = Verilog2001Parser(token_stream)
            visitor = Verilog2001EntityVisitor()
        else:
            lexer = SysVerilogHDLLexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = SysVerilogHDLParser(token_stream)
            visitor = SysVerilogHDLEntityVisitor()

        tree = parser.design_file()
        visitor.visit(tree)
        return visitor.entities, visitor.top_level

    def get_entity(self, entity: str) -> Entity:
        for e in self.__entities:
            if e.get_name() == entity:
                return e
        raise Exception(
            "Entity "
            + entity
            + " has not been found among parsed entities "
            + str(self.__entities)
        )

    def set_entity(self, entity: str) -> None:
        self.__selected_entity = self.get_entity(entity)

    def get_top_entity(self) -> Entity:
        return self.__selected_entity

    def get_path(self) -> str:
        return str(self.posix_path)

    def get_folder(self) -> str:
        return str(self.posix_path.parents[0])

    def get_hdl(self) -> RTL:
        return self.__RTL

    def get_entities(self) -> List[Entity]:
        return self.__entities

    def get_parameters(self) -> List[Parameter]:
        return self.__selected_entity.get_parameters()

    def __get_parameter(self, parameter: str) -> Parameter:
        for p in self.__selected_entity.get_parameters():
            if p.get_name() == parameter:
                return p
        raise Exception(
            "Parameter "
            + parameter
            + "has not been found among parsed parameters"
            + str(self.__selected_entity.get_parameters())
            + " in entity "
            + self.__selected_entity.get_name()
        )

    def get_top_level(self):
        return self.__top_level

    def get_parameter_value(self, parameter: str) -> Optional[int]:
        return self.__get_parameter(parameter).get_value()

    def __set_parameter_value(self, parameter: str, value: int) -> None:
        self.__get_parameter(parameter).set_value(value)

    def write_parameter_values(
        self, handler, values: Dict[str, int],
    ):
        # here the handler is a HdlBoxHandler, cannot import the name
        # due to circular import
        for p, v in values:
            self.__set_parameter_value(p, v)
        handler.fill_box(
            [
                p
                for p in self.__selected_entity.get_parameters()
                if p in values.keys()
            ]
        )

    def get_ports(self) -> List[Port]:
        return self.__selected_entity.get_ports()

    def get_port(self, port: str) -> Port:
        for p in self.__selected_entity.get_ports():
            if p.get_name() == port:
                return p
        raise Exception(
            "Port "
            + port
            + "has not been found among parsed ports"
            + str(self.__selected_entity.get_ports())
            + " in entity "
            + self.__selected_entity.get_name()
        )

    def check_port(self, port: str) -> Optional[Port]:
        for p in self.__selected_entity.get_ports():
            if p.get_name() == port:
                return p
        return None

    def get_port_direction(self, port: str) -> str:
        return self.get_port(port).get_direction()

    def get_port_type(self, port: str) -> str:
        return self.get_port(port).get_type()

    def get_imports(self) -> Tuple[List[str], List[str]]:
        return (
            self.__top_level.get_libraries(),
            self.__top_level.get_use_clauses(),
        )