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
.var 2 is a I from Label8 to Label9
	iload_1
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	istore_2
	iload_2
	invokestatic MCClass/func(Z)Z
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/putBoolLn(Z)V
Label9:
Label6:
	iload_1
	iconst_2
	iadd
	istore_1
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 21
.limit locals 3
.end method

.method public static func(Z)Z
.var 0 is a Z from Label0 to Label1
Label0:
	iload_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 4
.limit locals 1
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
