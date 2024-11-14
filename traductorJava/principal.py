from antlr4 import *;
from grammarJavaLexer import grammarJavaLexer;
from grammarJavaParser import grammarJavaParser;
from grammarJavaListener import grammarJavaListener;
from InPyToJava import InPyToJava

def main():
    in_morse_line = input ('File name>')
    # Leer archivo de entrada
    file = open (in_morse_line)
    lexer = grammarJavaLexer(InputStream(file.read()))
    t_stream = CommonTokenStream(lexer)

    parser = grammarJavaParser(t_stream)

    tree = parser.program()

    print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    walker.walk(InPyToJava(), tree)

# .... . .-. --- -----
if __name__== '__main__':
    main()