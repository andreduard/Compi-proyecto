package Triangle.ProgramWriter;

import Triangle.AbstractSyntaxTrees.*;

import java.io.FileWriter;
import java.io.IOException;

public class XMLVisitor implements Visitor {

    private final FileWriter fileWriter;

    public XMLVisitor(FileWriter fileWriter) {
        this.fileWriter = fileWriter;
    }

//<editor-fold desc="Commands" defaultstate=collapsed>
    @Override
    public Object visitAssignCommand(AssignCommand ast, Object o) {
        writeToXMLFile("<AssignCommand>\n");
        ast.V.visit(this, null);
        ast.E.visit(this, null);
        writeToXMLFile("</AssignCommand>\n");
        return null;
    }

    @Override
    public Object visitCallCommand(CallCommand ast, Object o) {
        writeToXMLFile("<CallCommand>\n");
        ast.I.visit(this, null);
        ast.APS.visit(this, null);
        writeToXMLFile("</CallCommand>\n");
        return null;
    }

    @Override
    public Object visitEmptyCommand(EmptyCommand ast, Object o) {
        writeToXMLFile("<EmptyCommand/>\n");
        return null;
    }

    @Override
    public Object visitIfCommand(IfCommand ast, Object o) {
        writeToXMLFile("<IfCommand>\n");
        ast.E.visit(this, null);
        ast.C1.visit(this, null);
        ast.C2.visit(this, null);
        writeToXMLFile("</IfCommand>\n");
        return null;
    }

    @Override
    public Object visitElsifCommand(ElsifCommand ast, Object o) {
        writeToXMLFile("<ElsifCommand>\n");
        ast.E.visit(this, null);
        ast.C1.visit(this, null);
        ast.C2.visit(this, null);
        writeToXMLFile("</ElsifCommand>\n");
        return null;
    }

    @Override
    public Object visitLetCommand(LetCommand ast, Object o) {
        writeToXMLFile("<LetCommand>\n");
        ast.D.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</LetCommand>\n");
        return null;
    }

    @Override
    public Object visitSequentialCommand(SequentialCommand ast, Object o) {
        writeToXMLFile("<SequentialCommand>\n");
        ast.C1.visit(this, null);
        ast.C2.visit(this, null);
        writeToXMLFile("</SequentialCommand>\n");
        return null;
    }

    @Override
    public Object visitWhileCommand(WhileCommand ast, Object o) {
        writeToXMLFile("<WhileCommand>\n");
        ast.E.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</WhileCommand>\n");
        return null;
    }

    @Override
    public Object visitUntilCommand(UntilCommand ast, Object o) {
        writeToXMLFile("<UntilCommand>\n");
        ast.E.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</UntilCommand>\n");
        return null;
    }

    @Override
    public Object visitDoWhileCommand(DoWhileCommand ast, Object o) {
        writeToXMLFile("<DoWhileCommand>\n");
        ast.E.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</DoWhileCommand>\n");
        return null;
    }

    @Override
    public Object visitDoUntilCommand(DoUntilCommand ast, Object o) {
        writeToXMLFile("<DoUntilCommand>\n");
        ast.E.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</DoUntilCommand>\n");
        return null;
    }

    @Override
    public Object visitRepeatVariableCommand(RepeatVariableCommand ast, Object o) {
        writeToXMLFile("<RepeatVariableCommand>\n");
        ast.RepVarDecl.visit(this, null);
        ast.E.visit(this, null);
        ast.C1.visit(this, null);
        writeToXMLFile("</RepeatVariableCommand>\n");
        return null;
    }
    //</editor-fold>

//<editor-fold desc="Expressions" defaultstate=collapsed>
    @Override
    public Object visitArrayExpression(ArrayExpression ast, Object o) {
        writeToXMLFile("<ArrayExpression>\n");
        ast.AA.visit(this, null);
        writeToXMLFile("</ArrayExpression>\n");
        return null;
    }

    @Override
    public Object visitBinaryExpression(BinaryExpression ast, Object o) {
        writeToXMLFile("<BinaryExpression>\n");
        ast.E1.visit(this, null);
        ast.O.visit(this, null);
        ast.E2.visit(this, null);
        writeToXMLFile("</BinaryExpression>\n");
        return null;
    }

