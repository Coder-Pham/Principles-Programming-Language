.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/cal()I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static cal()I
Label0:
.var 0 is b I from Label0 to Label1
	iconst_0
	istore_0
Label11:
	iload_0
	iconst_1
	iadd
	istore_0
	iload_0
	iconst_3
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label17
	goto Label18
Label17:
	iload_0
	ireturn
Label18:
Label13:
	iload_0
	iconst_5
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label3
	iload_0
	iconst_5
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label2
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifle Label12
	goto Label11
Label12:
Label14:
	iconst_1
	ireturn
Label1:
.limit stack 14
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
