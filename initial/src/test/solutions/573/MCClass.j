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
	iload_1
	iconst_3
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iconst_1
	invokestatic MCClass/boo(Z)Z
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
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	invokestatic io/putBoolLn(Z)V
	goto Label13
Label12:
	iconst_0
	invokestatic MCClass/boo(Z)Z
	ifgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifgt Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifgt Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	invokestatic io/putBoolLn(Z)V
Label13:
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
.limit stack 39
.limit locals 2
.end method

.method public static boo(Z)Z
.var 0 is boo Z from Label0 to Label1
Label0:
	iload_0
	ireturn
Label1:
.limit stack 1
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
