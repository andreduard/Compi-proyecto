package Triangle.AbstractSyntaxTrees;

import Triangle.SyntacticAnalyzer.SourcePosition;

public class PrivateDeclaration extends Declaration {
    public Declaration dAST;
    public Declaration dAST2;


    public PrivateDeclaration(Declaration declarationAST, Declaration declarationAST2, SourcePosition thePosition) {
        super(thePosition);
        this.dAST = declarationAST;
        this.dAST2 = declarationAST2;
    }

    @Override
    public Object visit(Visitor v, Object o) {
        return v.visitPrivateDeclaration(this, o);
    }
}
