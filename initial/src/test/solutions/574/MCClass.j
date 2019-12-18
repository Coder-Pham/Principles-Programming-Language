.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
Label8:
	iconst_0
	iload_1
	invokestatic MCClass/boo(ZI)Z
	invokestatic io/putBoolLn(Z)V
Label9:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static boo(ZI)Z
.var 0 is boo Z from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iload_1
	iconst_2
	irem
	ifgt Label2
	iload_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ireturn
Label2:
	iload_0
	ireturn
Label3:
	iconst_0
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
