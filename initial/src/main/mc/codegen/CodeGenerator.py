'''
 *   @author Pham Trong Nhan
 *   @version 1.0
 *   18/12/2019
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType([], IntType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym, isGlobal = False):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

        # self declare - list of global var
        self.listGlobalArray = []

    def getType(self, object_type):
        if type(object_type) is ArrayType:
            return ArrayPointerType(object_type.eleType)
        else:
            return object_type

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        globalDecl = self.env

        for x in ast.decl:
            if type(x) is FuncDecl:
                paralist = [para.varType for para in x.param]
                globalDecl = [Symbol(x.name.name, MType(paralist, x.returnType), CName(self.className))] + globalDecl
            else:
                varDecl = self.visit(x, SubBody(None, None, isGlobal = True))
                globalDecl = [varDecl] + globalDecl
        
        e = SubBody(None, globalDecl)
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, e)

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), c, Frame("<init>", VoidType))
        # ! ONLY create this function when there are GLOBAL ARRAY DECL
        # self.genMETHOD(FuncDecl(Id("<clinit>"), list(), None, Block(list())), c, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    '''
        Generate code for function declare
        Detect ast.name to generate right declaration:
        - main -> Add 1 more argument args
        - init -> Add 1 more argument this
        - clinit -> Create stack space for global array decl
        - other -> do nothing more
        Enterscope(True) -> to clear stack after exit function
    '''
    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None and consdecl.name.name == "<init>"
        isClassInit = consdecl.returnType is None and consdecl.name.name == "<clinit>"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        # isMain = consdecl.name.name == "main" and len(consdecl.param) == 0
        returnType = VoidType() if isInit or isClassInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [self.getType(x.varType) for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        isProc = type(returnType) is VoidType
        frame.enterScope(isProc)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        varList = SubBody(frame, glenv)
        for x in consdecl.param:
            varList = self.visit(x, varList)

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # ! Init global array declare - Class init

        for x in body.member:
            if type(x) is VarDecl:
                # var = self.visit(x, SubBody(None, None))
                varList = self.visit(x, varList)
            else:
                self.visit(x, varList)
                # list(map(lambda x: self.visit(x, varList), body.member))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        # return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    '''
        VarDecl global -> static variable (attribute)
        local -> local variable
    '''
    def visitVarDecl(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        isGlobal = ctxt.isGlobal
        varName = ast.variable
        varType = ast.varType

        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, varType, False, ""))
            return Symbol(varName, varType)
        # params - local var
        else:
            index = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            return SubBody(frame, [Symbol(varName, varType, Index(index))] + ctxt.sym)

    def visitCallExpr(self, ast: CallExpr, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value

        ctype = sym.mtype
        paraTypes = ctype.partype # List of type of parameter

        in_ = ""
        i = 0
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(paraTypes[i]) is FloatType and type(typ1) is IntType:
                str1 = str1 + self.emit.emitI2F(frame)
            in_ = in_ + str1
            i += 1

        if type(ctype.rettype) is VoidType:
            self.emit.printout(in_)
            self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
        else:
            return in_ + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), ctype.rettype

    def visitBlock(self, ast: Block, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym

        hasReturnStmt = False

        # Create Label for start - end scope
        frame.enterScope(False)
        varList = SubBody(frame, symbols)
        # print start LABEL
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Visit every stmt in scope
        for x in ast.member:
            if type(x) is VarDecl:
                varList = self.visit(x, varList)
            else:
                stmt = self.visit(x, varList)
                # Return Stmt
                if stmt == True:
                    hasReturnStmt = stmt 
        # Close scope
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return hasReturnStmt

# ---------------------------------------------------------------------------------------------------------------------------
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        # ast: BooleanLiteral
        # o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

# -----------------------------------------------------------------------------------------------------------
    def visitIf(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym

        expr, expType = self.visit(ast.expr, Access(frame, symbols, False, True))
        self.emit.printout(expr)

        labelTrue = frame.getNewLabel()
        labelEnd = frame.getNewLabel()

        self.emit.printout(self.emit.emitIFTRUE(labelTrue, frame))
        # Find return in Else Stmt
        hasReturnStmt = False
        if ast.elseStmt is not None:
            hasReturnStmt = True is self.visit(ast.elseStmt, ctxt)  
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelEnd, frame))
        # Find return in Then Stmt
        self.emit.printout(self.emit.emitLABEL(labelTrue, frame))
        hasReturnStmt = True is self.visit(ast.thenStmt, ctxt) and hasReturnStmt
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        return hasReturnStmt

    def visitDowhile(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        expr, expType = self.visit(ast.exp, Access(frame, symbols, False, True))

        labelStart = frame.getNewLabel()
        labelEnd = frame.getNewLabel()
        frame.enterLoop()
        # Start every statements in loop
        self.emit.printout(self.emit.emitLABEL(labelStart, frame))
        
        hasReturnStmt = False
        for x in ast.sl:
            stmt = self.visit(x, ctxt)
            if stmt is True:
                hasReturnStmt = True

        # * Jump to here if exist CONTINUE STMT
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        
        # * Check expression result if False then end
        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(labelEnd, frame))
        
        # * If dont have RETURN STMT -> keep looping
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelStart, frame))

        # * Jump here if exist BREAK
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitFor(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym

        # expr1 = self.visit(ast.expr1, Access(frame, symbols, False, True))
        expr2, expType = self.visit(ast.expr2, Access(frame, symbols, False, True))

        labelStart = frame.getNewLabel()
        labelEnd = frame.getNewLabel()

        # Init counter
        self.visit(ast.expr1, Access(frame, symbols, False, True))
        # Enter loop
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelStart, frame))
        
        # Check condition
        self.emit.printout(expr2)
        self.emit.printout(self.emit.emitIFFALSE(labelEnd, frame))

        # run stmts
        hasReturnStmt = True is self.visit(ast.loop, ctxt)
        
        # finish loop
        # * Jump to here if exist CONTINUE STMT
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        

        expr3 = self.visit(ast.expr3, Access(frame, symbols, False, True))

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelStart, frame))
        # * Jump here if exist BREAK
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitReturn(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame 
        sym = ctxt.sym
        returnType = frame.returnType
        if not type(returnType) is VoidType:
            expr, expType = self.visit(ast.expr, Access(frame, sym, False, True))
            if type(returnType) is FloatType and type(expType) is IntType:
                expr = expr + self.emit.emitI2F(frame)
            self.emit.printout(expr)
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        return True

# --------------------------------------------------------------------------------------------------------------------
    def visitId(self, ast, o: Access):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        variable = self.lookup(ast.name, sym, lambda x: x.name)

        if not isFirst and isLeft: 
            frame.push()
        elif not isFirst and not isLeft: 
            frame.pop()

        emitType = variable.mtype
        if variable.value is None:
            if isLeft:
                returnValue = self.emit.emitPUTSTATIC(self.className + "/" + variable.name, emitType, frame)
            else:
                returnValue = self.emit.emitGETSTATIC(self.className + "/" + variable.name, emitType, frame)
        else:
            if isLeft:
                returnValue = self.emit.emitWRITEVAR(variable.name, emitType, variable.value.value, frame)
            else:
                returnValue = self.emit.emitREADVAR(variable.name, emitType, variable.value.value, frame)
        return returnValue, emitType

    def visitBinaryOp(self, ast, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        op = ast.op

        if op in ['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=']:
            lhs, leftType = self.visit(ast.left, ctxt)
            rhs, rightType = self.visit(ast.right, ctxt)

            if type(leftType) in [IntType, BoolType] and type(rightType) in [IntType, BoolType]:
                retType = IntType()
            else:
                retType = FloatType()

            if type(leftType) is IntType and type(retType) != type(leftType): 
                lhs = lhs + self.emit.emitI2F(frame)
            if type(rightType) is IntType and type(retType) != type(rightType): 
                rhs = rhs + self.emit.emitI2F(frame)

            if op in ['+', '-']:
                return lhs + rhs + self.emit.emitADDOP(op, retType, frame), retType
            elif op in ['*', '/']:
                return lhs + rhs + self.emit.emitMULOP(op, retType, frame), retType
            elif op == '%':
                return lhs + rhs + self.emit.emitMOD(frame), retType
            else:
                return lhs + rhs + self.emit.emitREOP(op, retType, frame), BoolType()
        elif op in ['&&', '||']:
            # ! Try short-circuit HERE
            labelFalse = frame.getNewLabel()
            labelTrue = frame.getNewLabel()
            labelEnd = frame.getNewLabel()

            codegen = []
            lhs, leftType = self.visit(ast.left, ctxt)
            codegen.append(lhs)

            if op == '&&':
                codegen.append(self.emit.emitIFFALSE(labelFalse, frame))
            else:
                codegen.append(self.emit.emitIFTRUE(labelTrue, frame))
            rhs, rightType = self.visit(ast.right, ctxt)
            codegen.append(rhs)

            # post process if second clause is False 
            codegen.append(self.emit.emitIFFALSE(labelFalse, frame))
            codegen.append(self.emit.emitLABEL(labelTrue, frame))
            codegen.append(self.emit.emitPUSHICONST(1, frame))
            codegen.append(self.emit.emitGOTO(labelEnd, frame))
            # post process if second clause is TRUE
            codegen.append(self.emit.emitLABEL(labelFalse, frame))
            codegen.append(self.emit.emitPUSHICONST(0, frame))
            codegen.append(self.emit.emitLABEL(labelEnd, frame))

            return ''.join(codegen), BoolType()
            # if op == '&&':
            #     return lhs + rhs + self.emit.emitANDOP(frame), BoolType()
            # else:
            #     return lhs + rhs + self.emit.emitOROP(frame), BoolType()
        elif op == '=':
            rhs, rightType = self.visit(ast.right, Access(frame, sym, False, True))
            lhs, leftType = self.visit(ast.left, Access(frame, sym, True, True))
            if type(leftType) == FloatType and type(rightType) == IntType:
                rhs = rhs + self.emit.emitI2F(frame)
            # Assign to ID only
            self.emit.printout(rhs + lhs)
            lhs, leftType = self.visit(ast.left, Access(frame, sym, False, True))
            return lhs, leftType

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        op = ast.op
        value, vType = self.visit(ast.body, ctxt)
        if op == '-':
            return value + self.emit.emitNEGOP(vType, frame), vType
        else:
            return value + self.emit.emitNOT(vType, frame), vType