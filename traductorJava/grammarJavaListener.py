# Generated from grammarJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarJavaParser import grammarJavaParser
else:
    from grammarJavaParser import grammarJavaParser

# This class defines a complete listener for a parse tree produced by grammarJavaParser.
class grammarJavaListener(ParseTreeListener):

    # Enter a parse tree produced by grammarJavaParser#program.
    def enterProgram(self, ctx:grammarJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#program.
    def exitProgram(self, ctx:grammarJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#print.
    def enterPrint(self, ctx:grammarJavaParser.PrintContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#print.
    def exitPrint(self, ctx:grammarJavaParser.PrintContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#callfunction.
    def enterCallfunction(self, ctx:grammarJavaParser.CallfunctionContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#callfunction.
    def exitCallfunction(self, ctx:grammarJavaParser.CallfunctionContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#function.
    def enterFunction(self, ctx:grammarJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#function.
    def exitFunction(self, ctx:grammarJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#parameters.
    def enterParameters(self, ctx:grammarJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#parameters.
    def exitParameters(self, ctx:grammarJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#parameter.
    def enterParameter(self, ctx:grammarJavaParser.ParameterContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#parameter.
    def exitParameter(self, ctx:grammarJavaParser.ParameterContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#block.
    def enterBlock(self, ctx:grammarJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#block.
    def exitBlock(self, ctx:grammarJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#statement.
    def enterStatement(self, ctx:grammarJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#statement.
    def exitStatement(self, ctx:grammarJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#assignment.
    def enterAssignment(self, ctx:grammarJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#assignment.
    def exitAssignment(self, ctx:grammarJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#expression.
    def enterExpression(self, ctx:grammarJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#expression.
    def exitExpression(self, ctx:grammarJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#returnStmt.
    def enterReturnStmt(self, ctx:grammarJavaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#returnStmt.
    def exitReturnStmt(self, ctx:grammarJavaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by grammarJavaParser#printStmt.
    def enterPrintStmt(self, ctx:grammarJavaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by grammarJavaParser#printStmt.
    def exitPrintStmt(self, ctx:grammarJavaParser.PrintStmtContext):
        pass



del grammarJavaParser