    @Override
    public Object visitCallExpression(CallExpression ast, Object o) {
        writeToXMLFile("<CallExpression>\n");
        ast.I.visit(this, null);
        ast.APS.visit(this, null);
        writeToXMLFile("</CallExpression>\n");
        return null;
    }

    @Override
    public Object visitCharacterExpression(CharacterExpression ast, Object o) {
        writeToXMLFile("<CharacterExpression>\n");
        ast.CL.visit(this, null);
        writeToXMLFile("</CharacterExpression>\n");
        return null;
    }

    @Override
    public Object visitEmptyExpression(EmptyExpression ast, Object o) {
        writeToXMLFile("<EmptyExpression/>\n");
        return null;
    }

    @Override
    public Object visitIfExpression(IfExpression ast, Object o) {
        writeToXMLFile("<IfExpression>\n");
        ast.E1.visit(this, null);
        ast.E2.visit(this, null);
        ast.E3.visit(this, null);
        writeToXMLFile("</IfExpression>\n");
        return null;
    }

    @Override
    public Object visitIntegerExpression(IntegerExpression ast, Object o) {
        writeToXMLFile("<IntegerExpression>\n");
        ast.IL.visit(this, null);
        writeToXMLFile("</IntegerExpression>\n");
        return null;
    }

    @Override
    public Object visitLetExpression(LetExpression ast, Object o) {
        writeToXMLFile("<LetExpression>\n");
        ast.D.visit(this, null);
        ast.E.visit(this, null);
        writeToXMLFile("</LetExpression>\n");
        return null;
    }

    @Override
    public Object visitRecordExpression(RecordExpression ast, Object o) {
        writeToXMLFile("<RecordExpression>\n");
        ast.RA.visit(this, null);
        writeToXMLFile("</RecordExpression>\n");
        return null;
    }

    @Override
    public Object visitUnaryExpression(UnaryExpression ast, Object o) {
        writeToXMLFile("<UnaryExpression>\n");
        ast.O.visit(this, null);
        ast.E.visit(this, null);
        writeToXMLFile("</UnaryExpression>\n");
        return null;
    }

    @Override
    public Object visitVnameExpression(VnameExpression ast, Object o) {
        writeToXMLFile("<VnameExpression>\n");
        ast.V.visit(this, null);
        writeToXMLFile("</VnameExpression>\n");
        return null;
    }
    //</editor-fold>

//<editor-fold desc="Declarations" defaultstate=collapsed>
    @Override
    public Object visitBinaryOperatorDeclaration(BinaryOperatorDeclaration ast, Object o) {
        writeToXMLFile("BinaryOperatorDeclaration>\n");
        ast.ARG1.visit(this, null);
        ast.O.visit(this, null);
        ast.ARG2.visit(this, null);
        ast.RES.visit(this, null);
        writeToXMLFile("</BinaryOperatorDeclaration>\n");
        return null;
    }

    @Override
    public Object visitConstDeclaration(ConstDeclaration ast, Object o) {
        writeToXMLFile("ConstDeclaration>\n");
        ast.I.visit(this, null);
        ast.E.visit(this, null);
        writeToXMLFile("</ConstDeclaration>\n");
        return null;
    }

    @Override
    public Object visitFuncDeclaration(FuncDeclaration ast, Object o) {
        writeToXMLFile("FuncDeclaration>\n");
        ast.I.visit(this, null);
        ast.FPS.visit(this, null);
        ast.T.visit(this, null);
        ast.E.visit(this, null);
        writeToXMLFile("</FuncDeclaration>\n");
        return null;
    }

    @Override
    public Object visitProcDeclaration(ProcDeclaration ast, Object o) {
        writeToXMLFile("ProcDeclaration>\n");
        ast.I.visit(this, null);
        ast.FPS.visit(this, null);
        ast.C.visit(this, null);
        writeToXMLFile("</ProcDeclaration>\n");
        return null;
    }

    @Override
    public Object visitSequentialDeclaration(SequentialDeclaration ast, Object o) {
        writeToXMLFile("SequentialDeclaration>\n");
        ast.D1.visit(this, null);
        ast.D2.visit(this, null);
        writeToXMLFile("</SequentialDeclaration>\n");
        return null;
    }

