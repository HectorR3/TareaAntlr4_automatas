from antlr4 import *
from grammarJavaListener import grammarJavaListener
from grammarJavaParser import *

class InPyToJava(grammarJavaListener):
    def __init__(self):
        self.main = 'public class Main {\n'
        self.codigo_main = '\tpublic static void main(String[] args) {\n'
        self.method = ""
        self.function_body = ""
        self.output_code = ""

    def enterProgram(self, ctx: grammarJavaParser.ProgramContext):
        self.output_code += self.main

    def exitProgram(self, ctx: grammarJavaParser.ProgramContext):
        self.output_code += "\n\t}\n}"
        print('A terminado la ejecucion')
        # Guardar el código generado en un archivo .txt
        with open("main.java", "w") as file:
            file.write(self.output_code)

    def enterCallfunction(self, ctx: grammarJavaParser.CallfunctionContext):
        self.output_code += self.codigo_main + f'\t\tSystem.out.println({ctx.getText()});\n'

    def exitCallfunction(self, ctx: grammarJavaParser.CallfunctionContext):
        self.output_code += "\t}\n"

    def enterFunction(self, ctx: grammarJavaParser.FunctionContext):
        function_name = ctx.IDCLASS().getText()
        self.method = f'\tpublic static int {function_name}('

    def exitFunction(self, ctx: grammarJavaParser.FunctionContext):
        self.output_code += self.method + "\n" + self.function_body + "\t\t}\n"
        self.method = ""
        self.function_body = ""

    def enterParameters(self, ctx: grammarJavaParser.ParametersContext):
        parameters = ", ".join(f"int {param.getText()}" for param in ctx.getChildren() if param.getText() != ",")
        self.method += parameters + ") {\n"

    def enterAssignment(self, ctx: grammarJavaParser.AssignmentContext):
        variable = ctx.IDCLASS().getText()
        expression = ctx.expression().getText()
        self.function_body += f"\t\tint {variable} = {expression};\n"

    def enterReturnStmt(self, ctx: grammarJavaParser.ReturnStmtContext):
        expression = ctx.expression().getText()
        self.function_body += f"\t\treturn {expression};\n"

    def enterPrintStmt(self, ctx: grammarJavaParser.PrintStmtContext):
        expression = ctx.expression().getText()
        self.codigo_main += f"\t\tSystem.out.println({expression});\n"
