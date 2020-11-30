from dovado_rtl.antlr.HdlRepresentation import (
    Entity,
    TopLevel,
    Port,
    Parameter,
)
from dovado_rtl.antlr.generated.vhdl.vhdlParserVisitor import vhdlParserVisitor
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from typing import List
from itertools import repeat


class VhdlEntityVisitor(vhdlParserVisitor):
    def __init__(self):
        self.top_level: TopLevel = TopLevel([], [])
        self.entities: List[Entity] = []

    def visitDesign_file(self, ctx: vhdlParser.Design_fileContext):
        for d in ctx.design_unit():
            self.visitDesign_unit(d)

    def visitDesign_unit(self, ctx: vhdlParser.Design_unitContext):
        self.visitContext_clause(ctx.context_clause())
        self.visitLibrary_unit(ctx.library_unit())

    def visitContext_clause(
        self, ctx: vhdlParser.Context_clauseContext
    ) -> None:
        for i in ctx.context_item():
            self.visitContext_item(i)

    def visitContext_item(self, ctx: vhdlParser.Context_itemContext):
        if ctx.library_clause():
            self.visitLibrary_clause(ctx.library_clause())
        if ctx.use_clause():
            self.visitUse_clause(ctx.use_clause())
        if ctx.context_reference():
            pass

    def visitLibrary_clause(self, ctx: vhdlParser.Library_clauseContext):
        for ln in self.visitLogical_name_list(ctx.logical_name_list()):
            self.top_level.add_library(ln)

    def visitUse_clause(self, ctx: vhdlParser.Use_clauseContext):
        for n in ctx.selected_name():
            self.top_level.add_used(self.visitSelected_name(n))

    def visitLogical_name_list(
        self, ctx: vhdlParser.Logical_name_listContext
    ) -> List[str]:
        return self.visitIdentifier_list(ctx.identifier_list())

    def visitIdentifier_list(
        self, ctx: vhdlParser.Identifier_listContext
    ) -> List[str]:
        for i in ctx.identifier():
            yield self.visitIdentifier(i)

    def visitSelected_name(self, ctx: vhdlParser.Selected_nameContext) -> str:
        out = self.visitIdentifier(ctx.identifier())
        for s in ctx.suffix():
            out += ("." + self.visitSuffix(s)) if self.visitSuffix(s) else ""
        return out

    def visitSuffix(self, ctx: vhdlParser.SuffixContext):
        if ctx.name_literal():
            return self.visitName_literal(ctx.name_literal())
        if ctx.KW_ALL():
            return ctx.KW_ALL().getText()

    def visitIdentifier(self, ctx: vhdlParser.IdentifierContext):
        return (
            ctx.BASIC_IDENTIFIER().getText()
            if ctx.BASIC_IDENTIFIER()
            else ctx.EXTENDED_IDENTIFIER()
        )

    def visitLibrary_unit(self, ctx: vhdlParser.Library_unitContext):
        if ctx.primary_unit():
            self.visitPrimary_unit(ctx.primary_unit())
        if ctx.secondary_unit():
            # architecture body and package body ignored
            pass

    def visitPrimary_unit(self, ctx: vhdlParser.Primary_unitContext):
        if ctx.entity_declaration():
            self.visitEntity_declaration(ctx.entity_declaration())
        else:
            pass

    def visitEntity_declaration(
        self, ctx: vhdlParser.Entity_declarationContext
    ):
        self.entities.append(Entity(self.visitIdentifier(ctx.identifier()[0])))
        if ctx.generic_clause():
            self.visitGeneric_clause(ctx.generic_clause())
        if ctx.port_clause():
            self.visitPort_clause(ctx.port_clause())

    def visitGeneric_clause(self, ctx: vhdlParser.Generic_clauseContext):
        self.visitGeneric_list(ctx.generic_list())

    def visitPort_clause(self, ctx: vhdlParser.Port_clauseContext):
        self.visitPort_list(ctx.port_list())

    def visitGeneric_list(self, ctx: vhdlParser.Generic_listContext):
        for i in self.visitInterface_list(ctx.interface_list()):
            self.entities[-1].add_parameter(Parameter(*i))

    def visitPort_list(self, ctx: vhdlParser.Port_listContext):
        for i in self.visitInterface_list(ctx.interface_list()):
            self.entities[-1].add_port(Port(*i))

    def visitInterface_list(self, ctx: vhdlParser.Interface_listContext):
        out = []
        for i in ctx.interface_element():
            for e in self.visitInterface_element(i):
                out.append(e)
        return out

    def visitInterface_element(self, ctx: vhdlParser.Interface_elementContext):
        return self.visitInterface_declaration(ctx.interface_declaration())

    def visitInterface_declaration(
        self, ctx: vhdlParser.Interface_declarationContext
    ):
        if ctx.interface_object_declaration():
            return self.visitInterface_object_declaration(
                ctx.interface_object_declaration()
            )
        else:
            return []

    def visitInterface_object_declaration(
        self, ctx: vhdlParser.Interface_object_declarationContext
    ):
        if ctx.interface_constant_declaration():
            return self.visitInterface_constant_declaration(
                ctx.interface_constant_declaration()
            )
        if ctx.interface_signal_declaration():
            return self.visitInterface_signal_declaration(
                ctx.interface_signal_declaration()
            )

    def visitInterface_constant_declaration(
        self, ctx: vhdlParser.Interface_constant_declarationContext
    ):
        for i, t in zip(
            self.visitIdentifier_list(ctx.identifier_list()),
            repeat(self.visitSubtype_indication(ctx.subtype_indication())),
        ):
            yield i, t

    def visitInterface_signal_declaration(
        self, ctx: vhdlParser.Interface_signal_declarationContext
    ):
        out = []
        if not ctx.signal_mode():
            for i, t in zip(
                self.visitIdentifier_list(ctx.identifier_list()),
                repeat(self.visitSubtype_indication(ctx.subtype_indication())),
            ):
                out.append((i, t))
            return out
        else:
            for i, s, t in zip(
                self.visitIdentifier_list(ctx.identifier_list()),
                repeat(self.visitSignal_mode(ctx.signal_mode())),
                repeat(self.visitSubtype_indication(ctx.subtype_indication())),
            ):
                out.append((i, s, t))
            return out

    def visitSignal_mode(self, ctx: vhdlParser.Signal_modeContext):
        return (
            "input"
            if ctx.KW_IN()
            else "output"
            if ctx.KW_OUT()
            else "inout"
            if ctx.KW_INOUT()
            else "buffer"
            if ctx.KW_BUFFER()
            else "linkage"
        )

    def visitSubtype_indication(
        self, ctx: vhdlParser.Subtype_indicationContext
    ):
        return self.visitType_mark(ctx.type_mark())

    def visitType_mark(self, ctx: vhdlParser.Type_markContext):
        return self.visitName(ctx.name())

    def visitName(self, ctx: vhdlParser.NameContext):
        if ctx.name_literal():
            return self.visitName_literal(ctx.name_literal())
        if ctx.external_name():
            return self.visitExternal_name(ctx.external_name())
        else:
            # skipping range in e.g. std_logic_vector
            return self.visitName(ctx.name())
            pass

    def visitName_literal(self, ctx: vhdlParser.Name_literalContext):
        if ctx.identifier():
            return self.visitIdentifier(ctx.identifier())
        if ctx.operator_symbol():
            return self.visitOperator_symbol(ctx.operator_symbol())
        if ctx.CHARACTER_LITERAL():
            return ctx.CHARACTER_LITERAL().getText()

    def visitOperator_symbol(self, ctx: vhdlParser.Operator_symbolContext):
        return ctx.STRING_LITERAL().getText()

    def visitExternal_name(self, ctx: vhdlParser.External_nameContext):
        return (
            ctx.SHIFT_LEFT().getText() + ctx.KW_VARIABLE().getText()
            if ctx.KW_VARIABLE()
            else ctx.KW_CONSTANT().getText()
            if ctx.KW_CONSTANT
            else ctx.KW_SIGNAL().getText()
            + self.visitExternal_pathname(ctx.external_pathname())
            + ctx.COLON().getText()
            + self.visitSubtype_indication(ctx.subtype_indication())
            + ctx.SHIFT_RIGHT().getText()
        )

    def visitExternal_pathname(self, ctx: vhdlParser.External_pathnameContext):
        if ctx.package_pathname():
            return self.visitPackage_pathname(ctx.package_pathname())
        if ctx.absolute_pathname():
            return self.visitAbsolute_pathname(ctx.absolute_pathname())
        if ctx.relative_pathname():
            return self.visitRelative_pathname(ctx.relative_pathname())

    def visitPackage_pathname(self, ctx: vhdlParser.Package_pathnameContext):
        out = ctx.AT().getText()
        for i in ctx.identifier()[:-1]:
            out += self.visitIdentifier(i) + "."
        return out + self.visitIdentifier(ctx.identifier()[-1])

    def visitAbsolute_pathname(self, ctx: vhdlParser.Absolute_pathnameContext):
        return "." + self.visitPartial_pathname(ctx.partial_pathname())

    def visitRelative_pathname(self, ctx: vhdlParser.Relative_pathnameContext):
        return (
            (ctx.UP().getText() + ".")
            if ctx.UP()
            else "" + self.visitPartial_pathname(ctx.partial_pathname())
        )

    def visitPartial_pathname(self, ctx: vhdlParser.Partial_pathnameContext):
        out = ""
        for p in ctx.pathname_element():
            out += self.visitPathname_element(p) + "."
        return out + self.visitIdentifier(ctx.identifier())

    def visitPathname_element(self, ctx: vhdlParser.Pathname_elementContext):
        if ctx.expression():
            print("Expression in pathname are not supported, skipping")
        return self.visitLabel(ctx.label())

    def visitLabel(self, ctx: vhdlParser.LabelContext):
        return self.visitIdentifier(ctx.identifier())
