package Triangle.AbstractSyntaxTrees;

import Triangle.SyntacticAnalyzer.SourcePosition;

public class RecursiveProcFunc extends Declaration {
    public Declaration D;
    public RecursiveProcFunc(Declaration declarationAST, SourcePosition thePosition) {
        super(thePosition);
        this.D = declarationAST;
    }

    @Override
    public Object visit(Visitor v, Object o) {
        return v.visitRecursiveProcFunc(this,o);
    }
}
