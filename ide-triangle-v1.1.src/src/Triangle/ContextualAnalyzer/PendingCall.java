package Triangle.ContextualAnalyzer;

import Triangle.AbstractSyntaxTrees.Identifier;
import Triangle.AbstractSyntaxTrees.Visitor;

public abstract class PendingCall {
    private IdentificationTable callContextIdTable;
    private int level;

    public PendingCall(IdentificationTable callContextIdTable) {
        setCallContextIdTable(callContextIdTable);
        this.level = callContextIdTable.getLevel();
    }

    public abstract void visitPendingCall(Visitor v, Object o);

    public abstract Identifier getProcFuncIdentifier();

    public IdentificationTable getCallContextIdTable() {
        return callContextIdTable;
    }

    public void setCallContextIdTable(IdentificationTable callContextIdTable) {
        this.callContextIdTable = callContextIdTable;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
}