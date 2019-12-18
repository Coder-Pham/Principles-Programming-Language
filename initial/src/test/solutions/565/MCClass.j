.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static check I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MCClass/check I
	getstatic MCClass/check I
	ifgt Label2
	goto Label3
Label2:
Label4:
.var 1 is a I from Label4 to Label5
	iconst_5
	istore_1
	iload_1
	ifgt Label6
	goto Label7
Label6:
Label8:
	iconst_0
	istore_1
Label14:
	iload_1
	iconst_4
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label15
	iload_1
	invokestatic io/putIntLn(I)V
Label16:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label14
Label15:
Label17:
	ldc "end"
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iconst_0
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	goto Label21
Label20:
	goto Label11
Label21:
Label10:
	iconst_1
	ifle Label9
	goto Label8
Label9:
Label11:
Label7:
Label5:
Label3:
Label1:
	return
.limit stack 11
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
