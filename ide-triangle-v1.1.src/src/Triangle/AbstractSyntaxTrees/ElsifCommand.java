/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Triangle.AbstractSyntaxTrees;

import Triangle.SyntacticAnalyzer.SourcePosition;

/**
 *
 * @author AEGS
 */
public class ElsifCommand extends Command{

    public ElsifCommand (Expression eAST, Command c1AST, Command c2AST,
                    SourcePosition thePosition) {
    super (thePosition);
    E = eAST;
    C1 = c1AST;
    C2 = c2AST;
  }

    @Override
    public Object visit(Visitor v, Object o) {
        return v.visitElsifCommand(this, o);
    }
    
    public Expression E;
    public Command C1, C2;
}