    @Override
    public Object visitTypeDeclaration(TypeDeclaration ast, Object o) {
        writeToXMLFile("TypeDeclaration>\n");
        ast.I.visit(this, null);
        ast.T.visit(this, null);
        writeToXMLFile("</TypeDeclaration>\n");
        return null;
    }

    @Override
    public Object visitUnaryOperatorDeclaration(UnaryOperatorDeclaration ast, Object o) {
        writeToXMLFile("UnaryOperatorDeclaration>\n");
        ast.O.visit(this, null);
        ast.ARG.visit(this, null);
        ast.RES.visit(this, null);
        writeToXMLFile("</UnaryOperatorDeclaration>\n");
        return null;
    }

    @Override
    public Object visitVarDeclaration(VarDeclaration ast, Object o) {
        writeToXMLFile("VarDeclaration>\n");
        ast.I.visit(this, null);
        ast.T.visit(this, null);
        writeToXMLFile("</VarDeclaration>\n");
        return null;
    }

    @Override
    public Object visitRecursiveProcFunc(RecursiveProcFunc ast, Object o) {
        writeToXMLFile("RecursiveProcFunc>\n");
        ast.D.visit(this, null);
        writeToXMLFile("</RecursiveProcFunc>\n");
        return null;
    }

    @Override
    public Object visitPrivateDeclaration(PrivateDeclaration ast, Object o) {
        writeToXMLFile("PrivateDeclaration>\n");
        ast.dAST.visit(this, null);
        ast.dAST2.visit(this, null);
        writeToXMLFile("</PrivateDeclaration>\n");
        return null;
    }

    @Override
    public Object visitVarInitializedDeclaration(VarInitializedDeclaration ast, Object o) {
        writeToXMLFile("VarInitializedDeclaration>\n");
        ast.I.visit(this, null);
        ast.eAST.visit(this, null);
        writeToXMLFile("</VarInitializedDeclaration>\n");
        return null;
    }
    //</editor-fold>

//<editor-fold desc="Array Aggregates" defaultstate=collapsed>
    @Override
    public Object visitMultipleArrayAggregate(MultipleArrayAggregate ast, Object o) {
        writeToXMLFile("<MultipleArrayAggregate>\n");
        ast.E.visit(this, null);
        ast.AA.visit(this, null);
        writeToXMLFile("</MultipleArrayAggregate>\n");
        return null;
    }

