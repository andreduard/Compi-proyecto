package Triangle.AbstractSyntaxTrees;

import Triangle.SyntacticAnalyzer.SourcePosition;

public class VarInitializedDeclaration extends VarDeclaration {
    public Expression eAST;
    public VarInitializedDeclaration(Identifier iAST, Expression eAST, SourcePosition thePosition) {
        //semantico se encargara del tipo tAST mas adelante
        super(iAST,null,thePosition);
        this.eAST = eAST;
    }

    @Override
    public Object visit(Visitor v, Object o) {
        return v.visitVarInitializedDeclaration(this, o);
    }
}
