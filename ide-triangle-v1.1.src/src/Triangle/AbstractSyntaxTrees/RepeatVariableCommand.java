package Triangle.AbstractSyntaxTrees;

import Triangle.SyntacticAnalyzer.SourcePosition;

public class RepeatVariableCommand extends Command {

    public RepeatVariableCommand(Expression eAST, Command c1AST, ConstDeclaration dAST,
                                 SourcePosition thePosition) {
        super (thePosition);
        E = eAST;
        C1 = c1AST;
        RepVarDecl = dAST;
    }

    public Object visit(Visitor v, Object o) {
        return v.visitRepeatVariableCommand(this, o);
    }

    public Expression E;
    public Command C1;
    public ConstDeclaration RepVarDecl;
}