    @Override
    public Object visitSingleArrayAggregate(SingleArrayAggregate ast, Object o) {
        writeToXMLFile("<SingleArrayAggregate>\n");
        ast.E.visit(this, null);
        writeToXMLFile("</SingleArrayAggregate>\n");
        return null;
    }
    //</editor-fold>

//<editor-fold desc="Record Aggregates" defaultstate=collapsed>
@Override
public Object visitMultipleRecordAggregate(MultipleRecordAggregate ast, Object o) {
    writeToXMLFile("<MultipleRecordAggregate>\n");
    ast.I.visit(this, null);
    ast.E.visit(this, null);
    ast.RA.visit(this, null);
    writeToXMLFile("</MultipleRecordAggregate>\n");
    return null;
}

@Override
public Object visitSingleRecordAggregate(SingleRecordAggregate ast, Object o) {
    writeToXMLFile("<SingleRecordAggregate>\n");
    ast.I.visit(this, null);
    ast.E.visit(this, null);
    writeToXMLFile("</SingleRecordAggregate>\n");
    return null;
}
//</editor-fold>

//<editor-fold desc="Formal Parameters" defaultstate=collapsed>
@Override
public Object visitConstFormalParameter(ConstFormalParameter ast, Object o) {
    writeToXMLFile("<ConstantFormalParameters>/n");
    ast.I.visit(this, null);
    ast.T.visit(this, null);
    writeToXMLFile("</ConstantFormalParameters>/n");
    return null;
}

@Override
public Object visitFuncFormalParameter(FuncFormalParameter ast, Object o) {
    writeToXMLFile("<FuncFormalParameter>/n");
    ast.I.visit(this, null);
    ast.FPS.visit(this, null);
    ast.T.visit(this, null);
    writeToXMLFile("</FuncFormalParameter>/n");
    return null;
}

@Override
public Object visitProcFormalParameter(ProcFormalParameter ast, Object o) {
    writeToXMLFile("<ProcFormalParameter>/n");
    ast.I.visit(this, null);
    ast.FPS.visit(this, null);
    writeToXMLFile("</ProcFormalParameter>/n");
    return null;
}

@Override
public Object visitVarFormalParameter(VarFormalParameter ast, Object o) {
    writeToXMLFile("<VarFormalParameter>/n");
    ast.I.visit(this, null);
    ast.T.visit(this, null);
    writeToXMLFile("</VarFormalParameter>/n");
    return null;
}

@Override
public Object visitEmptyFormalParameterSequence(EmptyFormalParameterSequence ast, Object o) {
    writeToXMLFile("<EmptyFormalParameterSequence/>\n");
    return null;
}

@Override
public Object visitMultipleFormalParameterSequence(MultipleFormalParameterSequence ast, Object o) {
    writeToXMLFile("<MultipleFormalParameterSequence>/n");
    ast.FP.visit(this, null);
    ast.FPS.visit(this, null);
    writeToXMLFile("</MultipleFormalParameterSequence>/n");
    return null;
}

@Override
public Object visitSingleFormalParameterSequence(SingleFormalParameterSequence ast, Object o) {
    writeToXMLFile("<SingleFormalParameterSequence>/n");
    ast.FP.visit(this, null);
    writeToXMLFile("</SingleFormalParameterSequence>/n");
    return null;
}
//</editor-fold>

//<editor-fold desc="Actual Parameters" defaultstate=collapsed>
@Override
public Object visitConstActualParameter(ConstActualParameter ast, Object o) {
    writeToXMLFile("<ConstantActualParameter>\n");
    ast.E.visit(this, null);
    writeToXMLFile("</ConstantActualParameter>\n");
    return null;
}

@Override
public Object visitFuncActualParameter(FuncActualParameter ast, Object o) {
    writeToXMLFile("<FuncActualParameter>\n");
    ast.I.visit(this, null);
    writeToXMLFile("</FuncActualParameter>\n");
    return null;
}

@Override
public Object visitProcActualParameter(ProcActualParameter ast, Object o) {
    writeToXMLFile("<ProcActualParameter>\n");
    ast.I.visit(this, null);
    writeToXMLFile("</ProcActualParameter>\n");
    return null;
}

@Override
public Object visitVarActualParameter(VarActualParameter ast, Object o) {
    writeToXMLFile("<VarActualParameter>\n");
    ast.V.visit(this, null);
    writeToXMLFile("</VarActualParameter>\n");
    return null;
}

@Override
public Object visitEmptyActualParameterSequence(EmptyActualParameterSequence ast, Object o) {
    writeToXMLFile("<EmptyActualParameterSequence/>\n");
    return null;
}

@Override
public Object visitMultipleActualParameterSequence(MultipleActualParameterSequence ast, Object o) {
    writeToXMLFile("<MultipleActualParameterSequence>\n");
    ast.AP.visit(this, null);
    ast.APS.visit(this, null);
    writeToXMLFile("</MultipleActualParameterSequence>\n");
    return null;
}

@Override
public Object visitSingleActualParameterSequence(SingleActualParameterSequence ast, Object o) {
    writeToXMLFile("<SingleActualParameterSequence>\n");
    ast.AP.visit(this, null);
    writeToXMLFile("</SingleActualParameterSequence>\n");
    return null;
}
//</editor-fold>

//<editor-fold desc="Denoters" defaultstate=collapsed>
@Override
public Object visitAnyTypeDenoter(AnyTypeDenoter ast, Object o) {
    writeToXMLFile("<AnyTypeDenoter/>\n");
    return null;
}

@Override
public Object visitArrayTypeDenoter(ArrayTypeDenoter ast, Object o) {
    writeToXMLFile("<ArrayTypeDenoter>\n");
    ast.IL.visit(this, null);
    ast.T.visit(this, null);
    writeToXMLFile("</ArrayTypeDenoter>\n");
    return null;
}

@Override
public Object visitBoolTypeDenoter(BoolTypeDenoter ast, Object o) {
    writeToXMLFile("<BoolTypeDenoter/>\n");
    return null;
}

@Override
public Object visitCharTypeDenoter(CharTypeDenoter ast, Object o) {
    writeToXMLFile("<CharTypeDenoter/>\n");
    return null;
}

@Override
public Object visitErrorTypeDenoter(ErrorTypeDenoter ast, Object o) {
    writeToXMLFile("<ErrorTypeDenoter/>\n");
    return null;
}

@Override
public Object visitSimpleTypeDenoter(SimpleTypeDenoter ast, Object o) {
    writeToXMLFile("<SimpleTypeDenoter>\n");
    ast.I.visit(this, null);
    writeToXMLFile("</SimpleTypeDenoter>\n");
    return null;
}

@Override
public Object visitIntTypeDenoter(IntTypeDenoter ast, Object o) {
    writeToXMLFile("<IntTypeDenoter/>\n");
    return null;
}

@Override
public Object visitRecordTypeDenoter(RecordTypeDenoter ast, Object o) {
    writeToXMLFile("<RecordTypeDenoter>\n");
    ast.FT.visit(this, null);
    writeToXMLFile("</RecordTypeDenoter>\n");
    return null;
}

@Override
public Object visitMultipleFieldTypeDenoter(MultipleFieldTypeDenoter ast, Object o) {
    writeToXMLFile("<MultipleFieldTypeDenoter>\n");
    ast.I.visit(this, null);
    ast.T.visit(this, null);
    ast.FT.visit(this, null);
    writeToXMLFile("</MultipleFieldTypeDenoter>\n");
    return null;
}

@Override
public Object visitSingleFieldTypeDenoter(SingleFieldTypeDenoter ast, Object o) {
    writeToXMLFile("<SingleFieldTypeDenoter>\n");
    ast.I.visit(this, null);
    ast.T.visit(this, null);
    writeToXMLFile("</SingleFieldTypeDenoter>\n");
    return null;
}
//</editor-fold>

//<editor-fold desc="Literals, Identifiers and Operators" defaultstate=collapsed>
@Override
public Object visitCharacterLiteral(CharacterLiteral ast, Object o) {
    writeToXMLFile("<CharaterLiteral ".concat("value=\"").concat(ast.spelling).concat("\"/>\n"));
    return null;
}

@Override
public Object visitIdentifier(Identifier ast, Object o) {
    writeToXMLFile("<Identifier ".concat("value=\"").concat(ast.spelling).concat("\"/>\n"));
    return null;
}

@Override
public Object visitIntegerLiteral(IntegerLiteral ast, Object o) {
    writeToXMLFile("<IntegerLiteral ".concat("value=\"").concat(ast.spelling).concat("\"/>\n"));
    return null;
}

@Override
public Object visitOperator(Operator ast, Object o) {
    writeToXMLFile("<Operator ".concat("value=\"").concat(ast.spelling).concat("\"/>\n"));
    return null;
}
//</editor-fold>

//<editor-fold desc="Value-or-variable names" defaultstate=collapsed>
@Override
public Object visitDotVname(DotVname ast, Object o) {
    writeToXMLFile("<DotVname>\n");
    ast.I.visit(this, null);
    ast.V.visit(this, null);
    writeToXMLFile("</DotVname>\n");
    return null;
}

@Override
public Object visitSimpleVname(SimpleVname ast, Object o) {
    writeToXMLFile("<SimpleVname>\n");
    ast.I.visit(this, null);
    writeToXMLFile("</SimpleVname>\n");
    return null;
}

@Override
public Object visitSubscriptVname(SubscriptVname ast, Object o) {
    writeToXMLFile("<SubscriptVname>\n");
    ast.V.visit(this, null);
    ast.E.visit(this, null);
    writeToXMLFile("</SubscriptVname>\n");
    return null;
}
//</editor-fold>

//<editor-fold desc="Programs" defaultstate=collapsed>
@Override
public Object visitProgram(Program ast, Object o) {
    writeToXMLFile("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n");
    writeToXMLFile("<Program>\n");
    ast.C.visit(this, null);
    writeToXMLFile("</Program>\n");
    return null;
}
//</editor-fold>

    private void writeToXMLFile(String content) {
        try {
            fileWriter.write(content);
            fileWriter.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
